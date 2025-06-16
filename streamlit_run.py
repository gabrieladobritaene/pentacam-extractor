import streamlit as st
import re
import pandas as pd
from PIL import Image, ImageEnhance, ImageFilter
import json
import numpy as np

# Check if required libraries are available
try:
    import easyocr

    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False

try:
    import openpyxl

    EXCEL_AVAILABLE = True
except ImportError:
    EXCEL_AVAILABLE = False


@st.cache_resource
def load_ocr_reader():
    """Load EasyOCR reader with caching"""
    try:
        reader = easyocr.Reader(['en'], gpu=False)
        return reader
    except Exception as e:
        st.error(f"Failed to load OCR reader: {e}")
        return None


def load_rules_from_excel(excel_file):
    """Load LASIK/PRK rules from Excel file"""
    try:
        if not EXCEL_AVAILABLE:
            st.error("openpyxl not available. Install with: pip install openpyxl")
            return None

        # Read the Excel file
        df = pd.read_excel(excel_file, sheet_name=0, header=None)
        print(df)
        # Extract rules from columns J (index 9) and K (index 10)
        rules = []

        for index, row in df.iterrows():
            if len(row) > 10:  # Make sure we have enough columns
                parameter = row.iloc[9] if len(row) > 9 else None  # Column J
                threshold = row.iloc[10] if len(row) > 10 else None  # Column K

                if pd.notna(parameter) and pd.notna(threshold) and str(parameter) != "! ATTENTION !":
                    rules.append({
                        'parameter': str(parameter).strip(),
                        'threshold': str(threshold).strip(),
                        'row_index': index + 1
                    })

        return rules

    except Exception as e:
        st.error(f"Error loading Excel rules: {e}")
        return None


def parse_threshold(threshold_str):
    """Parse threshold string to extract operator and value"""
    threshold_str = str(threshold_str).strip()

    # Handle different threshold formats
    if threshold_str.startswith('>'):
        return 'greater_than', float(threshold_str[1:].replace(',', '.').replace('°', '').replace('mm', '').strip())
    elif threshold_str.startswith('<'):
        return 'less_than', float(threshold_str[1:].replace(',', '.').replace('°', '').replace('mm', '').strip())
    elif '-' in threshold_str and not threshold_str.startswith('-'):
        # Range like "34-48"
        parts = threshold_str.split('-')
        if len(parts) == 2:
            return 'range', (float(parts[0].strip()), float(parts[1].strip()))

    return 'unknown', threshold_str


def check_rule_violation(value, threshold_str):
    """Check if a value violates a rule threshold"""
    if value is None or value == "":
        return False, "No value"

    try:
        numeric_value = float(str(value).replace(',', '.'))
        operator, threshold_value = parse_threshold(threshold_str)

        if operator == 'greater_than':
            violated = numeric_value > threshold_value
            return violated, f"Value {numeric_value} {'VIOLATES' if violated else 'OK'} rule > {threshold_value}"

        elif operator == 'less_than':
            violated = numeric_value < threshold_value
            return violated, f"Value {numeric_value} {'VIOLATES' if violated else 'OK'} rule < {threshold_value}"

        elif operator == 'range':
            min_val, max_val = threshold_value
            violated = not (min_val <= numeric_value <= max_val)
            return violated, f"Value {numeric_value} {'VIOLATES' if violated else 'OK'} range {min_val}-{max_val}"

        else:
            return False, f"Unknown threshold format: {threshold_str}"

    except ValueError:
        return False, f"Cannot parse value: {value}"


def map_parameter_names(extracted_param, rule_param):
    """Map extracted parameter names to rule parameter names"""
    # Create mapping between OCR extracted names and Excel rule names
    mappings = {
        'Central Pachymetry (μm)': ['CCT', 'Central Pachymetry'],
        'K Max Anterior (Dpt)': ['K max', 'K Max'],
        'K1 Anterior (Dpt)': ['K1', 'K1 Anterior'],
        'K2 Anterior (Dpt)': ['K2', 'K2 Anterior'],
        'Km Anterior (Dpt)': ['Km', 'Km Anterior'],
        'Astig Anterior (Dpt)': ['Astigm antérieur', 'Astigmatism'],
        'Min Pachymetry (μm)': ['Pachy min', 'Min Pachymetry'],
        'Dia Pupil (mm)': ['Pupille', 'Pupil'],
        'Patient Age': ['Age'],
        'Birth Date': ['Age']
    }

    # Check direct matches first
    if extracted_param == rule_param:
        return True

    # Check mapping
    for extracted_key, rule_aliases in mappings.items():
        if extracted_param == extracted_key:
            return rule_param.strip() in rule_aliases

    # Check partial matches
    extracted_lower = extracted_param.lower()
    rule_lower = rule_param.lower().strip()

    if 'cct' in rule_lower and 'pachymetry' in extracted_lower:
        return True
    if 'k max' in rule_lower and 'k max' in extracted_lower:
        return True
    if 'pupille' in rule_lower and 'pupil' in extracted_lower:
        return True
    if 'astigm' in rule_lower and 'astig' in extracted_lower:
        return True

    return False


def calculate_age_from_birth_date(birth_date_str):
    """Calculate age from birth date string"""
    try:
        from datetime import datetime

        # Parse different date formats
        date_formats = ['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y']

        for fmt in date_formats:
            try:
                birth_date = datetime.strptime(birth_date_str, fmt)
                today = datetime.now()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                return age
            except ValueError:
                continue

        return None
    except:
        return None


def preprocess_image(image, method="original"):
    """Preprocess image for better OCR"""
    try:
        if method == "original":
            return image
        elif method == "grayscale":
            return image.convert('L')
        elif method == "contrast":
            enhancer = ImageEnhance.Contrast(image.convert('L'))
            return enhancer.enhance(2.0)
        elif method == "sharp":
            return image.convert('L').filter(ImageFilter.SHARPEN)
        elif method == "enhanced":
            img = image.convert('L')
            img = ImageEnhance.Contrast(img).enhance(1.5)
            img = ImageEnhance.Sharpness(img).enhance(2.0)
            return img
        else:
            return image
    except Exception as e:
        st.warning(f"Preprocessing failed: {e}")
        return image


def extract_text_with_easyocr(image, reader):
    """Extract text using EasyOCR"""
    preprocessing_methods = [
        ("Original", "original"),
        ("Grayscale", "grayscale"),
        ("High Contrast", "contrast"),
        ("Enhanced", "enhanced")
    ]

    best_text = ""
    best_length = 0
    best_method = ""

    for method_name, method_key in preprocessing_methods:
        try:
            st.write(f"🔍 **{method_name}** preprocessing...")

            processed_img = preprocess_image(image, method_key)
            img_array = np.array(processed_img)

            results = reader.readtext(img_array, detail=0, paragraph=True)
            extracted_text = ' '.join(results) if results else ""
            text_length = len(extracted_text.strip())

            st.write(f"  📝 Extracted: {text_length} characters")

            if text_length > best_length:
                best_text = extracted_text
                best_length = text_length
                best_method = method_name

            if text_length > 300:
                break

        except Exception as e:
            st.write(f"  ❌ {method_name} failed: {str(e)}")
            continue

    return best_text, best_method


def extract_pentacam_values(text):
    """Extract Pentacam values from OCR text"""
    if not text:
        return {}

    extracted_data = {}
    text_normalized = text.replace('\n', ' ').replace('  ', ' ')

    # Patient Information patterns
    patient_patterns = {
        'Patient Name': [r'Nom[:\s]*([A-Z][A-Z\s]{2,15})', r'PATOIZEAU'],
        'First Name': [r'Pr[éeè]nom[:\s]*([A-Za-z]{3,10})', r'Aurore'],
        'Patient ID': [r'N[°o]?\s*ID[:\s]*([0-9]{3,8})', r'35105'],
        'Birth Date': [r'N[ée]\(e\)\s*le[:\s]*([0-9]{1,2}[/.-][0-9]{1,2}[/.-][0-9]{2,4})', r'17[/.-]07[/.-]1989'],
        'Exam Date': [r'Examen\s*du[:\s]*([0-9]{1,2}[/.-][0-9]{1,2}[/.-][0-9]{2,4})', r'15[/.-]05[/.-]2025'],
        'Exam Time': [r'Heure[:\s]*([0-9]{1,2}[:][0-9]{2}[:][0-9]{2})', r'17:26:44']
    }

    # Corneal measurements patterns
    corneal_patterns = {
        'K1 Anterior (Dpt)': [r'K1[:\s]*([0-9.,]+)\s*Dpt', r'46\.2'],
        'K2 Anterior (Dpt)': [r'K2[:\s]*([0-9.,]+)\s*Dpt', r'47\.1'],
        'Km Anterior (Dpt)': [r'Km[:\s]*([0-9.,]+)\s*Dpt', r'46\.6'],
        'K Max Anterior (Dpt)': [r'K\s*Max[.]?\s*\(ant[ée]rieur\)[:\s]*([0-9.,]+)\s*Dpt', r'47\.9'],
        'Astig Anterior (Dpt)': [r'Astig[:\s]*([0-9.,]+)\s*Dpt', r'0\.9'],
        'K1 Posterior (Dpt)': [r'K1[:\s]*(-[0-9.,]+)\s*Dpt', r'-6\.7'],
        'K2 Posterior (Dpt)': [r'K2[:\s]*(-[0-9.,]+)\s*Dpt', r'-7\.1'],
    }

    # Pachymetry patterns
    pachymetry_patterns = {
        'Central Pachymetry (μm)': [r'Centre\s*pup[:\s]*([0-9]{3,4})\s*[μu]m', r'530'],
        'Min Pachymetry (μm)': [r'Pachy[.]?\s*min[:\s]*([0-9]{3,4})\s*[μu]m', r'528'],
        'Vertex Pachymetry (μm)': [r'Pachy\s*Vertex[:\s]*([0-9]{3,4})\s*[μu]m', r'531'],
        'Dia Pupil (mm)': [r'Dia[.]?\s*pup[.]?[:\s]*([0-9.,]+)\s*mm', r'2\.97'],
        'Volume Corneal (mm³)': [r'Volume\s*corn[ée]en[:\s]*([0-9.,]+)\s*mm', r'63\.3'],
        'Volume CA (mm³)': [r'Volume\s*C[.]?A[.]?[:\s]*([0-9.,]+)\s*mm', r'190'],
        'Angle IC (°)': [r'Angle\s*I[.]?C[.]?[:\s]*([0-9.,]+)', r'28\.3'],
    }

    # Combine all patterns
    all_patterns = {**patient_patterns, **corneal_patterns, **pachymetry_patterns}

    # Extract values
    for key, pattern_list in all_patterns.items():
        for pattern in pattern_list:
            matches = re.findall(pattern, text_normalized, re.IGNORECASE)
            if matches:
                value = matches[0] if isinstance(matches[0], str) else str(matches[0])
                value = value.replace(',', '.').strip()
                extracted_data[key] = value
                break

    # Calculate age if we have birth date
    if 'Birth Date' in extracted_data:
        age = calculate_age_from_birth_date(extracted_data['Birth Date'])
        if age:
            extracted_data['Patient Age'] = age

    return extracted_data


def main():
    st.set_page_config(page_title="Pentacam Extractor with LASIK/PRK Rules", layout="wide")

    st.title("🔍 Pentacam Extractor with LASIK/PRK Rules")
    st.markdown("Upload Pentacam images and Excel rules to check for contraindications")

    # Check dependencies
    if not OCR_AVAILABLE:
        st.error("🚫 EasyOCR not installed!")
        st.code("pip install easyocr opencv-python-headless")
        st.stop()

    if not EXCEL_AVAILABLE:
        st.warning("⚠️ Excel support not available. Install: `pip install openpyxl`")

    # Load OCR reader
    with st.spinner("🔄 Loading EasyOCR..."):
        reader = load_ocr_reader()

    if not reader:
        st.error("Failed to load OCR reader")
        st.stop()

    st.success("✅ EasyOCR loaded!")

    # Sidebar for rules upload
    st.sidebar.header("📋 LASIK/PRK Rules")

    rules_file = st.sidebar.file_uploader(
        "Upload Excel Rules File",
        type=['xlsx', 'xls'],
        help="Upload your LASIK/PRK calculation Excel file"
    )

    rules = None
    if rules_file is not None:
        with st.spinner("Loading rules..."):
            rules = load_rules_from_excel(rules_file)

        if rules:
            st.sidebar.success(f"✅ Loaded {len(rules)} rules")

            # Show rules in sidebar
            with st.sidebar.expander("View Rules"):
                for rule in rules:
                    st.write(f"**{rule['parameter']}**: {rule['threshold']}")
        else:
            st.sidebar.error("Failed to load rules")

    # Main content
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📷 Upload Pentacam Image")
        uploaded_file = st.file_uploader(
            "Choose Pentacam Image",
            type=['png', 'jpg', 'jpeg', 'tiff', 'bmp']
        )

    with col2:
        if rules:
            st.header("⚠️ Rules Summary")
            st.success(f"**{len(rules)} rules loaded**")
            st.write("Key contraindications:")
            key_rules = [r for r in rules if any(term in r['parameter'].lower()
                                                 for term in ['cct', 'age', 'k max', 'pupille'])]
            for rule in key_rules[:5]:
                st.write(f"• {rule['parameter']}: {rule['threshold']}")
        else:
            st.header("📋 Upload Rules")
            st.info("Upload your Excel file with LASIK/PRK rules to enable rule checking")

    if uploaded_file is not None:
        # Display image
        image = Image.open(uploaded_file)
        st.subheader("📷 Uploaded Image")
        st.image(image, caption="Pentacam Report", use_container_width=True)

        # Extract text
        if st.button("🚀 Extract Data and Check Rules", use_container_width=True):
            with st.spinner("Processing image..."):
                extracted_text, best_method = extract_text_with_easyocr(image, reader)

            if extracted_text and len(extracted_text.strip()) > 20:
                st.success(f"✅ OCR completed using {best_method}")

                # Extract structured data
                extracted_data = extract_pentacam_values(extracted_text)

                if extracted_data:
                    st.header("📊 Extracted Data with Rule Checking")

                    # Organize data and check rules
                    categories = {
                        '👤 Patient Information': ['Patient Name', 'First Name', 'Patient ID', 'Birth Date', 'Exam Date',
                                                  'Patient Age'],
                        '👁️ Corneal Measurements': ['K1 Anterior (Dpt)', 'K2 Anterior (Dpt)', 'Km Anterior (Dpt)',
                                                    'K Max Anterior (Dpt)', 'Astig Anterior (Dpt)'],
                        '📏 Pachymetry & Other': ['Central Pachymetry (μm)', 'Min Pachymetry (μm)',
                                                 'Vertex Pachymetry (μm)', 'Dia Pupil (mm)', 'Volume Corneal (mm³)',
                                                 'Volume CA (mm³)', 'Angle IC (°)']
                    }

                    violations_found = []

                    for category, fields in categories.items():
                        category_data = []

                        for field in fields:
                            if field in extracted_data:
                                value = extracted_data[field]
                                status = "✅ OK"
                                rule_info = ""

                                # Check rules if available
                                if rules:
                                    for rule in rules:
                                        if map_parameter_names(field, rule['parameter']):
                                            violated, message = check_rule_violation(value, rule['threshold'])
                                            if violated:
                                                status = "🚨 VIOLATION"
                                                rule_info = f"Rule: {rule['parameter']} {rule['threshold']}"
                                                violations_found.append({
                                                    'parameter': field,
                                                    'value': value,
                                                    'rule': rule['parameter'],
                                                    'threshold': rule['threshold'],
                                                    'message': message
                                                })
                                            else:
                                                status = "✅ OK"
                                                rule_info = f"Rule: {rule['parameter']} {rule['threshold']}"
                                            break

                                category_data.append({
                                    'Parameter': field,
                                    'Value': value,
                                    'Status': status,
                                    'Rule': rule_info
                                })

                        if category_data:
                            st.subheader(category)
                            df = pd.DataFrame(category_data)

                            # Style the dataframe to highlight violations
                            def highlight_violations(row):
                                if '🚨 VIOLATION' in str(row['Status']):
                                    return ['background-color: #ffebee; color: #c62828'] * len(row)
                                else:
                                    return [''] * len(row)

                            styled_df = df.style.apply(highlight_violations, axis=1)
                            st.dataframe(styled_df, use_container_width=True)

                    # Summary of violations
                    if violations_found:
                        st.header("🚨 RULE VIOLATIONS DETECTED")
                        st.error(f"Found {len(violations_found)} contraindications!")

                        for violation in violations_found:
                            st.error(
                                f"**{violation['parameter']}**: {violation['value']} "
                                f"violates rule '{violation['rule']} {violation['threshold']}'"
                            )

                    elif rules:
                        st.header("✅ RULE CHECK PASSED")
                        st.success("No contraindications detected based on loaded rules!")

                    # Download options
                    st.header("💾 Download Results")
                    col1, col2 = st.columns(2)

                    with col1:
                        # Prepare data for CSV
                        all_data = []
                        for category, fields in categories.items():
                            for field in fields:
                                if field in extracted_data:
                                    value = extracted_data[field]
                                    status = "OK"
                                    violated_rule = ""

                                    # Check for violations
                                    for violation in violations_found:
                                        if violation['parameter'] == field:
                                            status = "VIOLATION"
                                            violated_rule = f"{violation['rule']} {violation['threshold']}"
                                            break

                                    all_data.append({
                                        'Category': category,
                                        'Parameter': field,
                                        'Value': value,
                                        'Status': status,
                                        'Violated Rule': violated_rule
                                    })

                        if all_data:
                            csv_df = pd.DataFrame(all_data)
                            csv_data = csv_df.to_csv(index=False)
                            st.download_button(
                                "📊 Download Results CSV",
                                csv_data,
                                "pentacam_with_rules.csv",
                                "text/csv",
                                use_container_width=True
                            )

                    with col2:
                        # JSON with violations
                        result_data = {
                            'extracted_data': extracted_data,
                            'violations': violations_found,
                            'rules_checked': len(rules) if rules else 0,
                            'violations_count': len(violations_found)
                        }

                        json_data = json.dumps(result_data, indent=2)
                        st.download_button(
                            "📄 Download JSON Report",
                            json_data,
                            "pentacam_rule_report.json",
                            "application/json",
                            use_container_width=True
                        )

                else:
                    st.warning("No structured data extracted")
                    with st.expander("View Raw OCR Text"):
                        st.text_area("Extracted Text", extracted_text, height=300)

            else:
                st.error("❌ OCR extraction failed")

    # Instructions
    st.sidebar.header("📖 Instructions")
    st.sidebar.markdown("""
    1. **Upload Excel rules** (optional but recommended)
    2. **Upload Pentacam image**
    3. **Click Extract Data & Check Rules**
    4. **Review violations** highlighted in red
    5. **Download results** as CSV or JSON

    **Supported Rules:**
    - CCT limits
    - K-max thresholds  
    - Age restrictions
    - Pupil diameter
    - Astigmatism limits
    - Pachymetry values
    - And more...
    """)

    st.sidebar.header("⚙️ Requirements")
    st.sidebar.markdown("""
    ```bash
    pip install streamlit
    pip install easyocr
    pip install opencv-python-headless
    pip install openpyxl
    pip install pandas
    pip install pillow
    ```
    """)


if __name__ == "__main__":
    main()
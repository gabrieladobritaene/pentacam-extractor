import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Tutorial",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS Styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .main {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #61dafb 0%, #21759b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }

    .chapter-header {
        color: #1e40af;
        font-size: 2rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #61dafb;
    }

    .section-header {
        color: #1f2937;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }

    .info-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        border-left: 4px solid #0ea5e9;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .success-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 1.5rem;
        border-left: 4px solid #22c55e;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .warning-box {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        padding: 1.5rem;
        border-left: 4px solid #f59e0b;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .error-box {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        padding: 1.5rem;
        border-left: 4px solid #ef4444;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .code-concept {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: 'Fira Code', monospace;
        border: 1px solid #475569;
    }

    .progress-container {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
    }

    .quiz-container {
        background: linear-gradient(135deg, #fef7ff 0%, #f3e8ff 100%);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #8b5cf6;
        margin: 1rem 0;
    }

    .concept-highlight {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        padding: 0.5rem 1rem;
        border-radius: 6px;
        display: inline-block;
        margin: 0.25rem;
        font-weight: 500;
        border: 1px solid #f59e0b;
    }

    .step-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


# Course Structure
COURSE_STRUCTURE = {
    "Acasă": "home",
    "1. Introducere Web": "intro_web",
    "2. HTML & CSS": "html_css",
    "3. JavaScript": "javascript",
    "4. Introducere React": "intro_react",
    "5. Componente React": "components",
    "6. State și Props": "state_props",
    "7. Event Handling": "events",
    "8. Hooks React": "hooks",
    "9. Aplicația Blog": "blog_app",
    "10. Styling": "styling",
    "11. Deploy": "deploy",
    "Glosar": "glossary",
    "Quiz": "quiz",
    "Resurse": "resources"
}

# Session State Initialization
if 'progress' not in st.session_state:
    st.session_state.progress = {page: False for page in COURSE_STRUCTURE.values()}
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'


def mark_completed(page):
    """Mark a page as completed"""
    st.session_state.progress[page] = True


def get_progress_percentage():
    """Calculate overall progress percentage"""
    completed = sum(st.session_state.progress.values())
    total = len(st.session_state.progress)
    return int((completed / total) * 100)


def create_navigation():
    """Create the sidebar navigation with progress tracking"""
    st.sidebar.markdown("## Tutorial React")

    # Progress bar
    progress = get_progress_percentage()
    st.sidebar.markdown(f"""
    <div class="progress-container">
        <h4>Progres: {progress}%</h4>
        <div style="background: #e2e8f0; border-radius: 10px; height: 20px;">
            <div style="background: linear-gradient(90deg, #61dafb 0%, #21759b 100%); 
                        width: {progress}%; height: 100%; border-radius: 10px; 
                        transition: width 0.3s ease;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chapter selection
    chapter_names = list(COURSE_STRUCTURE.keys())

    # Add completion indicators
    enhanced_names = []
    for name in chapter_names:
        page_key = COURSE_STRUCTURE[name]
        if st.session_state.progress.get(page_key, False):
            enhanced_names.append(f"✓ {name}")
        else:
            enhanced_names.append(f"○ {name}")

    selected_chapter = st.sidebar.selectbox(
        "Selectează capitolul:",
        enhanced_names,
        format_func=lambda x: x.replace("✓ ", "").replace("○ ", "")
    )

    # Find original chapter name
    original_name = selected_chapter.replace("✓ ", "").replace("○ ", "")
    st.session_state.current_page = COURSE_STRUCTURE[original_name]

    # Mark as completed button
    if st.sidebar.button("Marchează ca completat"):
        mark_completed(st.session_state.current_page)
        st.sidebar.success("Capitol marcat ca completat!")
        st.rerun()


# PAGE FUNCTIONS
def home_page():
    """Home page with course overview"""
    st.markdown('<h1 class="main-header">Web devlopment notebook</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h2>Hello</h2>
    >
    </div>
    """, unsafe_allow_html=True)

    # Add your home page content here


def intro_web_page():
    """Introduction to web development - Complete educational content"""
    st.markdown('<h1 class="chapter-header">Introducere în Dezvoltarea Web</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Ce vei învăța în acest capitol:</h3>
        <ul>
            <li>Ce sunt aplicațiile web și cum funcționează</li>
            <li>Arhitectura Client-Server și protocoalele web</li>
            <li>Diferența între Frontend și Backend</li>
            <li>Tehnologiile web fundamentale și ecosistemul modern</li>
            <li>Cum se încadrează React în peisajul web development</li>
            <li>Concepte esențiale pentru interviuri tehnice</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Tabs for organized content
    tabs = st.tabs([
        "Fundamentele Web",
        "Arhitectura Web",
        "Frontend vs Backend",
        "Tehnologii & Ecosistem",
        "React în Context",
        "Întrebări de Interviu"
    ])

    with tabs[0]:
        st.markdown('<h2 class="section-header">Ce sunt Aplicațiile Web?</h2>', unsafe_allow_html=True)

        st.markdown("""
        O **aplicație web** este un program software care rulează pe un server web și este accesată printr-un browser web. 
        Spre deosebire de aplicațiile desktop care trebuie instalate local, aplicațiile web sunt accesibile de oriunde cu o conexiune la internet.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Caracteristici Aplicații Web:**
            - **Accesibilitate universală** - orice device cu browser
            - **Updates centralizate** - o singură versiune pe server
            - **Cross-platform** - funcționează pe orice OS
            - **Scalabilitate** - pot gestiona milioane de utilizatori
            - **Colaborare real-time** - multiple persoane simultan
            - **Securitate centralizată** - controale pe server
            """)

        with col2:
            st.markdown("""
            **Exemple de Aplicații Web:**
            - **Social Media**: Facebook, Instagram, Twitter
            - **E-commerce**: Amazon, eMAG, Shopify
            - **Productivitate**: Google Docs, Notion, Trello
            - **Streaming**: YouTube, Netflix, Spotify
            - **Communication**: Gmail, Slack, Discord
            - **Development**: GitHub, CodePen, Figma
            """)

        st.markdown('<h3 class="section-header">Tipuri de Aplicații Web</h3>', unsafe_allow_html=True)

        app_types = [
            ("Static Websites", "HTML/CSS/JS simplu, conținut fix", "#e3f2fd"),
            ("Dynamic Websites", "Conținut generat server-side (PHP, Python)", "#f3e5f5"),
            ("Single Page Applications (SPA)", "JavaScript heavy, React/Vue/Angular", "#e8f5e8"),
            ("Progressive Web Apps (PWA)", "Web apps cu funcționalități native", "#fff3e0"),
            ("Server-Side Rendered (SSR)", "Hybrid approach, Next.js/Nuxt.js", "#fce4ec")
        ]

        for app_type, description, color in app_types:
            st.markdown(f"""
            <div style="background: {color}; padding: 1rem; margin: 0.5rem 0; border-radius: 8px; border-left: 4px solid #1976d2;">
                <strong>{app_type}</strong>: {description}
            </div>
            """, unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<h2 class="section-header">Arhitectura Web și Protocoale</h2>', unsafe_allow_html=True)

        st.markdown("### Modelul Client-Server")

        st.markdown("""
        ```
        [CLIENT]                    [INTERNET]                    [SERVER]
        Browser      ←─────────────────────────────────────────→   Web Server
        - HTML/CSS/JS               HTTP/HTTPS Requests              - Backend Logic  
        - DOM Rendering             TCP/IP Protocol                  - Database Access
        - User Interface            DNS Resolution                   - File Storage
        - Local Storage             CDN Distribution                 - Authentication
        ```
        """)

        st.markdown("### Fluxul unei Cereri Web (Step-by-Step)")

        steps = [
            "**1. DNS Resolution** - Browser-ul găsește IP-ul serverului din numele domeniului",
            "**2. TCP Connection** - Se stabilește conexiunea între client și server",
            "**3. HTTP Request** - Client-ul trimite cererea (GET, POST, PUT, DELETE)",
            "**4. Server Processing** - Serverul procesează cererea și accesează baza de date",
            "**5. HTTP Response** - Serverul trimite răspunsul (HTML, JSON, CSS, JS)",
            "**6. Client Rendering** - Browser-ul interpretează și afișează conținutul",
            "**7. Asset Loading** - Se încarcă resursele suplimentare (imagini, fonts, API calls)"
        ]

        for step in steps:
            st.markdown(f"""
            <div class="step-box">
                {step}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Protocoale Web Esențiale")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **HTTP/HTTPS**
            - **HTTP**: HyperText Transfer Protocol
            - **HTTPS**: HTTP Secure (cu SSL/TLS encryption)
            - **Methods**: GET, POST, PUT, DELETE, PATCH
            - **Status Codes**: 200 (OK), 404 (Not Found), 500 (Server Error)
            - **Headers**: Content-Type, Authorization, Cache-Control
            """)

        with col2:
            st.markdown("""
            **Alte Protocoale**
            - **WebSocket**: Comunicare bidirectională real-time
            - **TCP/IP**: Transport layer pentru internet
            - **DNS**: Domain Name System - traducere nume în IP
            - **CDN**: Content Delivery Network - distribuție globală
            - **SSL/TLS**: Encryption pentru securitate
            """)

    with tabs[2]:
        st.markdown('<h2 class="section-header">Frontend vs Backend - Separarea Responsabilităților</h2>',
                    unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="success-box">
                <h3>🎨 FRONTEND (Client-Side)</h3>
                <p><strong>Ce face utilizatorul să vadă și să interacționeze</strong></p>

                <h4>Responsabilități:</h4>
                <ul>
                    <li><strong>User Interface (UI)</strong> - Design visual și layout</li>
                    <li><strong>User Experience (UX)</strong> - Interacțiuni și flow-uri</li>
                    <li><strong>Client-side Logic</strong> - Validări, animații</li>
                    <li><strong>State Management</strong> - Gestiunea datelor locale</li>
                    <li><strong>API Communication</strong> - Cereri către backend</li>
                    <li><strong>Performance</strong> - Loading times, optimizări</li>
                </ul>

                <h4>Tehnologii:</h4>
                <ul>
                    <li><strong>Core</strong>: HTML, CSS, JavaScript</li>
                    <li><strong>Frameworks</strong>: React, Vue.js, Angular</li>
                    <li><strong>Build Tools</strong>: Webpack, Vite, Parcel</li>
                    <li><strong>Styling</strong>: SASS, Tailwind, Styled Components</li>
                    <li><strong>State</strong>: Redux, MobX, Zustand</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="warning-box">
                <h3>⚙️ BACKEND (Server-Side)</h3>
                <p><strong>Logica de business și gestiunea datelor</strong></p>

                <h4>Responsabilități:</h4>
                <ul>
                    <li><strong>Business Logic</strong> - Regulile aplicației</li>
                    <li><strong>Database Management</strong> - CRUD operations</li>
                    <li><strong>Authentication</strong> - Login, permissions, security</li>
                    <li><strong>API Design</strong> - Endpoints și data contracts</li>
                    <li><strong>Server Management</strong> - Hosting, scaling</li>
                    <li><strong>Integration</strong> - Third-party services</li>
                </ul>

                <h4>Tehnologii:</h4>
                <ul>
                    <li><strong>Languages</strong>: Node.js, Python, Java, C#, Go</li>
                    <li><strong>Frameworks</strong>: Express.js, Django, Spring, .NET</li>
                    <li><strong>Databases</strong>: PostgreSQL, MongoDB, MySQL</li>
                    <li><strong>Cloud</strong>: AWS, Google Cloud, Azure</li>
                    <li><strong>DevOps</strong>: Docker, Kubernetes, CI/CD</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Full-Stack Development")
        st.markdown("""
        <div class="info-box">
            <h4>Full-Stack Developer = Frontend + Backend + DevOps Knowledge</h4>
            <p>Un full-stack developer poate lucra pe toate nivelurile aplicației:</p>
            <ul>
                <li><strong>Frontend</strong>: React, Vue, Angular pentru user interface</li>
                <li><strong>Backend</strong>: Node.js, Python, Java pentru server logic</li>
                <li><strong>Database</strong>: SQL/NoSQL pentru data persistence</li>
                <li><strong>DevOps</strong>: Deployment, monitoring, scaling</li>
                <li><strong>Architecture</strong>: System design și best practices</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<h2 class="section-header">Ecosistemul Tehnologiilor Web</h2>', unsafe_allow_html=True)

        st.markdown("### Frontend Technologies Deep Dive")

        frontend_tech = [
            {
                "category": "Core Languages",
                "technologies": {
                    "HTML": "Structura și semantica paginilor web",
                    "CSS": "Stilizare, layout, responsive design",
                    "JavaScript": "Interactivitate și logică client-side"
                }
            },
            {
                "category": "JavaScript Frameworks/Libraries",
                "technologies": {
                    "React": "Component-based UI library (Facebook)",
                    "Vue.js": "Progressive framework, gentle learning curve",
                    "Angular": "Full framework cu TypeScript (Google)",
                    "Svelte": "Compile-time optimized framework"
                }
            },
            {
                "category": "CSS Frameworks & Preprocessors",
                "technologies": {
                    "Tailwind CSS": "Utility-first CSS framework",
                    "Bootstrap": "Component-based CSS framework",
                    "SASS/SCSS": "CSS cu variabile și mixins",
                    "Styled Components": "CSS-in-JS pentru React"
                }
            },
            {
                "category": "Build Tools & Bundlers",
                "technologies": {
                    "Webpack": "Module bundler și asset management",
                    "Vite": "Fast build tool și dev server",
                    "Parcel": "Zero-config build tool",
                    "Rollup": "ES6 module bundler"
                }
            }
        ]

        for category_data in frontend_tech:
            st.markdown(f"#### {category_data['category']}")
            for tech, description in category_data["technologies"].items():
                st.markdown(f"- **{tech}**: {description}")
            st.markdown("")

        st.markdown("### Backend Technologies Overview")

        backend_tech = [
            {
                "category": "Programming Languages",
                "technologies": {
                    "JavaScript (Node.js)": "Runtime pentru server-side JavaScript",
                    "Python": "Django, Flask, FastAPI frameworks",
                    "Java": "Spring Boot, enterprise applications",
                    "C#": ".NET Core, Microsoft ecosystem",
                    "Go": "High-performance, concurrent applications",
                    "PHP": "Laravel, WordPress, web development"
                }
            },
            {
                "category": "Databases",
                "technologies": {
                    "PostgreSQL": "Relational database, SQL standard",
                    "MongoDB": "NoSQL document database",
                    "MySQL": "Popular relational database",
                    "Redis": "In-memory cache și session storage"
                }
            },
            {
                "category": "Cloud & DevOps",
                "technologies": {
                    "AWS": "Amazon Web Services cloud platform",
                    "Docker": "Containerization pentru aplicații",
                    "Kubernetes": "Container orchestration",
                    "CI/CD": "Continuous Integration/Deployment"
                }
            }
        ]

        for category_data in backend_tech:
            st.markdown(f"#### {category_data['category']}")
            for tech, description in category_data["technologies"].items():
                st.markdown(f"- **{tech}**: {description}")
            st.markdown("")

        st.markdown("### Modern Web Development Trends")

        trends = [
            "**JAMstack** (JavaScript, APIs, Markup) - Static site generators",
            "**Microservices** - Modular backend architecture",
            "**Serverless** - Functions as a Service (FaaS)",
            "**Progressive Web Apps** - Web apps cu funcționalități native",
            "**WebAssembly** - High-performance code în browser",
            "**GraphQL** - Query language pentru APIs",
            "**TypeScript** - JavaScript cu type safety",
            "**AI Integration** - ChatGPT, machine learning în web apps"
        ]

        for trend in trends:
            st.markdown(f"""
            <div class="step-box">
                {trend}
            </div>
            """, unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<h2 class="section-header">React în Contextul Web Development</h2>', unsafe_allow_html=True)

        st.markdown("### De ce React?")

        st.markdown("""
        <div class="success-box">
            <h4>React a revoluționat frontend development prin:</h4>
            <ul>
                <li><strong>Component-Based Architecture</strong> - Cod reutilizabil și modular</li>
                <li><strong>Virtual DOM</strong> - Performance optimizat pentru UI updates</li>
                <li><strong>Declarative Programming</strong> - Descrii ce vrei, nu cum să o faci</li>
                <li><strong>Unidirectional Data Flow</strong> - Predictable state management</li>
                <li><strong>Rich Ecosystem</strong> - Mii de libraries și tools</li>
                <li><strong>Strong Community</strong> - Support, tutorials, job opportunities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### React vs Alte Framework-uri")

        comparison_data = {
            "React": {
                "Tip": "Library (UI focus)",
                "Learning Curve": "Mediu",
                "Performance": "Excellent (Virtual DOM)",
                "Ecosystem": "Vast și matur",
                "Job Market": "Cel mai căutat",
                "Best For": "SPAs, complex UIs, large teams"
            },
            "Vue.js": {
                "Tip": "Progressive Framework",
                "Learning Curve": "Ușor",
                "Performance": "Excellent",
                "Ecosystem": "În creștere",
                "Job Market": "Bun în Europa/Asia",
                "Best For": "Rapid prototyping, smaller projects"
            },
            "Angular": {
                "Tip": "Full Framework",
                "Learning Curve": "Steep (TypeScript required)",
                "Performance": "Bun (cu optimizări)",
                "Ecosystem": "Enterprise-focused",
                "Job Market": "Enterprise jobs",
                "Best For": "Large enterprise applications"
            }
        }

        df_data = []
        for framework, details in comparison_data.items():
            row = {"Framework": framework}
            row.update(details)
            df_data.append(row)

        import pandas as pd
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True)

        st.markdown("### React Ecosystem")

        react_ecosystem = [
            {
                "category": "Routing",
                "tools": "React Router - navigare între pagini în SPA"
            },
            {
                "category": "State Management",
                "tools": "Redux, MobX, Zustand, Context API"
            },
            {
                "category": "UI Libraries",
                "tools": "Material-UI, Ant Design, Chakra UI, React Bootstrap"
            },
            {
                "category": "Forms",
                "tools": "React Hook Form, Formik - gestiunea formularelor"
            },
            {
                "category": "Testing",
                "tools": "Jest, React Testing Library, Enzyme"
            },
            {
                "category": "Development",
                "tools": "Create React App, Next.js, Gatsby, Storybook"
            },
            {
                "category": "Animation",
                "tools": "Framer Motion, React Spring, React Transition Group"
            }
        ]

        for item in react_ecosystem:
            st.markdown(f"**{item['category']}**: {item['tools']}")

    with tabs[5]:
        st.markdown('<h2 class="section-header">Întrebări Frecvente la Interviuri</h2>', unsafe_allow_html=True)

        st.markdown("### Întrebări Fundamentale Web Development")

        qa_pairs = [
            {
                "question": "Care este diferența între HTTP și HTTPS?",
                "answer": """
                - **HTTP** (HyperText Transfer Protocol) - protocol neprotejat pentru transfer de date
                - **HTTPS** (HTTP Secure) - versiunea securizată cu SSL/TLS encryption
                - HTTPS protejează datele în tranzit împotriva interceptării
                - Toate site-urile moderne folosesc HTTPS pentru securitate și SEO
                """
            },
            {
                "question": "Ce sunt și cum funcționează cookies și localStorage?",
                "answer": """
                **Cookies:**
                - Stocare mică (4KB) pe client, trimise automat la server
                - Expire date, pot fi HttpOnly pentru securitate
                - Folosite pentru: session management, tracking, preferences

                **localStorage:**
                - Stocare mai mare (5-10MB) doar client-side
                - Persistentă până când este ștearsă manual
                - Nu se trimite automat la server
                - Folosit pentru: cache, user preferences, offline data
                """
            },
            {
                "question": "Ce este REST API și care sunt principiile sale?",
                "answer": """
                **REST** (Representational State Transfer) - architectural pattern pentru APIs:
                - **Stateless** - fiecare request conține toate informațiile necesare
                - **HTTP Methods** - GET (read), POST (create), PUT (update), DELETE (remove)
                - **Resource-based URLs** - /users/123 în loc de /getUser?id=123
                - **JSON format** - standard pentru data exchange
                - **Status Codes** - 200 (success), 404 (not found), 500 (server error)
                """
            },
            {
                "question": "Care este diferența între SPA și aplicații tradiționale?",
                "answer": """
                **Single Page Applications (SPA):**
                - O singură pagină HTML, content dinamic via JavaScript
                - Client-side routing, fără page refreshes
                - Faster navigation după încărcarea inițială
                - Exemple: Gmail, Facebook, Twitter

                **Multi-Page Applications (MPA):**
                - Multiple pagini HTML, server-side rendering
                - Page refreshes la navigare
                - Better SEO și first-time loading
                - Exemple: Wikipedia, news websites
                """
            }
        ]

        for qa in qa_pairs:
            with st.expander(f"❓ {qa['question']}"):
                st.markdown(qa['answer'])

        st.markdown("### Întrebări React Specifice")

        react_qa = [
            {
                "question": "De ce să folosesc React în loc de vanilla JavaScript?",
                "answer": """
                **Avantajele React:**
                - **Component reusability** - scrii o dată, folosești oriunde
                - **Virtual DOM** - performance optimizat pentru UI updates  
                - **Declarative** - descrii starea finală, nu pașii
                - **Ecosystem** - soluții pentru orice problemă
                - **Developer tools** - debugging și development experience
                - **Job market** - cele mai multe oportunități de lucru
                """
            },
            {
                "question": "Ce este Virtual DOM și cum îmbunătățește performance?",
                "answer": """
                **Virtual DOM** - reprezentare în JavaScript a DOM-ului real:
                - React creează o copie virtuală a DOM-ului în memorie
                - La schimbări, compară virtual DOM vechi cu cel nou (diffing)
                - Aplică doar diferențele în DOM-ul real (reconciliation)
                - Mult mai rapid decât manipularea directă a DOM-ului
                - Permite batch updates și optimizări inteligente
                """
            },
            {
                "question": "Care este diferența între state și props?",
                "answer": """
                **Props (Properties):**
                - Date transmise DE LA component părinte CĂTRE copil
                - Read-only, nu pot fi modificate în componenta copil
                - Sunt ca argumentele unei funcții
                - Permit reutilizarea componentelor cu date diferite

                **State:**
                - Date INTERNE ale unui component
                - Pot fi modificate cu setState sau useState hook
                - Când se schimbă, componenta se re-renderează
                - Local la componenta respectivă
                """
            }
        ]

        for qa in react_qa:
            with st.expander(f"⚛️ {qa['question']}"):
                st.markdown(qa['answer'])

        st.markdown("### Tips pentru Interviuri ")

        st.markdown("""
        <div class="success-box">
            <h4>🎯 Strategii de Success:</h4>
            <ul>
                <li><strong>Vorbește în timp ce gândești</strong> - explică procesul de gândire</li>
                <li><strong>clarificări</strong> - asigură-te că înțelegi cerința</li>
                <li><strong>Începe simplu</strong> - construiește soluția pas cu pas</li>
                <li><strong>Testează edge cases</strong> - gândește la cazuri extreme</li>
                <li><strong>Optimizează gradual</strong> - first make it work, then make it fast</li>
                <li><strong>Cunoaște trade-offs</strong> - fiecare tehnologie are pros/cons</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
            <h4> Red Flags:</h4>
            <ul>
                <li>Nu spune "nu știu" fără să încerci să gândești</li>
                <li>Nu critica tehnologiile pe care nu le cunoști</li>
                <li>Nu da copy-paste răspunsuri fără înțelegere</li>
                <li>Nu ignora performance și scalability considerations</li>
                <li>Nu uita să întrebi despre requirements și constraints</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Final summary
    st.markdown("---")
    st.markdown("""
    
    """, unsafe_allow_html=True)


def html_css_page():
    """HTML & CSS fundamentals - Complete educational content"""
    st.markdown('<h1 class="chapter-header">HTML & CSS - Fundamentele</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Fundamentele care stau la baza oricărei aplicații web</h3>
        <p>HTML și CSS sunt pilonii dezvoltării web moderne. Fără o înțelegere solidă a acestora, 
        nu poți construi aplicații React performante și accesibile. Acest capitol acoperă conceptele 
        esențiale și avansate necesare pentru interviuri tehnice și dezvoltare profesională.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["HTML", "CSS"])

    with tab1:
        st.markdown('<h2 class="section-header">HTML (HyperText Markup Language)</h2>', unsafe_allow_html=True)

        # HTML Tabs
        html_tabs = st.tabs([
            "Fundamentele HTML",
            "Structura și Semantica",
            "HTML5 Modern",
            "Accessibility & SEO",
            "Best Practices",
            "Întrebări Interviu"
        ])

        with html_tabs[0]:
            st.markdown("### Ce este HTML și cum funcționează")

            st.markdown("""
            HTML este un limbaj de marcare care definește structura și semantica conținutului web. 
            Nu este un limbaj de programare, ci un sistem de etichete (tags) care descriu elementele unei pagini.
            """)

            st.markdown("### Anatomia unui document HTML")

            st.code("""
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descrierea paginii pentru SEO">
    <title>Titlul care apare în tab</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Acasă</a></li>
                <li><a href="#about">Despre</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <article>
                <h1>Titlu principal</h1>
                <p>Paragraf cu <strong>text important</strong> și <em>text accentuat</em>.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Numele companiei</p>
    </footer>
</body>
</html>
            """, language="html")

            st.markdown("### Concepte fundamentale")

            concepts = [
                {
                    "concept": "DOCTYPE Declaration",
                    "explanation": "Specifică versiunea HTML folosită. HTML5 folosește simplu '<!DOCTYPE html>'"
                },
                {
                    "concept": "Meta Tags",
                    "explanation": "Informații despre document: charset, viewport, description pentru SEO"
                },
                {
                    "concept": "Block vs Inline Elements",
                    "explanation": "Block (div, p, h1) ocupă toată lățimea; Inline (span, a, strong) doar spațiul necesar"
                },
                {
                    "concept": "Void Elements",
                    "explanation": "Tag-uri care nu se închid: <img>, <br>, <hr>, <input>, <meta>"
                }
            ]

            for concept in concepts:
                st.markdown(f"""
                <div class="step-box">
                    <strong>{concept['concept']}</strong>: {concept['explanation']}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### Tag-uri esențiale grupate pe categorii")

            tag_categories = {
                "Text și Tipografie": {
                    "h1-h6": "Headings - ierarhie de titluri",
                    "p": "Paragrafe de text",
                    "strong": "Text important (bold semantic)",
                    "em": "Text accentuat (italic semantic)",
                    "mark": "Text evidențiat (highlighter effect)",
                    "small": "Text de dimensiune mică (fine print)",
                    "blockquote": "Citate lungi cu cite attribute"
                },
                "Structură și Layout": {
                    "header": "Antetul paginii sau secțiunii",
                    "nav": "Navigare și meniuri",
                    "main": "Conținutul principal al paginii",
                    "section": "Secțiuni tematice",
                    "article": "Conținut independent și reutilizabil",
                    "aside": "Conținut complementar (sidebar)",
                    "footer": "Subsolul paginii sau secțiunii"
                },
                "Liste și Tabele": {
                    "ul/ol/li": "Liste neordonate/ordonate cu elemente",
                    "dl/dt/dd": "Liste de definiții (description lists)",
                    "table/thead/tbody/tr/td/th": "Structură completă pentru tabele"
                },
                "Multimedia": {
                    "img": "Imagini cu alt text obligatoriu",
                    "figure/figcaption": "Imagini cu legende semantice",
                    "video": "Conținut video cu controls",
                    "audio": "Conținut audio",
                    "picture": "Imagini responsive cu multiple surse"
                }
            }

            for category, tags in tag_categories.items():
                st.markdown(f"#### {category}")
                for tag, description in tags.items():
                    st.markdown(f"- **{tag}**: {description}")
                st.markdown("")

        with html_tabs[1]:
            st.markdown("### HTML Semantic - De ce contează")

            st.markdown("""
            HTML semantic folosește tag-uri care descriu semnificația conținutului, nu doar aspectul. 
            Aceasta îmbunătățește accesibilitatea, SEO-ul și mentenabilitatea codului.
            """)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Exemplu Non-Semantic (Greșit)**")
                st.code("""
<div class="header">
    <div class="nav">
        <div class="nav-item">Home</div>
        <div class="nav-item">About</div>
    </div>
</div>

<div class="content">
    <div class="title">Titlu articol</div>
    <div class="text">Conținutul articolului...</div>
</div>

<div class="footer">
    <div class="copyright">© 2025</div>
</div>
                """, language="html")

            with col2:
                st.markdown("**Exemplu Semantic (Corect)**")
                st.code("""
<header>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h1>Titlu articol</h1>
        <p>Conținutul articolului...</p>
    </article>
</main>

<footer>
    <p>&copy; 2025</p>
</footer>
                """, language="html")

            st.markdown("### Ierarhia heading-urilor")

            st.markdown("""
            <div class="warning-box">
                <h4>Regulile pentru h1-h6:</h4>
                <ul>
                    <li><strong>Un singur h1 per pagină</strong> - titlul principal</li>
                    <li><strong>Progresie logică</strong> - nu sări de la h1 la h3</li>
                    <li><strong>Nu folosi pentru styling</strong> - folosește CSS pentru mărime</li>
                    <li><strong>Screen readers</strong> le folosesc pentru navigare</li>
                    <li><strong>SEO impact</strong> - motoarele de căutare analizează ierarhia</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.code("""
<h1>Titlul principal al paginii</h1>
    <h2>Sectiunea 1</h2>
        <h3>Subsecțiunea 1.1</h3>
        <h3>Subsecțiunea 1.2</h3>
            <h4>Detaliu 1.2.1</h4>
    <h2>Secțiunea 2</h2>
        <h3>Subsecțiunea 2.1</h3>
            """, language="html")

        with html_tabs[2]:
            st.markdown("### HTML5 - Funcționalități moderne")

            st.markdown("#### Input Types noi în HTML5")

            html5_inputs = {
                "email": "Validare automată pentru adrese email",
                "tel": "Optimizat pentru numere de telefon",
                "url": "Validare pentru URL-uri",
                "number": "Input numeric cu min/max/step",
                "range": "Slider pentru valori numerice",
                "date": "Date picker nativ",
                "time": "Time picker pentru ore",
                "datetime-local": "Data și ora locale",
                "color": "Color picker nativ",
                "search": "Input optimizat pentru căutare"
            }

            st.code("""
<form>
    <input type="email" placeholder="email@example.com" required>
    <input type="tel" placeholder="+40 123 456 789">
    <input type="url" placeholder="https://example.com">
    <input type="number" min="1" max="100" step="1">
    <input type="range" min="0" max="100" value="50">
    <input type="date" min="2025-01-01">
    <input type="color" value="#ff0000">
    <input type="search" placeholder="Caută...">
</form>
            """, language="html")

            for input_type, description in html5_inputs.items():
                st.markdown(f"- **{input_type}**: {description}")

            st.markdown("#### Atribute HTML5 importante")

            attributes = {
                "data-*": "Atribute personalizate pentru stocare de date",
                "contenteditable": "Face orice element editabil",
                "draggable": "Activează drag and drop",
                "hidden": "Ascunde elementul complet",
                "spellcheck": "Controlează verificarea ortografică",
                "translate": "Controlează traducerea automată",
                "loading": "Controlează încărcarea imaginilor (lazy loading)"
            }

            st.code("""
<div data-user-id="123" data-role="admin">User info</div>
<p contenteditable="true">Text editabil</p>
<img src="image.jpg" loading="lazy" alt="Imagine">
<div draggable="true">Element care se poate trage</div>
<p spellcheck="false">Text fără spell check</p>
            """, language="html")

            for attr, description in attributes.items():
                st.markdown(f"- **{attr}**: {description}")

            st.markdown("#### Web Components și Custom Elements")

            st.code("""
<!-- Custom elements definite în JavaScript -->
<my-button type="primary" size="large">Click me</my-button>
<user-card data-user="john-doe"></user-card>

<!-- Shadow DOM pentru encapsulare -->
<template id="user-template">
    <style>
        .user { padding: 10px; border: 1px solid #ccc; }
    </style>
    <div class="user">
        <slot name="name"></slot>
        <slot name="email"></slot>
    </div>
</template>
            """, language="html")

        with html_tabs[3]:
            st.markdown("### Accessibility (a11y) și SEO")

            st.markdown("#### ARIA (Accessible Rich Internet Applications)")

            st.markdown("""
            ARIA oferă informații suplimentare pentru screen readers și alte tehnologii asistive 
            când HTML semantic nu este suficient.
            """)

            aria_examples = [
                {
                    "title": "aria-label și aria-labelledby",
                    "code": """<button aria-label="Închide fereastra">×</button>
<input type="search" aria-labelledby="search-label">
<label id="search-label">Caută produse</label>"""
                },
                {
                    "title": "aria-describedby pentru descrieri suplimentare",
                    "code": """<input type="password" aria-describedby="pwd-help">
<div id="pwd-help">Parola trebuie să aibă minim 8 caractere</div>"""
                },
                {
                    "title": "role pentru definirea rolului elementului",
                    "code": """<div role="button" tabindex="0">Buton personalizat</div>
<ul role="tablist">
    <li role="tab" aria-selected="true">Tab 1</li>
    <li role="tab" aria-selected="false">Tab 2</li>
</ul>"""
                },
                {
                    "title": "aria-expanded pentru elemente expandabile",
                    "code": """<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" aria-hidden="true">
    <li>Item 1</li>
    <li>Item 2</li>
</ul>"""
                }
            ]

            for example in aria_examples:
                st.markdown(f"**{example['title']}**")
                st.code(example['code'], language="html")
                st.markdown("")

            st.markdown("#### SEO Fundamentale")

            st.code("""
<head>
    <!-- Titulo specific fiecărei pagini (50-60 caractere) -->
    <title>Ghid HTML și CSS - Tutorial Complet</title>

    <!-- Meta description pentru rezultatele căutării -->
    <meta name="description" content="Învață HTML și CSS de la fundamentele până la conceptele avansate. Ghid complet cu exemple practice și best practices.">

    <!-- Open Graph pentru social media -->
    <meta property="og:title" content="Ghid HTML CSS">
    <meta property="og:description" content="Tutorial complet HTML CSS">
    <meta property="og:image" content="https://site.com/image.jpg">
    <meta property="og:url" content="https://site.com/html-css">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Ghid HTML CSS">

    <!-- Schema.org pentru structured data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": "HTML CSS Tutorial",
        "description": "Curs complet HTML și CSS",
        "provider": {
            "@type": "Organization", 
            "name": "Tutorial Site"
        }
    }
    </script>
</head>
            """, language="html")

        with html_tabs[4]:
            st.markdown("### Best Practices și Performance")

            st.markdown("#### Optimizarea imaginilor")

            st.code("""
<!-- Imagini responsive cu multiple surse -->
<picture>
    <source media="(min-width: 800px)" srcset="large.webp" type="image/webp">
    <source media="(min-width: 800px)" srcset="large.jpg">
    <source srcset="small.webp" type="image/webp">
    <img src="small.jpg" alt="Descriere detaliată" loading="lazy">
</picture>

<!-- Lazy loading pentru performanță -->
<img src="placeholder.jpg" 
     data-src="real-image.jpg" 
     loading="lazy" 
     alt="Descriere completă">

<!-- Preload pentru imagini critice -->
<link rel="preload" as="image" href="hero-image.jpg">
            """, language="html")

            st.markdown("#### Formulare accesibile și securizate")

            st.code("""
<form novalidate>
    <fieldset>
        <legend>Informații personale</legend>

        <div class="form-group">
            <label for="name">
                Nume complet
                <span class="required" aria-label="câmp obligatoriu">*</span>
            </label>
            <input type="text" 
                   id="name" 
                   name="name" 
                   required 
                   aria-describedby="name-error"
                   autocomplete="name">
            <div id="name-error" class="error" role="alert"></div>
        </div>

        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" 
                   id="email" 
                   name="email" 
                   required
                   autocomplete="email"
                   pattern="[^@]+@[^@]+\.[^@]+">
        </div>

        <button type="submit" aria-describedby="submit-help">
            Trimite formularul
        </button>
        <div id="submit-help">
            Apasă Enter sau click pentru a trimite
        </div>
    </fieldset>
</form>
            """, language="html")

            st.markdown("#### Performance și Loading")

            performance_tips = [
                "**Minifică HTML-ul** în producție pentru reducerea dimensiunii",
                "**Folosește CDN** pentru resursele statice",
                "**Preload** resurse critice cu <link rel='preload'>",
                "**Defer** script-uri non-critice cu defer sau async",
                "**Lazy load** imagini și conținut sub fold",
                "**Compresia gzip/brotli** pe server pentru transferuri mai rapide",
                "**Resource hints** pentru prefetch și preconnect"
            ]

            for tip in performance_tips:
                st.markdown(f"""
                <div class="step-box">
                    {tip}
                </div>
                """, unsafe_allow_html=True)

        with html_tabs[5]:
            st.markdown("### Întrebări frecvente la interviuri HTML")

            html_qa = [
                {
                    "question": "Care este diferența între div și span?",
                    "answer": """
                    **div** - element block-level:
                    - Ocupă toată lățimea disponibilă
                    - Începe pe o linie nouă
                    - Folosit pentru structurarea layout-ului
                    - Poate conține alte elemente block sau inline

                    **span** - element inline:
                    - Ocupă doar spațiul necesar conținutului
                    - Nu începe pe linie nouă
                    - Folosit pentru stilizarea textului în linie
                    - Poate conține doar alte elemente inline
                    """
                },
                {
                    "question": "Ce sunt void elements și de ce nu se închid?",
                    "answer": """
                    **Void elements** sunt tag-uri HTML care nu au conținut și nu necesită tag de închidere:

                    Exemple: <img>, <br>, <hr>, <input>, <meta>, <link>, <area>, <base>, <col>, <embed>, <source>, <track>, <wbr>

                    **De ce nu se închid:**
                    - Nu au conținut în interior
                    - Sunt self-contained (informațiile sunt în atribute)
                    - În XHTML se închid cu /> dar în HTML5 nu este necesar
                    - Încercarea de a le închide poate cauza probleme de parsing
                    """
                },
                {
                    "question": "Cum funcționează data attributes și la ce se folosesc?",
                    "answer": """
                    **Data attributes** (data-*) permit stocarea de informații personalizate în elemente HTML:

                    **Sintaxa:** data-[name]="value"
                    **Accesare JavaScript:** element.dataset.name sau getAttribute('data-name')
                    **CSS:** content: attr(data-name)

                    **Cazuri de utilizare:**
                    - Configurare componente JavaScript
                    - Stocarea ID-urilor pentru integrări
                    - Metadata pentru analytics
                    - State management simplu
                    - A/B testing flags
                    """
                },
                {
                    "question": "Care este diferența între strong și b, em și i?",
                    "answer": """
                    **Semantic vs Visual:**

                    **strong** - importanță semantică ridicată (bold)
                    **b** - doar stilizare bold fără semantică

                    **em** - accentuare semantică (italic)  
                    **i** - doar stilizare italic fără semantică

                    **De ce contează:**
                    - Screen readers interpretează diferit
                    - SEO înțelege importanța conținutului
                    - Mentenabilitatea codului este mai bună
                    - Separarea conținutului de prezentare
                    """
                }
            ]

            for qa in html_qa:
                with st.expander(f"❓ {qa['question']}"):
                    st.markdown(qa['answer'])

    with tab2:
        st.markdown('<h2 class="section-header">CSS (Cascading Style Sheets)</h2>', unsafe_allow_html=True)

        # CSS Tabs
        css_tabs = st.tabs([
            "Fundamentele CSS",
            "Selectors & Specificity",
            "Box Model & Layout",
            "Flexbox & Grid",
            "Responsive Design",
            "CSS Modern",
            "Performance & Best Practices",
            "Întrebări Interviu"
        ])

        with css_tabs[0]:
            st.markdown("### Cum funcționează CSS")

            st.markdown("""
            CSS (Cascading Style Sheets) controlează prezentarea elementelor HTML. 
            Principiul fundamental este separarea conținutului (HTML) de prezentare (CSS).
            """)

            st.markdown("#### Sintaxa CSS")

            st.code("""
/* Comentariu CSS */
selector {
    property: value;
    property: value value;
    property: value, value, value;
}

/* Exemple concrete */
h1 {
    color: #333;              /* Culoare text */
    font-size: 2rem;          /* Mărime font */
    margin-bottom: 1rem;      /* Spațiu exterior jos */
    font-family: Arial, sans-serif; /* Font cu fallback */
}

p {
    line-height: 1.6;         /* Înălțime linie */
    color: rgba(0, 0, 0, 0.8); /* Culoare cu transparență */
    text-align: justify;      /* Aliniere text */
}
            """, language="css")

            st.markdown("#### Unit measurements în CSS")

            units_data = {
                "Absolute Units": {
                    "px": "Pixels - unitatea de bază pentru ecrane",
                    "pt": "Points - folosită pentru print (1pt = 1/72 inch)",
                    "in": "Inches - pentru print",
                    "cm/mm": "Centimetri/milimetri - pentru print"
                },
                "Relative Units": {
                    "em": "Relativ la font-size-ul părintelui",
                    "rem": "Relativ la font-size-ul root (html)",
                    "%": "Procent din valoarea părintelui",
                    "vw/vh": "Viewport width/height (1vw = 1% din lățimea viewport-ului)",
                    "vmin/vmax": "Cel mai mic/mare dintre vw și vh",
                    "ch": "Lățimea caracterului '0' din fontul curent",
                    "ex": "Înălțimea caracterului 'x' din fontul curent"
                }
            }

            for category, units in units_data.items():
                st.markdown(f"**{category}:**")
                for unit, description in units.items():
                    st.markdown(f"- **{unit}**: {description}")
                st.markdown("")

            st.markdown("#### Cascading și Inheritance")

            st.code("""
/* Cascading - ordinea importanței */
element {
    color: blue;           /* 1. Browser defaults */
}

element {
    color: green !important; /* 2. !important declarations */
}

/* Inheritance - proprietăți moștenite */
body {
    font-family: Arial, sans-serif; /* Moștenit de toți copiii */
    color: #333;                     /* Moștenit de toți copiii */
}

div {
    /* Moștenește font-family și color de la body */
    border: 1px solid red;           /* NU se moștenește */
    margin: 10px;                    /* NU se moștenește */
}
            """, language="css")

        with css_tabs[1]:
            st.markdown("### CSS Selectors și Specificity")

            st.markdown("#### Tipuri de selectori")

            selectors_data = [
                {
                    "type": "Element Selector",
                    "syntax": "element",
                    "example": "p { color: blue; }",
                    "description": "Selectează toate elementele de acel tip"
                },
                {
                    "type": "Class Selector",
                    "syntax": ".class",
                    "example": ".highlight { background: yellow; }",
                    "description": "Selectează elemente cu clasa respectivă"
                },
                {
                    "type": "ID Selector",
                    "syntax": "#id",
                    "example": "#header { height: 100px; }",
                    "description": "Selectează elementul cu ID-ul respectiv"
                },
                {
                    "type": "Attribute Selector",
                    "syntax": "[attribute]",
                    "example": "[type='email'] { border: 2px solid green; }",
                    "description": "Selectează pe baza atributelor"
                },
                {
                    "type": "Descendant Selector",
                    "syntax": "parent child",
                    "example": "nav a { text-decoration: none; }",
                    "description": "Selectează copii la orice nivel"
                },
                {
                    "type": "Child Selector",
                    "syntax": "parent > child",
                    "example": "ul > li { list-style: none; }",
                    "description": "Selectează copii direcți"
                },
                {
                    "type": "Adjacent Sibling",
                    "syntax": "element + sibling",
                    "example": "h1 + p { margin-top: 0; }",
                    "description": "Urmașul imediat"
                },
                {
                    "type": "General Sibling",
                    "syntax": "element ~ sibling",
                    "example": "h1 ~ p { color: gray; }",
                    "description": "Toți urmașii de același nivel"
                }
            ]

            for selector in selectors_data:
                st.markdown(f"**{selector['type']}** (`{selector['syntax']}`)")
                st.code(selector['example'], language="css")
                st.markdown(f"{selector['description']}")
                st.markdown("")

            st.markdown("#### Pseudo-classes și Pseudo-elements")

            st.code("""
/* Pseudo-classes - stări ale elementelor */
a:hover { color: red; }              /* La hover */
a:focus { outline: 2px solid blue; }  /* La focus */
a:visited { color: purple; }         /* Link vizitat */
input:required { border-color: red; } /* Input obligatoriu */
input:valid { border-color: green; }  /* Input valid */
input:invalid { border-color: red; }  /* Input invalid */

li:first-child { font-weight: bold; } /* Primul copil */
li:last-child { margin-bottom: 0; }   /* Ultimul copil */
li:nth-child(2n) { background: #f0f0f0; } /* Copii pari */
li:nth-child(3n+1) { color: blue; }   /* Al 3-lea, 6-lea, etc. */

/* Pseudo-elements - părți ale elementelor */
p::first-line { font-weight: bold; }   /* Prima linie */
p::first-letter { font-size: 2em; }    /* Prima literă */
div::before { content: "→ "; }         /* Conținut înainte */
div::after { content: " ←"; }          /* Conținut după */
::selection { background: yellow; }     /* Text selectat */
            """, language="css")

            st.markdown("#### CSS Specificity - Calculul priorității")

            st.markdown("""
            <div class="warning-box">
                <h4>Calculul Specificity (a, b, c, d):</h4>
                <ul>
                    <li><strong>a</strong> - Inline styles (style attribute) = 1000</li>
                    <li><strong>b</strong> - IDs = 100</li>
                    <li><strong>c</strong> - Classes, attributes, pseudo-classes = 10</li>
                    <li><strong>d</strong> - Elements, pseudo-elements = 1</li>
                </ul>
                <p><strong>!important</strong> are prioritate maximă (10000)</p>
            </div>
            """, unsafe_allow_html=True)

            st.code("""
/* Exemple de specificity */
p { color: blue; }                    /* (0,0,0,1) = 1 */
.text { color: red; }                 /* (0,0,1,0) = 10 */
#main { color: green; }               /* (0,1,0,0) = 100 */
div p { color: yellow; }              /* (0,0,0,2) = 2 */
div .text { color: purple; }          /* (0,0,1,1) = 11 */
#main .text { color: orange; }        /* (0,1,1,0) = 110 */
p { color: black !important; }        /* !important câștigă */

/* Winner: #main .text cu specificity 110 */
            """, language="css")

        with css_tabs[2]:
            st.markdown("### Box Model și Layout Fundamentale")

            st.markdown("#### CSS Box Model explicat")

            st.markdown("""
            Fiecare element HTML este o cutie dreptunghiulară cu patru zone distincte:
            """)

            st.code("""
/* Box model standard */
.box {
    /* Content area */
    width: 200px;
    height: 100px;

    /* Padding - spațiu interior */
    padding: 20px;              /* Toate laturile */
    padding: 10px 20px;         /* Vertical | Horizontal */
    padding: 5px 10px 15px 20px; /* Top | Right | Bottom | Left */

    /* Border - marginea */
    border: 2px solid #333;
    border-width: 1px 2px 3px 4px; /* Diferite grosimi */
    border-style: solid dashed dotted ridge;
    border-color: red green blue yellow;

    /* Margin - spațiu exterior */
    margin: 10px;
    margin: 10px auto;          /* Centreaza orizontal */
    margin: -5px;               /* Margini negative */
}

/* Box-sizing control */
.standard-box {
    box-sizing: content-box;    /* Default: width = doar content */
}

.border-box {
    box-sizing: border-box;     /* width = content + padding + border */
}
            """, language="css")

            st.markdown("#### Display Types")

            display_types = {
                "block": "Ocupă toată lățimea, începe pe linie nouă (div, p, h1)",
                "inline": "Doar lățimea conținutului, pe aceeași linie (span, a, strong)",
                "inline-block": "Hybrid - lățimea conținutului dar acceptă width/height",
                "none": "Elementul dispare complet din layout",
                "flex": "Container flexibil pentru layout modern",
                "grid": "Container grid pentru layout 2D",
                "table": "Se comportă ca un tabel HTML",
                "inline-flex": "Flex container care se comportă inline",
                "inline-grid": "Grid container care se comportă inline"
            }

            for display, description in display_types.items():
                st.markdown(f"- **{display}**: {description}")

            st.markdown("#### Position și Z-index")

            st.code("""
/* Position values */
.static { position: static; }     /* Default - urmează flow-ul */
.relative { 
    position: relative;           /* Relativ la poziția normală */
    top: 10px;                   /* Offset de la poziția normală */
    left: 20px;
}
.absolute { 
    position: absolute;           /* Relativ la primul părinte pozitionat */
    top: 0;                      /* Relative to positioned parent */
    right: 0;
}
.fixed { 
    position: fixed;              /* Relativ la viewport */
    bottom: 20px;                /* Sticky la bottom */
    right: 20px;
}
.sticky { 
    position: sticky;             /* Hybrid relative/fixed */
    top: 0;                      /* Sticky când scrollezi */
}

/* Z-index pentru layering */
.background { z-index: -1; }      /* În spate */
.content { z-index: 1; }          /* Conținut normal */
.modal { z-index: 1000; }         /* Modal în față */
.tooltip { z-index: 9999; }       /* Tooltip peste tot */
            """, language="css")

        with css_tabs[3]:
            st.markdown("### Flexbox și CSS Grid")

            st.markdown("#### Flexbox - Layout unidimensional")

            st.code("""
/* Flex Container */
.flex-container {
    display: flex;

    /* Direction */
    flex-direction: row;          /* row | row-reverse | column | column-reverse */

    /* Wrapping */
    flex-wrap: wrap;              /* nowrap | wrap | wrap-reverse */

    /* Shorthand */
    flex-flow: row wrap;          /* direction + wrap */

    /* Main axis alignment */
    justify-content: space-between; /* flex-start | flex-end | center | 
                                       space-between | space-around | space-evenly */

    /* Cross axis alignment */
    align-items: center;          /* stretch | flex-start | flex-end | center | baseline */

    /* Multi-line cross axis */
    align-content: space-around;  /* stretch | flex-start | flex-end | center | 
                                     space-between | space-around | space-evenly */

    /* Gap între elemente */
    gap: 1rem;                    /* sau row-gap și column-gap separat */
}

/* Flex Items */
.flex-item {
    /* Growth factor */
    flex-grow: 1;                 /* Cât să crească relativ la alții */

    /* Shrink factor */
    flex-shrink: 0;               /* Cât să se micșoreze */

    /* Base size */
    flex-basis: 200px;            /* Mărimea de bază */

    /* Shorthand */
    flex: 1 0 200px;              /* grow shrink basis */
    flex: 1;                      /* grow: 1, shrink: 1, basis: 0 */

    /* Individual alignment */
    align-self: flex-end;         /* Suprascrie align-items pentru acest item */

    /* Order */
    order: 2;                     /* Schimbă ordinea vizuală */
}
            """, language="css")

            st.markdown("#### CSS Grid - Layout bidimensional")

            st.code("""
/* Grid Container */
.grid-container {
    display: grid;

    /* Define columns */
    grid-template-columns: 1fr 2fr 1fr;      /* Fracții flexibile */
    grid-template-columns: 200px 1fr 100px;  /* Pixeli și fracții */
    grid-template-columns: repeat(3, 1fr);   /* 3 coloane egale */
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive */

    /* Define rows */
    grid-template-rows: 100px auto 50px;
    grid-template-rows: repeat(3, 1fr);

    /* Named grid lines */
    grid-template-columns: [start] 250px [content-start] 1fr [content-end] 250px [end];

    /* Grid areas template */
    grid-template-areas: 
        "header header header"
        "sidebar content ads"
        "footer footer footer";

    /* Gaps */
    gap: 1rem;                    /* row-gap și column-gap */
    row-gap: 1rem;
    column-gap: 2rem;

    /* Alignment */
    justify-items: center;        /* Items alignment horizontal */
    align-items: center;          /* Items alignment vertical */
    justify-content: space-around; /* Grid alignment horizontal */
    align-content: space-around;   /* Grid alignment vertical */
}

/* Grid Items */
.grid-item {
    /* Position by line numbers */
    grid-column: 1 / 3;           /* From line 1 to line 3 */
    grid-row: 2 / 4;

    /* Position by span */
    grid-column: span 2;          /* Span 2 columns */
    grid-row: span 1;

    /* Named areas */
    grid-area: header;            /* Use named area */

    /* Shorthand */
    grid-area: 1 / 1 / 3 / 3;     /* row-start / col-start / row-end / col-end */

    /* Item alignment */
    justify-self: end;            /* Individual horizontal alignment */
    align-self: start;            /* Individual vertical alignment */
}
            """, language="css")

            st.markdown("### Flexbox vs Grid - Când să folosești ce")

            st.markdown("""
            <div class="info-box">
                <h4>Flexbox - Layout unidimensional:</h4>
                <ul>
                    <li><strong>Navigation bars</strong> - distribuirea spațiului pe o axă</li>
                    <li><strong>Button groups</strong> - alinierea elementelor inline</li>
                    <li><strong>Centering</strong> - centrarea perfectă pe ambele axe</li>
                    <li><strong>Equal height columns</strong> - coloane de aceeași înălțime</li>
                    <li><strong>Form layouts</strong> - alinierea label-urilor și input-urilor</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="success-box">
                <h4>CSS Grid - Layout bidimensional:</h4>
                <ul>
                    <li><strong>Page layouts</strong> - header, sidebar, content, footer</li>
                    <li><strong>Card grids</strong> - galerii de produse sau articole</li>
                    <li><strong>Complex forms</strong> - alinierea pe rânduri și coloane</li>
                    <li><strong>Dashboard layouts</strong> - panouri de control complexe</li>
                    <li><strong>Magazine layouts</strong> - layout-uri asimetrice creative</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with css_tabs[4]:
            st.markdown("### Responsive Design")

            st.markdown("#### Media Queries")

            st.code("""
/* Mobile First Approach */
/* Base styles pentru mobile */
.container {
    width: 100%;
    padding: 1rem;
}

/* Tablet */
@media screen and (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media screen and (min-width: 1024px) {
    .container {
        max-width: 1200px;
        padding: 2rem;
    }
}

/* Large Desktop */
@media screen and (min-width: 1440px) {
    .container {
        max-width: 1400px;
    }
}

/* Print styles */
@media print {
    .no-print { display: none; }
    body { font-size: 12pt; color: black; }
}

/* Landscape orientation */
@media screen and (orientation: landscape) {
    .mobile-menu { display: none; }
}

/* High DPI displays */
@media screen and (-webkit-min-device-pixel-ratio: 2) {
    .logo { background-image: url('logo@2x.png'); }
}

/* Prefers reduced motion */
@media (prefers-reduced-motion: reduce) {
    * { animation-duration: 0.01ms !important; }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    body { background: #1a1a1a; color: #ffffff; }
}
            """, language="css")

            st.markdown("#### Responsive Units și Techniques")

            st.code("""
/* Fluid Typography */
.title {
    /* Clamp pentru dimensiuni fluide */
    font-size: clamp(1.5rem, 4vw, 3rem); /* min, preferred, max */
}

/* Responsive Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* Aspect Ratio */
.video-container {
    aspect-ratio: 16 / 9;         /* Modern browsers */
    width: 100%;
}

/* Legacy aspect ratio */
.video-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;       /* 16:9 ratio */
}

.video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

/* Container Queries (New!) */
@container (min-width: 400px) {
    .card {
        display: flex;
        align-items: center;
    }
}

/* Responsive Grid */
.responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}
            """, language="css")

            st.markdown("#### Common Breakpoints")

            breakpoints_data = {
                "Mobile": "320px - 767px",
                "Tablet": "768px - 1023px",
                "Desktop": "1024px - 1439px",
                "Large Desktop": "1440px+",
                "Common breakpoints": "576px, 768px, 992px, 1200px, 1400px"
            }

            for device, size in breakpoints_data.items():
                st.markdown(f"- **{device}**: {size}")

        with css_tabs[5]:
            st.markdown("### CSS Modern Features")

            st.markdown("#### CSS Custom Properties (Variables)")

            st.code("""
/* Root variables */
:root {
    /* Colors */
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;

    /* Typography */
    --font-family: 'Inter', sans-serif;
    --font-size-base: 1rem;
    --font-size-large: 1.25rem;
    --line-height: 1.6;

    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 3rem;

    /* Breakpoints */
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;

    /* Shadows */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 25px rgba(0,0,0,0.15);
}

/* Usage */
.button {
    background-color: var(--primary-color);
    color: white;
    padding: var(--spacing-sm) var(--spacing-md);
    box-shadow: var(--shadow-sm);
    font-family: var(--font-family);
}

/* Dynamic theming */
[data-theme="dark"] {
    --primary-color: #4dabf7;
    --background-color: #1a1a1a;
    --text-color: #ffffff;
}

/* Fallback values */
.element {
    color: var(--text-color, #333); /* Fallback to #333 */
}
            """, language="css")

            st.markdown("#### Modern Layout și Animation")

            st.code("""
/* Scroll Snap */
.scroll-container {
    scroll-snap-type: x mandatory;
    overflow-x: scroll;
    display: flex;
}

.scroll-item {
    scroll-snap-align: start;
    flex: none;
    width: 100%;
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}

/* Modern Transitions */
.card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    transform: translateY(0);
}

.card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: var(--shadow-lg);
}

/* CSS Animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-100%);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.slide-in {
    animation: slideIn 0.5s ease-out forwards;
}

/* CSS Filters */
.image {
    filter: brightness(1.1) contrast(1.1) saturate(1.2);
    transition: filter 0.3s ease;
}

.image:hover {
    filter: brightness(1.2) contrast(1.2) saturate(1.3);
}

/* Backdrop Filter */
.glass-effect {
    backdrop-filter: blur(10px) saturate(150%);
    background: rgba(255, 255, 255, 0.8);
}

/* CSS Shapes */
.circular-text {
    shape-outside: circle(50%);
    float: left;
    width: 200px;
    height: 200px;
}
            """, language="css")

            st.markdown("#### CSS Logical Properties")

            st.code("""
/* Traditional properties */
.old-way {
    margin-left: 1rem;
    margin-right: 1rem;
    border-left: 1px solid #ccc;
    text-align: left;
}

/* Logical properties (RTL/LTR support) */
.new-way {
    margin-inline-start: 1rem;    /* left in LTR, right in RTL */
    margin-inline-end: 1rem;      /* right in LTR, left in RTL */
    border-inline-start: 1px solid #ccc;
    text-align: start;
}

/* Block and inline directions */
.element {
    margin-block-start: 1rem;     /* margin-top */
    margin-block-end: 1rem;       /* margin-bottom */
    margin-inline-start: 1rem;    /* margin-left in LTR */
    margin-inline-end: 1rem;      /* margin-right in LTR */

    padding-block: 1rem 2rem;     /* padding-top padding-bottom */
    padding-inline: 0.5rem 1rem;  /* padding-left padding-right in LTR */
}
            """, language="css")

        with css_tabs[6]:
            st.markdown("### Performance și Best Practices")

            st.markdown("#### CSS Performance Optimization")

            performance_tips = [
                {
                    "title": "Selector Performance",
                    "content": """
                    **Evită selectori complecși:**
                    ```css
                    /* Slow */
                    body div.container > ul li:nth-child(odd) a[href*="example"]

                    /* Fast */
                    .odd-link
                    ```

                    **Ordinea performanței (de la rapid la lent):**
                    1. ID selectors (#id)
                    2. Class selectors (.class)  
                    3. Element selectors (div)
                    4. Universal selector (*)
                    5. Attribute selectors ([type="text"])
                    6. Pseudo-classes (:hover)
                    """
                },
                {
                    "title": "CSS Loading Optimization",
                    "content": """
                    **Critical CSS inline:**
                    ```html
                    <style>
                        /* Above-the-fold styles */
                        .header { background: #333; }
                        .hero { height: 100vh; }
                    </style>

                    <!-- Non-critical CSS -->
                    <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
                    ```

                    **Minimize reflows și repaints:**
                    - Folosește transform în loc de left/top pentru animații
                    - Grupează DOM reads și writes
                    - Folosește will-change pentru animații
                    """
                },
                {
                    "title": "CSS Architecture",
                    "content": """
                    **BEM Methodology:**
                    ```css
                    /* Block */
                    .card { }

                    /* Element */
                    .card__title { }
                    .card__content { }

                    /* Modifier */
                    .card--featured { }
                    .card__title--large { }
                    ```

                    **Utility-first approach:**
                    ```css
                    .text-center { text-align: center; }
                    .mb-4 { margin-bottom: 1rem; }
                    .flex { display: flex; }
                    ```
                    """
                }
            ]

            for tip in performance_tips:
                st.markdown(f"#### {tip['title']}")
                st.markdown(tip['content'])
                st.markdown("")

            st.markdown("#### CSS Debugging Tips")

            st.code("""
/* Debug borders */
* {
    outline: 1px solid red;      /* Vezi toate elementele */
}

/* Debug specific elements */
.debug {
    background: rgba(255, 0, 0, 0.1);
    border: 1px solid red;
}

/* CSS Grid debugging */
.grid-container {
    display: grid;
    gap: 1px;
    background: red;             /* Gap-urile vor fi roșii */
}

.grid-item {
    background: white;           /* Items vor fi albe */
}

/* Print debug info */
.element::after {
    content: "Width: " attr(data-width) " Height: " attr(data-height);
    position: absolute;
    background: yellow;
    font-size: 12px;
    padding: 2px;
}
            """, language="css")

        with css_tabs[7]:
            st.markdown("### Întrebări frecvente la interviuri CSS")

            css_qa = [
                {
                    "question": "Care este diferența între margin și padding?",
                    "answer": """
                    **Margin** - spațiul exterior al elementului:
                    - Spațiul dintre element și elementele vecine
                    - Nu are culoare de fundal
                    - Poate avea valori negative
                    - Margin collapse între elemente adjacente
                    - Nu afectează dimensiunea clickable area

                    **Padding** - spațiul interior al elementului:
                    - Spațiul dintre conținut și border
                    - Moștenește culoarea fundalului elementului
                    - Nu poate avea valori negative
                    - Nu se collapse niciodată
                    - Face parte din clickable area
                    """
                },
                {
                    "question": "Cum funcționează CSS Specificity și cum se calculează?",
                    "answer": """
                    **Calculul specificity (a,b,c,d):**
                    - a: Inline styles (1000 points)
                    - b: IDs (100 points each)
                    - c: Classes, attributes, pseudo-classes (10 points each)
                    - d: Elements și pseudo-elements (1 point each)

                    **Exemple:**
                    - `p` = (0,0,0,1) = 1
                    - `.text` = (0,0,1,0) = 10
                    - `#main` = (0,1,0,0) = 100
                    - `div p.text` = (0,0,1,2) = 12
                    - `#main .text p` = (0,1,1,1) = 111

                    **Important:** !important are prioritate maximă (10000)
                    """
                },
                {
                    "question": "Care este diferența între display: none, visibility: hidden și opacity: 0?",
                    "answer": """
                    **display: none:**
                    - Elementul dispare complet din layout
                    - Nu ocupă spațiu
                    - Nu poate fi accesat cu tab
                    - Nu declanșează evenimente

                    **visibility: hidden:**
                    - Elementul nu este vizibil dar ocupă spațiu
                    - Layout-ul rămâne același
                    - Nu poate fi accesat cu tab
                    - Nu declanșează evenimente

                    **opacity: 0:**
                    - Elementul este invizibil dar ocupă spațiu
                    - Poate fi accesat cu tab
                    - Declanșează evenimente (clickable)
                    - Folosit pentru animații smooth
                    """
                },
                {
                    "question": "Cum funcționează CSS Grid vs Flexbox și când să folosești fiecare?",
                    "answer": """
                    **CSS Grid - Layout bidimensional:**
                    - Control complet pe rânduri și coloane
                    - Ideal pentru layout-uri complexe de pagină
                    - Poate poziționa elemente în orice celulă
                    - Named grid areas pentru semantic layout
                    - Auto-placement cu algoritmi inteligenți

                    **Flexbox - Layout unidimensional:**
                    - Control pe o singură axă (row sau column)
                    - Ideal pentru componente și alinierea elementelor
                    - Distribuția spațiului între elemente
                    - Centrarea perfectă pe ambele axe
                    - Ordinea vizuală fără schimbarea HTML

                    **Când să folosești:**
                    - Grid: page layouts, complex forms, dashboards
                    - Flexbox: navigation, buttons, centering, equal heights
                    """
                },
                {
                    "question": "Ce sunt CSS Custom Properties și cum se diferențiază de preprocessor variables?",
                    "answer": """
                    **CSS Custom Properties (--variables):**
                    - Native CSS, funcționează în browser
                    - Reactive - se actualizează dinamic
                    - Pot fi modificate cu JavaScript
                    - Respectă cascading și inheritance
                    - Suport pentru fallback values
                    - Scoped la selector

                    **Preprocessor Variables ($sass, @less):**
                    - Compilate la build time
                    - Static - nu se pot schimba runtime
                    - Nu există în CSS final
                    - Mai multe funcții (math, loops, conditionals)
                    - Nu sunt reactive la schimbări

                    **Exemple:**
                    ```css
                    /* CSS Custom Properties */
                    :root { --color: blue; }
                    .element { color: var(--color, red); }

                    /* JavaScript can change */
                    document.documentElement.style.setProperty('--color', 'green');
                    ```
                    """
                }
            ]

            for qa in css_qa:
                with st.expander(f"❓ {qa['question']}"):
                    st.markdown(qa['answer'])

    # Final summary
    st.markdown("---")
    st.markdown("""
    
    """, unsafe_allow_html=True)


def javascript_page():
    """JavaScript fundamentals - Complete educational content"""
    st.markdown('<h1 class="chapter-header">JavaScript - Limbajul Web-ului</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>JavaScript - Motorul interactivității web</h3>
        <p>JavaScript este limbajul de programare care aduce viață paginilor web. De la validarea formularelor 
        la aplicații complexe single-page, JavaScript este esențial pentru orice dezvoltator frontend. 
        Acest capitol acoperă tot ce trebuie să știi pentru a stăpâni JavaScript modern și pentru a reuși la interviuri tehnice.</p>
    </div>
    """, unsafe_allow_html=True)

    # JavaScript Tabs
    js_tabs = st.tabs([
        "Fundamentele JS",
        "Variables & Data Types",
        "Functions & Scope",
        "Objects & Arrays",
        "ES6+ Modern Features",
        "Asynchronous JavaScript",
        "DOM Manipulation",
        "Error Handling & Debugging",
        "Performance & Best Practices",
        "Întrebări Interviu"
    ])

    with js_tabs[0]:
        st.markdown("### Ce este JavaScript și cum funcționează")

        st.markdown("""
        JavaScript este un limbaj de programare interpretat, dinamic, cu tipizare slabă (loosely typed) 
        și suport pentru programare orientată pe obiecte, funcțională și procedurală. Rulează în browser 
        (client-side) și pe server (Node.js).
        """)

        st.markdown("#### JavaScript Engine și Execution Context")

        st.code("""
// JavaScript Engine Process:
// 1. Parsing - code → Abstract Syntax Tree (AST)
// 2. Compilation - AST → Bytecode  
// 3. Execution - Bytecode runs in Call Stack

// Execution Context are trei faze:
// 1. Creation Phase - Hoisting, Scope Chain, this binding
// 2. Execution Phase - Code runs line by line
// 3. Cleanup Phase - Garbage Collection

console.log(myVar); // undefined (not ReferenceError)
var myVar = 'Hello';

console.log(myFunc()); // "Hello World" - function is hoisted
function myFunc() {
    return 'Hello World';
}

// Let și const nu sunt hoisted în aceeași măsură
console.log(myLet); // ReferenceError: Cannot access before initialization
let myLet = 'World';
        """, language="javascript")

        st.markdown("#### Tipuri de date primitive și non-primitive")

        data_types = {
            "Primitive Types": {
                "number": "Numerele întregi și cu virgulă mobilă",
                "string": "Text încadrat în ghilimele",
                "boolean": "true sau false",
                "undefined": "Variabilă declarată dar fără valoare",
                "null": "Absența intenționată a unei valori",
                "symbol": "(ES6) Identificatori unici",
                "bigint": "(ES2020) Numere mari peste Number.MAX_SAFE_INTEGER"
            },
            "Non-Primitive Types": {
                "object": "Colecții de proprietăți key-value",
                "array": "Liste ordonate de valori",
                "function": "Blocuri de cod reutilizabile",
                "date": "Obiecte pentru data și ora",
                "regexp": "Expresii regulate pentru pattern matching"
            }
        }

        for category, types in data_types.items():
            st.markdown(f"**{category}:**")
            for type_name, description in types.items():
                st.markdown(f"- **{type_name}**: {description}")
            st.markdown("")

        st.code("""
// Type checking examples
console.log(typeof 42);           // "number"
console.log(typeof "Hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof null);         // "object" (JavaScript quirk!)
console.log(typeof {});           // "object"
console.log(typeof []);           // "object" (arrays are objects)
console.log(typeof function(){}); // "function"

// Precise type checking
console.log(Array.isArray([]));              // true
console.log(Object.prototype.toString.call([])); // "[object Array]"
console.log(null === null);                  // true (strict equality)
        """, language="javascript")

        st.markdown("#### Type Coercion și Truthy/Falsy Values")

        st.code("""
// Type Coercion - implicit conversion
console.log('5' + 3);    // "53" (number coerced to string)
console.log('5' - 3);    // 2 (string coerced to number)
console.log('5' * '2');  // 10 (both strings coerced to numbers)
console.log(true + 1);   // 2 (boolean coerced to number)

// Falsy values (doar acestea 8)
if (false) {}        // false
if (0) {}           // zero
if (-0) {}          // negative zero
if (0n) {}          // BigInt zero
if ("") {}          // empty string
if (null) {}        // null
if (undefined) {}   // undefined
if (NaN) {}         // Not a Number

// Everything else is truthy
if ("0") {}         // truthy (non-empty string)
if ("false") {}     // truthy (non-empty string)
if ([]) {}          // truthy (empty array is object)
if ({}) {}          // truthy (empty object)
if (function(){}) {} // truthy (functions are objects)

// Comparison quirks
console.log(null == undefined);  // true (abstract equality)
console.log(null === undefined); // false (strict equality)
console.log(NaN === NaN);        // false (NaN is not equal to itself)
console.log(Object.is(NaN, NaN)); // true (better equality check)
        """, language="javascript")

    with js_tabs[1]:
        st.markdown("### Variables și Declarații")

        st.markdown("#### var, let, const - Diferențele cruciale")

        st.code("""
// VAR - Function scoped, hoisted, can be redeclared
function varExample() {
    console.log(x); // undefined (hoisted but not initialized)

    if (true) {
        var x = 1;
        var x = 2; // Redeclaration allowed
    }

    console.log(x); // 2 (accessible outside block)
}

// LET - Block scoped, temporal dead zone, no redeclaration
function letExample() {
    // console.log(y); // ReferenceError: Cannot access before initialization

    if (true) {
        let y = 1;
        // let y = 2; // SyntaxError: Identifier 'y' has already been declared
        y = 3; // Reassignment is allowed
    }

    // console.log(y); // ReferenceError: y is not defined
}

// CONST - Block scoped, must be initialized, no reassignment
function constExample() {
    // const z; // SyntaxError: Missing initializer
    const z = 1;
    // z = 2; // TypeError: Assignment to constant variable

    // Objects și arrays pot fi mutate
    const obj = { name: 'John' };
    obj.name = 'Jane'; // Allowed - modifying property
    obj.age = 30;      // Allowed - adding property
    // obj = {}; // Error - reassigning the variable

    const arr = [1, 2, 3];
    arr.push(4);    // Allowed - modifying array
    arr[0] = 0;     // Allowed - changing element
    // arr = []; // Error - reassigning the variable
}
        """, language="javascript")

        st.markdown("#### Hoisting explicat în detaliu")

        st.code("""
// Function hoisting
console.log(add(2, 3)); // 5 - functions are fully hoisted

function add(a, b) {
    return a + b;
}

// Variable hoisting with var
console.log(name); // undefined (not ReferenceError)
var name = 'John';

// Equivalent to:
// var name; // Declaration hoisted
// console.log(name); // undefined
// name = 'John'; // Assignment stays in place

// Let/const hoisting (Temporal Dead Zone)
function temporalDeadZone() {
    // TDZ starts
    console.log(x); // ReferenceError
    console.log(y); // ReferenceError

    let x = 1;    // TDZ ends for x
    const y = 2;  // TDZ ends for y
}

// Function expressions are NOT hoisted
console.log(multiply); // undefined
console.log(multiply(2, 3)); // TypeError: multiply is not a function

var multiply = function(a, b) {
    return a * b;
};

// Arrow functions follow same rules as function expressions
console.log(divide); // ReferenceError (if using let/const)
const divide = (a, b) => a / b;
        """, language="javascript")

        st.markdown("#### Scope Chain și Lexical Scoping")

        st.code("""
// Global Scope
var globalVar = 'I am global';

function outerFunction(x) {
    // Function Scope
    var outerVar = 'I am outer';

    function innerFunction(y) {
        // Inner Function Scope
        var innerVar = 'I am inner';

        // Access to all scopes due to scope chain
        console.log(globalVar); // Accessible
        console.log(outerVar);  // Accessible  
        console.log(innerVar);  // Accessible
        console.log(x);         // Parameter accessible
        console.log(y);         // Parameter accessible
    }

    innerFunction(20);

    // console.log(innerVar); // ReferenceError
    // console.log(y); // ReferenceError
}

outerFunction(10);

// Block Scope (ES6+)
if (true) {
    let blockScoped = 'I am block scoped';
    var functionScoped = 'I am function scoped';
}

// console.log(blockScoped); // ReferenceError
console.log(functionScoped); // Accessible

// Lexical scoping example
function makeCounter() {
    let count = 0;

    return function() {
        return ++count; // Accesses outer variable
    };
}

const counter1 = makeCounter();
const counter2 = makeCounter();

console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter2()); // 1 (separate closure)
        """, language="javascript")

    with js_tabs[2]:
        st.markdown("### Functions și Scope Advanced")

        st.markdown("#### Function Declarations vs Expressions vs Arrow Functions")

        st.code("""
// Function Declaration - fully hoisted
function declaration(a, b) {
    return a + b;
}

// Function Expression - variable hoisted, function not
const expression = function(a, b) {
    return a + b;
};

// Named Function Expression - for recursion/debugging
const factorial = function fact(n) {
    return n <= 1 ? 1 : n * fact(n - 1);
};

// Arrow Functions - shorter syntax, lexical this
const arrow = (a, b) => a + b;

// Arrow function variations
const single = x => x * 2;                    // Single parameter
const noParams = () => 'Hello';               // No parameters
const multiLine = (x, y) => {                 // Multi-line
    const sum = x + y;
    return sum * 2;
};

// IIFE - Immediately Invoked Function Expression
(function(global) {
    var privateVar = 'I am private';
    global.publicVar = 'I am public';
})(window);

// Arrow IIFE
((name) => {
    console.log(`Hello ${name}`);
})('World');
        """, language="javascript")

        st.markdown("#### 'this' Keyword și Binding")

        st.code("""
// Global context
console.log(this); // Window object (browser) or global (Node.js)

// Object method
const person = {
    name: 'John',
    greet: function() {
        console.log(this.name); // 'John' - this refers to person
    },

    greetArrow: () => {
        console.log(this.name); // undefined - arrow functions don't bind this
    }
};

person.greet();      // 'John'
person.greetArrow(); // undefined

// Method extraction problem
const greetFunc = person.greet;
greetFunc(); // undefined - this is not person anymore

// Solutions for this binding
// 1. bind()
const boundGreet = person.greet.bind(person);
boundGreet(); // 'John'

// 2. call()
person.greet.call(person); // 'John'

// 3. apply()
person.greet.apply(person); // 'John'

// Constructor function
function Person(name) {
    this.name = name;
    this.greet = function() {
        console.log(`Hello, I'm ${this.name}`);
    };
}

const john = new Person('John');
john.greet(); // "Hello, I'm John"

// Event handlers context
button.addEventListener('click', function() {
    console.log(this); // button element
});

button.addEventListener('click', () => {
    console.log(this); // Window/global (arrow function)
});

// Class methods
class MyClass {
    constructor(name) {
        this.name = name;
    }

    method() {
        console.log(this.name); // Instance context
    }

    arrowMethod = () => {
        console.log(this.name); // Lexically bound to instance
    }
}
        """, language="javascript")

        st.markdown("#### Closures și Practical Applications")

        st.code("""
// Basic Closure
function createGreeting(greeting) {
    return function(name) {
        return `${greeting}, ${name}!`;
    };
}

const sayHello = createGreeting('Hello');
const sayGoodbye = createGreeting('Goodbye');

console.log(sayHello('John'));    // "Hello, John!"
console.log(sayGoodbye('Jane'));  // "Goodbye, Jane!"

// Module Pattern using Closures
const counterModule = (function() {
    let count = 0; // Private variable

    return {
        increment: function() {
            return ++count;
        },
        decrement: function() {
            return --count;
        },
        getCount: function() {
            return count;
        }
    };
})();

console.log(counterModule.increment()); // 1
console.log(counterModule.getCount());  // 1
// count is not accessible directly

// Practical: Function Factory
function createValidator(type) {
    const patterns = {
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phone: /^\+?[\d\s-()]+$/,
        zipCode: /^\d{5}(-\d{4})?$/
    };

    return function(value) {
        return patterns[type].test(value);
    };
}

const validateEmail = createValidator('email');
const validatePhone = createValidator('phone');

console.log(validateEmail('test@example.com')); // true
console.log(validatePhone('123-456-7890'));     // true

// Common Closure Pitfall in Loops
// Wrong way
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i); // 3, 3, 3 (not 0, 1, 2)
    }, 100);
}

// Correct ways
// 1. Using let (block scoped)
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i); // 0, 1, 2
    }, 100);
}

// 2. Using IIFE
for (var i = 0; i < 3; i++) {
    (function(index) {
        setTimeout(function() {
            console.log(index); // 0, 1, 2
        }, 100);
    })(i);
}

// 3. Using bind
for (var i = 0; i < 3; i++) {
    setTimeout(function(index) {
        console.log(index); // 0, 1, 2
    }.bind(null, i), 100);
}
        """, language="javascript")

    with js_tabs[3]:
        st.markdown("### Objects și Arrays Deep Dive")

        st.markdown("#### Object Creation și Manipulation")

        st.code("""
// Object creation methods
// 1. Object literal
const obj1 = {
    name: 'John',
    age: 30,
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

// 2. Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    return `Hello, I'm ${this.name}`;
};

const obj2 = new Person('Jane', 25);

// 3. Object.create()
const personPrototype = {
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

const obj3 = Object.create(personPrototype);
obj3.name = 'Bob';
obj3.age = 35;

// 4. Class syntax (ES6)
class PersonClass {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        return `Hello, I'm ${this.name}`;
    }
}

const obj4 = new PersonClass('Alice', 28);

// Property access methods
const key = 'name';
console.log(obj1.name);     // Dot notation
console.log(obj1['name']);  // Bracket notation
console.log(obj1[key]);     // Dynamic key access

// Property descriptor
Object.defineProperty(obj1, 'id', {
    value: 123,
    writable: false,      // Cannot be changed
    enumerable: false,    // Doesn't show in for...in
    configurable: false   // Cannot be deleted or redefined
});

// Object methods
const user = { name: 'John', age: 30, city: 'NYC' };

console.log(Object.keys(user));        // ['name', 'age', 'city']
console.log(Object.values(user));      // ['John', 30, 'NYC']
console.log(Object.entries(user));     // [['name', 'John'], ['age', 30], ['city', 'NYC']]

// Object.assign() for shallow copying
const userCopy = Object.assign({}, user);
const userCopy2 = { ...user }; // Spread operator (ES6)

// Deep vs Shallow copy
const original = {
    name: 'John',
    address: {
        city: 'NYC',
        zip: '10001'
    }
};

const shallowCopy = { ...original };
shallowCopy.address.city = 'LA'; // Modifies original too!

// Deep copy methods
const deepCopy1 = JSON.parse(JSON.stringify(original)); // Limited
const deepCopy2 = structuredClone(original); // Modern browsers

// Object destructuring
const { name, age, city = 'Unknown' } = user;
const { name: userName, ...rest } = user; // Rename and rest
        """, language="javascript")

        st.markdown("#### Array Methods și Functional Programming")

        st.code("""
const numbers = [1, 2, 3, 4, 5];
const users = [
    { id: 1, name: 'John', age: 30, active: true },
    { id: 2, name: 'Jane', age: 25, active: false },
    { id: 3, name: 'Bob', age: 35, active: true }
];

// Mutating methods (modify original array)
const arr1 = [1, 2, 3];
arr1.push(4);           // [1, 2, 3, 4] - add to end
arr1.pop();             // [1, 2, 3] - remove from end
arr1.unshift(0);        // [0, 1, 2, 3] - add to beginning
arr1.shift();           // [1, 2, 3] - remove from beginning
arr1.splice(1, 1, 'x'); // [1, 'x', 3] - remove/add at index
arr1.sort();            // Sort in place
arr1.reverse();         // Reverse in place

// Non-mutating methods (return new array)
const doubled = numbers.map(n => n * 2);           // [2, 4, 6, 8, 10]
const evens = numbers.filter(n => n % 2 === 0);    // [2, 4]
const sum = numbers.reduce((acc, n) => acc + n, 0); // 15

// Advanced array methods
const found = users.find(user => user.age > 30);        // First match
const foundIndex = users.findIndex(user => user.age > 30); // Index of first match
const hasActive = users.some(user => user.active);      // true if any match
const allActive = users.every(user => user.active);     // true if all match

// Chaining methods (functional style)
const result = users
    .filter(user => user.active)                    // Get active users
    .map(user => ({ ...user, age: user.age + 1 }))  // Increment age
    .sort((a, b) => a.age - b.age)                  // Sort by age
    .slice(0, 2);                                   // Take first 2

// Advanced reduce examples
// Group by property
const groupedByAge = users.reduce((acc, user) => {
    const age = user.age;
    if (!acc[age]) acc[age] = [];
    acc[age].push(user);
    return acc;
}, {});

// Count occurrences
const counts = ['apple', 'banana', 'apple', 'orange', 'banana'].reduce((acc, fruit) => {
    acc[fruit] = (acc[fruit] || 0) + 1;
    return acc;
}, {});

// Flatten nested arrays
const nested = [[1, 2], [3, 4], [5, 6]];
const flattened = nested.reduce((acc, arr) => acc.concat(arr), []);
// Or use flat()
const flattened2 = nested.flat();

// Array destructuring
const [first, second, ...rest] = numbers;  // first=1, second=2, rest=[3,4,5]
const [, , third] = numbers;               // Skip first two, get third

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];  // a=2, b=1

// Array.from() - create arrays
const range = Array.from({ length: 5 }, (_, i) => i + 1); // [1, 2, 3, 4, 5]
const chars = Array.from('Hello');                         // ['H', 'e', 'l', 'l', 'o']

// Set operations using arrays
const arr1 = [1, 2, 3, 4];
const arr2 = [3, 4, 5, 6];
const union = [...new Set([...arr1, ...arr2])];        // [1, 2, 3, 4, 5, 6]
const intersection = arr1.filter(x => arr2.includes(x)); // [3, 4]
const difference = arr1.filter(x => !arr2.includes(x));  // [1, 2]
        """, language="javascript")

    with js_tabs[4]:
        st.markdown("### ES6+ Modern JavaScript Features")

        st.markdown("#### Template Literals și Tagged Templates")

        st.code("""
// Template literals
const name = 'John';
const age = 30;

// Old way
const greeting1 = 'Hello, my name is ' + name + ' and I am ' + age + ' years old.';

// Template literal way
const greeting2 = `Hello, my name is ${name} and I am ${age} years old.`;

// Multi-line strings
const html = `
    <div class="user">
        <h2>${name}</h2>
        <p>Age: ${age}</p>
    </div>
`;

// Expression evaluation
const price = 19.99;
const tax = 0.08;
const total = `Total: $${(price * (1 + tax)).toFixed(2)}`;

// Tagged templates (advanced)
function highlight(strings, ...values) {
    return strings.reduce((result, string, i) => {
        const value = values[i] ? `<mark>${values[i]}</mark>` : '';
        return result + string + value;
    });
}

const highlighted = highlight`Hello ${name}, you are ${age} years old!`;
// "Hello <mark>John</mark>, you are <mark>30</mark> years old!"

// Styled components example pattern
const css = (strings, ...values) => {
    return strings.reduce((result, string, i) => {
        return result + string + (values[i] || '');
    });
};

const primaryColor = '#007bff';
const buttonStyles = css`
    background-color: ${primaryColor};
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
`;
        """, language="javascript")

        st.markdown("#### Destructuring Assignment Advanced")

        st.code("""
// Object destructuring
const user = {
    id: 1,
    name: 'John',
    email: 'john@example.com',
    address: {
        street: '123 Main St',
        city: 'NYC',
        country: 'USA'
    },
    hobbies: ['reading', 'coding', 'gaming']
};

// Basic destructuring
const { name, email } = user;

// Renaming variables
const { name: userName, email: userEmail } = user;

// Default values
const { name, age = 0, phone = 'N/A' } = user;

// Nested destructuring
const { address: { city, country } } = user;

// Rest in destructuring
const { name, ...userInfo } = user;

// Function parameter destructuring
function greetUser({ name, age = 0 }) {
    return `Hello ${name}, you are ${age} years old`;
}

greetUser(user); // "Hello John, you are 0 years old"

// Array destructuring
const colors = ['red', 'green', 'blue', 'yellow'];

// Basic
const [primary, secondary] = colors;

// Skip elements
const [first, , third] = colors;

// Rest elements
const [head, ...tail] = colors;

// Swapping variables
let a = 1, b = 2;
[a, b] = [b, a];

// Nested array destructuring
const matrix = [[1, 2], [3, 4], [5, 6]];
const [[a, b], [c, d]] = matrix;

// Mixed destructuring
const response = {
    data: {
        users: [
            { id: 1, name: 'John' },
            { id: 2, name: 'Jane' }
        ]
    },
    status: 200
};

const { 
    data: { 
        users: [firstUser, ...otherUsers] 
    }, 
    status 
} = response;
        """, language="javascript")

        st.markdown("#### Spread și Rest Operators")

        st.code("""
// Rest operator (...) - collect multiple elements
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15

// Rest in destructuring
const [first, ...rest] = [1, 2, 3, 4, 5];
// first = 1, rest = [2, 3, 4, 5]

const { name, ...userInfo } = { name: 'John', age: 30, city: 'NYC' };
// name = 'John', userInfo = { age: 30, city: 'NYC' }

// Spread operator (...) - spread elements
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Array spreading
const combined = [...arr1, ...arr2];        // [1, 2, 3, 4, 5, 6]
const withExtra = [0, ...arr1, 3.5, ...arr2, 7]; // [0, 1, 2, 3, 3.5, 4, 5, 6, 7]

// Object spreading
const user = { name: 'John', age: 30 };
const updatedUser = { ...user, age: 31, city: 'NYC' };
// { name: 'John', age: 31, city: 'NYC' }

// Function call spreading
const numbers = [1, 5, 3, 9, 2];
console.log(Math.max(...numbers)); // 9 (instead of Math.max.apply(null, numbers))

// Copying arrays and objects
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray];     // Shallow copy

const originalObject = { a: 1, b: 2 };
const copiedObject = { ...originalObject }; // Shallow copy

// Converting NodeList to Array
const divs = document.querySelectorAll('div');
const divsArray = [...divs];

// String to array
const chars = [...'Hello']; // ['H', 'e', 'l', 'l', 'o']

// Set to array
const uniqueNumbers = [...new Set([1, 2, 2, 3, 3, 4])]; // [1, 2, 3, 4]

// Practical examples
// Merge objects with precedence
const defaults = { theme: 'light', language: 'en' };
const userPrefs = { theme: 'dark' };
const config = { ...defaults, ...userPrefs }; 
// { theme: 'dark', language: 'en' }

// Add element to array immutably
const todos = ['Buy milk', 'Walk dog'];
const newTodos = [...todos, 'Pay bills'];

// Remove element immutably
const index = 1;
const filtered = [...todos.slice(0, index), ...todos.slice(index + 1)];
        """, language="javascript")

        st.markdown("#### Classes și Inheritance")

        st.code("""
// Basic class syntax
class Person {
    // Constructor
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this._id = Math.random(); // "private" by convention
    }

    // Instance method
    greet() {
        return `Hello, I'm ${this.name}`;
    }

    // Getter
    get info() {
        return `${this.name} (${this.age})`;
    }

    // Setter
    set age(value) {
        if (value < 0) throw new Error('Age cannot be negative');
        this._age = value;
    }

    get age() {
        return this._age;
    }

    // Static method
    static compareAge(person1, person2) {
        return person1.age - person2.age;
    }

    // Static property
    static species = 'Homo sapiens';
}

// Usage
const john = new Person('John', 30);
console.log(john.greet());     // "Hello, I'm John"
console.log(john.info);        // "John (30)" - getter
console.log(Person.species);   // "Homo sapiens" - static

// Inheritance
class Student extends Person {
    constructor(name, age, studentId) {
        super(name, age);           // Call parent constructor
        this.studentId = studentId;
    }

    // Override method
    greet() {
        return `${super.greet()}, I'm a student with ID ${this.studentId}`;
    }

    // Additional method
    study(subject) {
        return `${this.name} is studying ${subject}`;
    }
}

const jane = new Student('Jane', 22, 'S123');
console.log(jane.greet());      // "Hello, I'm Jane, I'm a student with ID S123"
console.log(jane.study('Math')); // "Jane is studying Math"

// Private fields (ES2022)
class BankAccount {
    #balance = 0;           // Private field
    #accountNumber;         // Private field

    constructor(accountNumber) {
        this.#accountNumber = accountNumber;
    }

    deposit(amount) {
        this.#balance += amount;
        return this.#balance;
    }

    withdraw(amount) {
        if (amount > this.#balance) {
            throw new Error('Insufficient funds');
        }
        this.#balance -= amount;
        return this.#balance;
    }

    get balance() {
        return this.#balance;
    }

    // Private method
    #validateTransaction(amount) {
        return amount > 0;
    }
}

const account = new BankAccount('ACC123');
account.deposit(100);
// console.log(account.#balance); // SyntaxError: Private field '#balance' must be declared in an enclosing class

// Mixins pattern
const Flyable = {
    fly() {
        return `${this.name} is flying`;
    }
};

const Swimmable = {
    swim() {
        return `${this.name} is swimming`;
    }
};

class Duck extends Person {
    constructor(name) {
        super(name, 0);
    }
}

// Add mixins
Object.assign(Duck.prototype, Flyable, Swimmable);

const duck = new Duck('Donald');
console.log(duck.fly());   // "Donald is flying"
console.log(duck.swim());  // "Donald is swimming"
        """, language="javascript")

    with js_tabs[5]:
        st.markdown("### Asynchronous JavaScript")

        st.markdown("#### Promises și Promise Chains")

        st.code("""
// Creating a Promise
const myPromise = new Promise((resolve, reject) => {
    const success = Math.random() > 0.5;

    setTimeout(() => {
        if (success) {
            resolve('Operation successful!');
        } else {
            reject(new Error('Operation failed!'));
        }
    }, 1000);
});

// Consuming a Promise
myPromise
    .then(result => {
        console.log(result);
        return result.toUpperCase(); // Return value for next then
    })
    .then(upperResult => {
        console.log(upperResult);
    })
    .catch(error => {
        console.error('Error:', error.message);
    })
    .finally(() => {
        console.log('Promise settled (resolved or rejected)');
    });

// Promise utilities
const promise1 = Promise.resolve(1);
const promise2 = Promise.resolve(2);
const promise3 = Promise.resolve(3);
const rejectedPromise = Promise.reject(new Error('Failed'));

// Promise.all - waits for all to resolve
Promise.all([promise1, promise2, promise3])
    .then(results => console.log(results)); // [1, 2, 3]

// Promise.allSettled - waits for all to settle
Promise.allSettled([promise1, promise2, rejectedPromise])
    .then(results => console.log(results));
    // [
    //   { status: 'fulfilled', value: 1 },
    //   { status: 'fulfilled', value: 2 },
    //   { status: 'rejected', reason: Error }
    // ]

// Promise.race - first to settle wins
Promise.race([promise1, promise2, promise3])
    .then(result => console.log(result)); // 1 (first to resolve)

// Promise.any - first to resolve wins (ignores rejections)
Promise.any([rejectedPromise, promise2, promise3])
    .then(result => console.log(result)); // 2

// Practical example: API calls
function fetchUser(id) {
    return fetch(`/api/users/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        });
}

function fetchUserPosts(userId) {
    return fetch(`/api/users/${userId}/posts`)
        .then(response => response.json());
}

// Sequential API calls
fetchUser(1)
    .then(user => {
        console.log('User:', user);
        return fetchUserPosts(user.id);
    })
    .then(posts => {
        console.log('Posts:', posts);
    })
    .catch(error => {
        console.error('Error fetching user data:', error);
    });

// Parallel API calls
Promise.all([
    fetchUser(1),
    fetchUserPosts(1)
])
.then(([user, posts]) => {
    console.log('User and posts loaded:', { user, posts });
})
.catch(error => {
    console.error('Error:', error);
});
        """, language="javascript")

        st.markdown("#### Async/Await Syntax")

        st.code("""
// Async function declaration
async function fetchUserData(id) {
    try {
        const response = await fetch(`/api/users/${id}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const user = await response.json();
        const posts = await fetchUserPosts(user.id);

        return { user, posts };
    } catch (error) {
        console.error('Error:', error);
        throw error; // Re-throw to allow caller to handle
    }
}

// Async arrow function
const fetchUserDataArrow = async (id) => {
    const user = await fetchUser(id);
    const posts = await fetchUserPosts(id);
    return { user, posts };
};

// Using async function
async function main() {
    try {
        const userData = await fetchUserData(1);
        console.log('User data:', userData);
    } catch (error) {
        console.error('Failed to fetch user data:', error);
    }
}

main();

// Error handling patterns
async function handleErrors() {
    try {
        const result = await riskyOperation();
        return result;
    } catch (error) {
        if (error.name === 'NetworkError') {
            // Retry logic
            return await retryOperation();
        }
        throw error; // Re-throw unknown errors
    }
}

// Parallel execution with async/await
async function fetchMultipleUsers(ids) {
    // Wrong way - sequential
    const users = [];
    for (const id of ids) {
        const user = await fetchUser(id); // Waits for each one
        users.push(user);
    }
    return users;
}

async function fetchMultipleUsersParallel(ids) {
    // Correct way - parallel
    const promises = ids.map(id => fetchUser(id));
    const users = await Promise.all(promises);
    return users;
}

// Async iteration
async function processUsers(userIds) {
    for (const id of userIds) {
        try {
            const user = await fetchUser(id);
            await processUser(user);
            console.log(`Processed user ${id}`);
        } catch (error) {
            console.error(`Failed to process user ${id}:`, error);
        }
    }
}

// Async generators (advanced)
async function* fetchUsersPaginated(pageSize = 10) {
    let page = 1;
    let hasMore = true;

    while (hasMore) {
        const response = await fetch(`/api/users?page=${page}&size=${pageSize}`);
        const data = await response.json();

        yield data.users;

        hasMore = data.hasMore;
        page++;
    }
}

// Using async generator
async function processAllUsers() {
    for await (const users of fetchUsersPaginated()) {
        users.forEach(user => console.log(user.name));
    }
}

// Top-level await (ES2022)
// Can use await at module level
const userData = await fetchUserData(1);
console.log(userData);

// Async IIFE for older environments
(async () => {
    const userData = await fetchUserData(1);
    console.log(userData);
})();
        """, language="javascript")

        st.markdown("#### Event Loop și Concurrency Model")

        st.code("""
// Understanding the Event Loop
console.log('1: Start');

setTimeout(() => {
    console.log('2: setTimeout 0ms');
}, 0);

Promise.resolve().then(() => {
    console.log('3: Promise then');
});

console.log('4: End');

// Output order: 1, 4, 3, 2
// Explanation:
// 1. Call stack: synchronous code runs first
// 2. Microtask queue: Promises, queueMicrotask
// 3. Macrotask queue: setTimeout, setInterval, DOM events

// Microtasks vs Macrotasks
console.log('Start');

// Macrotask
setTimeout(() => console.log('setTimeout 1'), 0);
setTimeout(() => console.log('setTimeout 2'), 0);

// Microtasks
Promise.resolve().then(() => console.log('Promise 1'));
Promise.resolve().then(() => console.log('Promise 2'));

queueMicrotask(() => console.log('queueMicrotask'));

console.log('End');

// Output: Start, End, Promise 1, Promise 2, queueMicrotask, setTimeout 1, setTimeout 2

// Blocking vs Non-blocking code
// Blocking (bad)
function blockingOperation() {
    const start = Date.now();
    while (Date.now() - start < 3000) {
        // Block for 3 seconds
    }
    return 'Done';
}

// Non-blocking (good)
function nonBlockingOperation() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('Done');
        }, 3000);
    });
}

// Worker threads for CPU-intensive tasks
// main.js
const worker = new Worker('worker.js');
worker.postMessage({ numbers: [1, 2, 3, 4, 5] });
worker.onmessage = (event) => {
    console.log('Result from worker:', event.data);
};

// worker.js
self.onmessage = (event) => {
    const { numbers } = event.data;
    const result = numbers.reduce((sum, num) => sum + num, 0);
    self.postMessage(result);
};

// Debouncing and Throttling
function debounce(func, delay) {
    let timeoutId;
    return function (...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

function throttle(func, delay) {
    let inThrottle;
    return function (...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, delay);
        }
    };
}

// Usage
const debouncedSearch = debounce((query) => {
    console.log('Searching for:', query);
}, 300);

const throttledScroll = throttle(() => {
    console.log('Scroll event');
}, 100);

// Event listeners
input.addEventListener('input', debouncedSearch);
window.addEventListener('scroll', throttledScroll);
        """, language="javascript")

    with js_tabs[6]:
        st.markdown("### DOM Manipulation")

        st.markdown("#### DOM Selection și Traversal")

        st.code("""
// DOM Selection Methods
// Single element selection
const elementById = document.getElementById('myId');
const elementByQuery = document.querySelector('.my-class');
const elementByTag = document.getElementsByTagName('div')[0];

// Multiple element selection
const elementsByClass = document.getElementsByClassName('my-class');
const elementsByQuery = document.querySelectorAll('.my-class');
const elementsByTag = document.getElementsByTagName('div');

// Modern selection with error handling
function safeQuery(selector) {
    try {
        const element = document.querySelector(selector);
        if (!element) {
            console.warn(`Element not found: ${selector}`);
            return null;
        }
        return element;
    } catch (error) {
        console.error(`Invalid selector: ${selector}`, error);
        return null;
    }
}

// DOM Traversal
const element = document.querySelector('.container');

// Parent traversal
const parent = element.parentElement;
const parentNode = element.parentNode; // includes text nodes
const closestContainer = element.closest('.wrapper'); // Up the tree until match

// Child traversal
const children = element.children;          // HTMLCollection of element children
const childNodes = element.childNodes;      // NodeList including text nodes
const firstChild = element.firstElementChild;
const lastChild = element.lastElementChild;

// Sibling traversal
const nextSibling = element.nextElementSibling;
const prevSibling = element.previousElementSibling;

// Advanced traversal
function getAllSiblings(element) {
    const siblings = [];
    let sibling = element.parentElement.firstElementChild;

    while (sibling) {
        if (sibling !== element) {
            siblings.push(sibling);
        }
        sibling = sibling.nextElementSibling;
    }

    return siblings;
}

// Tree walking
function walkDOM(element, callback) {
    callback(element);
    element = element.firstElementChild;

    while (element) {
        walkDOM(element, callback);
        element = element.nextElementSibling;
    }
}

// Usage
walkDOM(document.body, (el) => {
    if (el.classList.contains('highlight')) {
        console.log('Found highlighted element:', el);
    }
});
        """, language="javascript")

        st.markdown("#### DOM Manipulation și Creation")

        st.code("""
// Creating elements
const div = document.createElement('div');
const text = document.createTextNode('Hello World');
const fragment = document.createDocumentFragment(); // Performance optimization

// Setting attributes and properties
div.id = 'myDiv';
div.className = 'container active';
div.classList.add('new-class');
div.classList.remove('old-class');
div.classList.toggle('visible');
div.classList.contains('active'); // true/false

div.setAttribute('data-id', '123');
div.setAttribute('data-role', 'button');
const dataId = div.getAttribute('data-id');
div.removeAttribute('data-role');

// Modern dataset API
div.dataset.userId = '456';        // Sets data-user-id
div.dataset.userName = 'john';     // Sets data-user-name
console.log(div.dataset.userId);   // Gets data-user-id

// Setting content
div.textContent = 'Plain text'; // Safe, escapes HTML
div.innerHTML = '<span>HTML content</span>'; // Potentially unsafe
div.innerText = 'Visible text'; // Considers CSS styling

// Inserting elements
// Old way
parent.appendChild(div);
parent.insertBefore(div, referenceElement);

// Modern way (more flexible)
div.insertAdjacentElement('beforebegin', newElement); // Before div
div.insertAdjacentElement('afterbegin', newElement);  // First child of div
div.insertAdjacentElement('beforeend', newElement);   // Last child of div
div.insertAdjacentElement('afterend', newElement);    // After div

div.insertAdjacentHTML('beforeend', '<span>New span</span>');
div.insertAdjacentText('afterbegin', 'Text content');

// Modern insertion methods
div.prepend(element1, element2, 'text'); // Add to beginning
div.append(element1, element2, 'text');  // Add to end
div.before(element);                     // Insert before div
div.after(element);                      // Insert after div
div.replaceWith(newElement);             // Replace div entirely

// Removing elements
// Old way
parent.removeChild(element);

// Modern way
element.remove();

// Performance optimization with DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
    const li = document.createElement('li');
    li.textContent = `Item ${i}`;
    fragment.appendChild(li); // No reflow/repaint yet
}
ul.appendChild(fragment); // Single reflow/repaint

// Cloning elements
const clone = element.cloneNode(false); // Shallow clone
const deepClone = element.cloneNode(true); // Deep clone with children

// Template element (HTML5)
const template = document.querySelector('#my-template');
const templateContent = template.content.cloneNode(true);
document.body.appendChild(templateContent);

// Dynamic element creation utility
function createElement(tag, attributes = {}, children = []) {
    const element = document.createElement(tag);

    // Set attributes
    Object.entries(attributes).forEach(([key, value]) => {
        if (key === 'className') {
            element.className = value;
        } else if (key === 'dataset') {
            Object.assign(element.dataset, value);
        } else if (key.startsWith('on') && typeof value === 'function') {
            element.addEventListener(key.slice(2), value);
        } else {
            element.setAttribute(key, value);
        }
    });

    // Add children
    children.forEach(child => {
        if (typeof child === 'string') {
            element.appendChild(document.createTextNode(child));
        } else if (child instanceof Element) {
            element.appendChild(child);
        }
    });

    return element;
}

// Usage
const button = createElement('button', {
    className: 'btn btn-primary',
    dataset: { action: 'submit', id: '123' },
    onclick: () => console.log('Clicked!')
}, ['Submit']);
        """, language="javascript")

        st.markdown("#### Event Handling Advanced")

        st.code("""
// Event listener basics
const button = document.querySelector('#myButton');

// Multiple ways to add listeners
button.onclick = handleClick;                    // Property (overwrites previous)
button.addEventListener('click', handleClick);   // Method (can add multiple)
button.addEventListener('click', handleClick, {  // With options
    once: true,        // Remove after first trigger
    passive: true,     // Never calls preventDefault
    capture: true      // Capture phase instead of bubbling
});

function handleClick(event) {
    console.log('Button clicked!', event);
}

// Event object properties
function handleEvent(event) {
    console.log('Type:', event.type);              // 'click', 'keydown', etc.
    console.log('Target:', event.target);          // Element that triggered event
    console.log('Current Target:', event.currentTarget); // Element with listener
    console.log('Timestamp:', event.timeStamp);    // When event occurred

    // Mouse events
    if (event instanceof MouseEvent) {
        console.log('Mouse position:', event.clientX, event.clientY);
        console.log('Button pressed:', event.button); // 0=left, 1=middle, 2=right
        console.log('Modifier keys:', {
            ctrl: event.ctrlKey,
            shift: event.shiftKey,
            alt: event.altKey,
            meta: event.metaKey
        });
    }

    // Keyboard events
    if (event instanceof KeyboardEvent) {
        console.log('Key:', event.key);         // 'a', 'Enter', 'ArrowUp'
        console.log('Code:', event.code);       // 'KeyA', 'Enter', 'ArrowUp'
        console.log('Key code:', event.keyCode); // Deprecated but still used
    }

    // Prevent default behavior
    event.preventDefault();

    // Stop event propagation
    event.stopPropagation();
    event.stopImmediatePropagation(); // Also stops other listeners on same element
}

// Event delegation (performance optimization)
document.addEventListener('click', function(event) {
    // Handle clicks on buttons anywhere in document
    if (event.target.matches('button')) {
        console.log('Button clicked:', event.target.textContent);
    }

    // Handle clicks on elements with specific class
    if (event.target.closest('.card')) {
        console.log('Card clicked:', event.target.closest('.card'));
    }
});

// Custom events
const customEvent = new CustomEvent('userLogin', {
    detail: { userId: 123, userName: 'john' }
});

// Listen for custom event
document.addEventListener('userLogin', function(event) {
    console.log('User logged in:', event.detail);
});

// Dispatch custom event
document.dispatchEvent(customEvent);

// Event delegation utility
function delegate(parent, eventType, selector, handler) {
    parent.addEventListener(eventType, function(event) {
        const target = event.target.closest(selector);
        if (target && parent.contains(target)) {
            handler.call(target, event);
        }
    });
}

// Usage
delegate(document, 'click', '.btn', function(event) {
    console.log('Button clicked:', this.textContent);
});

// Removing event listeners
function removeListeners() {
    button.removeEventListener('click', handleClick);

    // For anonymous functions, store reference
    const handler = (e) => console.log('Clicked');
    button.addEventListener('click', handler);
    button.removeEventListener('click', handler);
}

// Event listener cleanup for SPA
class ComponentManager {
    constructor() {
        this.listeners = [];
    }

    addEventListener(element, type, handler, options) {
        element.addEventListener(type, handler, options);
        this.listeners.push({ element, type, handler });
    }

    cleanup() {
        this.listeners.forEach(({ element, type, handler }) => {
            element.removeEventListener(type, handler);
        });
        this.listeners = [];
    }
}

// Throttling scroll events for performance
let scrollTimeout;
window.addEventListener('scroll', function() {
    if (scrollTimeout) return;

    scrollTimeout = setTimeout(() => {
        console.log('Scroll event processed');
        scrollTimeout = null;
    }, 16); // ~60fps
});

// Intersection Observer for efficient scroll tracking
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            console.log('Element is visible:', entry.target);
        }
    });
});

// Observe elements
document.querySelectorAll('.observe-me').forEach(el => {
    observer.observe(el);
});
        """, language="javascript")

    with js_tabs[7]:
        st.markdown("### Error Handling și Debugging")

        st.markdown("#### Try-Catch și Error Types")

        st.code("""
// Basic try-catch
try {
    const result = riskyOperation();
    console.log(result);
} catch (error) {
    console.error('An error occurred:', error.message);
} finally {
    console.log('This always runs');
}

// Different error types
try {
    // Syntax errors (caught at parse time, not runtime)
    // eval('const x = ;'); // SyntaxError

    // Reference errors
    console.log(undefinedVariable); // ReferenceError

    // Type errors
    null.someMethod(); // TypeError

    // Range errors
    new Array(-1); // RangeError

} catch (error) {
    console.log('Error type:', error.constructor.name);
    console.log('Error message:', error.message);
    console.log('Stack trace:', error.stack);

    // Handle different error types
    if (error instanceof ReferenceError) {
        console.log('Variable not defined');
    } else if (error instanceof TypeError) {
        console.log('Wrong type or method not found');
    } else if (error instanceof SyntaxError) {
        console.log('Syntax error in code');
    }
}

// Creating custom errors
class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = 'ValidationError';
        this.field = field;
    }
}

class NetworkError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.name = 'NetworkError';
        this.statusCode = statusCode;
    }
}

// Using custom errors
function validateUser(user) {
    if (!user.email) {
        throw new ValidationError('Email is required', 'email');
    }
    if (!user.email.includes('@')) {
        throw new ValidationError('Invalid email format', 'email');
    }
}

try {
    validateUser({ name: 'John' });
} catch (error) {
    if (error instanceof ValidationError) {
        console.log(`Validation failed for ${error.field}: ${error.message}`);
    } else {
        console.log('Unexpected error:', error);
    }
}

// Async error handling
async function asyncErrorHandling() {
    try {
        const response = await fetch('/api/data');

        if (!response.ok) {
            throw new NetworkError(
                `Request failed: ${response.statusText}`,
                response.status
            );
        }

        const data = await response.json();
        return data;
    } catch (error) {
        if (error instanceof NetworkError) {
            if (error.statusCode === 404) {
                console.log('Resource not found');
            } else if (error.statusCode >= 500) {
                console.log('Server error, please try again later');
            }
        } else if (error instanceof TypeError) {
            console.log('Network error or JSON parsing failed');
        }

        throw error; // Re-throw to allow caller to handle
    }
}

// Error boundaries pattern (React-inspired)
class ErrorHandler {
    constructor() {
        this.errorCallbacks = [];
        this.setupGlobalHandlers();
    }

    setupGlobalHandlers() {
        // Catch unhandled errors
        window.addEventListener('error', (event) => {
            this.handleError(event.error, 'Global Error');
        });

        // Catch unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            this.handleError(event.reason, 'Unhandled Promise Rejection');
        });
    }

    handleError(error, context) {
        console.error(`${context}:`, error);

        // Log to external service
        this.logError(error, context);

        // Notify error callbacks
        this.errorCallbacks.forEach(callback => {
            try {
                callback(error, context);
            } catch (callbackError) {
                console.error('Error in error callback:', callbackError);
            }
        });
    }

    logError(error, context) {
        // Send to monitoring service (Sentry, LogRocket, etc.)
        const errorData = {
            message: error.message,
            stack: error.stack,
            context,
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent,
            url: window.location.href
        };

        // Example: send to monitoring service
        // fetch('/api/errors', {
        //     method: 'POST',
        //     body: JSON.stringify(errorData)
        // });
    }

    onError(callback) {
        this.errorCallbacks.push(callback);
    }
}

const errorHandler = new ErrorHandler();
errorHandler.onError((error, context) => {
    // Show user-friendly error message
    showErrorToast(`Something went wrong. Please try again.`);
});
        """, language="javascript")

        st.markdown("#### Debugging Techniques")

        st.code("""
// Console methods beyond console.log
console.log('Basic log');
console.info('Information');
console.warn('Warning message');
console.error('Error message');

// Styled console output
console.log('%cStyled text', 'color: blue; font-size: 20px; font-weight: bold;');

// Grouping console output
console.group('User Data');
console.log('Name: John');
console.log('Age: 30');
console.groupEnd();

// Conditional logging
const DEBUG = true;
console.assert(DEBUG, 'Debug mode is off');

// Timing operations
console.time('Operation');
// Some operation
setTimeout(() => {
    console.timeEnd('Operation'); // Operation: 1000.123ms
}, 1000);

// Table display for objects/arrays
const users = [
    { name: 'John', age: 30, city: 'NYC' },
    { name: 'Jane', age: 25, city: 'LA' }
];
console.table(users);

// Stack trace
console.trace('Trace point');

// Counting occurrences
function countClicks() {
    console.count('Button clicks'); // Button clicks: 1, 2, 3...
}

// Performance debugging
function measurePerformance(fn, iterations = 1000) {
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
        fn();
    }

    const end = performance.now();
    console.log(`Function took ${end - start} milliseconds`);
}

// Memory usage (Chrome DevTools)
function checkMemory() {
    if (performance.memory) {
        console.log('Used JS Heap Size:', 
            (performance.memory.usedJSHeapSize / 1024 / 1024).toFixed(2) + ' MB');
        console.log('Total JS Heap Size:', 
            (performance.memory.totalJSHeapSize / 1024 / 1024).toFixed(2) + ' MB');
    }
}

// Debugging utilities
const debug = {
    enabled: localStorage.getItem('debug') === 'true',

    log(...args) {
        if (this.enabled) {
            console.log('[DEBUG]', ...args);
        }
    },

    time(label) {
        if (this.enabled) {
            console.time(`[DEBUG] ${label}`);
        }
    },

    timeEnd(label) {
        if (this.enabled) {
            console.timeEnd(`[DEBUG] ${label}`);
        }
    },

    inspect(obj) {
        if (this.enabled) {
            console.log('[DEBUG] Object inspection:');
            console.dir(obj);
        }
    }
};

// Usage: localStorage.setItem('debug', 'true') to enable
debug.log('This will only show if debug is enabled');

// Function debugging decorator
function debugFunction(fn) {
    return function(...args) {
        console.log(`Calling ${fn.name} with args:`, args);
        const result = fn.apply(this, args);
        console.log(`${fn.name} returned:`, result);
        return result;
    };
}

// Usage
const add = debugFunction(function add(a, b) {
    return a + b;
});

add(2, 3); // Logs input and output

// Breakpoint in code
function debugBreakpoint(data) {
    debugger; // Pauses execution in DevTools
    return processData(data);
}

// Source maps debugging tip
// When using build tools, ensure source maps are enabled
// webpack.config.js: devtool: 'source-map'
// This allows debugging original source code instead of minified

// Remote debugging setup
class RemoteDebugger {
    constructor(endpoint) {
        this.endpoint = endpoint;
        this.enabled = false;
    }

    enable() {
        this.enabled = true;
        this.interceptConsole();
        this.interceptErrors();
    }

    interceptConsole() {
        const originalLog = console.log;
        console.log = (...args) => {
            originalLog.apply(console, args);
            if (this.enabled) {
                this.send('console', args);
            }
        };
    }

    interceptErrors() {
        window.addEventListener('error', (event) => {
            if (this.enabled) {
                this.send('error', {
                    message: event.error.message,
                    stack: event.error.stack,
                    filename: event.filename,
                    line: event.lineno
                });
            }
        });
    }

    send(type, data) {
        fetch(this.endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type, data, timestamp: Date.now() })
        }).catch(err => console.error('Failed to send debug data:', err));
    }
}

// const remoteDebugger = new RemoteDebugger('/api/debug');
// remoteDebugger.enable();
        """, language="javascript")

    with js_tabs[8]:
        st.markdown("### Performance și Best Practices")

        st.markdown("#### JavaScript Performance Optimization")

        st.code("""
// Memory Management și Garbage Collection
// Avoid memory leaks
class MemoryLeakExamples {
    constructor() {
        this.listeners = [];
        this.timers = [];
    }

    // Bad: Creates memory leak
    badEventListener() {
        const button = document.querySelector('#button');
        button.addEventListener('click', () => {
            console.log('Clicked');
            // Handler references 'this', preventing GC
        });
    }

    // Good: Clean up listeners
    goodEventListener() {
        const button = document.querySelector('#button');
        const handler = this.handleClick.bind(this);
        button.addEventListener('click', handler);
        this.listeners.push({ element: button, type: 'click', handler });
    }

    handleClick() {
        console.log('Clicked');
    }

    // Bad: Circular references
    badCircularRef() {
        const parent = { name: 'parent' };
        const child = { name: 'child', parent };
        parent.child = child; // Circular reference
        return parent;
    }

    // Good: Weak references
    goodWeakRef() {
        const parent = { name: 'parent' };
        const child = { name: 'child' };
        const relationships = new WeakMap();
        relationships.set(child, parent);
        return { parent, child, relationships };
    }

    // Cleanup method
    destroy() {
        // Remove event listeners
        this.listeners.forEach(({ element, type, handler }) => {
            element.removeEventListener(type, handler);
        });

        // Clear timers
        this.timers.forEach(clearTimeout);

        // Clear arrays
        this.listeners.length = 0;
        this.timers.length = 0;
    }
}

// Performance optimization techniques
// 1. Object pooling
class ObjectPool {
    constructor(createFn, resetFn, maxSize = 100) {
        this.createFn = createFn;
        this.resetFn = resetFn;
        this.pool = [];
        this.maxSize = maxSize;
    }

    get() {
        if (this.pool.length > 0) {
            return this.pool.pop();
        }
        return this.createFn();
    }

    release(obj) {
        if (this.pool.length < this.maxSize) {
            this.resetFn(obj);
            this.pool.push(obj);
        }
    }
}

// Usage
const vectorPool = new ObjectPool(
    () => ({ x: 0, y: 0 }),
    (vector) => { vector.x = 0; vector.y = 0; }
);

// 2. Debouncing expensive operations
function debounce(func, wait, immediate = false) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            timeout = null;
            if (!immediate) func.apply(this, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(this, args);
    };
}

// 3. Throttling for high-frequency events
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// 4. Efficient DOM manipulation
class DOMBatcher {
    constructor() {
        this.reads = [];
        this.writes = [];
        this.scheduled = false;
    }

    read(fn) {
        this.reads.push(fn);
        this.schedule();
    }

    write(fn) {
        this.writes.push(fn);
        this.schedule();
    }

    schedule() {
        if (!this.scheduled) {
            this.scheduled = true;
            requestAnimationFrame(() => this.flush());
        }
    }

    flush() {
        // Execute all reads first
        this.reads.forEach(fn => fn());
        this.reads.length = 0;

        // Then all writes
        this.writes.forEach(fn => fn());
        this.writes.length = 0;

        this.scheduled = false;
    }
}

const batcher = new DOMBatcher();

// Usage
elements.forEach(el => {
    batcher.read(() => {
        const height = el.offsetHeight; // DOM read
    });
    batcher.write(() => {
        el.style.height = height + 'px'; // DOM write
    });
});

// 5. Lazy loading and code splitting
// Dynamic imports
async function loadModule(moduleName) {
    try {
        const module = await import(`./modules/${moduleName}.js`);
        return module.default;
    } catch (error) {
        console.error(`Failed to load module ${moduleName}:`, error);
        throw error;
    }
}

// Lazy initialization
class LazyComponent {
    constructor() {
        this._instance = null;
    }

    get instance() {
        if (!this._instance) {
            this._instance = this.createInstance();
        }
        return this._instance;
    }

    createInstance() {
        // Expensive initialization
        return new ExpensiveClass();
    }
}
        """, language="javascript")

        st.markdown("#### Code Quality și Best Practices")

        st.code("""
// 1. Pure functions și immutability
// Bad: Mutates input
function addTax(product, tax) {
    product.price += product.price * tax; // Mutates original
    return product;
}

// Good: Returns new object
function addTax(product, tax) {
    return {
        ...product,
        price: product.price * (1 + tax)
    };
}

// 2. Function composition
const pipe = (...fns) => (value) => fns.reduce((acc, fn) => fn(acc), value);
const compose = (...fns) => (value) => fns.reduceRight((acc, fn) => fn(acc), value);

const multiply = (x) => (y) => x * y;
const add = (x) => (y) => x + y;
const subtract = (x) => (y) => y - x;

// Usage
const calculate = pipe(
    multiply(2),
    add(10),
    subtract(5)
);

console.log(calculate(5)); // (5 * 2 + 10) - 5 = 15

// 3. Error handling patterns
// Result pattern for error handling
class Result {
    constructor(value, error) {
        this.value = value;
        this.error = error;
    }

    static ok(value) {
        return new Result(value, null);
    }

    static error(error) {
        return new Result(null, error);
    }

    isOk() {
        return this.error === null;
    }

    isError() {
        return this.error !== null;
    }

    map(fn) {
        if (this.isError()) return this;
        try {
            return Result.ok(fn(this.value));
        } catch (error) {
            return Result.error(error);
        }
    }

    flatMap(fn) {
        if (this.isError()) return this;
        try {
            return fn(this.value);
        } catch (error) {
            return Result.error(error);
        }
    }
}

// Usage
function parseJSON(str) {
    try {
        return Result.ok(JSON.parse(str));
    } catch (error) {
        return Result.error(error);
    }
}

const result = parseJSON('{"name": "John"}')
    .map(obj => obj.name)
    .map(name => name.toUpperCase());

if (result.isOk()) {
    console.log('Success:', result.value);
} else {
    console.error('Error:', result.error);
}

// 4. Module patterns
// Revealing Module Pattern
const UserModule = (function() {
    // Private variables
    let users = [];
    const API_URL = '/api/users';

    // Private functions
    function validateUser(user) {
        return user.name && user.email;
    }

    function makeRequest(url, options) {
        return fetch(url, options).then(r => r.json());
    }

    // Public API
    return {
        addUser(user) {
            if (!validateUser(user)) {
                throw new Error('Invalid user data');
            }
            users.push(user);
            return makeRequest(API_URL, {
                method: 'POST',
                body: JSON.stringify(user)
            });
        },

        getUsers() {
            return [...users]; // Return copy
        },

        getUserCount() {
            return users.length;
        }
    };
})();

// 5. Design patterns
// Observer Pattern
class EventEmitter {
    constructor() {
        this.events = {};
    }

    on(event, callback) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(callback);
    }

    off(event, callback) {
        if (!this.events[event]) return;
        this.events[event] = this.events[event].filter(cb => cb !== callback);
    }

    emit(event, data) {
        if (!this.events[event]) return;
        this.events[event].forEach(callback => callback(data));
    }

    once(event, callback) {
        const onceCallback = (data) => {
            callback(data);
            this.off(event, onceCallback);
        };
        this.on(event, onceCallback);
    }
}

// Singleton Pattern
class DatabaseConnection {
    constructor() {
        if (DatabaseConnection.instance) {
            return DatabaseConnection.instance;
        }

        this.connection = null;
        DatabaseConnection.instance = this;
    }

    connect() {
        if (!this.connection) {
            this.connection = 'Connected to database';
        }
        return this.connection;
    }
}

// Factory Pattern
class ShapeFactory {
    static createShape(type, ...args) {
        switch (type) {
            case 'circle':
                return new Circle(...args);
            case 'rectangle':
                return new Rectangle(...args);
            case 'triangle':
                return new Triangle(...args);
            default:
                throw new Error(`Unknown shape type: ${type}`);
        }
    }
}

// 6. Modern JavaScript practices
// Using optional chaining
const user = {
    profile: {
        social: {
            twitter: '@johnDoe'
        }
    }
};

// Old way
const twitter = user && user.profile && user.profile.social && user.profile.social.twitter;

// New way
const twitter = user?.profile?.social?.twitter;

// Nullish coalescing
const name = user?.name ?? 'Anonymous';  // Only null or undefined
const name2 = user?.name || 'Anonymous'; // Any falsy value

// Private fields in classes
class BankAccount {
    #balance = 0;
    #pin;

    constructor(initialBalance, pin) {
        this.#balance = initialBalance;
        this.#pin = pin;
    }

    #validatePin(pin) {
        return pin === this.#pin;
    }

    withdraw(amount, pin) {
        if (!this.#validatePin(pin)) {
            throw new Error('Invalid PIN');
        }
        if (amount > this.#balance) {
            throw new Error('Insufficient funds');
        }
        this.#balance -= amount;
        return this.#balance;
    }

    get balance() {
        return this.#balance;
    }
}
        """, language="javascript")

    with js_tabs[9]:
        st.markdown("### Întrebări frecvente la interviuri JavaScript")

        js_qa = [
            {
                "question": "Explică diferența între var, let și const și conceptul de hoisting",
                "answer": """
                **var:**
                - Function-scoped sau globally-scoped
                - Poate fi redeclarat în același scope
                - Hoisted și inițializat cu undefined
                - Poate fi accesat înainte de declarație (undefined)

                **let:**
                - Block-scoped
                - Nu poate fi redeclarat în același scope
                - Hoisted dar în Temporal Dead Zone
                - ReferenceError dacă e accesat înainte de declarație

                **const:**
                - Block-scoped
                - Trebuie inițializat la declarație
                - Nu poate fi reasignat (dar obiectele pot fi mutate)
                - Same hoisting behavior ca let

                **Hoisting:** Declarațiile sunt "ridicate" la începutul scope-ului lor, dar inițializarea rămâne în loc.
                """
            },
            {
                "question": "Cum funcționează 'this' keyword în JavaScript și care sunt metodele de binding?",
                "answer": """
                **'this' binding rules (în ordinea priorității):**

                1. **new binding:** `const obj = new MyFunction()` - this = noul obiect
                2. **Explicit binding:** `fn.call(obj)`, `fn.apply(obj)`, `fn.bind(obj)` - this = obj
                3. **Implicit binding:** `obj.method()` - this = obj
                4. **Default binding:** function call în global scope - this = window/global (undefined în strict mode)

                **Arrow functions:** Nu au propriul 'this', îl moștenesc lexical din scope-ul înconjurător.

                **Event handlers:** this = elementul care a declanșat evenimentul (cu funcții normale), window (cu arrow functions).

                **Metode de binding:**
                - `call()`: execută imediat cu argumente individuale
                - `apply()`: execută imediat cu array de argumente  
                - `bind()`: returnează nouă funcție cu this fixat
                """
            },
            {
                "question": "Ce sunt closures și care sunt aplicațiile practice?",
                "answer": """
                **Closure** = funcție care are acces la variabilele din scope-ul său lexical, chiar și după ce scope-ul părinte s-a terminat.

                **Cum funcționează:**
                - Funcția interioară "închide" asupra variabilelor din funcția exterioară
                - Variabilele rămân în memorie atâta timp cât closure-ul există
                - Fiecare closure are propria instanță a variabilelor

                **Aplicații practice:**
                1. **Module pattern** - encapsularea datelor private
                2. **Factory functions** - crearea de funcții specializate  
                3. **Callbacks și event handlers** - păstrarea contextului
                4. **Memoization** - cache pentru rezultate computaționale
                5. **Partial application** - funcții cu argumente pre-setate
                6. **Data binding** în frameworks

                **Atenție:** Closures pot crea memory leaks dacă nu sunt gestionate corect.
                """
            },
            {
                "question": "Explică event loop-ul și diferența între microtasks și macrotasks",
                "answer": """
                **Event Loop** procesează task-urile în această ordine:

                1. **Call Stack** - execută codul sincron
                2. **Microtask Queue** - Promises, queueMicrotask, MutationObserver
                3. **Macrotask Queue** - setTimeout, setInterval, DOM events, I/O

                **Algoritm:**
                1. Execută toate task-urile din Call Stack
                2. Execută TOATE microtask-urile din queue
                3. Execută UN macrotask din queue
                4. Repeat

                **Microtasks** au prioritate mare și se execută toate înainte de orice macrotask.

                **Blocking operations** blochează event loop-ul, de aceea operațiile I/O sunt asincrone.

                **Exemple:**
                - Microtasks: Promise.then(), async/await, queueMicrotask()
                - Macrotasks: setTimeout(), setInterval(), DOM events
                """
            },
            {
                "question": "Care este diferența între Promise.all(), Promise.allSettled(), Promise.race() și Promise.any()?",
                "answer": """
                **Promise.all([p1, p2, p3]):**
                - Așteaptă ca TOATE promisele să se rezolve
                - Dacă una fail, toată operația fail (fail-fast)
                - Returnează array cu toate rezultatele în ordinea originală
                - Use case: operații dependente care trebuie să reușească toate

                **Promise.allSettled([p1, p2, p3]):**
                - Așteaptă ca TOATE promisele să se "settle" (resolve sau reject)
                - Nu fail niciodată, returnează status pentru fiecare
                - Use case: când vrei să vezi rezultatul tuturor, indiferent de succces/fail

                **Promise.race([p1, p2, p3]):**
                - Prima promisă care se settle câștigă (resolve SAU reject)
                - Use case: timeout implementations, redundant requests

                **Promise.any([p1, p2, p3]):**
                - Prima promisă care se RESOLVE câștigă (ignore rejections)
                - Fail doar dacă toate promisele fail (AggregateError)
                - Use case: multiple surse pentru aceeași dată, prima care reușește
                """
            },
            {
                "question": "Explică prototype chain și diferența între __proto__ și prototype",
                "answer": """
                **Prototype Chain** = mecanismul prin care obiectele moștenesc proprietăți și metode din alte obiecte.

                **prototype:**
                - Proprietate a FUNCȚIILOR (constructors)
                - Obiectul care devine prototype pentru instanțele create cu 'new'
                - `Function.prototype.property`

                **__proto__ (sau [[Prototype]]):**
                - Proprietate a OBIECTELOR (instances)  
                - Link către obiectul prototype
                - `instance.__proto__ === Constructor.prototype`

                **Cum funcționează:**
                1. JavaScript caută proprietatea în obiect
                2. Dacă nu o găsește, caută în __proto__
                3. Continuă în chain până la Object.prototype
                4. Dacă nu găsește, returnează undefined

                **Metode moderne:**
                - `Object.getPrototypeOf(obj)` în loc de __proto__
                - `Object.setPrototypeOf(obj, proto)` pentru schimbarea prototype
                - `Object.create(proto)` pentru crearea cu prototype specific
                """
            },
            {
                "question": "Ce este type coercion și cum funcționează equality operators (== vs ===)?",
                "answer": """
                **Type Coercion** = conversie automată între tipuri de date.

                **Implicit coercion:**
                - `'5' + 3` = '53' (number → string pentru concatenare)
                - `'5' - 3` = 2 (string → number pentru scădere)
                - `true + 1` = 2 (boolean → number)

                **== (Abstract Equality):**
                - Permite type coercion
                - Algoritm complex de conversie
                - `'5' == 5` = true
                - `null == undefined` = true
                - `[] == false` = true (atenție la traps!)

                **=== (Strict Equality):**
                - NO type coercion
                - Compară și tip și valoare
                - `'5' === 5` = false
                - `null === null` = true
                - `NaN === NaN` = false (special case)

                **Best Practice:** Folosește === pentru predictibilitate, == doar când înțelegi exact comportamentul.

                **Object.is():** Similar cu ===, dar `Object.is(NaN, NaN)` = true și `Object.is(+0, -0)` = false.
                """
            },
            {
                "question": "Cum funcționează async/await și care sunt avantajele față de Promises?",
                "answer": """
                **Async/Await** = syntactic sugar peste Promises pentru cod mai lizibil.

                **Cum funcționează:**
                - `async` function returnează întotdeauna o Promise
                - `await` pauzează execuția până când Promise se rezolvă
                - Dacă Promise fail, await throw error (poate fi prins cu try/catch)

                **Avantaje față de Promise chains:**
                1. **Lizibilitate:** cod care arată sincron dar e asincron
                2. **Error handling:** try/catch în loc de .catch()
                3. **Debugging:** stack traces mai clare
                4. **Control flow:** mai ușor cu loops și conditionals

                **Dezavantaje:**
                - Poate fi mai lent decât Promise.all() pentru operații paralele
                - Top-level await disponibil doar în ES2022

                **Best practices:**
                - Folosește Promise.all() pentru operații paralele
                - Gestionează erorile cu try/catch
                - Atenție la loops cu await (pot fi secvențiale în loc de paralele)

                **Sequential vs Parallel:**
                ```javascript
                // Sequential (slow)
                const user = await fetchUser();
                const posts = await fetchPosts();

                // Parallel (fast)  
                const [user, posts] = await Promise.all([fetchUser(), fetchPosts()]);
                ```
                """
            }
        ]

        for qa in js_qa:
            with st.expander(f"❓ {qa['question']}"):
                st.markdown(qa['answer'])

    # Final summary
    st.markdown("---")
    st.markdown("""
    
    """, unsafe_allow_html=True)


def intro_react_page():
    """Introduction to React - Complete educational content"""
    st.markdown('<h1 class="chapter-header">Introducere în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>React - Revoluția în dezvoltarea interfețelor utilizator</h3>
        <p>React este biblioteca JavaScript care a schimbat radical modul în care construim aplicații web. 
        Creată de Facebook în 2013, React a devenit standardul de facto pentru dezvoltarea frontendului modern. 
        Acest capitol te va ghida de la conceptele fundamentale până la înțelegerea profundă necesară pentru 
        interviuri tehnice și dezvoltare profesională.</p>
    </div>
    """, unsafe_allow_html=True)

    # React Tabs
    react_tabs = st.tabs([
        "De ce React?",
        "JSX Deep Dive",
        "Components & Props",
        "State Management",
        "Event Handling",
        "Virtual DOM & Rendering",
        "React Ecosystem",
        "Best Practices",
        "Întrebări Interviu"
    ])

    with react_tabs[0]:
        st.markdown("### Istoria și motivația React")

        st.markdown("""
        React a fost creat de Jordan Walke la Facebook în 2013 pentru a rezolva problemele complexității 
        crescânde în dezvoltarea interfețelor utilizator. Înainte de React, dezvoltatorii se confruntau cu:

        - **Manipularea directă a DOM-ului** - cod imperativ greu de întreținut
        - **State management complex** - sincronizarea datelor între componente
        - **Lipsa reutilizabilității** - copy-paste code pentru funcționalități similare
        - **Debugging dificil** - bug-uri greu de identificat în aplicații mari
        """)

        st.markdown("### Principiile fundamentale React")

        principles = [
            {
                "title": "Declarative Programming",
                "description": "Descrii CE vrei să obții, nu CUM să o faci",
                "example": """
                // Imperativ (DOM vanilla)
                const button = document.createElement('button');
                button.textContent = 'Click me';
                button.addEventListener('click', handleClick);
                document.body.appendChild(button);

                // Declarativ (React)
                const Button = () => <button onClick={handleClick}>Click me</button>;
                """
            },
            {
                "title": "Component-Based Architecture",
                "description": "Aplicația este construită din componente independente și reutilizabile",
                "example": """
                // Componentă reutilizabilă
                function UserCard({ user }) {
                    return (
                        <div className="user-card">
                            <img src={user.avatar} alt={user.name} />
                            <h3>{user.name}</h3>
                            <p>{user.email}</p>
                        </div>
                    );
                }

                // Folosită în multiple locuri
                <UserCard user={admin} />
                <UserCard user={currentUser} />
                """
            },
            {
                "title": "Learn Once, Write Anywhere",
                "description": "Conceptele React se aplică pe web, mobile (React Native), desktop",
                "example": """
                // Same concepts pentru:
                // Web: React DOM
                // Mobile: React Native  
                // Desktop: Electron + React
                // Server: Next.js SSR
                // Static: Gatsby
                """
            },
            {
                "title": "Virtual DOM",
                "description": "Reprezentare în memorie pentru optimizarea performanțelor",
                "example": """
                // React compară Virtual DOM trees
                // și aplică doar diferențele în DOM real
                const prevVDOM = <div>Hello World</div>;
                const nextVDOM = <div>Hello React</div>;
                // Doar textContent se schimbă, nu întregul element
                """
            }
        ]

        for principle in principles:
            st.markdown(f"#### {principle['title']}")
            st.markdown(principle['description'])
            st.code(principle['example'], language="javascript")
            st.markdown("")

        st.markdown("### React vs Alternative")

        comparison_data = {
            "Aspect": ["Learning Curve", "Performance", "Ecosystem", "Job Market", "Community", "Bundle Size",
                       "TypeScript"],
            "React": ["Mediu", "Excellent", "Vast", "Highest", "Largest", "Medium", "Great"],
            "Vue.js": ["Easy", "Excellent", "Growing", "Good", "Active", "Small", "Good"],
            "Angular": ["Steep", "Good", "Enterprise", "Enterprise", "Strong", "Large", "Native"],
            "Svelte": ["Easy", "Excellent", "Small", "Emerging", "Growing", "Smallest", "Good"],
            "Vanilla JS": ["Variable", "Depends", "Native", "Declining", "N/A", "None", "Manual"]
        }

        import pandas as pd
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)

        st.markdown("### Când să folosești React")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="success-box">
                <h4>React este ideal pentru:</h4>
                <ul>
                    <li><strong>Single Page Applications</strong> - interfețe complexe și interactive</li>
                    <li><strong>Component reusability</strong> - design systems și UI libraries</li>
                    <li><strong>Large teams</strong> - arhitectura modulară facilitează colaborarea</li>
                    <li><strong>Complex state</strong> - gestionarea datelor între multe componente</li>
                    <li><strong>Real-time features</strong> - chat, notifications, live updates</li>
                    <li><strong>Progressive enhancement</strong> - adăugarea graduală a funcționalităților</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="warning-box">
                <h4>Considera alternative pentru:</h4>
                <ul>
                    <li><strong>Static sites</strong> - blog-uri simple, landing pages</li>
                    <li><strong>SEO-critical content</strong> - fără SSR setup</li>
                    <li><strong>Beginner projects</strong> - overhead pentru aplicații simple</li>
                    <li><strong>Performance-critical</strong> - apps cu cerințe extreme de viteză</li>
                    <li><strong>Small budget</strong> - timp limitat pentru învățare</li>
                    <li><strong>Legacy systems</strong> - integrare dificilă cu tehnologii vechi</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with react_tabs[1]:
        st.markdown("### JSX - JavaScript XML Explained")

        st.markdown("""
        JSX este o extensie de sintaxă pentru JavaScript care permite scrierea de markup HTML 
        în cod JavaScript. Nu este HTML adevărat, ci o reprezentare care se compilează în 
        funcții JavaScript.
        """)

        st.markdown("#### Cum funcționează JSX")

        st.code("""
// JSX Code
const element = <h1 className="greeting">Hello, World!</h1>;

// Se compilează în:
const element = React.createElement(
    'h1',                              // tag
    { className: 'greeting' },         // props  
    'Hello, World!'                    // children
);

// Rezultatul final (React Element):
{
    type: 'h1',
    props: {
        className: 'greeting',
        children: 'Hello, World!'
    },
    key: null,
    ref: null
}
        """, language="javascript")

        st.markdown("#### Regulile JSX")

        jsx_rules = [
            {
                "rule": "Un singur element părinte",
                "explanation": "JSX trebuie să aibă un singur root element",
                "good": """
                // Corect
                return (
                    <div>
                        <h1>Title</h1>
                        <p>Paragraph</p>
                    </div>
                );

                // Sau cu React Fragment
                return (
                    <>
                        <h1>Title</h1>
                        <p>Paragraph</p>
                    </>
                );
                """,
                "bad": """
                // Greșit
                return (
                    <h1>Title</h1>
                    <p>Paragraph</p>
                );
                """
            },
            {
                "rule": "className în loc de class",
                "explanation": "class este cuvânt rezervat în JavaScript",
                "good": '<div className="container">Content</div>',
                "bad": '<div class="container">Content</div>'
            },
            {
                "rule": "Self-closing tags",
                "explanation": "Tag-urile fără conținut trebuie închise",
                "good": '<img src="image.jpg" alt="Description" />',
                "bad": '<img src="image.jpg" alt="Description">'
            },
            {
                "rule": "camelCase pentru atribute",
                "explanation": "Atributele HTML devin camelCase în JSX",
                "good": '<input onChange={handleChange} tabIndex={1} />',
                "bad": '<input onchange={handleChange} tabindex={1} />'
            }
        ]

        for rule in jsx_rules:
            st.markdown(f"**{rule['rule']}**")
            st.markdown(rule['explanation'])

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Corect:**")
                st.code(rule['good'], language="javascript")

            if 'bad' in rule:
                with col2:
                    st.markdown("**Greșit:**")
                    st.code(rule['bad'], language="javascript")
            st.markdown("")

        st.markdown("#### JavaScript în JSX")

        st.code("""
function UserProfile({ user, isOnline }) {
    const formatName = (name) => name.toUpperCase();

    return (
        <div className={`user-profile ${isOnline ? 'online' : 'offline'}`}>
            {/* Comments în JSX */}
            <img 
                src={user.avatar || '/default-avatar.png'} 
                alt={`${user.name}'s avatar`} 
            />

            {/* Expresii JavaScript în {} */}
            <h2>{formatName(user.name)}</h2>
            <p>Age: {new Date().getFullYear() - user.birthYear}</p>

            {/* Conditional rendering */}
            {user.bio && <p className="bio">{user.bio}</p>}

            {/* Ternary operator */}
            <span className="status">
                {isOnline ? 'Online now' : `Last seen ${user.lastSeen}`}
            </span>

            {/* Lists rendering */}
            <ul className="skills">
                {user.skills.map((skill, index) => (
                    <li key={skill.id || index}>{skill.name}</li>
                ))}
            </ul>

            {/* Inline styles (camelCase) */}
            <div style={{
                backgroundColor: isOnline ? 'green' : 'red',
                borderRadius: '4px',
                padding: '8px'
            }}>
                Status indicator
            </div>
        </div>
    );
}
        """, language="javascript")

        st.markdown("#### JSX Advanced Patterns")

        st.code("""
// Conditional rendering patterns
function ConditionalExample({ user, loading, error }) {
    // Early return pattern
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    if (!user) return <div>No user found</div>;

    return (
        <div>
            {/* Short-circuit evaluation */}
            {user.isAdmin && <AdminPanel />}

            {/* Ternary operator */}
            {user.verified ? <VerifiedBadge /> : <UnverifiedWarning />}

            {/* Complex conditional */}
            {user.posts.length > 0 ? (
                <PostList posts={user.posts} />
            ) : (
                <EmptyState message="No posts yet" />
            )}

            {/* IIFE for complex logic */}
            {(() => {
                if (user.role === 'admin') return <AdminTools />;
                if (user.role === 'moderator') return <ModeratorTools />;
                return <UserTools />;
            })()}
        </div>
    );
}

// Higher-order components pattern
function withLoading(Component) {
    return function WrappedComponent(props) {
        if (props.loading) {
            return <div className="spinner">Loading...</div>;
        }
        return <Component {...props} />;
    };
}

// Render props pattern  
function DataFetcher({ url, children }) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setData(data);
                setLoading(false);
            });
    }, [url]);

    return children({ data, loading });
}

// Usage:
<DataFetcher url="/api/users">
    {({ data, loading }) => (
        loading ? <Spinner /> : <UserList users={data} />
    )}
</DataFetcher>

// Fragments for cleaner markup
function FragmentExample() {
    return (
        <>
            <h1>Title</h1>
            <p>Description</p>

            {/* Fragment with key (for lists) */}
            {items.map(item => (
                <React.Fragment key={item.id}>
                    <dt>{item.term}</dt>
                    <dd>{item.definition}</dd>
                </React.Fragment>
            ))}
        </>
    );
}
        """, language="javascript")

    with react_tabs[2]:
        st.markdown("### Components și Props Deep Dive")

        st.markdown("#### Tipuri de componente")

        st.code("""
// 1. Function Components (Recommended)
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;
}

// 2. Arrow Function Components
const Welcome = (props) => {
    return <h1>Hello, {props.name}!</h1>;
};

// 3. Arrow Function with implicit return
const Welcome = (props) => <h1>Hello, {props.name}!</h1>;

// 4. Class Components (Legacy, dar încă întâlnite)
class Welcome extends React.Component {
    render() {
        return <h1>Hello, {this.props.name}!</h1>;
    }
}

// 5. Component cu destructuring
function Welcome({ name, age, isOnline = false }) {
    return (
        <div>
            <h1>Hello, {name}!</h1>
            <p>Age: {age}</p>
            {isOnline && <span className="online-indicator">Online</span>}
        </div>
    );
}
        """, language="javascript")

        st.markdown("#### Props în detaliu")

        st.code("""
// Props ca date simple
function Greeting({ name, age }) {
    return <p>Hello {name}, you are {age} years old</p>;
}

// Props ca funcții (callbacks)
function Button({ onClick, children, disabled = false }) {
    return (
        <button onClick={onClick} disabled={disabled}>
            {children}
        </button>
    );
}

// Props ca obiecte complexe
function UserCard({ user }) {
    return (
        <div className="user-card">
            <img src={user.avatar} alt={user.name} />
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <div className="skills">
                {user.skills.map(skill => (
                    <span key={skill} className="skill-tag">{skill}</span>
                ))}
            </div>
        </div>
    );
}

// Props validation cu PropTypes
import PropTypes from 'prop-types';

function UserCard({ user, onEdit, isEditable }) {
    return (
        <div className="user-card">
            <h3>{user.name}</h3>
            {isEditable && (
                <button onClick={() => onEdit(user.id)}>Edit</button>
            )}
        </div>
    );
}

UserCard.propTypes = {
    user: PropTypes.shape({
        id: PropTypes.number.isRequired,
        name: PropTypes.string.isRequired,
        email: PropTypes.string
    }).isRequired,
    onEdit: PropTypes.func,
    isEditable: PropTypes.bool
};

UserCard.defaultProps = {
    isEditable: false,
    onEdit: () => {}
};

// Spread props pattern
function InputField(props) {
    const { label, error, ...inputProps } = props;

    return (
        <div className="field">
            <label>{label}</label>
            <input 
                {...inputProps}  // Spread remaining props
                className={`input ${error ? 'error' : ''}`}
            />
            {error && <span className="error-text">{error}</span>}
        </div>
    );
}

// Usage
<InputField 
    label="Email"
    type="email"
    placeholder="Enter your email"
    required
    onChange={handleEmailChange}
    error={emailError}
/>
        """, language="javascript")

        st.markdown("#### Composition vs Inheritance")

        st.code("""
// React favorizează composition peste inheritance

// 1. Children prop pentru slot pattern
function Card({ children, title, className = '' }) {
    return (
        <div className={`card ${className}`}>
            {title && <div className="card-header">{title}</div>}
            <div className="card-body">
                {children}
            </div>
        </div>
    );
}

// Usage
<Card title="User Profile">
    <UserAvatar user={user} />
    <UserDetails user={user} />
    <UserActions user={user} />
</Card>

// 2. Multiple slots pattern
function Layout({ header, sidebar, main, footer }) {
    return (
        <div className="layout">
            <header className="layout-header">{header}</header>
            <div className="layout-content">
                <aside className="layout-sidebar">{sidebar}</aside>
                <main className="layout-main">{main}</main>
            </div>
            <footer className="layout-footer">{footer}</footer>
        </div>
    );
}

// Usage
<Layout
    header={<Navigation />}
    sidebar={<Sidebar />}
    main={<MainContent />}
    footer={<Footer />}
/>

// 3. Render props pattern pentru behavior sharing
function MouseTracker({ children }) {
    const [position, setPosition] = useState({ x: 0, y: 0 });

    const handleMouseMove = (event) => {
        setPosition({ x: event.clientX, y: event.clientY });
    };

    return (
        <div onMouseMove={handleMouseMove}>
            {children(position)}
        </div>
    );
}

// Usage
<MouseTracker>
    {({ x, y }) => (
        <div>Mouse is at ({x}, {y})</div>
    )}
</MouseTracker>

// 4. Higher-Order Components (HOCs)
function withAuth(WrappedComponent) {
    return function AuthComponent(props) {
        const { user, isAuthenticated } = useAuth();

        if (!isAuthenticated) {
            return <LoginForm />;
        }

        return <WrappedComponent {...props} user={user} />;
    };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);

// 5. Custom hooks pentru logic sharing (Modern approach)
function useAuth() {
    const [user, setUser] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        // Auth logic here
    }, []);

    return { user, isAuthenticated, login, logout };
}

// Usage în multiple componente
function Dashboard() {
    const { user, isAuthenticated } = useAuth();

    if (!isAuthenticated) return <LoginForm />;

    return <div>Welcome, {user.name}!</div>;
}
        """, language="javascript")

    with react_tabs[3]:
        st.markdown("### State Management în React")

        st.markdown("#### useState Hook Fundamentals")

        st.code("""
import { useState } from 'react';

// Basic useState
function Counter() {
    const [count, setCount] = useState(0);

    const increment = () => setCount(count + 1);
    const decrement = () => setCount(count - 1);
    const reset = () => setCount(0);

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>+</button>
            <button onClick={decrement}>-</button>
            <button onClick={reset}>Reset</button>
        </div>
    );
}

// State cu functional updates (important pentru consistency)
function CounterBetter() {
    const [count, setCount] = useState(0);

    // Folosește function form pentru updates bazate pe starea anterioară
    const increment = () => setCount(prev => prev + 1);
    const incrementBy = (amount) => setCount(prev => prev + amount);

    // Multiple updates în același event handler
    const incrementTwice = () => {
        setCount(prev => prev + 1);  // Correct
        setCount(prev => prev + 1);  // Correct

        // setCount(count + 1);      // Wrong - folosește stale value
        // setCount(count + 1);      // Wrong - doar ultima execută
    };

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>+1</button>
            <button onClick={() => incrementBy(5)}>+5</button>
            <button onClick={incrementTwice}>+2</button>
        </div>
    );
}

// State cu obiecte (immutability pattern)
function UserProfile() {
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: 0,
        preferences: {
            theme: 'light',
            notifications: true
        }
    });

    // Updating nested objects
    const updateName = (name) => {
        setUser(prev => ({
            ...prev,
            name
        }));
    };

    const updatePreferences = (key, value) => {
        setUser(prev => ({
            ...prev,
            preferences: {
                ...prev.preferences,
                [key]: value
            }
        }));
    };

    // Generic update function
    const updateUser = (updates) => {
        setUser(prev => ({ ...prev, ...updates }));
    };

    return (
        <form>
            <input 
                value={user.name}
                onChange={(e) => updateName(e.target.value)}
                placeholder="Name"
            />
            <input 
                value={user.email}
                onChange={(e) => updateUser({ email: e.target.value })}
                placeholder="Email"
            />
            <select 
                value={user.preferences.theme}
                onChange={(e) => updatePreferences('theme', e.target.value)}
            >
                <option value="light">Light</option>
                <option value="dark">Dark</option>
            </select>
        </form>
    );
}

// State cu arrays
function TodoList() {
    const [todos, setTodos] = useState([]);
    const [inputValue, setInputValue] = useState('');

    const addTodo = () => {
        if (inputValue.trim()) {
            const newTodo = {
                id: Date.now(),
                text: inputValue,
                completed: false
            };
            setTodos(prev => [...prev, newTodo]);
            setInputValue('');
        }
    };

    const toggleTodo = (id) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        ));
    };

    const deleteTodo = (id) => {
        setTodos(prev => prev.filter(todo => todo.id !== id));
    };

    const updateTodo = (id, newText) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id ? { ...todo, text: newText } : todo
        ));
    };

    return (
        <div>
            <input 
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && addTodo()}
            />
            <button onClick={addTodo}>Add Todo</button>

            <ul>
                {todos.map(todo => (
                    <li key={todo.id}>
                        <input 
                            type="checkbox"
                            checked={todo.completed}
                            onChange={() => toggleTodo(todo.id)}
                        />
                        <span 
                            style={{ 
                                textDecoration: todo.completed ? 'line-through' : 'none' 
                            }}
                        >
                            {todo.text}
                        </span>
                        <button onClick={() => deleteTodo(todo.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}
        """, language="javascript")

        st.markdown("#### State Patterns și Best Practices")

        st.code("""
// 1. Lazy initial state pentru expensive computations
function ExpensiveComponent() {
    // Wrong - runs on every render
    const [data, setData] = useState(expensiveComputation());

    // Right - runs only once
    const [data, setData] = useState(() => expensiveComputation());

    return <div>{data}</div>;
}

// 2. State normalization pentru complex data
function UserManagement() {
    // Wrong - nested arrays/objects
    const [users, setUsers] = useState([
        { id: 1, name: 'John', posts: [{ id: 1, title: 'Post 1' }] }
    ]);

    // Right - normalized structure
    const [state, setState] = useState({
        users: { 1: { id: 1, name: 'John', postIds: [1] } },
        posts: { 1: { id: 1, title: 'Post 1', userId: 1 } },
        userIds: [1],
        postIds: [1]
    });

    const addPost = (userId, post) => {
        setState(prev => ({
            ...prev,
            posts: {
                ...prev.posts,
                [post.id]: post
            },
            users: {
                ...prev.users,
                [userId]: {
                    ...prev.users[userId],
                    postIds: [...prev.users[userId].postIds, post.id]
                }
            },
            postIds: [...prev.postIds, post.id]
        }));
    };
}

// 3. useReducer pentru complex state logic
function useShoppingCart() {
    const cartReducer = (state, action) => {
        switch (action.type) {
            case 'ADD_ITEM':
                const existingItem = state.items.find(item => item.id === action.payload.id);
                if (existingItem) {
                    return {
                        ...state,
                        items: state.items.map(item =>
                            item.id === action.payload.id
                                ? { ...item, quantity: item.quantity + 1 }
                                : item
                        )
                    };
                }
                return {
                    ...state,
                    items: [...state.items, { ...action.payload, quantity: 1 }]
                };

            case 'REMOVE_ITEM':
                return {
                    ...state,
                    items: state.items.filter(item => item.id !== action.payload)
                };

            case 'UPDATE_QUANTITY':
                return {
                    ...state,
                    items: state.items.map(item =>
                        item.id === action.payload.id
                            ? { ...item, quantity: action.payload.quantity }
                            : item
                    )
                };

            case 'CLEAR_CART':
                return { ...state, items: [] };

            default:
                return state;
        }
    };

    const [state, dispatch] = useReducer(cartReducer, { items: [] });

    const addItem = (item) => dispatch({ type: 'ADD_ITEM', payload: item });
    const removeItem = (id) => dispatch({ type: 'REMOVE_ITEM', payload: id });
    const updateQuantity = (id, quantity) => 
        dispatch({ type: 'UPDATE_QUANTITY', payload: { id, quantity } });
    const clearCart = () => dispatch({ type: 'CLEAR_CART' });

    const total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const itemCount = state.items.reduce((sum, item) => sum + item.quantity, 0);

    return {
        items: state.items,
        total,
        itemCount,
        addItem,
        removeItem,
        updateQuantity,
        clearCart
    };
}

// 4. Custom hooks pentru state logic reuse
function useLocalStorage(key, initialValue) {
    const [storedValue, setStoredValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            console.error(`Error reading localStorage key "${key}":`, error);
            return initialValue;
        }
    });

    const setValue = (value) => {
        try {
            const valueToStore = value instanceof Function ? value(storedValue) : value;
            setStoredValue(valueToStore);
            window.localStorage.setItem(key, JSON.stringify(valueToStore));
        } catch (error) {
            console.error(`Error setting localStorage key "${key}":`, error);
        }
    };

    return [storedValue, setValue];
}

// Usage
function Settings() {
    const [theme, setTheme] = useLocalStorage('theme', 'light');
    const [language, setLanguage] = useLocalStorage('language', 'en');

    return (
        <div>
            <select value={theme} onChange={(e) => setTheme(e.target.value)}>
                <option value="light">Light</option>
                <option value="dark">Dark</option>
            </select>
        </div>
    );
}

// 5. State batching și performance
function BatchingExample() {
    const [count, setCount] = useState(0);
    const [flag, setFlag] = useState(false);

    const handleClick = () => {
        // React 18+ automatically batches these updates
        setCount(c => c + 1);
        setFlag(f => !f);
        // Only one re-render happens
    };

    const handleClickAsync = () => {
        setTimeout(() => {
            // Before React 18: two separate re-renders
            // React 18+: still batched with automatic batching
            setCount(c => c + 1);
            setFlag(f => !f);
        }, 1000);
    };

    return (
        <div>
            <p>Count: {count}, Flag: {flag ? 'true' : 'false'}</p>
            <button onClick={handleClick}>Update sync</button>
            <button onClick={handleClickAsync}>Update async</button>
        </div>
    );
}
        """, language="javascript")

    with react_tabs[4]:
        st.markdown("### Event Handling în React")

        st.markdown("#### SyntheticEvent System")

        st.code("""
// React folosește SyntheticEvent - wrapper peste native events
function EventExample() {
    const handleClick = (event) => {
        // SyntheticEvent properties
        console.log('Event type:', event.type);
        console.log('Target element:', event.target);
        console.log('Current target:', event.currentTarget);
        console.log('Timestamp:', event.timeStamp);

        // Prevent default behavior
        event.preventDefault();

        // Stop event propagation
        event.stopPropagation();

        // Access native event
        const nativeEvent = event.nativeEvent;
        console.log('Native event:', nativeEvent);

        // Persist event (pentru async operations)
        event.persist(); // Not needed în React 17+
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData.entries());
        console.log('Form data:', data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <button onClick={handleClick}>Click me</button>
            <input name="username" placeholder="Username" />
            <button type="submit">Submit</button>
        </form>
    );
}

// Event pooling (React < 17)
function EventPoolingExample() {
    const handleClick = (event) => {
        // În React < 17, event objects erau reused
        setTimeout(() => {
            // console.log(event.type); // null în React < 17
            // event.persist(); // necesară pentru a păstra event-ul
        }, 1000);
    };

    return <button onClick={handleClick}>Click</button>;
}
        """, language="javascript")

        st.markdown("#### Event Patterns și Best Practices")

        st.code("""
// 1. Event delegation și performance
function TodoApp() {
    const [todos, setTodos] = useState([
        { id: 1, text: 'Learn React', completed: false },
        { id: 2, text: 'Build app', completed: false }
    ]);

    // Good: Single event handler pentru toate todos
    const handleTodoClick = (event) => {
        const todoId = parseInt(event.target.dataset.todoId);
        const action = event.target.dataset.action;

        if (action === 'toggle') {
            setTodos(prev => prev.map(todo =>
                todo.id === todoId ? { ...todo, completed: !todo.completed } : todo
            ));
        } else if (action === 'delete') {
            setTodos(prev => prev.filter(todo => todo.id !== todoId));
        }
    };

    return (
        <ul onClick={handleTodoClick}>
            {todos.map(todo => (
                <li key={todo.id}>
                    <span data-todo-id={todo.id} data-action="toggle">
                        {todo.text}
                    </span>
                    <button data-todo-id={todo.id} data-action="delete">
                        Delete
                    </button>
                </li>
            ))}
        </ul>
    );
}

// 2. Handling different event types
function FormExample() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        age: '',
        country: '',
        interests: [],
        newsletter: false
    });

    // Generic input handler
    const handleInputChange = (event) => {
        const { name, value, type, checked } = event.target;

        setFormData(prev => ({
            ...prev,
            [name]: type === 'checkbox' ? checked : value
        }));
    };

    // Checkbox group handler
    const handleInterestChange = (event) => {
        const { value, checked } = event.target;

        setFormData(prev => ({
            ...prev,
            interests: checked
                ? [...prev.interests, value]
                : prev.interests.filter(interest => interest !== value)
        }));
    };

    // File input handler
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                setFormData(prev => ({
                    ...prev,
                    avatar: e.target.result
                }));
            };
            reader.readAsDataURL(file);
        }
    };

    // Keyboard event handler
    const handleKeyDown = (event) => {
        if (event.key === 'Enter' && event.ctrlKey) {
            handleSubmit(event);
        }

        if (event.key === 'Escape') {
            resetForm();
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Submitting:', formData);
    };

    const resetForm = () => {
        setFormData({
            name: '',
            email: '',
            age: '',
            country: '',
            interests: [],
            newsletter: false
        });
    };

    return (
        <form onSubmit={handleSubmit} onKeyDown={handleKeyDown}>
            <input
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                placeholder="Name"
                required
            />

            <input
                name="email"
                type="email"
                value={formData.email}
                onChange={handleInputChange}
                placeholder="Email"
                required
            />

            <select name="country" value={formData.country} onChange={handleInputChange}>
                <option value="">Select country</option>
                <option value="US">United States</option>
                <option value="RO">Romania</option>
            </select>

            <div>
                <label>
                    <input
                        type="checkbox"
                        value="coding"
                        checked={formData.interests.includes('coding')}
                        onChange={handleInterestChange}
                    />
                    Coding
                </label>
                <label>
                    <input
                        type="checkbox"
                        value="design"
                        checked={formData.interests.includes('design')}
                        onChange={handleInterestChange}
                    />
                    Design
                </label>
            </div>

            <label>
                <input
                    name="newsletter"
                    type="checkbox"
                    checked={formData.newsletter}
                    onChange={handleInputChange}
                />
                Subscribe to newsletter
            </label>

            <input
                type="file"
                accept="image/*"
                onChange={handleFileChange}
            />

            <button type="submit">Submit</button>
            <button type="button" onClick={resetForm}>Reset</button>
        </form>
    );
}

// 3. Custom event hooks
function useKeyPress(targetKey) {
    const [keyPressed, setKeyPressed] = useState(false);

    useEffect(() => {
        const downHandler = ({ key }) => {
            if (key === targetKey) {
                setKeyPressed(true);
            }
        };

        const upHandler = ({ key }) => {
            if (key === targetKey) {
                setKeyPressed(false);
            }
        };

        window.addEventListener('keydown', downHandler);
        window.addEventListener('keyup', upHandler);

        return () => {
            window.removeEventListener('keydown', downHandler);
            window.removeEventListener('keyup', upHandler);
        };
    }, [targetKey]);

    return keyPressed;
}

// Usage
function Game() {
    const leftPressed = useKeyPress('ArrowLeft');
    const rightPressed = useKeyPress('ArrowRight');
    const spacePressed = useKeyPress(' ');

    useEffect(() => {
        if (leftPressed) console.log('Moving left');
        if (rightPressed) console.log('Moving right');
        if (spacePressed) console.log('Jumping');
    }, [leftPressed, rightPressed, spacePressed]);

    return <div>Use arrow keys and space to play!</div>;
}

// 4. Debounced events
function useDebounce(value, delay) {
    const [debouncedValue, setDebouncedValue] = useState(value);

    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);

        return () => {
            clearTimeout(handler);
        };
    }, [value, delay]);

    return debouncedValue;
}

function SearchComponent() {
    const [searchTerm, setSearchTerm] = useState('');
    const debouncedSearchTerm = useDebounce(searchTerm, 500);

    useEffect(() => {
        if (debouncedSearchTerm) {
            // Perform search
            console.log('Searching for:', debouncedSearchTerm);
        }
    }, [debouncedSearchTerm]);

    return (
        <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
        />
    );
}
        """, language="javascript")

    with react_tabs[5]:
        st.markdown("### Virtual DOM și Rendering Process")

        st.markdown("#### Cum funcționează Virtual DOM")

        st.markdown("""
        Virtual DOM este una dintre inovațiile cheie ale React. Este o reprezentare în JavaScript 
        a DOM-ului real, păstrată în memorie, care permite React să optimizeze actualizările interfeței.
        """)

        st.code("""
// Virtual DOM Element Structure
const virtualElement = {
    type: 'div',                    // Tag name sau component
    props: {                        // Attributes și event handlers
        className: 'container',
        onClick: handleClick,
        children: [                 // Child elements
            {
                type: 'h1',
                props: {
                    children: 'Hello World'
                }
            },
            {
                type: 'p',
                props: {
                    children: 'This is a paragraph'
                }
            }
        ]
    },
    key: null,                      // Pentru list optimization
    ref: null                       // Reference to DOM node
};

// JSX care creează acest Virtual DOM element:
const element = (
    <div className="container" onClick={handleClick}>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
    </div>
);

// React.createElement() equivalent:
const element = React.createElement(
    'div',
    { className: 'container', onClick: handleClick },
    React.createElement('h1', null, 'Hello World'),
    React.createElement('p', null, 'This is a paragraph')
);
        """, language="javascript")

        st.markdown("#### Reconciliation Algorithm")

        st.code("""
// React Reconciliation Process (Simplified)

// 1. Previous Virtual DOM Tree
const prevVDOM = {
    type: 'div',
    props: {
        className: 'container',
        children: [
            { type: 'h1', props: { children: 'Old Title' } },
            { type: 'p', props: { children: 'Old paragraph' } },
            { type: 'button', props: { children: 'Old Button' } }
        ]
    }
};

// 2. New Virtual DOM Tree
const nextVDOM = {
    type: 'div',
    props: {
        className: 'container updated',  // Changed
        children: [
            { type: 'h1', props: { children: 'New Title' } },      // Changed
            { type: 'p', props: { children: 'Old paragraph' } },   // Same
            { type: 'span', props: { children: 'New Element' } }   // Different type
        ]
    }
};

// 3. Diffing Result (what React calculates):
const changes = [
    {
        type: 'UPDATE_PROPS',
        target: 'div',
        changes: { className: 'container updated' }
    },
    {
        type: 'UPDATE_TEXT',
        target: 'h1',
        newText: 'New Title'
    },
    // p element unchanged - no operation needed
    {
        type: 'REPLACE_NODE',
        target: 'button',
        newNode: { type: 'span', props: { children: 'New Element' } }
    }
];

// 4. DOM Updates (what actually happens):
// Only these DOM operations are performed:
// - div.className = 'container updated'
// - h1.textContent = 'New Title'  
// - button element is replaced with span element
        """, language="javascript")

        st.markdown("#### React Fiber Architecture")

        st.code("""
// React Fiber (React 16+) - Incremental Rendering

// Fiber Node Structure (simplified)
const fiberNode = {
    type: 'div',                    // Component type
    key: null,                      // Key for reconciliation
    props: { className: 'container' }, // Props
    state: null,                    // Component state

    // Tree structure
    parent: parentFiber,            // Parent fiber
    child: firstChildFiber,         // First child
    sibling: nextSiblingFiber,      // Next sibling

    // Work tracking
    alternate: currentFiber,        // Previous fiber version
    effectTag: 'UPDATE',            // What kind of work needs to be done
    effects: [],                    // Side effects to commit

    // Scheduling
    expirationTime: 1000,           // When this work expires
    pendingProps: newProps,         // New props to apply
    memoizedProps: oldProps,        // Previous props
    memoizedState: oldState         // Previous state
};

// Work Loop (simplified)
function workLoop(deadline) {
    let shouldYield = false;

    while (nextUnitOfWork && !shouldYield) {
        nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
        shouldYield = deadline.timeRemaining() < 1;
    }

    if (!nextUnitOfWork && wipRoot) {
        commitRoot(); // Apply all changes to DOM
    }

    requestIdleCallback(workLoop);
}

// Priority Levels
const priorities = {
    ImmediatePriority: 1,      // User input, animations
    UserBlockingPriority: 2,   // User interactions
    NormalPriority: 3,         // Network responses, transitions
    LowPriority: 4,            // Analytics, non-critical updates
    IdlePriority: 5            // Background work
};

// Time Slicing Example
function App() {
    const [items, setItems] = useState([]);

    const generateItems = () => {
        // This creates a lot of work that can be interrupted
        const newItems = Array.from({ length: 10000 }, (_, i) => ({
            id: i,
            value: Math.random()
        }));
        setItems(newItems);
    };

    return (
        <div>
            <button onClick={generateItems}>Generate 10k items</button>
            {/* React can interrupt rendering of this list if higher priority work comes in */}
            {items.map(item => (
                <div key={item.id}>{item.value}</div>
            ))}
        </div>
    );
}
        """, language="javascript")

        st.markdown("#### Performance Optimization Patterns")

        st.code("""
// 1. React.memo pentru component memoization
const ExpensiveComponent = React.memo(function ExpensiveComponent({ data, onUpdate }) {
    console.log('ExpensiveComponent rendered');

    const processedData = useMemo(() => {
        return data.map(item => ({
            ...item,
            processed: expensiveComputation(item)
        }));
    }, [data]);

    return (
        <div>
            {processedData.map(item => (
                <div key={item.id}>{item.processed}</div>
            ))}
        </div>
    );
});

// Custom comparison function
const MyComponent = React.memo(function MyComponent({ user, posts }) {
    return <UserProfile user={user} posts={posts} />;
}, (prevProps, nextProps) => {
    // Return true if props are equal (skip re-render)
    return prevProps.user.id === nextProps.user.id &&
           prevProps.posts.length === nextProps.posts.length;
});

// 2. useMemo pentru expensive computations
function DataVisualization({ rawData, filters }) {
    const filteredData = useMemo(() => {
        console.log('Filtering data...');
        return rawData
            .filter(item => filters.categories.includes(item.category))
            .filter(item => item.date >= filters.startDate)
            .sort((a, b) => new Date(b.date) - new Date(a.date));
    }, [rawData, filters.categories, filters.startDate]);

    const chartData = useMemo(() => {
        console.log('Processing chart data...');
        return processDataForChart(filteredData);
    }, [filteredData]);

    return <Chart data={chartData} />;
}

// 3. useCallback pentru function memoization
function ParentComponent({ items }) {
    const [filter, setFilter] = useState('');

    // Without useCallback - new function on every render
    const handleItemClick = (itemId) => {
        console.log('Item clicked:', itemId);
        // Some logic here
    };

    // With useCallback - same function reference if dependencies don't change
    const handleItemClickMemo = useCallback((itemId) => {
        console.log('Item clicked:', itemId);
        // Some logic that depends on filter
        if (filter) {
            // Do something with filter
        }
    }, [filter]);

    return (
        <div>
            <input value={filter} onChange={(e) => setFilter(e.target.value)} />
            {items.map(item => (
                <ItemComponent
                    key={item.id}
                    item={item}
                    onClick={handleItemClickMemo} // Stable reference
                />
            ))}
        </div>
    );
}

// 4. List optimization cu keys
function OptimizedList({ items, onReorder }) {
    return (
        <div>
            {items.map((item, index) => (
                <ListItem
                    key={item.id}  // Good: stable, unique key
                    // key={index}  // Bad: can cause issues when reordering
                    item={item}
                    index={index}
                    onReorder={onReorder}
                />
            ))}
        </div>
    );
}

// 5. Code splitting și lazy loading
const LazyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
    return (
        <div>
            <Suspense fallback={<div>Loading...</div>}>
                <LazyComponent />
            </Suspense>
        </div>
    );
}

// 6. Virtualization pentru large lists
function VirtualizedList({ items }) {
    const [startIndex, setStartIndex] = useState(0);
    const [endIndex, setEndIndex] = useState(10);
    const itemHeight = 50;
    const containerHeight = 500;

    const handleScroll = (event) => {
        const scrollTop = event.target.scrollTop;
        const newStartIndex = Math.floor(scrollTop / itemHeight);
        const visibleCount = Math.ceil(containerHeight / itemHeight);

        setStartIndex(newStartIndex);
        setEndIndex(newStartIndex + visibleCount);
    };

    const visibleItems = items.slice(startIndex, endIndex);

    return (
        <div 
            style={{ height: containerHeight, overflow: 'auto' }}
            onScroll={handleScroll}
        >
            <div style={{ height: items.length * itemHeight, position: 'relative' }}>
                {visibleItems.map((item, index) => (
                    <div
                        key={item.id}
                        style={{
                            position: 'absolute',
                            top: (startIndex + index) * itemHeight,
                            height: itemHeight,
                            width: '100%'
                        }}
                    >
                        {item.content}
                    </div>
                ))}
            </div>
        </div>
    );
}
        """, language="javascript")

    with react_tabs[6]:
        st.markdown("### React Ecosystem")

        st.markdown("#### Instrumentele esențiale pentru dezvoltarea React")

        ecosystem_categories = {
            "Development Tools": {
                "Create React App": "Tool oficial pentru inițializarea proiectelor React cu zero configurație",
                "Vite": "Build tool rapid cu HMR îmbunătățit pentru dezvoltare",
                "React Developer Tools": "Extensie browser pentru debugging React components și hooks",
                "ESLint + Prettier": "Linting și code formatting pentru cod consistent",
                "TypeScript": "Type safety pentru aplicații React mari"
            },
            "Routing": {
                "React Router": "Standard pentru client-side routing în aplicații SPA",
                "Reach Router": "Router simplu (acum integrat în React Router v6)",
                "Next.js Router": "File-based routing pentru aplicații Next.js"
            },
            "State Management": {
                "Redux Toolkit": "Approach modern pentru Redux cu mai puțin boilerplate",
                "Zustand": "State manager simplu și lightweight",
                "Jotai": "Atomic state management cu approach bottom-up",
                "Context API": "Built-in React pentru state global simplu",
                "React Query/TanStack Query": "Server state management și caching"
            },
            "Styling": {
                "Styled Components": "CSS-in-JS cu template literals",
                "Emotion": "CSS-in-JS library performantă",
                "Tailwind CSS": "Utility-first CSS framework",
                "Chakra UI": "Component library cu design system",
                "Material-UI": "React components implementând Material Design"
            },
            "Forms": {
                "React Hook Form": "Performant forms cu minimal re-renders",
                "Formik": "Form library cu validation integrat",
                "React Final Form": "High performance subscription-based form state"
            },
            "Testing": {
                "Jest": "JavaScript testing framework",
                "React Testing Library": "Testing utilities pentru React components",
                "Enzyme": "JavaScript testing utility (mai puțin folosit recent)",
                "Cypress": "End-to-end testing framework"
            },
            "UI Component Libraries": {
                "Ant Design": "Enterprise-grade UI library cu multe componente",
                "React Bootstrap": "Bootstrap components pentru React",
                "Semantic UI React": "React integration pentru Semantic UI",
                "Mantine": "Modern React components library",
                "Headless UI": "Unstyled, accessible UI components"
            }
        }

        for category, tools in ecosystem_categories.items():
            st.markdown(f"#### {category}")
            for tool, description in tools.items():
                st.markdown(f"- **{tool}**: {description}")
            st.markdown("")

        st.markdown("#### Comparație State Management Solutions")

        st.code("""
// 1. Context API (Built-in)
const ThemeContext = createContext();

function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

// Pros: Built-in, no dependencies
// Cons: Can cause unnecessary re-renders, verbose for complex state

// 2. Redux Toolkit (Traditional but modernized)
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
    name: 'counter',
    initialState: { value: 0 },
    reducers: {
        increment: (state) => {
            state.value += 1; // Immer makes this immutable
        },
        decrement: (state) => {
            state.value -= 1;
        }
    }
});

const store = configureStore({
    reducer: { counter: counterSlice.reducer }
});

// Pros: Predictable, great DevTools, time-travel debugging
// Cons: Boilerplate, learning curve, might be overkill for simple apps

// 3. Zustand (Simple and modern)
import { create } from 'zustand';

const useStore = create((set) => ({
    count: 0,
    increment: () => set((state) => ({ count: state.count + 1 })),
    decrement: () => set((state) => ({ count: state.count - 1 })),
    reset: () => set({ count: 0 })
}));

// Usage
function Counter() {
    const { count, increment, decrement } = useStore();
    return (
        <div>
            <span>{count}</span>
            <button onClick={increment}>+</button>
            <button onClick={decrement}>-</button>
        </div>
    );
}

// Pros: Minimal boilerplate, TypeScript friendly, no providers needed
// Cons: Less ecosystem support than Redux

// 4. React Query pentru server state
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function UserProfile({ userId }) {
    const queryClient = useQueryClient();

    const { data: user, isLoading, error } = useQuery({
        queryKey: ['user', userId],
        queryFn: () => fetchUser(userId),
        staleTime: 5 * 60 * 1000, // 5 minutes
    });

    const updateUserMutation = useMutation({
        mutationFn: updateUser,
        onSuccess: () => {
            queryClient.invalidateQueries(['user', userId]);
        },
    });

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div>
            <h1>{user.name}</h1>
            <button onClick={() => updateUserMutation.mutate({ id: userId, name: 'New Name' })}>
                Update Name
            </button>
        </div>
    );
}

// Pros: Caching, background updates, optimistic updates, offline support
// Cons: Additional learning curve, focused on server state only
        """, language="javascript")

        st.markdown("#### Framework-uri built on React")

        frameworks = {
            "Next.js": {
                "description": "Full-stack React framework cu SSR, SSG, și API routes",
                "use_cases": "E-commerce, blog-uri, aplicații enterprise cu SEO requirements",
                "pros": "SEO excelent, performance, file-based routing, API integration",
                "cons": "Overhead pentru aplicații simple, vendor lock-in"
            },
            "Gatsby": {
                "description": "Static site generator cu GraphQL și plugin ecosystem",
                "use_cases": "Blog-uri, documentație, marketing sites, portfolios",
                "pros": "Performance excelentă, SEO, plugin ecosystem bogat",
                "cons": "Build times mari pentru site-uri mari, learning curve pentru GraphQL"
            },
            "Remix": {
                "description": "Full-stack framework focusat pe web standards și UX",
                "use_cases": "Aplicații web tradiționale cu enhanced UX",
                "pros": "Web standards, progressive enhancement, excellent UX",
                "cons": "Nou pe piață, ecosistem mai mic"
            }
        }

        for framework, details in frameworks.items():
            st.markdown(f"**{framework}**")
            st.markdown(f"- **Descriere**: {details['description']}")
            st.markdown(f"- **Use cases**: {details['use_cases']}")
            st.markdown(f"- **Pros**: {details['pros']}")
            st.markdown(f"- **Cons**: {details['cons']}")
            st.markdown("")

    with react_tabs[7]:
        st.markdown("### Best Practices React")

        st.markdown("#### Arhitectura componentelor")

        st.code("""
// 1. Single Responsibility Principle
// Bad: Component that does too much
function UserDashboard({ userId }) {
    const [user, setUser] = useState(null);
    const [posts, setPosts] = useState([]);
    const [notifications, setNotifications] = useState([]);
    const [theme, setTheme] = useState('light');

    // Lots of useEffect hooks and logic...

    return (
        <div>
            {/* Lots of JSX mixing different concerns */}
        </div>
    );
}

// Good: Separate components for different responsibilities
function UserDashboard({ userId }) {
    return (
        <div className="dashboard">
            <UserProfile userId={userId} />
            <UserPosts userId={userId} />
            <NotificationCenter userId={userId} />
        </div>
    );
}

function UserProfile({ userId }) {
    const { user, loading, error } = useUser(userId);

    if (loading) return <UserProfileSkeleton />;
    if (error) return <ErrorMessage error={error} />;
    if (!user) return <EmptyState message="User not found" />;

    return (
        <div className="user-profile">
            <UserAvatar user={user} />
            <UserDetails user={user} />
            <UserActions user={user} />
        </div>
    );
}

// 2. Container vs Presentational Components
// Container Component (Smart/Stateful)
function UserListContainer() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [filter, setFilter] = useState('');

    useEffect(() => {
        fetchUsers().then(setUsers).finally(() => setLoading(false));
    }, []);

    const filteredUsers = users.filter(user => 
        user.name.toLowerCase().includes(filter.toLowerCase())
    );

    const handleUserSelect = (user) => {
        // Handle business logic
    };

    return (
        <UserListPresentation
            users={filteredUsers}
            loading={loading}
            filter={filter}
            onFilterChange={setFilter}
            onUserSelect={handleUserSelect}
        />
    );
}

// Presentational Component (Dumb/Stateless)
function UserListPresentation({ 
    users, 
    loading, 
    filter, 
    onFilterChange, 
    onUserSelect 
}) {
    return (
        <div className="user-list">
            <SearchInput
                value={filter}
                onChange={onFilterChange}
                placeholder="Search users..."
            />

            {loading ? (
                <LoadingSpinner />
            ) : (
                <div className="user-grid">
                    {users.map(user => (
                        <UserCard
                            key={user.id}
                            user={user}
                            onClick={() => onUserSelect(user)}
                        />
                    ))}
                </div>
            )}
        </div>
    );
}

// 3. Custom Hooks pentru logic reuse
function useUsers() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchUsers = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);
            const userData = await api.getUsers();
            setUsers(userData);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchUsers();
    }, [fetchUsers]);

    const addUser = useCallback(async (userData) => {
        try {
            const newUser = await api.createUser(userData);
            setUsers(prev => [...prev, newUser]);
            return newUser;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);

    const updateUser = useCallback(async (userId, updates) => {
        try {
            const updatedUser = await api.updateUser(userId, updates);
            setUsers(prev => prev.map(user => 
                user.id === userId ? updatedUser : user
            ));
            return updatedUser;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);

    const deleteUser = useCallback(async (userId) => {
        try {
            await api.deleteUser(userId);
            setUsers(prev => prev.filter(user => user.id !== userId));
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);

    return {
        users,
        loading,
        error,
        refetch: fetchUsers,
        addUser,
        updateUser,
        deleteUser
    };
}
        """, language="javascript")

        st.markdown("#### Performance Best Practices")

        st.code("""
// 1. Prop drilling vs Context usage
// Bad: Prop drilling through many components
function App() {
    const [user, setUser] = useState(null);
    const [theme, setTheme] = useState('light');

    return (
        <Layout user={user} theme={theme} setTheme={setTheme}>
            <Dashboard user={user} theme={theme} setTheme={setTheme}>
                <Sidebar user={user} theme={theme} setTheme={setTheme}>
                    <UserMenu user={user} theme={theme} setTheme={setTheme} />
                </Sidebar>
            </Dashboard>
        </Layout>
    );
}

// Good: Use Context for widely needed data
const AppContext = createContext();

function AppProvider({ children }) {
    const [user, setUser] = useState(null);
    const [theme, setTheme] = useState('light');

    return (
        <AppContext.Provider value={{ user, setUser, theme, setTheme }}>
            {children}
        </AppContext.Provider>
    );
}

function UserMenu() {
    const { user, theme, setTheme } = useContext(AppContext);
    // Use context data directly
}

// 2. Memoization patterns
const ExpensiveList = React.memo(function ExpensiveList({ items, onItemClick }) {
    console.log('ExpensiveList render');

    return (
        <div>
            {items.map(item => (
                <ExpensiveItem
                    key={item.id}
                    item={item}
                    onClick={onItemClick}
                />
            ))}
        </div>
    );
});

const ExpensiveItem = React.memo(function ExpensiveItem({ item, onClick }) {
    const handleClick = useCallback(() => {
        onClick(item.id);
    }, [item.id, onClick]);

    const processedData = useMemo(() => {
        return expensiveComputation(item);
    }, [item]);

    return (
        <div onClick={handleClick}>
            {processedData}
        </div>
    );
});

// 3. Error Boundaries
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null, errorInfo: null };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true };
    }

    componentDidCatch(error, errorInfo) {
        this.setState({
            error: error,
            errorInfo: errorInfo
        });

        // Log error to monitoring service
        console.error('Error caught by boundary:', error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return (
                <div className="error-boundary">
                    <h2>Something went wrong</h2>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        {this.state.error && this.state.error.toString()}
                        <br />
                        {this.state.errorInfo.componentStack}
                    </details>
                </div>
            );
        }

        return this.props.children;
    }
}

// Usage
function App() {
    return (
        <ErrorBoundary>
            <Header />
            <ErrorBoundary>
                <MainContent />
            </ErrorBoundary>
            <ErrorBoundary>
                <Sidebar />
            </ErrorBoundary>
        </ErrorBoundary>
    );
}

// 4. Proper cleanup în useEffect
function Component() {
    useEffect(() => {
        const controller = new AbortController();

        async function fetchData() {
            try {
                const response = await fetch('/api/data', {
                    signal: controller.signal
                });
                const data = await response.json();
                setData(data);
            } catch (error) {
                if (error.name !== 'AbortError') {
                    setError(error);
                }
            }
        }

        fetchData();

        return () => {
            controller.abort(); // Cleanup
        };
    }, []);

    useEffect(() => {
        const interval = setInterval(() => {
            updateData();
        }, 1000);

        return () => clearInterval(interval); // Cleanup
    }, []);

    useEffect(() => {
        const handleResize = () => setWindowSize(window.innerWidth);
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize); // Cleanup
        };
    }, []);
}
        """, language="javascript")

        st.markdown("#### Code Organization și File Structure")

        st.code("""
// Recommended folder structure for React apps

src/
├── components/           # Reusable UI components
│   ├── ui/              # Basic UI components (Button, Input, etc.)
│   │   ├── Button/
│   │   │   ├── Button.jsx
│   │   │   ├── Button.test.js
│   │   │   ├── Button.stories.js
│   │   │   └── index.js
│   │   └── Input/
│   └── layout/          # Layout components (Header, Footer, etc.)
├── pages/               # Page components (top-level routes)
├── hooks/               # Custom hooks
├── services/            # API calls and external services
├── utils/               # Utility functions
├── contexts/            # React contexts
├── store/               # State management (Redux/Zustand)
├── styles/              # Global styles
├── assets/              # Images, fonts, etc.
├── types/               # TypeScript type definitions
└── __tests__/           # Test utilities and global tests

// Component naming conventions
// ✅ Good
export function UserProfile() { }
export const UserProfile = () => { };

// Component file naming
// ✅ Good
UserProfile.jsx
UserProfile.tsx
user-profile.jsx  // kebab-case alternative

// ❌ Avoid
userProfile.jsx   // camelCase for files
UserProfile.js    // .js extension for JSX

// Export patterns
// Named export (preferred for most components)
export function Button({ children, onClick }) {
    return <button onClick={onClick}>{children}</button>;
}

// Default export with named function
export default function Button({ children, onClick }) {
    return <button onClick={onClick}>{children}</button>;
}

// Barrel exports (index.js files)
// components/ui/index.js
export { Button } from './Button';
export { Input } from './Input';
export { Card } from './Card';

// Usage
import { Button, Input, Card } from 'components/ui';

// API service organization
// services/api.js
const API_BASE_URL = process.env.REACT_APP_API_URL;

class ApiService {
    async request(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        };

        if (config.body && typeof config.body === 'object') {
            config.body = JSON.stringify(config.body);
        }

        const response = await fetch(url, config);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return response.json();
    }

    get(endpoint) {
        return this.request(endpoint);
    }

    post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: data,
        });
    }

    put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: data,
        });
    }

    delete(endpoint) {
        return this.request(endpoint, {
            method: 'DELETE',
        });
    }
}

export const api = new ApiService();

// services/userService.js
import { api } from './api';

export const userService = {
    getUsers: () => api.get('/users'),
    getUser: (id) => api.get(`/users/${id}`),
    createUser: (userData) => api.post('/users', userData),
    updateUser: (id, userData) => api.put(`/users/${id}`, userData),
    deleteUser: (id) => api.delete(`/users/${id}`),
};
        """, language="javascript")

    with react_tabs[8]:
        st.markdown("### Întrebări frecvente la interviuri React")

        react_qa = [
            {
                "question": "Explică Virtual DOM și cum îmbunătățește performanța",
                "answer": """
                **Virtual DOM** este o reprezentare în JavaScript a DOM-ului real, păstrată în memorie.

                **Cum funcționează:**
                1. React creează o copie virtuală a DOM-ului în JavaScript
                2. Când state-ul se schimbă, se creează un nou Virtual DOM tree
                3. React compară (diff) noul tree cu cel precedent
                4. Calculează setul minimal de schimbări necesare (reconciliation)
                5. Aplică doar aceste schimbări în DOM-ul real (commit phase)

                **Avantaje performanță:**
                - **Batching**: Grupează multiple actualizări într-o singură operație DOM
                - **Minimal updates**: Doar elementele modificate sunt actualizate
                - **Predictable performance**: Algoritmul de diffing este O(n) în loc de O(n³)
                - **Cross-browser consistency**: Abstractizează diferențele între browsere

                **Reconciliation algorithm**: Folosește heuristica că două elemente de tipuri diferite vor produce arbori diferiți, și dezvoltatorii pot indica care elemente copil rămân stabile prin key prop.
                """
            },
            {
                "question": "Care este diferența între useState și useRef? Când folosești fiecare?",
                "answer": """
                **useState:**
                - **Purpose**: Gestionează starea componentei care declanșează re-render
                - **Re-render**: DA - componenta se re-renderează când se schimbă
                - **Persistence**: Valoarea persistă între render-uri
                - **Usage**: Pentru date care afectează UI-ul

                **useRef:**
                - **Purpose**: Păstrează o referință mutabilă care nu declanșează re-render
                - **Re-render**: NU - modificarea valorii nu re-renderează componenta
                - **Persistence**: Valoarea persistă între render-uri
                - **Usage**: Pentru access la DOM elements, storing mutable values

                **Când să folosești useState:**
                ```javascript
                const [count, setCount] = useState(0); // UI depends on count
                const [user, setUser] = useState(null); // UI shows user data
                ```

                **Când să folosești useRef:**
                ```javascript
                const inputRef = useRef(null); // Access DOM element
                const timerRef = useRef(null); // Store timer ID
                const prevValueRef = useRef(); // Store previous value
                ```

                **Important**: useRef.current este mutabil și modificarea lui nu declanșează re-render, în timp ce useState setter declanșează întotdeauna re-render.
                """
            },
            {
                "question": "Explică React Fiber și cum îmbunătățește user experience",
                "answer": """
                **React Fiber** este reimplementarea algoritmului de reconciliation din React 16+.

                **Problema anterioară (Stack Reconciler):**
                - Procesarea era sincronă și bloca thread-ul principal
                - Updates mari puteau cauza frame drops și UI jank
                - Nu se putea întrerupe pentru high-priority updates

                **Soluția Fiber:**
                - **Incremental rendering**: Împarte lucrul în unități mici
                - **Interruptible**: Poate fi întrerupt pentru priority tasks
                - **Resumable**: Poate continua lucrul după întrerupere
                - **Time slicing**: Folosește requestIdleCallback pentru smooth UX

                **Priority levels:**
                1. **Immediate**: User input (clicks, typing)
                2. **UserBlocking**: Hover effects, scrolling  
                3. **Normal**: Network responses, transitions
                4. **Low**: Analytics, logging
                5. **Idle**: Background work

                **Beneficii UX:**
                - UI rămâne responsive în timpul updates mari
                - Animațiile nu se blochează
                - User input are întotdeauna prioritate
                - Better perceived performance

                **Implementation**: Fiber node-urile formează o linked list care poate fi traversată incremental, permițând pauze și reluări.
                """
            },
            {
                "question": "Cum funcționează React key prop și de ce este important?",
                "answer": """
                **Key prop** este un hint special pentru algoritMul de reconciliation al React.

                **Cum funcționează:**
                - React folosește keys pentru a identifica care items au fost schimbați, adăugați sau eliminați
                - În timpul diffing, React compară keys pentru a decide dacă să refolosească un element existent
                - Fără keys, React folosește ordinea elementelor (index-based)

                **Probleme fără keys sau cu keys greșite:**
                ```javascript
                // Bad: Using array index
                {items.map((item, index) => (
                    <Item key={index} data={item} />
                ))}
                // Problem: Reordering causes unnecessary re-renders and lost state

                // Bad: Non-unique keys
                {items.map(item => (
                    <Item key={item.category} data={item} />
                ))}
                // Problem: Multiple items with same key cause rendering issues
                ```

                **Correct usage:**
                ```javascript
                // Good: Stable, unique keys
                {items.map(item => (
                    <Item key={item.id} data={item} />
                ))}
                ```

                **Performance impact:**
                - **Correct keys**: Efficient reconciliation, preserved component state
                - **Wrong keys**: Unnecessary unmounting/mounting, lost state, poor performance

                **Key best practices:**
                - Use stable, unique identifiers (IDs from database)
                - Avoid array indices unless list never reorders
                - Don't generate keys during render (Math.random(), Date.now())
                """
            },
            {
                "question": "Care este diferența între Class Components și Function Components?",
                "answer": """
                **Class Components (Legacy approach):**
                ```javascript
                class UserProfile extends React.Component {
                    constructor(props) {
                        super(props);
                        this.state = { user: null };
                    }

                    componentDidMount() {
                        this.fetchUser();
                    }

                    componentDidUpdate(prevProps) {
                        if (prevProps.userId !== this.props.userId) {
                            this.fetchUser();
                        }
                    }

                    componentWillUnmount() {
                        this.cleanup();
                    }

                    render() {
                        return <div>{this.state.user?.name}</div>;
                    }
                }
                ```

                **Function Components (Modern approach):**
                ```javascript
                function UserProfile({ userId }) {
                    const [user, setUser] = useState(null);

                    useEffect(() => {
                        fetchUser(userId).then(setUser);
                        return cleanup; // componentWillUnmount equivalent
                    }, [userId]); // componentDidUpdate equivalent

                    return <div>{user?.name}</div>;
                }
                ```

                **Diferențe cheie:**
                - **Sintaxă**: Function components sunt mai concise
                - **State**: Class folosește this.state, Function folosește hooks
                - **Lifecycle**: Class are metode specifice, Function folosește useEffect
                - **Performance**: Function components sunt optimizate mai bine
                - **Reusability**: Custom hooks permit sharing logic între componente
                - **Testing**: Function components sunt mai ușor de testat

                **De ce Function Components sunt preferate:**
                - Mai puțin boilerplate code
                - Hooks permit logic reuse
                - Better tree-shaking și code splitting
                - Viitorul React development se focusează pe function components
                """
            },
            {
                "question": "Explică React Context și când să îl folosești vs alte state management solutions",
                "answer": """
                **React Context** permite transmiterea datelor prin component tree fără prop drilling.

                **Cum funcționează:**
                ```javascript
                // 1. Create context
                const UserContext = createContext();

                // 2. Provide value
                function App() {
                    const [user, setUser] = useState(null);
                    return (
                        <UserContext.Provider value={{ user, setUser }}>
                            <ComponentTree />
                        </UserContext.Provider>
                    );
                }

                // 3. Consume value
                function Profile() {
                    const { user } = useContext(UserContext);
                    return <div>{user?.name}</div>;
                }
                ```

                **Când să folosești Context:**
                - Theme/UI preferences (dark/light mode)
                - Current user authentication
                - Language/localization
                - Application-wide settings
                - Data needed by many components at different nesting levels

                **Când să NU folosești Context:**
                - Frequently changing data (causes unnecessary re-renders)
                - Complex state logic (use useReducer or external libraries)
                - Performance-critical applications with deep nesting
                - Caching și server state management

                **Context vs alternatives:**
                - **vs Prop drilling**: Context elimină prop drilling dar poate cauza over-rendering
                - **vs Redux**: Context e built-in dar Redux oferă mai multe features (DevTools, middleware)
                - **vs State management libs**: Context e simplu pentru cazuri simple, libs externe pentru complexitate

                **Performance considerations**: Split contexts pentru different concerns pentru a evita unnecessary re-renders.
                """
            },
            {
                "question": "Cum optimizezi performanța unei aplicații React mari?",
                "answer": """
                **1. Component-level optimizations:**
                - **React.memo()**: Memoizează componente pentru props shallow comparison
                - **useMemo()**: Memoizează expensive computations
                - **useCallback()**: Memoizează functions pentru stable references
                - **Proper key props**: Pentru efficient list rendering

                **2. Bundle optimization:**
                - **Code splitting**: React.lazy() și dynamic imports
                - **Tree shaking**: Elimină unused code
                - **Bundle analysis**: Identify și elimină large dependencies
                - **Lazy loading**: Load componente on demand

                **3. State management:**
                - **Normalize state**: Avoid nested objects/arrays
                - **Split contexts**: Prevent unnecessary re-renders
                - **Proper dependency arrays**: În useEffect și useCallback
                - **State colocation**: Keep state close to where it's used

                **4. Network optimization:**
                - **React Query/SWR**: Pentru server state management și caching
                - **Request deduplication**: Prevent duplicate API calls
                - **Prefetching**: Load data before it's needed
                - **Image optimization**: Lazy loading, proper formats

                **5. Rendering optimization:**
                - **Virtualization**: Pentru large lists (react-window)
                - **Debouncing**: Pentru search inputs și expensive operations
                - **Error boundaries**: Prevent entire app crashes
                - **Suspense**: Better loading states

                **6. Development tools:**
                - **React DevTools Profiler**: Identify performance bottlenecks
                - **Bundle analyzers**: webpack-bundle-analyzer
                - **Performance monitoring**: Core Web Vitals tracking
                """
            }
        ]

        for qa in react_qa:
            with st.expander(f"❓ {qa['question']}"):
                st.markdown(qa['answer'])

    # Final summary
    st.markdown("---")
    st.markdown("""
    
    """, unsafe_allow_html=True)


def components_page():
    """React Components - Complete educational content"""
    st.markdown('<h1 class="chapter-header">Componentele React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Components - Building blocks ale aplicațiilor React</h3>
        <p>Componentele sunt fundamentul arhitecturii React. Ele încapsulează logica și interfața unei părți 
        specifice din aplicație, permitând reutilizarea și mentenabilitatea codului. Acest capitol acoperă 
        de la conceptele de bază până la patterns avansate folosite în aplicații enterprise de producție.</p>
    </div>
    """, unsafe_allow_html=True)

    # Components Tabs
    components_tabs = st.tabs([
        "Types & Fundamentals",
        "Component Communication",
        "Composition Patterns",
        "Lifecycle Management",
        "Performance Optimization",
        "Advanced Patterns",
        "Testing Components",
        "Architecture & Design",
        "Întrebări Interviu"
    ])

    with components_tabs[0]:
        st.markdown("### Tipuri de componente și evoluția lor")

        st.markdown("""
        React a evoluat de la Class Components la Function Components cu hooks. 
        Înțelegerea ambelor abordări este esențială pentru munca cu codebases existente și pentru interviuri.
        """)

        st.markdown("#### Class Components - Legacy dar încă importante")

        st.code("""
// Class Component cu toate lifecycle methods
class UserProfile extends React.Component {
    constructor(props) {
        super(props);

        // Initial state
        this.state = {
            user: null,
            loading: true,
            error: null,
            posts: [],
            isEditing: false
        };

        // Bind methods (pentru correct this context)
        this.handleEdit = this.handleEdit.bind(this);
        this.handleSave = this.handleSave.bind(this);
    }

    // Lifecycle: Component mounting
    componentDidMount() {
        this.fetchUserData();
        this.setupEventListeners();
    }

    // Lifecycle: Component updating
    componentDidUpdate(prevProps, prevState) {
        // Re-fetch data când props se schimbă
        if (prevProps.userId !== this.props.userId) {
            this.fetchUserData();
        }

        // Logic bazată pe state changes
        if (prevState.isEditing !== this.state.isEditing) {
            this.handleEditModeChange();
        }
    }

    // Lifecycle: Component unmounting
    componentWillUnmount() {
        this.cleanupEventListeners();
        this.cancelPendingRequests();
    }

    // Error boundary method
    componentDidCatch(error, errorInfo) {
        console.error('Error in UserProfile:', error, errorInfo);
        this.setState({ error: error.message });
    }

    // Instance methods
    fetchUserData = async () => {
        try {
            this.setState({ loading: true, error: null });

            const [userResponse, postsResponse] = await Promise.all([
                fetch(`/api/users/${this.props.userId}`),
                fetch(`/api/users/${this.props.userId}/posts`)
            ]);

            const user = await userResponse.json();
            const posts = await postsResponse.json();

            this.setState({ user, posts, loading: false });
        } catch (error) {
            this.setState({ error: error.message, loading: false });
        }
    };

    handleEdit() {
        this.setState({ isEditing: true });
    }

    handleSave = async (userData) => {
        try {
            const response = await fetch(`/api/users/${this.props.userId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            const updatedUser = await response.json();
            this.setState({ 
                user: updatedUser, 
                isEditing: false 
            });

            this.props.onUserUpdate?.(updatedUser);
        } catch (error) {
            this.setState({ error: error.message });
        }
    };

    setupEventListeners() {
        window.addEventListener('resize', this.handleResize);
    }

    cleanupEventListeners() {
        window.removeEventListener('resize', this.handleResize);
    }

    handleResize = () => {
        // Handle responsive behavior
    };

    cancelPendingRequests() {
        // Cancel any pending async operations
    }

    handleEditModeChange() {
        if (this.state.isEditing) {
            // Focus first input when entering edit mode
            setTimeout(() => {
                const firstInput = document.querySelector('.user-form input');
                firstInput?.focus();
            }, 0);
        }
    }

    render() {
        const { user, loading, error, posts, isEditing } = this.state;
        const { className, onUserUpdate, ...otherProps } = this.props;

        if (loading) {
            return <LoadingSpinner />;
        }

        if (error) {
            return (
                <ErrorMessage 
                    error={error} 
                    onRetry={this.fetchUserData}
                />
            );
        }

        if (!user) {
            return <EmptyState message="User not found" />;
        }

        return (
            <div className={`user-profile ${className || ''}`} {...otherProps}>
                <div className="user-header">
                    <UserAvatar user={user} size="large" />
                    <div className="user-info">
                        {isEditing ? (
                            <UserEditForm
                                user={user}
                                onSave={this.handleSave}
                                onCancel={() => this.setState({ isEditing: false })}
                            />
                        ) : (
                            <UserDisplay
                                user={user}
                                onEdit={this.handleEdit}
                            />
                        )}
                    </div>
                </div>

                <div className="user-posts">
                    <h3>Recent Posts ({posts.length})</h3>
                    <PostList posts={posts} />
                </div>
            </div>
        );
    }
}

// PropTypes pentru validation
UserProfile.propTypes = {
    userId: PropTypes.string.isRequired,
    className: PropTypes.string,
    onUserUpdate: PropTypes.func
};

UserProfile.defaultProps = {
    className: '',
    onUserUpdate: null
};
        """, language="javascript")

        st.markdown("#### Function Components - Modern approach")

        st.code("""
import { useState, useEffect, useCallback, useMemo } from 'react';

// Same functionality ca Class Component dar cu hooks
function UserProfile({ userId, className = '', onUserUpdate }) {
    // State hooks
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [posts, setPosts] = useState([]);
    const [isEditing, setIsEditing] = useState(false);

    // Memoized values
    const userDisplayName = useMemo(() => {
        return user ? `${user.firstName} ${user.lastName}` : '';
    }, [user]);

    // Memoized callbacks
    const handleEdit = useCallback(() => {
        setIsEditing(true);
    }, []);

    const handleSave = useCallback(async (userData) => {
        try {
            const response = await fetch(`/api/users/${userId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            const updatedUser = await response.json();
            setUser(updatedUser);
            setIsEditing(false);
            onUserUpdate?.(updatedUser);
        } catch (error) {
            setError(error.message);
        }
    }, [userId, onUserUpdate]);

    const handleCancel = useCallback(() => {
        setIsEditing(false);
    }, []);

    // Custom hook pentru data fetching
    const fetchUserData = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);

            const [userResponse, postsResponse] = await Promise.all([
                fetch(`/api/users/${userId}`),
                fetch(`/api/users/${userId}/posts`)
            ]);

            const userData = await userResponse.json();
            const postsData = await postsResponse.json();

            setUser(userData);
            setPosts(postsData);
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    }, [userId]);

    // Effect hooks
    useEffect(() => {
        fetchUserData();
    }, [fetchUserData]);

    // Handle edit mode changes
    useEffect(() => {
        if (isEditing) {
            const timer = setTimeout(() => {
                const firstInput = document.querySelector('.user-form input');
                firstInput?.focus();
            }, 0);

            return () => clearTimeout(timer);
        }
    }, [isEditing]);

    // Window resize handler
    useEffect(() => {
        const handleResize = () => {
            // Handle responsive behavior
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    // Cleanup effect
    useEffect(() => {
        return () => {
            // Cancel any pending operations
        };
    }, []);

    // Early returns pentru loading states
    if (loading) return <LoadingSpinner />;
    if (error) return <ErrorMessage error={error} onRetry={fetchUserData} />;
    if (!user) return <EmptyState message="User not found" />;

    return (
        <div className={`user-profile ${className}`}>
            <div className="user-header">
                <UserAvatar user={user} size="large" />
                <div className="user-info">
                    {isEditing ? (
                        <UserEditForm
                            user={user}
                            onSave={handleSave}
                            onCancel={handleCancel}
                        />
                    ) : (
                        <UserDisplay
                            user={user}
                            displayName={userDisplayName}
                            onEdit={handleEdit}
                        />
                    )}
                </div>
            </div>

            <div className="user-posts">
                <h3>Recent Posts ({posts.length})</h3>
                <PostList posts={posts} />
            </div>
        </div>
    );
}

// Modern approach pentru PropTypes (TypeScript e preferabil)
UserProfile.propTypes = {
    userId: PropTypes.string.isRequired,
    className: PropTypes.string,
    onUserUpdate: PropTypes.func
};
        """, language="javascript")

        st.markdown("#### Specialized Component Types")

        st.code("""
// 1. Pure Components (Class)
class PureCounter extends React.PureComponent {
    render() {
        console.log('PureCounter rendered');
        return <div>Count: {this.props.count}</div>;
    }
}

// Equivalent cu React.memo (Function)
const MemoCounter = React.memo(function Counter({ count }) {
    console.log('MemoCounter rendered');
    return <div>Count: {count}</div>;
});

// 2. Forward Ref Components
const FancyButton = React.forwardRef(function FancyButton(props, ref) {
    return (
        <button ref={ref} className="fancy-button" {...props}>
            {props.children}
        </button>
    );
});

// Usage
function App() {
    const buttonRef = useRef(null);

    const focusButton = () => {
        buttonRef.current?.focus();
    };

    return (
        <div>
            <FancyButton ref={buttonRef}>Click me</FancyButton>
            <button onClick={focusButton}>Focus fancy button</button>
        </div>
    );
}

// 3. Error Boundary Components (doar Class Components)
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null, errorInfo: null };
    }

    static getDerivedStateFromError(error) {
        // Update state to trigger fallback UI
        return { hasError: true };
    }

    componentDidCatch(error, errorInfo) {
        // Log error details
        this.setState({
            error,
            errorInfo
        });

        // Send error to monitoring service
        this.logErrorToService(error, errorInfo);
    }

    logErrorToService(error, errorInfo) {
        // Send to Sentry, LogRocket, etc.
        console.error('Error logged:', error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return (
                <div className="error-fallback">
                    <h2>Something went wrong</h2>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        <summary>Error details</summary>
                        {this.state.error && this.state.error.toString()}
                        <br />
                        {this.state.errorInfo.componentStack}
                    </details>
                    <button 
                        onClick={() => this.setState({ hasError: false, error: null, errorInfo: null })}
                    >
                        Try again
                    </button>
                </div>
            );
        }

        return this.props.children;
    }
}

// 4. Higher-Order Components (HOCs)
function withAuth(WrappedComponent) {
    return function AuthenticatedComponent(props) {
        const { isAuthenticated, user } = useAuth();

        if (!isAuthenticated) {
            return <LoginPrompt />;
        }

        return <WrappedComponent {...props} user={user} />;
    };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);

// 5. Render Props Components
class MouseTracker extends React.Component {
    state = { x: 0, y: 0 };

    handleMouseMove = (event) => {
        this.setState({
            x: event.clientX,
            y: event.clientY
        });
    };

    render() {
        return (
            <div style={{ height: '100vh' }} onMouseMove={this.handleMouseMove}>
                {this.props.children(this.state)}
            </div>
        );
    }
}

// Usage
<MouseTracker>
    {({ x, y }) => (
        <div>Mouse position: ({x}, {y})</div>
    )}
</MouseTracker>

// 6. Compound Components
function Tabs({ children, defaultActiveKey }) {
    const [activeKey, setActiveKey] = useState(defaultActiveKey);

    return (
        <div className="tabs">
            {React.Children.map(children, (child, index) => {
                if (child.type === TabList) {
                    return React.cloneElement(child, { activeKey, setActiveKey });
                }
                if (child.type === TabPanels) {
                    return React.cloneElement(child, { activeKey });
                }
                return child;
            })}
        </div>
    );
}

function TabList({ children, activeKey, setActiveKey }) {
    return (
        <div className="tab-list">
            {React.Children.map(children, (child, index) => 
                React.cloneElement(child, { 
                    index, 
                    isActive: index === activeKey,
                    onClick: () => setActiveKey(index)
                })
            )}
        </div>
    );
}

function Tab({ children, isActive, onClick }) {
    return (
        <button 
            className={`tab ${isActive ? 'active' : ''}`}
            onClick={onClick}
        >
            {children}
        </button>
    );
}

function TabPanels({ children, activeKey }) {
    return (
        <div className="tab-panels">
            {React.Children.toArray(children)[activeKey]}
        </div>
    );
}

function TabPanel({ children }) {
    return <div className="tab-panel">{children}</div>;
}

// Usage
<Tabs defaultActiveKey={0}>
    <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
    </TabList>
    <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
    </TabPanels>
</Tabs>
        """, language="javascript")

    with components_tabs[1]:
        st.markdown("### Component Communication")

        st.markdown("#### Props - Data flow de la părinte la copil")

        st.code("""
// 1. Basic Props Passing
function ParentComponent() {
    const user = {
        id: 1,
        name: 'John Doe',
        email: 'john@example.com',
        preferences: {
            theme: 'dark',
            notifications: true
        }
    };

    const handleUserUpdate = (updatedUser) => {
        console.log('User updated:', updatedUser);
        // Update parent state
    };

    return (
        <div>
            <UserCard 
                user={user}
                showEmail={true}
                onUpdate={handleUserUpdate}
                className="main-user-card"
            />
        </div>
    );
}

function UserCard({ user, showEmail = false, onUpdate, className = '' }) {
    return (
        <div className={`user-card ${className}`}>
            <h3>{user.name}</h3>
            {showEmail && <p>{user.email}</p>}
            <button onClick={() => onUpdate({ ...user, lastSeen: new Date() })}>
                Update Last Seen
            </button>
        </div>
    );
}

// 2. Props Validation și Type Checking
import PropTypes from 'prop-types';

UserCard.propTypes = {
    user: PropTypes.shape({
        id: PropTypes.number.isRequired,
        name: PropTypes.string.isRequired,
        email: PropTypes.string.isRequired,
        preferences: PropTypes.shape({
            theme: PropTypes.oneOf(['light', 'dark']),
            notifications: PropTypes.bool
        })
    }).isRequired,
    showEmail: PropTypes.bool,
    onUpdate: PropTypes.func.isRequired,
    className: PropTypes.string
};

UserCard.defaultProps = {
    showEmail: false,
    className: ''
};

// 3. Props Destructuring Patterns
// Basic destructuring
function Button({ children, variant = 'primary', size = 'medium', ...rest }) {
    return (
        <button 
            className={`btn btn-${variant} btn-${size}`}
            {...rest}
        >
            {children}
        </button>
    );
}

// Nested destructuring
function UserProfile({ user: { name, email, address: { city, country } } }) {
    return (
        <div>
            <h1>{name}</h1>
            <p>{email}</p>
            <p>{city}, {country}</p>
        </div>
    );
}

// Array destructuring în props
function Coordinates({ position: [x, y, z] }) {
    return <div>Position: x={x}, y={y}, z={z}</div>;
}

// 4. Children Props Patterns
// Basic children
function Container({ children, title }) {
    return (
        <div className="container">
            {title && <h2>{title}</h2>}
            <div className="content">
                {children}
            </div>
        </div>
    );
}

// Function as children (render props)
function DataFetcher({ url, children }) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error);
                setLoading(false);
            });
    }, [url]);

    return children({ data, loading, error });
}

// Usage
<DataFetcher url="/api/users">
    {({ data, loading, error }) => {
        if (loading) return <LoadingSpinner />;
        if (error) return <ErrorMessage error={error} />;
        return <UserList users={data} />;
    }}
</DataFetcher>

// Multiple children patterns
function Layout({ header, sidebar, main, footer }) {
    return (
        <div className="layout">
            <header>{header}</header>
            <div className="body">
                <aside>{sidebar}</aside>
                <main>{main}</main>
            </div>
            <footer>{footer}</footer>
        </div>
    );
}

// Named slots pattern
function Card({ title, actions, children, footer }) {
    return (
        <div className="card">
            <div className="card-header">
                <h3>{title}</h3>
                <div className="card-actions">{actions}</div>
            </div>
            <div className="card-body">
                {children}
            </div>
            {footer && <div className="card-footer">{footer}</div>}
        </div>
    );
}

// Usage
<Card
    title="User Profile"
    actions={<Button>Edit</Button>}
    footer={<span>Last updated: Today</span>}
>
    <UserDetails user={user} />
</Card>
        """, language="javascript")

        st.markdown("#### Callback Props - Comunicarea de la copil la părinte")

        st.code("""
// 1. Basic Event Callbacks
function TodoApp() {
    const [todos, setTodos] = useState([
        { id: 1, text: 'Learn React', completed: false },
        { id: 2, text: 'Build app', completed: true }
    ]);

    const handleAddTodo = (text) => {
        const newTodo = {
            id: Date.now(),
            text,
            completed: false
        };
        setTodos(prev => [...prev, newTodo]);
    };

    const handleToggleTodo = (id) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        ));
    };

    const handleDeleteTodo = (id) => {
        setTodos(prev => prev.filter(todo => todo.id !== id));
    };

    const handleEditTodo = (id, newText) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id ? { ...todo, text: newText } : todo
        ));
    };

    return (
        <div className="todo-app">
            <TodoForm onAddTodo={handleAddTodo} />
            <TodoList 
                todos={todos}
                onToggle={handleToggleTodo}
                onDelete={handleDeleteTodo}
                onEdit={handleEditTodo}
            />
        </div>
    );
}

function TodoForm({ onAddTodo }) {
    const [text, setText] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (text.trim()) {
            onAddTodo(text.trim());
            setText('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Add a todo..."
            />
            <button type="submit">Add</button>
        </form>
    );
}

function TodoList({ todos, onToggle, onDelete, onEdit }) {
    return (
        <ul className="todo-list">
            {todos.map(todo => (
                <TodoItem
                    key={todo.id}
                    todo={todo}
                    onToggle={() => onToggle(todo.id)}
                    onDelete={() => onDelete(todo.id)}
                    onEdit={(newText) => onEdit(todo.id, newText)}
                />
            ))}
        </ul>
    );
}

function TodoItem({ todo, onToggle, onDelete, onEdit }) {
    const [isEditing, setIsEditing] = useState(false);
    const [editText, setEditText] = useState(todo.text);

    const handleSave = () => {
        if (editText.trim() && editText !== todo.text) {
            onEdit(editText.trim());
        }
        setIsEditing(false);
    };

    const handleCancel = () => {
        setEditText(todo.text);
        setIsEditing(false);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSave();
        } else if (e.key === 'Escape') {
            handleCancel();
        }
    };

    return (
        <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={onToggle}
            />

            {isEditing ? (
                <div className="edit-mode">
                    <input
                        type="text"
                        value={editText}
                        onChange={(e) => setEditText(e.target.value)}
                        onKeyDown={handleKeyPress}
                        onBlur={handleSave}
                        autoFocus
                    />
                </div>
            ) : (
                <span 
                    className="todo-text"
                    onDoubleClick={() => setIsEditing(true)}
                >
                    {todo.text}
                </span>
            )}

            <div className="todo-actions">
                {!isEditing && (
                    <>
                        <button onClick={() => setIsEditing(true)}>Edit</button>
                        <button onClick={onDelete}>Delete</button>
                    </>
                )}
            </div>
        </li>
    );
}

// 2. Advanced Callback Patterns
function FormField({ 
    name, 
    label, 
    type = 'text', 
    value, 
    onChange, 
    onValidate,
    required = false 
}) {
    const [error, setError] = useState('');
    const [touched, setTouched] = useState(false);

    const handleChange = (e) => {
        const newValue = e.target.value;
        onChange(name, newValue);

        // Clear error on change
        if (error) setError('');
    };

    const handleBlur = () => {
        setTouched(true);
        if (onValidate) {
            const validationError = onValidate(value, name);
            setError(validationError || '');
        }
    };

    return (
        <div className={`form-field ${error ? 'error' : ''}`}>
            <label htmlFor={name}>
                {label}
                {required && <span className="required">*</span>}
            </label>
            <input
                id={name}
                name={name}
                type={type}
                value={value}
                onChange={handleChange}
                onBlur={handleBlur}
                className={error && touched ? 'invalid' : ''}
            />
            {error && touched && (
                <span className="error-message">{error}</span>
            )}
        </div>
    );
}

// Usage with validation callbacks
function ContactForm() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: ''
    });

    const handleFieldChange = (fieldName, value) => {
        setFormData(prev => ({
            ...prev,
            [fieldName]: value
        }));
    };

    const validateField = (value, fieldName) => {
        switch (fieldName) {
            case 'name':
                return value.length < 2 ? 'Name must be at least 2 characters' : '';
            case 'email':
                return !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? 'Invalid email format' : '';
            case 'phone':
                return value && !/^\+?[\d\s-()]+$/.test(value) ? 'Invalid phone format' : '';
            default:
                return '';
        }
    };

    return (
        <form>
            <FormField
                name="name"
                label="Full Name"
                value={formData.name}
                onChange={handleFieldChange}
                onValidate={validateField}
                required
            />
            <FormField
                name="email"
                label="Email"
                type="email"
                value={formData.email}
                onChange={handleFieldChange}
                onValidate={validateField}
                required
            />
            <FormField
                name="phone"
                label="Phone"
                type="tel"
                value={formData.phone}
                onChange={handleFieldChange}
                onValidate={validateField}
            />
        </form>
    );
}
        """, language="javascript")

        st.markdown("#### Context API pentru Global Communication")

        st.code("""
// 1. Theme Context Example
const ThemeContext = createContext({
    theme: 'light',
    toggleTheme: () => {}
});

function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');

    const toggleTheme = useCallback(() => {
        setTheme(prev => prev === 'light' ? 'dark' : 'light');
    }, []);

    // Memoize context value pentru performance
    const contextValue = useMemo(() => ({
        theme,
        toggleTheme
    }), [theme, toggleTheme]);

    return (
        <ThemeContext.Provider value={contextValue}>
            <div className={`app-theme-${theme}`}>
                {children}
            </div>
        </ThemeContext.Provider>
    );
}

// Custom hook pentru easy consumption
function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within ThemeProvider');
    }
    return context;
}

// Components folosind theme context
function Header() {
    const { theme, toggleTheme } = useTheme();

    return (
        <header className="app-header">
            <h1>My App</h1>
            <button onClick={toggleTheme}>
                Switch to {theme === 'light' ? 'dark' : 'light'} mode
            </button>
        </header>
    );
}

function Article({ title, content }) {
    const { theme } = useTheme();

    return (
        <article className={`article article-${theme}`}>
            <h2>{title}</h2>
            <p>{content}</p>
        </article>
    );
}

// 2. Authentication Context
const AuthContext = createContext({
    user: null,
    isAuthenticated: false,
    login: () => {},
    logout: () => {},
    loading: false
});

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    // Check authentication status on mount
    useEffect(() => {
        const checkAuth = async () => {
            try {
                const token = localStorage.getItem('authToken');
                if (token) {
                    const response = await fetch('/api/me', {
                        headers: { Authorization: `Bearer ${token}` }
                    });
                    if (response.ok) {
                        const userData = await response.json();
                        setUser(userData);
                    } else {
                        localStorage.removeItem('authToken');
                    }
                }
            } catch (error) {
                console.error('Auth check failed:', error);
            } finally {
                setLoading(false);
            }
        };

        checkAuth();
    }, []);

    const login = useCallback(async (credentials) => {
        try {
            setLoading(true);
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(credentials)
            });

            if (response.ok) {
                const { user, token } = await response.json();
                localStorage.setItem('authToken', token);
                setUser(user);
                return { success: true };
            } else {
                const error = await response.json();
                return { success: false, error: error.message };
            }
        } catch (error) {
            return { success: false, error: error.message };
        } finally {
            setLoading(false);
        }
    }, []);

    const logout = useCallback(() => {
        localStorage.removeItem('authToken');
        setUser(null);
        // Optionally call logout API endpoint
    }, []);

    const value = useMemo(() => ({
        user,
        isAuthenticated: !!user,
        login,
        logout,
        loading
    }), [user, login, logout, loading]);

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within AuthProvider');
    }
    return context;
}

// Protected Route Component
function ProtectedRoute({ children }) {
    const { isAuthenticated, loading } = useAuth();

    if (loading) {
        return <LoadingSpinner />;
    }

    if (!isAuthenticated) {
        return <Navigate to="/login" replace />;
    }

    return children;
}

// 3. Multiple Contexts Pattern
function AppProviders({ children }) {
    return (
        <AuthProvider>
            <ThemeProvider>
                <NotificationProvider>
                    <LanguageProvider>
                        {children}
                    </LanguageProvider>
                </NotificationProvider>
            </ThemeProvider>
        </AuthProvider>
    );
}

// Combined hooks pentru multiple contexts
function useAppContext() {
    const auth = useAuth();
    const theme = useTheme();
    const notifications = useNotifications();
    const language = useLanguage();

    return {
        auth,
        theme,
        notifications,
        language
    };
}
        """, language="javascript")

    with components_tabs[2]:
        st.markdown("### Composition Patterns")

        st.markdown("#### Container și Presentational Components")

        st.code("""
// Container Component (Smart) - Gestionează logic și state
function UserListContainer() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [filters, setFilters] = useState({
        search: '',
        role: 'all',
        status: 'all'
    });
    const [pagination, setPagination] = useState({
        page: 1,
        limit: 10,
        total: 0
    });

    // Data fetching logic
    const fetchUsers = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);

            const params = new URLSearchParams({
                page: pagination.page,
                limit: pagination.limit,
                search: filters.search,
                role: filters.role !== 'all' ? filters.role : '',
                status: filters.status !== 'all' ? filters.status : ''
            });

            const response = await fetch(`/api/users?${params}`);
            const data = await response.json();

            setUsers(data.users);
            setPagination(prev => ({
                ...prev,
                total: data.total
            }));
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, [filters, pagination.page, pagination.limit]);

    useEffect(() => {
        fetchUsers();
    }, [fetchUsers]);

    // Event handlers
    const handleFilterChange = useCallback((newFilters) => {
        setFilters(prev => ({ ...prev, ...newFilters }));
        setPagination(prev => ({ ...prev, page: 1 })); // Reset to first page
    }, []);

    const handlePageChange = useCallback((newPage) => {
        setPagination(prev => ({ ...prev, page: newPage }));
    }, []);

    const handleUserAction = useCallback(async (action, userId) => {
        try {
            await fetch(`/api/users/${userId}/${action}`, { method: 'POST' });
            fetchUsers(); // Refresh list
        } catch (err) {
            setError(err.message);
        }
    }, [fetchUsers]);

    // Pass everything to presentational component
    return (
        <UserListPresentation
            users={users}
            loading={loading}
            error={error}
            filters={filters}
            pagination={pagination}
            onFilterChange={handleFilterChange}
            onPageChange={handlePageChange}
            onUserAction={handleUserAction}
            onRetry={fetchUsers}
        />
    );
}

// Presentational Component (Dumb) - Doar UI și display logic
function UserListPresentation({
    users,
    loading,
    error,
    filters,
    pagination,
    onFilterChange,
    onPageChange,
    onUserAction,
    onRetry
}) {
    if (error) {
        return (
            <ErrorBoundary>
                <ErrorMessage 
                    message={error} 
                    onRetry={onRetry}
                />
            </ErrorBoundary>
        );
    }

    return (
        <div className="user-list">
            <div className="user-list-header">
                <h2>Users ({pagination.total})</h2>
                <UserFilters
                    filters={filters}
                    onChange={onFilterChange}
                />
            </div>

            <div className="user-list-body">
                {loading ? (
                    <LoadingSpinner />
                ) : users.length === 0 ? (
                    <EmptyState 
                        message="No users found"
                        icon="users"
                    />
                ) : (
                    <UserGrid
                        users={users}
                        onUserAction={onUserAction}
                    />
                )}
            </div>

            {pagination.total > pagination.limit && (
                <UserPagination
                    currentPage={pagination.page}
                    totalPages={Math.ceil(pagination.total / pagination.limit)}
                    onPageChange={onPageChange}
                />
            )}
        </div>
    );
}

// Sub-components (also presentational)
function UserFilters({ filters, onChange }) {
    return (
        <div className="user-filters">
            <SearchInput
                value={filters.search}
                onChange={(search) => onChange({ search })}
                placeholder="Search users..."
            />

            <Select
                value={filters.role}
                onChange={(role) => onChange({ role })}
                options={[
                    { value: 'all', label: 'All Roles' },
                    { value: 'admin', label: 'Admin' },
                    { value: 'user', label: 'User' },
                    { value: 'moderator', label: 'Moderator' }
                ]}
            />

            <Select
                value={filters.status}
                onChange={(status) => onChange({ status })}
                options={[
                    { value: 'all', label: 'All Status' },
                    { value: 'active', label: 'Active' },
                    { value: 'inactive', label: 'Inactive' },
                    { value: 'pending', label: 'Pending' }
                ]}
            />
        </div>
    );
}

function UserGrid({ users, onUserAction }) {
    return (
        <div className="user-grid">
            {users.map(user => (
                <UserCard
                    key={user.id}
                    user={user}
                    onEdit={() => onUserAction('edit', user.id)}
                    onDelete={() => onUserAction('delete', user.id)}
                    onToggleStatus={() => onUserAction('toggle-status', user.id)}
                />
            ))}
        </div>
    );
}

function UserCard({ user, onEdit, onDelete, onToggleStatus }) {
    return (
        <div className={`user-card user-card-${user.status}`}>
            <div className="user-avatar">
                <img src={user.avatar} alt={user.name} />
                <span className={`status-indicator status-${user.status}`} />
            </div>

            <div className="user-info">
                <h3>{user.name}</h3>
                <p>{user.email}</p>
                <span className="user-role">{user.role}</span>
            </div>

            <div className="user-actions">
                <IconButton 
                    icon="edit" 
                    onClick={onEdit}
                    tooltip="Edit user"
                />
                <IconButton 
                    icon={user.status === 'active' ? 'pause' : 'play'}
                    onClick={onToggleStatus}
                    tooltip={user.status === 'active' ? 'Deactivate' : 'Activate'}
                />
                <IconButton 
                    icon="delete" 
                    onClick={onDelete}
                    tooltip="Delete user"
                    variant="danger"
                />
            </div>
        </div>
    );
}
        """, language="javascript")

        st.markdown("#### Higher-Order Components (HOCs)")

        st.code("""
// 1. Authentication HOC
function withAuth(WrappedComponent, options = {}) {
    const { requiredRole = null, redirectTo = '/login' } = options;

    return function AuthenticatedComponent(props) {
        const { user, isAuthenticated, loading } = useAuth();
        const navigate = useNavigate();

        useEffect(() => {
            if (!loading && !isAuthenticated) {
                navigate(redirectTo);
            } else if (requiredRole && user && user.role !== requiredRole) {
                navigate('/unauthorized');
            }
        }, [loading, isAuthenticated, user, navigate]);

        if (loading) {
            return <LoadingSpinner />;
        }

        if (!isAuthenticated) {
            return null;
        }

        if (requiredRole && user.role !== requiredRole) {
            return <UnauthorizedMessage />;
        }

        return <WrappedComponent {...props} user={user} />;
    };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);
const AdminPanel = withAuth(AdminPanelComponent, { requiredRole: 'admin' });

// 2. Loading HOC
function withLoading(WrappedComponent, loadingComponent = LoadingSpinner) {
    return function LoadingComponent({ isLoading, ...props }) {
        if (isLoading) {
            return React.createElement(loadingComponent);
        }

        return <WrappedComponent {...props} />;
    };
}

// Usage
const UserListWithLoading = withLoading(UserList);
// <UserListWithLoading isLoading={loading} users={users} />

// 3. Data Fetching HOC
function withData(WrappedComponent, dataSource) {
    return function DataComponent(props) {
        const [data, setData] = useState(null);
        const [loading, setLoading] = useState(true);
        const [error, setError] = useState(null);

        useEffect(() => {
            const fetchData = async () => {
                try {
                    setLoading(true);
                    setError(null);

                    let result;
                    if (typeof dataSource === 'function') {
                        result = await dataSource(props);
                    } else {
                        const response = await fetch(dataSource);
                        result = await response.json();
                    }

                    setData(result);
                } catch (err) {
                    setError(err);
                } finally {
                    setLoading(false);
                }
            };

            fetchData();
        }, [props.id]); // Re-fetch when id changes

        return (
            <WrappedComponent
                {...props}
                data={data}
                loading={loading}
                error={error}
            />
        );
    };
}

// Usage
const UserProfile = withData(
    function UserProfileComponent({ data: user, loading, error, ...props }) {
        if (loading) return <LoadingSpinner />;
        if (error) return <ErrorMessage error={error} />;
        return <div>Welcome, {user.name}!</div>;
    },
    (props) => fetch(`/api/users/${props.id}`).then(r => r.json())
);

// 4. Error Boundary HOC
function withErrorBoundary(WrappedComponent, ErrorFallback = DefaultErrorFallback) {
    class ErrorBoundaryHOC extends React.Component {
        constructor(props) {
            super(props);
            this.state = { hasError: false, error: null };
        }

        static getDerivedStateFromError(error) {
            return { hasError: true, error };
        }

        componentDidCatch(error, errorInfo) {
            console.error('Error caught by HOC:', error, errorInfo);
            // Log to error reporting service
        }

        render() {
            if (this.state.hasError) {
                return <ErrorFallback error={this.state.error} />;
            }

            return <WrappedComponent {...this.props} />;
        }
    }

    ErrorBoundaryHOC.displayName = `withErrorBoundary(${WrappedComponent.displayName || WrappedComponent.name})`;

    return ErrorBoundaryHOC;
}

// 5. Performance Monitoring HOC
function withPerformanceMonitoring(WrappedComponent) {
    return React.memo(function PerformanceMonitoringComponent(props) {
        const renderStartTime = useRef();
        const componentName = WrappedComponent.displayName || WrappedComponent.name;

        renderStartTime.current = performance.now();

        useLayoutEffect(() => {
            const renderTime = performance.now() - renderStartTime.current;

            if (renderTime > 16) { // Longer than one frame
                console.warn(`Slow render detected in ${componentName}: ${renderTime.toFixed(2)}ms`);
            }

            // Send to analytics service
            if (window.gtag) {
                window.gtag('event', 'component_render_time', {
                    component: componentName,
                    render_time: renderTime
                });
            }
        });

        return <WrappedComponent {...props} />;
    });
}

// 6. Composing Multiple HOCs
const enhance = compose(
    withAuth,
    withErrorBoundary,
    withPerformanceMonitoring,
    withLoading
);

const EnhancedDashboard = enhance(Dashboard);

// Helper function pentru HOC composition
function compose(...funcs) {
    return funcs.reduce((a, b) => (...args) => a(b(...args)));
}
        """, language="javascript")

        st.markdown("#### Render Props Pattern")

        st.code("""
// 1. Mouse Position Tracker
class MouseTracker extends React.Component {
    state = { x: 0, y: 0 };

    handleMouseMove = (event) => {
        this.setState({
            x: event.clientX,
            y: event.clientY
        });
    };

    render() {
        return (
            <div 
                style={{ height: '100vh', width: '100%' }}
                onMouseMove={this.handleMouseMove}
            >
                {this.props.children(this.state)}
            </div>
        );
    }
}

// Usage
function App() {
    return (
        <MouseTracker>
            {({ x, y }) => (
                <div>
                    <h1>Mouse Position Tracker</h1>
                    <p>Current mouse position: ({x}, {y})</p>
                    <div
                        style={{
                            position: 'absolute',
                            left: x - 10,
                            top: y - 10,
                            width: 20,
                            height: 20,
                            backgroundColor: 'red',
                            borderRadius: '50%',
                            pointerEvents: 'none'
                        }}
                    />
                </div>
            )}
        </MouseTracker>
    );
}

// 2. Data Fetcher with Render Props
function DataFetcher({ url, children, refreshInterval }) {
    const [state, setState] = useState({
        data: null,
        loading: true,
        error: null
    });

    const fetchData = useCallback(async () => {
        try {
            setState(prev => ({ ...prev, loading: true, error: null }));

            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            setState({ data, loading: false, error: null });
        } catch (error) {
            setState(prev => ({
                ...prev,
                loading: false,
                error: error.message
            }));
        }
    }, [url]);

    useEffect(() => {
        fetchData();

        if (refreshInterval) {
            const interval = setInterval(fetchData, refreshInterval);
            return () => clearInterval(interval);
        }
    }, [fetchData, refreshInterval]);

    return children({
        ...state,
        refetch: fetchData
    });
}

// Usage
function UserList() {
    return (
        <DataFetcher url="/api/users" refreshInterval={30000}>
            {({ data: users, loading, error, refetch }) => {
                if (loading && !users) {
                    return <LoadingSpinner />;
                }

                if (error) {
                    return (
                        <ErrorMessage 
                            error={error} 
                            onRetry={refetch}
                        />
                    );
                }

                return (
                    <div>
                        <div className="list-header">
                            <h2>Users ({users?.length || 0})</h2>
                            <button 
                                onClick={refetch}
                                disabled={loading}
                            >
                                {loading ? 'Refreshing...' : 'Refresh'}
                            </button>
                        </div>

                        <div className="user-grid">
                            {users?.map(user => (
                                <UserCard key={user.id} user={user} />
                            ))}
                        </div>
                    </div>
                );
            }}
        </DataFetcher>
    );
}

// 3. Form Validation with Render Props
function FormValidator({ validationRules, children }) {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});

    const validateField = useCallback((name, value) => {
        const rules = validationRules[name];
        if (!rules) return '';

        for (const rule of rules) {
            const error = rule(value, values);
            if (error) return error;
        }

        return '';
    }, [validationRules, values]);

    const setValue = useCallback((name, value) => {
        setValues(prev => ({ ...prev, [name]: value }));

        // Clear error when user starts typing
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: '' }));
        }
    }, [errors]);

    const setFieldTouched = useCallback((name) => {
        setTouched(prev => ({ ...prev, [name]: true }));

        // Validate on blur
        const error = validateField(name, values[name]);
        setErrors(prev => ({ ...prev, [name]: error }));
    }, [validateField, values]);

    const validateAll = useCallback(() => {
        const newErrors = {};
        let isValid = true;

        Object.keys(validationRules).forEach(name => {
            const error = validateField(name, values[name]);
            newErrors[name] = error;
            if (error) isValid = false;
        });

        setErrors(newErrors);
        setTouched(Object.keys(validationRules).reduce((acc, key) => {
            acc[key] = true;
            return acc;
        }, {}));

        return isValid;
    }, [validationRules, validateField, values]);

    return children({
        values,
        errors,
        touched,
        setValue,
        setFieldTouched,
        validateAll,
        isValid: Object.values(errors).every(error => !error)
    });
}

// Usage
function RegistrationForm() {
    const validationRules = {
        email: [
            (value) => !value ? 'Email is required' : '',
            (value) => !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? 'Invalid email format' : ''
        ],
        password: [
            (value) => !value ? 'Password is required' : '',
            (value) => value.length < 8 ? 'Password must be at least 8 characters' : ''
        ],
        confirmPassword: [
            (value) => !value ? 'Please confirm password' : '',
            (value, values) => value !== values.password ? 'Passwords do not match' : ''
        ]
    };

    return (
        <FormValidator validationRules={validationRules}>
            {({ values, errors, touched, setValue, setFieldTouched, validateAll, isValid }) => (
                <form onSubmit={(e) => {
                    e.preventDefault();
                    if (validateAll()) {
                        console.log('Form is valid:', values);
                    }
                }}>
                    <FormField
                        name="email"
                        type="email"
                        placeholder="Email"
                        value={values.email || ''}
                        error={touched.email ? errors.email : ''}
                        onChange={(e) => setValue('email', e.target.value)}
                        onBlur={() => setFieldTouched('email')}
                    />

                    <FormField
                        name="password"
                        type="password"
                        placeholder="Password"
                        value={values.password || ''}
                        error={touched.password ? errors.password : ''}
                        onChange={(e) => setValue('password', e.target.value)}
                        onBlur={() => setFieldTouched('password')}
                    />

                    <FormField
                        name="confirmPassword"
                        type="password"
                        placeholder="Confirm Password"
                        value={values.confirmPassword || ''}
                        error={touched.confirmPassword ? errors.confirmPassword : ''}
                        onChange={(e) => setValue('confirmPassword', e.target.value)}
                        onBlur={() => setFieldTouched('confirmPassword')}
                    />

                    <button type="submit" disabled={!isValid}>
                        Register
                    </button>
                </form>
            )}
        </FormValidator>
    );
}
        """, language="javascript")

    with components_tabs[3]:
        st.markdown("### Lifecycle Management")

        st.markdown("#### Class Component Lifecycle Methods")

        st.code("""
// Complete Class Component Lifecycle Example
class LifecycleDemo extends React.Component {
    constructor(props) {
        super(props);
        console.log('1. Constructor called');

        this.state = {
            data: null,
            loading: true,
            error: null,
            count: 0
        };

        // Create refs
        this.intervalRef = null;
        this.abortController = null;
    }

    // MOUNTING PHASE
    static getDerivedStateFromProps(props, state) {
        console.log('2. getDerivedStateFromProps called');

        // Return object to update state, or null for no update
        // Used rarely - when state depends on props changes
        if (props.initialCount !== state.previousInitialCount) {
            return {
                count: props.initialCount,
                previousInitialCount: props.initialCount
            };
        }

        return null;
    }

    componentDidMount() {
        console.log('4. componentDidMount called');

        // Perfect for:
        // - API calls
        // - Setting up subscriptions
        // - Starting timers
        // - Adding event listeners

        this.fetchData();
        this.startTimer();
        window.addEventListener('resize', this.handleResize);

        // Focus management
        if (this.inputRef) {
            this.inputRef.focus();
        }
    }

    // UPDATING PHASE
    shouldComponentUpdate(nextProps, nextState) {
        console.log('5. shouldComponentUpdate called');

        // Performance optimization - return false to skip update
        // Rarely used - prefer React.PureComponent or React.memo

        // Example: only update if specific props/state changed
        return (
            nextProps.userId !== this.props.userId ||
            nextState.count !== this.state.count ||
            nextState.data !== this.state.data
        );
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log('6. getSnapshotBeforeUpdate called');

        // Capture information before DOM updates
        // Return value is passed to componentDidUpdate

        // Example: preserve scroll position
        if (prevState.data !== this.state.data) {
            const list = document.getElementById('data-list');
            return {
                scrollTop: list.scrollTop,
                scrollHeight: list.scrollHeight
            };
        }

        return null;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log('7. componentDidUpdate called');

        // Perfect for:
        // - API calls based on prop/state changes
        // - DOM manipulation after updates
        // - Third-party library updates

        // Re-fetch data when userId changes
        if (prevProps.userId !== this.props.userId) {
            this.fetchData();
        }

        // Update document title when data changes
        if (prevState.data !== this.state.data && this.state.data) {
            document.title = `User: ${this.state.data.name}`;
        }

        // Use snapshot to restore scroll position
        if (snapshot !== null) {
            const list = document.getElementById('data-list');
            const newScrollHeight = list.scrollHeight;

            if (newScrollHeight > snapshot.scrollHeight) {
                list.scrollTop = snapshot.scrollTop + (newScrollHeight - snapshot.scrollHeight);
            }
        }

        // Restart timer if interval changed
        if (prevProps.timerInterval !== this.props.timerInterval) {
            this.stopTimer();
            this.startTimer();
        }
    }

    // UNMOUNTING PHASE
    componentWillUnmount() {
        console.log('8. componentWillUnmount called');

        // CRITICAL for preventing memory leaks:
        // - Cancel API requests
        // - Clear timers/intervals
        // - Remove event listeners
        // - Clean up subscriptions

        this.stopTimer();

        if (this.abortController) {
            this.abortController.abort();
        }

        window.removeEventListener('resize', this.handleResize);

        // Clear any pending timeouts
        if (this.timeoutId) {
            clearTimeout(this.timeoutId);
        }
    }

    // ERROR HANDLING
    static getDerivedStateFromError(error) {
        console.log('9. getDerivedStateFromError called');

        // Update state to show error UI
        return { hasError: true, error: error.message };
    }

    componentDidCatch(error, errorInfo) {
        console.log('10. componentDidCatch called');

        // Log error to reporting service
        console.error('Component error:', error, errorInfo);

        // Send to error monitoring service
        if (window.Sentry) {
            window.Sentry.captureException(error, {
                contexts: {
                    react: {
                        componentStack: errorInfo.componentStack
                    }
                }
            });
        }
    }

    // INSTANCE METHODS
    fetchData = async () => {
        try {
            this.setState({ loading: true, error: null });

            // Create abort controller for cancellation
            this.abortController = new AbortController();

            const response = await fetch(`/api/users/${this.props.userId}`, {
                signal: this.abortController.signal
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            this.setState({ data, loading: false });

        } catch (error) {
            if (error.name !== 'AbortError') {
                this.setState({ error: error.message, loading: false });
            }
        }
    };

    startTimer = () => {
        this.intervalRef = setInterval(() => {
            this.setState(prevState => ({
                count: prevState.count + 1
            }));
        }, this.props.timerInterval || 1000);
    };

    stopTimer = () => {
        if (this.intervalRef) {
            clearInterval(this.intervalRef);
            this.intervalRef = null;
        }
    };

    handleResize = () => {
        // Debounce resize handler
        if (this.resizeTimeout) {
            clearTimeout(this.resizeTimeout);
        }

        this.resizeTimeout = setTimeout(() => {
            this.forceUpdate(); // Trigger re-render for responsive behavior
        }, 250);
    };

    render() {
        console.log('3. Render called');

        const { data, loading, error, count, hasError } = this.state;

        if (hasError) {
            return (
                <div className="error-boundary">
                    <h2>Something went wrong</h2>
                    <p>{error}</p>
                    <button onClick={() => this.setState({ hasError: false, error: null })}>
                        Try again
                    </button>
                </div>
            );
        }

        return (
            <div className="lifecycle-demo">
                <h2>Lifecycle Demo</h2>
                <p>Count: {count}</p>

                {loading && <div>Loading...</div>}
                {error && <div className="error">Error: {error}</div>}
                {data && (
                    <div id="data-list">
                        <h3>{data.name}</h3>
                        <p>{data.email}</p>
                    </div>
                )}

                <input
                    ref={(ref) => { this.inputRef = ref; }}
                    placeholder="This input gets focused on mount"
                />

                <button onClick={() => this.setState({ count: 0 })}>
                    Reset Count
                </button>
                <button onClick={this.fetchData}>
                    Refetch Data
                </button>
            </div>
        );
    }
}
        """, language="javascript")

        st.markdown("#### Function Component Lifecycle cu Hooks")

        st.code("""
// Function Component echivalent cu toate lifecycle methods
function LifecycleDemoHooks({ userId, timerInterval = 1000, initialCount = 0 }) {
    // State hooks
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [count, setCount] = useState(initialCount);
    const [hasError, setHasError] = useState(false);

    // Refs for cleanup
    const intervalRef = useRef(null);
    const abortControllerRef = useRef(null);
    const timeoutRef = useRef(null);
    const inputRef = useRef(null);

    // getDerivedStateFromProps equivalent
    useEffect(() => {
        setCount(initialCount);
    }, [initialCount]);

    // Fetch data function
    const fetchData = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);

            // Cancel previous request
            if (abortControllerRef.current) {
                abortControllerRef.current.abort();
            }

            // Create new abort controller
            abortControllerRef.current = new AbortController();

            const response = await fetch(`/api/users/${userId}`, {
                signal: abortControllerRef.current.signal
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const userData = await response.json();
            setData(userData);
            setLoading(false);

        } catch (error) {
            if (error.name !== 'AbortError') {
                setError(error.message);
                setLoading(false);
            }
        }
    }, [userId]);

    // componentDidMount equivalent
    useEffect(() => {
        console.log('Component mounted');

        // Initial data fetch
        fetchData();

        // Focus input
        if (inputRef.current) {
            inputRef.current.focus();
        }

        // componentWillUnmount equivalent (cleanup)
        return () => {
            console.log('Component will unmount');

            // Cancel any pending request
            if (abortControllerRef.current) {
                abortControllerRef.current.abort();
            }

            // Clear any timeouts
            if (timeoutRef.current) {
                clearTimeout(timeoutRef.current);
            }
        };
    }, []); // Empty dependency array = run once on mount

    // componentDidUpdate equivalent - userId changes
    useEffect(() => {
        console.log('UserId changed, refetching data');
        fetchData();
    }, [fetchData]); // Runs when fetchData changes (which depends on userId)

    // componentDidUpdate equivalent - data changes (document title)
    useEffect(() => {
        if (data) {
            document.title = `User: ${data.name}`;

            // Cleanup function runs before next effect or unmount
            return () => {
                document.title = 'React App'; // Reset title
            };
        }
    }, [data]);

    // Timer management
    useEffect(() => {
        console.log('Setting up timer');

        const startTimer = () => {
            intervalRef.current = setInterval(() => {
                setCount(prevCount => prevCount + 1);
            }, timerInterval);
        };

        startTimer();

        // Cleanup function
        return () => {
            console.log('Cleaning up timer');
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, [timerInterval]); // Restart timer when interval changes

    // Window resize handler
    useEffect(() => {
        const handleResize = () => {
            // Debounce resize events
            if (timeoutRef.current) {
                clearTimeout(timeoutRef.current);
            }

            timeoutRef.current = setTimeout(() => {
                console.log('Window resized');
                // Handle responsive logic here
            }, 250);
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
            if (timeoutRef.current) {
                clearTimeout(timeoutRef.current);
            }
        };
    }, []); // Empty dependency - set up once

    // Error boundary equivalent (requires custom hook or higher-order component)
    useEffect(() => {
        const handleError = (event) => {
            console.error('Global error caught:', event.error);
            setHasError(true);
            setError(event.error.message);
        };

        window.addEventListener('error', handleError);

        return () => {
            window.removeEventListener('error', handleError);
        };
    }, []);

    // Event handlers
    const handleResetCount = useCallback(() => {
        setCount(0);
    }, []);

    const handleRetry = useCallback(() => {
        setHasError(false);
        setError(null);
        fetchData();
    }, [fetchData]);

    // Render logic
    if (hasError) {
        return (
            <div className="error-boundary">
                <h2>Something went wrong</h2>
                <p>{error}</p>
                <button onClick={handleRetry}>
                    Try again
                </button>
            </div>
        );
    }

    return (
        <div className="lifecycle-demo">
            <h2>Lifecycle Demo (Hooks)</h2>
            <p>Count: {count}</p>

            {loading && <div>Loading...</div>}
            {error && <div className="error">Error: {error}</div>}
            {data && (
                <div id="data-list">
                    <h3>{data.name}</h3>
                    <p>{data.email}</p>
                </div>
            )}

            <input
                ref={inputRef}
                placeholder="This input gets focused on mount"
            />

            <button onClick={handleResetCount}>
                Reset Count
            </button>
            <button onClick={fetchData}>
                Refetch Data
            </button>
        </div>
    );
}

// Custom hook pentru error boundary functionality
function useErrorBoundary() {
    const [error, setError] = useState(null);

    const resetError = useCallback(() => {
        setError(null);
    }, []);

    const captureError = useCallback((error, errorInfo = {}) => {
        setError({ error, errorInfo });

        // Log to monitoring service
        console.error('Error captured:', error, errorInfo);
    }, []);

    useEffect(() => {
        const handleError = (event) => {
            captureError(event.error);
        };

        const handleUnhandledRejection = (event) => {
            captureError(event.reason);
        };

        window.addEventListener('error', handleError);
        window.addEventListener('unhandledrejection', handleUnhandledRejection);

        return () => {
            window.removeEventListener('error', handleError);
            window.removeEventListener('unhandledrejection', handleUnhandledRejection);
        };
    }, [captureError]);

    return { error, resetError, captureError };
}

// Usage cu error boundary hook
function ComponentWithErrorBoundary() {
    const { error, resetError, captureError } = useErrorBoundary();

    const riskyOperation = () => {
        try {
            // Some risky code
            throw new Error('Something went wrong!');
        } catch (err) {
            captureError(err);
        }
    };

    if (error) {
        return (
            <div className="error-fallback">
                <h2>Oops! Something went wrong</h2>
                <pre>{error.error.message}</pre>
                <button onClick={resetError}>Try again</button>
            </div>
        );
    }

    return (
        <div>
            <button onClick={riskyOperation}>
                Trigger Error
            </button>
        </div>
    );
}
        """, language="javascript")

    with components_tabs[4]:
        st.markdown("### Performance Optimization")

        st.markdown("#### React.memo și Pure Components")

        st.code("""
// 1. React.memo pentru Function Components
const ExpensiveComponent = React.memo(function ExpensiveComponent({ 
    data, 
    onItemClick, 
    sortBy, 
    filterBy 
}) {
    console.log('ExpensiveComponent rendered');

    // Expensive computation
    const processedData = useMemo(() => {
        console.log('Processing data...');

        let result = [...data];

        // Filter data
        if (filterBy) {
            result = result.filter(item => 
                item.category === filterBy || 
                item.name.toLowerCase().includes(filterBy.toLowerCase())
            );
        }

        // Sort data
        if (sortBy) {
            result.sort((a, b) => {
                if (sortBy === 'name') return a.name.localeCompare(b.name);
                if (sortBy === 'date') return new Date(b.date) - new Date(a.date);
                if (sortBy === 'price') return b.price - a.price;
                return 0;
            });
        }

        return result;
    }, [data, sortBy, filterBy]);

    return (
        <div className="expensive-component">
            <h3>Processed Items ({processedData.length})</h3>
            <div className="items-grid">
                {processedData.map(item => (
                    <ItemCard
                        key={item.id}
                        item={item}
                        onClick={() => onItemClick(item.id)}
                    />
                ))}
            </div>
        </div>
    );
});

// Custom comparison function pentru React.memo
const UserCard = React.memo(function UserCard({ user, settings, onEdit }) {
    return (
        <div className="user-card">
            <img src={user.avatar} alt={user.name} />
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            {settings.showEditButton && (
                <button onClick={() => onEdit(user.id)}>Edit</button>
            )}
        </div>
    );
}, (prevProps, nextProps) => {
    // Custom comparison - return true to skip re-render
    // Compare user object
    if (prevProps.user.id !== nextProps.user.id) return false;
    if (prevProps.user.name !== nextProps.user.name) return false;
    if (prevProps.user.email !== nextProps.user.email) return false;
    if (prevProps.user.avatar !== nextProps.user.avatar) return false;

    // Compare settings
    if (prevProps.settings.showEditButton !== nextProps.settings.showEditButton) return false;

    // Compare callbacks (usually stable with useCallback)
    if (prevProps.onEdit !== nextProps.onEdit) return false;

    // All comparisons passed - skip re-render
    return true;
});

// 2. PureComponent pentru Class Components
class PureUserCard extends React.PureComponent {
    render() {
        console.log('PureUserCard rendered');
        const { user, settings, onEdit } = this.props;

        return (
            <div className="user-card">
                <img src={user.avatar} alt={user.name} />
                <h3>{user.name}</h3>
                <p>{user.email}</p>
                {settings.showEditButton && (
                    <button onClick={() => onEdit(user.id)}>Edit</button>
                )}
            </div>
        );
    }
}

// 3. Performance comparison demo
function PerformanceDemo() {
    const [users, setUsers] = useState(generateUsers(1000));
    const [filter, setFilter] = useState('');
    const [showEdit, setShowEdit] = useState(true);
    const [counter, setCounter] = useState(0);

    // Memoized filtered users
    const filteredUsers = useMemo(() => {
        console.log('Filtering users...');
        return users.filter(user => 
            user.name.toLowerCase().includes(filter.toLowerCase())
        );
    }, [users, filter]);

    // Stable callback with useCallback
    const handleEdit = useCallback((userId) => {
        console.log('Editing user:', userId);
        // Edit logic here
    }, []);

    // Settings object that changes reference every render (BAD)
    const badSettings = { showEditButton: showEdit };

    // Memoized settings object (GOOD)
    const goodSettings = useMemo(() => ({
        showEditButton: showEdit
    }), [showEdit]);

    return (
        <div>
            <div className="controls">
                <input
                    type="text"
                    placeholder="Filter users..."
                    value={filter}
                    onChange={(e) => setFilter(e.target.value)}
                />
                <label>
                    <input
                        type="checkbox"
                        checked={showEdit}
                        onChange={(e) => setShowEdit(e.target.checked)}
                    />
                    Show Edit Button
                </label>
                <button onClick={() => setCounter(c => c + 1)}>
                    Counter: {counter}
                </button>
            </div>

            <div className="comparison">
                <div className="column">
                    <h3>With memo (optimized)</h3>
                    {filteredUsers.slice(0, 10).map(user => (
                        <UserCard
                            key={user.id}
                            user={user}
                            settings={goodSettings} // Stable reference
                            onEdit={handleEdit}      // Stable reference
                        />
                    ))}
                </div>

                <div className="column">
                    <h3>Without memo (re-renders always)</h3>
                    {filteredUsers.slice(0, 10).map(user => (
                        <RegularUserCard
                            key={user.id}
                            user={user}
                            settings={badSettings} // New object every render
                            onEdit={(id) => console.log('Edit:', id)} // New function every render
                        />
                    ))}
                </div>
            </div>
        </div>
    );
}

// Regular component (no memo) pentru comparison
function RegularUserCard({ user, settings, onEdit }) {
    console.log('RegularUserCard rendered');

    return (
        <div className="user-card">
            <img src={user.avatar} alt={user.name} />
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            {settings.showEditButton && (
                <button onClick={() => onEdit(user.id)}>Edit</button>
            )}
        </div>
    );
}

function generateUsers(count) {
    return Array.from({ length: count }, (_, i) => ({
        id: i,
        name: `User ${i}`,
        email: `user${i}@example.com`,
        avatar: `https://i.pravatar.cc/40?img=${i}`
    }));
}
        """, language="javascript")

        st.markdown("#### useMemo și useCallback")

        st.code("""
// 1. useMemo pentru expensive computations
function DataAnalytics({ salesData, dateRange, filters }) {
    // Expensive calculation - only re-run when dependencies change
    const analytics = useMemo(() => {
        console.log('Calculating analytics...');

        // Filter data by date range
        const filteredData = salesData.filter(sale => {
            const saleDate = new Date(sale.date);
            return saleDate >= dateRange.start && saleDate <= dateRange.end;
        });

        // Apply additional filters
        const finalData = filteredData.filter(sale => {
            if (filters.category && sale.category !== filters.category) return false;
            if (filters.minAmount && sale.amount < filters.minAmount) return false;
            if (filters.region && sale.region !== filters.region) return false;
            return true;
        });

        // Calculate metrics
        const totalSales = finalData.reduce((sum, sale) => sum + sale.amount, 0);
        const averageSale = finalData.length > 0 ? totalSales / finalData.length : 0;
        const salesByCategory = finalData.reduce((acc, sale) => {
            acc[sale.category] = (acc[sale.category] || 0) + sale.amount;
            return acc;
        }, {});

        const topProducts = Object.entries(
            finalData.reduce((acc, sale) => {
                acc[sale.product] = (acc[sale.product] || 0) + sale.amount;
                return acc;
            }, {})
        )
        .sort(([,a], [,b]) => b - a)
        .slice(0, 10);

        return {
            totalSales,
            averageSale,
            salesCount: finalData.length,
            salesByCategory,
            topProducts,
            rawData: finalData
        };
    }, [salesData, dateRange, filters]);

    // Memoized chart data transformation
    const chartData = useMemo(() => {
        console.log('Preparing chart data...');

        return analytics.rawData.map(sale => ({
            date: sale.date,
            amount: sale.amount,
            category: sale.category
        }));
    }, [analytics.rawData]);

    return (
        <div className="analytics-dashboard">
            <div className="metrics">
                <MetricCard title="Total Sales" value={analytics.totalSales} />
                <MetricCard title="Average Sale" value={analytics.averageSale} />
                <MetricCard title="Sales Count" value={analytics.salesCount} />
            </div>

            <div className="charts">
                <SalesChart data={chartData} />
                <CategoryChart data={analytics.salesByCategory} />
            </div>

            <TopProductsList products={analytics.topProducts} />
        </div>
    );
}

// 2. useCallback pentru stable function references
function TodoApp() {
    const [todos, setTodos] = useState([]);
    const [filter, setFilter] = useState('all');
    const [editingId, setEditingId] = useState(null);

    // Stable callbacks that don't change on every render
    const addTodo = useCallback((text) => {
        const newTodo = {
            id: Date.now(),
            text: text.trim(),
            completed: false,
            createdAt: new Date().toISOString()
        };
        setTodos(prev => [...prev, newTodo]);
    }, []);

    const toggleTodo = useCallback((id) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id 
                ? { ...todo, completed: !todo.completed }
                : todo
        ));
    }, []);

    const deleteTodo = useCallback((id) => {
        setTodos(prev => prev.filter(todo => todo.id !== id));
    }, []);

    const editTodo = useCallback((id, newText) => {
        setTodos(prev => prev.map(todo =>
            todo.id === id 
                ? { ...todo, text: newText.trim() }
                : todo
        ));
        setEditingId(null);
    }, []);

    const startEditing = useCallback((id) => {
        setEditingId(id);
    }, []);

    const cancelEditing = useCallback(() => {
        setEditingId(null);
    }, []);

    // Memoized filtered todos
    const filteredTodos = useMemo(() => {
        switch (filter) {
            case 'active':
                return todos.filter(todo => !todo.completed);
            case 'completed':
                return todos.filter(todo => todo.completed);
            default:
                return todos;
        }
    }, [todos, filter]);

    // Memoized stats
    const stats = useMemo(() => ({
        total: todos.length,
        active: todos.filter(todo => !todo.completed).length,
        completed: todos.filter(todo => todo.completed).length
    }), [todos]);

    return (
        <div className="todo-app">
            <TodoHeader onAddTodo={addTodo} />

            <TodoFilter
                currentFilter={filter}
                onFilterChange={setFilter}
                stats={stats}
            />

            <TodoList
                todos={filteredTodos}
                editingId={editingId}
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
                onStartEdit={startEditing}
                onCancelEdit={cancelEditing}
            />
        </div>
    );
}

// Memoized components that receive stable props
const TodoList = React.memo(function TodoList({
    todos,
    editingId,
    onToggle,
    onDelete,
    onEdit,
    onStartEdit,
    onCancelEdit
}) {
    console.log('TodoList rendered');

    return (
        <ul className="todo-list">
            {todos.map(todo => (
                <TodoItem
                    key={todo.id}
                    todo={todo}
                    isEditing={editingId === todo.id}
                    onToggle={() => onToggle(todo.id)}
                    onDelete={() => onDelete(todo.id)}
                    onEdit={(text) => onEdit(todo.id, text)}
                    onStartEdit={() => onStartEdit(todo.id)}
                    onCancelEdit={onCancelEdit}
                />
            ))}
        </ul>
    );
});

const TodoItem = React.memo(function TodoItem({
    todo,
    isEditing,
    onToggle,
    onDelete,
    onEdit,
    onStartEdit,
    onCancelEdit
}) {
    console.log(`TodoItem ${todo.id} rendered`);

    const [editText, setEditText] = useState(todo.text);

    // Reset edit text when editing starts
    useEffect(() => {
        if (isEditing) {
            setEditText(todo.text);
        }
    }, [isEditing, todo.text]);

    const handleSave = useCallback(() => {
        if (editText.trim()) {
            onEdit(editText);
        } else {
            onCancelEdit();
        }
    }, [editText, onEdit, onCancelEdit]);

    const handleKeyPress = useCallback((e) => {
        if (e.key === 'Enter') {
            handleSave();
        } else if (e.key === 'Escape') {
            onCancelEdit();
        }
    }, [handleSave, onCancelEdit]);

    return (
        <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={onToggle}
            />

            {isEditing ? (
                <input
                    type="text"
                    value={editText}
                    onChange={(e) => setEditText(e.target.value)}
                    onKeyDown={handleKeyPress}
                    onBlur={handleSave}
                    autoFocus
                />
            ) : (
                <span 
                    className="todo-text"
                    onDoubleClick={onStartEdit}
                >
                    {todo.text}
                </span>
            )}

            <button onClick={onDelete} className="delete-btn">
                Delete
            </button>
        </li>
    );
});

// 3. Performance anti-patterns și solutions
function PerformanceAntiPatterns() {
    const [items, setItems] = useState([]);
    const [filter, setFilter] = useState('');

    // ❌ BAD: Inline object creation
    const badStyle = { color: 'red', fontSize: '14px' };

    // ✅ GOOD: Memoized style object
    const goodStyle = useMemo(() => ({
        color: 'red',
        fontSize: '14px'
    }), []);

    // ❌ BAD: Inline function creation
    const renderBadItems = () => {
        return items.map(item => (
            <div
                key={item.id}
                style={{ padding: '10px' }} // New object every render
                onClick={() => console.log(item.id)} // New function every render
            >
                {item.name}
            </div>
        ));
    };

    // ✅ GOOD: Stable callbacks și memoized styles
    const itemStyle = useMemo(() => ({ padding: '10px' }), []);

    const handleItemClick = useCallback((id) => {
        console.log('Item clicked:', id);
    }, []);

    const renderGoodItems = useMemo(() => {
        return items.map(item => (
            <div
                key={item.id}
                style={itemStyle}
                onClick={() => handleItemClick(item.id)}
            >
                {item.name}
            </div>
        ));
    }, [items, itemStyle, handleItemClick]);

    return (
        <div>
            <input
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
                placeholder="Filter items..."
            />

            <div className="bad-example">
                <h3>Bad Performance (creates new objects/functions)</h3>
                {renderBadItems()}
            </div>

            <div className="good-example">
                <h3>Good Performance (stable references)</h3>
                {renderGoodItems}
            </div>
        </div>
    );
}
        """, language="javascript")

    with components_tabs[5]:
        st.markdown("### Advanced Patterns")

        st.markdown("#### Compound Components Pattern")

        st.code("""
// 1. Tabs Compound Component
const TabsContext = createContext();

function Tabs({ children, defaultActiveKey = 0, onChange }) {
    const [activeKey, setActiveKey] = useState(defaultActiveKey);

    const handleChange = useCallback((key) => {
        setActiveKey(key);
        onChange?.(key);
    }, [onChange]);

    const contextValue = useMemo(() => ({
        activeKey,
        setActiveKey: handleChange
    }), [activeKey, handleChange]);

    return (
        <TabsContext.Provider value={contextValue}>
            <div className="tabs">{children}</div>
        </TabsContext.Provider>
    );
}

function TabList({ children }) {
    return <div className="tab-list">{children}</div>;
}

function Tab({ children, eventKey, disabled = false }) {
    const { activeKey, setActiveKey } = useContext(TabsContext);
    const isActive = activeKey === eventKey;

    const handleClick = () => {
        if (!disabled) {
            setActiveKey(eventKey);
        }
    };

    return (
        <button
            className={`className={`tab ${isActive ? 'active' : ''} ${disabled ? 'disabled' : ''}`}
            onClick={handleClick}
            disabled={disabled}
            role="tab"
            aria-selected={isActive}
            tabIndex={isActive ? 0 : -1}
        >
            {children}
        </button>
    );
}

function TabPanels({ children }) {
    const { activeKey } = useContext(TabsContext);
    
    return (
        <div className="tab-panels">
            {React.Children.map(children, (child, index) => {
                if (index === activeKey) {
                    return React.cloneElement(child, { isActive: true });
                }
                return null;
            })}
        </div>
    );
}

function TabPanel({ children, isActive }) {
    return (
        <div 
            className={`tab-panel ${isActive ? 'active' : ''}`}
            role="tabpanel"
        >
            {children}
        </div>
    );
}

// Usage
function TabsExample() {
    return (
        <Tabs defaultActiveKey={0} onChange={(key) => console.log('Tab changed:', key)}>
            <TabList>
                <Tab eventKey={0}>Dashboard</Tab>
                <Tab eventKey={1}>Profile</Tab>
                <Tab eventKey={2}>Settings</Tab>
                <Tab eventKey={3} disabled>Disabled</Tab>
            </TabList>
            
            <TabPanels>
                <TabPanel>
                    <DashboardContent />
                </TabPanel>
                <TabPanel>
                    <ProfileContent />
                </TabPanel>
                <TabPanel>
                    <SettingsContent />
                </TabPanel>
                <TabPanel>
                    <div>This tab is disabled</div>
                </TabPanel>
            </TabPanels>
        </Tabs>
    );
}

// 2. Modal Compound Component
const ModalContext = createContext();

function Modal({ children, isOpen, onClose, size = 'medium' }) {
    const [isClosing, setIsClosing] = useState(false);
    
    const handleClose = useCallback(() => {
        setIsClosing(true);
        setTimeout(() => {
            setIsClosing(false);
            onClose();
        }, 200);
    }, [onClose]);
    
    const contextValue = useMemo(() => ({
        isOpen,
        onClose: handleClose,
        size
    }), [isOpen, handleClose, size]);
    
    useEffect(() => {
        const handleEscape = (e) => {
            if (e.key === 'Escape' && isOpen) {
                handleClose();
            }
        };
        
        if (isOpen) {
            document.addEventListener('keydown', handleEscape);
            document.body.style.overflow = 'hidden';
        }
        
        return () => {
            document.removeEventListener('keydown', handleEscape);
            document.body.style.overflow = 'auto';
        };
    }, [isOpen, handleClose]);
    
    if (!isOpen && !isClosing) return null;
    
    return createPortal(
        <ModalContext.Provider value={contextValue}>
            <div 
                className={`modal-overlay ${isClosing ? 'closing' : ''}`}
                onClick={handleClose}
            >
                <div 
                    className={`modal modal-${size}`}
                    onClick={(e) => e.stopPropagation()}
                >
                    {children}
                </div>
            </div>
        </ModalContext.Provider>,
        document.body
    );
}

function ModalHeader({ children, showCloseButton = true }) {
    const { onClose } = useContext(ModalContext);
    
    return (
        <div className="modal-header">
            <div className="modal-title">{children}</div>
            {showCloseButton && (
                <button 
                    className="modal-close-button"
                    onClick={onClose}
                    aria-label="Close modal"
                >
                    ×
                </button>
            )}
        </div>
    );
}

function ModalBody({ children }) {
    return <div className="modal-body">{children}</div>;
}

function ModalFooter({ children }) {
    return <div className="modal-footer">{children}</div>;
}

// Usage
function ModalExample() {
    const [isModalOpen, setIsModalOpen] = useState(false);
    
    return (
        <div>
            <button onClick={() => setIsModalOpen(true)}>
                Open Modal
            </button>
            
            <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
                <ModalHeader>Confirm Action</ModalHeader>
                <ModalBody>
                    <p>Are you sure you want to delete this item?</p>
                </ModalBody>
                <ModalFooter>
                    <button onClick={() => setIsModalOpen(false)}>Cancel</button>
                    <button className="danger" onClick={() => setIsModalOpen(false)}>
                        Delete
                    </button>
                </ModalFooter>
            </Modal>
        </div>
    );
}

// 3. Form Compound Component
const FormContext = createContext();

function Form({ children, onSubmit, validation = {} }) {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});
    
    const setValue = useCallback((name, value) => {
        setValues(prev => ({ ...prev, [name]: value }));
        
        // Clear error when user starts typing
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: '' }));
        }
    }, [errors]);
    
    const setFieldTouched = useCallback((name) => {
        setTouched(prev => ({ ...prev, [name]: true }));
        
        // Validate field on blur
        if (validation[name]) {
            const error = validation[name](values[name], values);
            setErrors(prev => ({ ...prev, [name]: error }));
        }
    }, [validation, values]);
    
    const validateForm = useCallback(() => {
        const newErrors = {};
        let isValid = true;
        
        Object.keys(validation).forEach(fieldName => {
            const error = validation[fieldName](values[fieldName], values);
            if (error) {
                newErrors[fieldName] = error;
                isValid = false;
            }
        });
        
        setErrors(newErrors);
        setTouched(Object.keys(validation).reduce((acc, key) => {
            acc[key] = true;
            return acc;
        }, {}));
        
        return isValid;
    }, [validation, values]);
    
    const handleSubmit = useCallback((e) => {
        e.preventDefault();
        
        if (validateForm()) {
            onSubmit(values);
        }
    }, [validateForm, onSubmit, values]);
    
    const contextValue = useMemo(() => ({
        values,
        errors,
        touched,
        setValue,
        setFieldTouched
    }), [values, errors, touched, setValue, setFieldTouched]);
    
    return (
        <FormContext.Provider value={contextValue}>
            <form onSubmit={handleSubmit} noValidate>
                {children}
            </form>
        </FormContext.Provider>
    );
}

function FormField({ name, label, type = 'text', required = false, ...props }) {
    const { values, errors, touched, setValue, setFieldTouched } = useContext(FormContext);
    
    const value = values[name] || '';
    const error = touched[name] ? errors[name] : '';
    
    return (
        <div className={`form-field ${error ? 'error' : ''}`}>
            <label htmlFor={name}>
                {label}
                {required && <span className="required">*</span>}
            </label>
            <input
                id={name}
                name={name}
                type={type}
                value={value}
                onChange={(e) => setValue(name, e.target.value)}
                onBlur={() => setFieldTouched(name)}
                {...props}
            />
            {error && <span className="error-message">{error}</span>}
        </div>
    );
}

function FormActions({ children }) {
    return <div className="form-actions">{children}</div>;
}

// Usage
function FormExample() {
    const validation = {
        email: (value) => {
            if (!value) return 'Email is required';
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) return 'Invalid email';
            return '';
        },
        password: (value) => {
            if (!value) return 'Password is required';
            if (value.length < 8) return 'Password must be at least 8 characters';
            return '';
        }
    };
    
    const handleSubmit = (values) => {
        console.log('Form submitted:', values);
    };
    
    return (
        <Form onSubmit={handleSubmit} validation={validation}>
            <FormField
                name="email"
                label="Email"
                type="email"
                required
                placeholder="Enter your email"
            />
            <FormField
                name="password"
                label="Password"
                type="password"
                required
                placeholder="Enter your password"
            />
            <FormActions>
                <button type="submit">Login</button>
            </FormActions>
        </Form>
    );
}
        """, language="javascript")

        st.markdown("#### Polymorphic Components")

        st.code("""
// Polymorphic component - poate fi orice element HTML
function Box({ as: Component = 'div', children, ...props }) {
    return <Component {...props}>{children}</Component>;
}

// Advanced polymorphic component cu TypeScript-like behavior în JavaScript
function Button({ 
    as = 'button', 
    variant = 'primary', 
    size = 'medium', 
    children, 
    ...props 
}) {
    const Component = as;
    
    const baseClasses = 'btn';
    const variantClasses = {
        primary: 'btn-primary',
        secondary: 'btn-secondary',
        danger: 'btn-danger',
        ghost: 'btn-ghost'
    };
    const sizeClasses = {
        small: 'btn-sm',
        medium: 'btn-md',
        large: 'btn-lg'
    };
    
    const className = [
        baseClasses,
        variantClasses[variant],
        sizeClasses[size],
        props.className
    ].filter(Boolean).join(' ');
    
    return (
        <Component {...props} className={className}>
            {children}
        </Component>
    );
}

// Usage examples
function PolymorphicExamples() {
    return (
        <div>
            {/* As button */}
            <Button onClick={() => console.log('clicked')}>
                Click me
            </Button>
            
            {/* As link */}
            <Button as="a" href="/profile" variant="secondary">
                Go to Profile
            </Button>
            
            {/* As div with custom behavior */}
            <Button 
                as="div" 
                variant="ghost"
                onClick={() => console.log('div clicked')}
                style={{ cursor: 'pointer' }}
            >
                Custom div button
            </Button>
            
            {/* As React Router Link */}
            <Button as={Link} to="/dashboard" variant="primary" size="large">
                Dashboard
            </Button>
        </div>
    );
}

// 4. Headless Components Pattern
function useDisclosure(initialState = false) {
    const [isOpen, setIsOpen] = useState(initialState);
    
    const open = useCallback(() => setIsOpen(true), []);
    const close = useCallback(() => setIsOpen(false), []);
    const toggle = useCallback(() => setIsOpen(prev => !prev), []);
    
    return { isOpen, open, close, toggle };
}

function useDropdown({ closeOnSelect = true } = {}) {
    const { isOpen, open, close, toggle } = useDisclosure();
    const [selectedValue, setSelectedValue] = useState(null);
    const triggerRef = useRef(null);
    const menuRef = useRef(null);
    
    const handleSelect = useCallback((value) => {
        setSelectedValue(value);
        if (closeOnSelect) {
            close();
        }
    }, [close, closeOnSelect]);
    
    // Close on outside click
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (
                isOpen &&
                triggerRef.current &&
                menuRef.current &&
                !triggerRef.current.contains(event.target) &&
                !menuRef.current.contains(event.target)
            ) {
                close();
            }
        };
        
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, [isOpen, close]);
    
    // Close on escape
    useEffect(() => {
        const handleEscape = (event) => {
            if (event.key === 'Escape' && isOpen) {
                close();
            }
        };
        
        document.addEventListener('keydown', handleEscape);
        return () => document.removeEventListener('keydown', handleEscape);
    }, [isOpen, close]);
    
    return {
        isOpen,
        selectedValue,
        triggerRef,
        menuRef,
        open,
        close,
        toggle,
        handleSelect
    };
}

// Headless Dropdown component
function Dropdown({ children, closeOnSelect }) {
    const dropdown = useDropdown({ closeOnSelect });
    
    return (
        <div className="dropdown">
            {typeof children === 'function' ? children(dropdown) : children}
        </div>
    );
}

// Usage of headless component
function DropdownExample() {
    return (
        <Dropdown closeOnSelect={true}>
            {({ isOpen, triggerRef, menuRef, toggle, handleSelect, selectedValue }) => (
                <>
                    <button
                        ref={triggerRef}
                        onClick={toggle}
                        className="dropdown-trigger"
                    >
                        {selectedValue || 'Select option'} {isOpen ? '▲' : '▼'}
                    </button>
                    
                    {isOpen && (
                        <div ref={menuRef} className="dropdown-menu">
                            <button onClick={() => handleSelect('Option 1')}>
                                Option 1
                            </button>
                            <button onClick={() => handleSelect('Option 2')}>
                                Option 2
                            </button>
                            <button onClick={() => handleSelect('Option 3')}>
                                Option 3
                            </button>
                        </div>
                    )}
                </>
            )}
        </Dropdown>
    );
}

// 5. Provider Pattern pentru complex state
function createContextProvider(useValue) {
    const Context = createContext(null);
    
    function Provider({ children }) {
        const value = useValue();
        return <Context.Provider value={value}>{children}</Context.Provider>;
    }
    
    function useContext() {
        const context = React.useContext(Context);
        if (!context) {
            throw new Error('useContext must be used within Provider');
        }
        return context;
    }
    
    return [Provider, useContext];
}

// Shopping cart provider
function useShoppingCartValue() {
    const [items, setItems] = useState([]);
    const [isOpen, setIsOpen] = useState(false);
    
    const addItem = useCallback((product) => {
        setItems(prev => {
            const existing = prev.find(item => item.id === product.id);
            if (existing) {
                return prev.map(item =>
                    item.id === product.id
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                );
            }
            return [...prev, { ...product, quantity: 1 }];
        });
    }, []);
    
    const removeItem = useCallback((productId) => {
        setItems(prev => prev.filter(item => item.id !== productId));
    }, []);
    
    const updateQuantity = useCallback((productId, quantity) => {
        if (quantity <= 0) {
            removeItem(productId);
            return;
        }
        
        setItems(prev => prev.map(item =>
            item.id === productId ? { ...item, quantity } : item
        ));
    }, [removeItem]);
    
    const clearCart = useCallback(() => {
        setItems([]);
    }, []);
    
    const toggleCart = useCallback(() => {
        setIsOpen(prev => !prev);
    }, []);
    
    const total = useMemo(() => {
        return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }, [items]);
    
    const itemCount = useMemo(() => {
        return items.reduce((sum, item) => sum + item.quantity, 0);
    }, [items]);
    
    return {
        items,
        isOpen,
        total,
        itemCount,
        addItem,
        removeItem,
        updateQuantity,
        clearCart,
        toggleCart
    };
}

const [ShoppingCartProvider, useShoppingCart] = createContextProvider(useShoppingCartValue);

// Usage
function App() {
    return (
        <ShoppingCartProvider>
            <Header />
            <ProductList />
            <ShoppingCart />
        </ShoppingCartProvider>
    );
}

function Header() {
    const { itemCount, toggleCart } = useShoppingCart();
    
    return (
        <header>
            <h1>My Store</h1>
            <button onClick={toggleCart}>
                Cart ({itemCount})
            </button>
        </header>
    );
}

function ProductCard({ product }) {
    const { addItem } = useShoppingCart();
    
    return (
        <div className="product-card">
            <h3>{product.name}</h3>
            <p>${product.price}</p>
            <button onClick={() => addItem(product)}>
                Add to Cart
            </button>
        </div>
    );
}
        """, language="javascript")

    with components_tabs[6]:
        st.markdown("### Testing Components")

        st.markdown("#### React Testing Library Fundamentals")

        st.code("""
// 1. Basic Component Testing
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';

// Component to test
function Counter({ initialCount = 0, onCountChange }) {
    const [count, setCount] = useState(initialCount);
    
    const increment = () => {
        const newCount = count + 1;
        setCount(newCount);
        onCountChange?.(newCount);
    };
    
    const decrement = () => {
        const newCount = count - 1;
        setCount(newCount);
        onCountChange?.(newCount);
    };
    
    const reset = () => {
        setCount(initialCount);
        onCountChange?.(initialCount);
    };
    
    return (
        <div>
            <h2>Counter: {count}</h2>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
            <button onClick={reset}>Reset</button>
            {count > 10 && <p>Count is high!</p>}
        </div>
    );
}

// Test suite
describe('Counter Component', () => {
    test('renders with initial count', () => {
        render(<Counter initialCount={5} />);
        
        expect(screen.getByText('Counter: 5')).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /increment/i })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /decrement/i })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /reset/i })).toBeInTheDocument();
    });
    
    test('increments count when increment button is clicked', async () => {
        const user = userEvent.setup();
        render(<Counter initialCount={0} />);
        
        const incrementButton = screen.getByRole('button', { name: /increment/i });
        
        await user.click(incrementButton);
        expect(screen.getByText('Counter: 1')).toBeInTheDocument();
        
        await user.click(incrementButton);
        expect(screen.getByText('Counter: 2')).toBeInTheDocument();
    });
    
    test('decrements count when decrement button is clicked', async () => {
        const user = userEvent.setup();
        render(<Counter initialCount={5} />);
        
        const decrementButton = screen.getByRole('button', { name: /decrement/i });
        
        await user.click(decrementButton);
        expect(screen.getByText('Counter: 4')).toBeInTheDocument();
    });
    
    test('resets count to initial value', async () => {
        const user = userEvent.setup();
        render(<Counter initialCount={3} />);
        
        const incrementButton = screen.getByRole('button', { name: /increment/i });
        const resetButton = screen.getByRole('button', { name: /reset/i });
        
        // Increment a few times
        await user.click(incrementButton);
        await user.click(incrementButton);
        expect(screen.getByText('Counter: 5')).toBeInTheDocument();
        
        // Reset
        await user.click(resetButton);
        expect(screen.getByText('Counter: 3')).toBeInTheDocument();
    });
    
    test('shows high count message when count > 10', async () => {
        const user = userEvent.setup();
        render(<Counter initialCount={10} />);
        
        const incrementButton = screen.getByRole('button', { name: /increment/i });
        
        // Count is 10, message should not be visible
        expect(screen.queryByText('Count is high!')).not.toBeInTheDocument();
        
        // Increment to 11
        await user.click(incrementButton);
        expect(screen.getByText('Count is high!')).toBeInTheDocument();
    });
    
    test('calls onCountChange callback when count changes', async () => {
        const user = userEvent.setup();
        const mockOnCountChange = jest.fn();
        
        render(<Counter initialCount={0} onCountChange={mockOnCountChange} />);
        
        const incrementButton = screen.getByRole('button', { name: /increment/i });
        
        await user.click(incrementButton);
        
        expect(mockOnCountChange).toHaveBeenCalledWith(1);
        expect(mockOnCountChange).toHaveBeenCalledTimes(1);
    });
});

// 2. Testing Forms
function ContactForm({ onSubmit }) {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    const [errors, setErrors] = useState({});
    const [isSubmitting, setIsSubmitting] = useState(false);
    
    const validateForm = () => {
        const newErrors = {};
        
        if (!formData.name.trim()) {
            newErrors.name = 'Name is required';
        }
        
        if (!formData.email.trim()) {
            newErrors.email = 'Email is required';
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
            newErrors.email = 'Invalid email format';
        }
        
        if (!formData.message.trim()) {
            newErrors.message = 'Message is required';
        }
        
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!validateForm()) return;
        
        setIsSubmitting(true);
        try {
            await onSubmit(formData);
        } finally {
            setIsSubmitting(false);
        }
    };
    
    const handleChange = (field) => (e) => {
        setFormData(prev => ({ ...prev, [field]: e.target.value }));
        if (errors[field]) {
            setErrors(prev => ({ ...prev, [field]: '' }));
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="name">Name</label>
                <input
                    id="name"
                    type="text"
                    value={formData.name}
                    onChange={handleChange('name')}
                />
                {errors.name && <span role="alert">{errors.name}</span>}
            </div>
            
            <div>
                <label htmlFor="email">Email</label>
                <input
                    id="email"
                    type="email"
                    value={formData.email}
                    onChange={handleChange('email')}
                />
                {errors.email && <span role="alert">{errors.email}</span>}
            </div>
            
            <div>
                <label htmlFor="message">Message</label>
                <textarea
                    id="message"
                    value={formData.message}
                    onChange={handleChange('message')}
                />
                {errors.message && <span role="alert">{errors.message}</span>}
            </div>
            
            <button type="submit" disabled={isSubmitting}>
                {isSubmitting ? 'Submitting...' : 'Submit'}
            </button>
        </form>
    );
}

// Form tests
describe('ContactForm', () => {
    test('validates required fields', async () => {
        const user = userEvent.setup();
        const mockOnSubmit = jest.fn();
        
        render(<ContactForm onSubmit={mockOnSubmit} />);
        
        const submitButton = screen.getByRole('button', { name: /submit/i });
        
        await user.click(submitButton);
        
        expect(screen.getByText('Name is required')).toBeInTheDocument();
        expect(screen.getByText('Email is required')).toBeInTheDocument();
        expect(screen.getByText('Message is required')).toBeInTheDocument();
        expect(mockOnSubmit).not.toHaveBeenCalled();
    });
    
    test('validates email format', async () => {
        const user = userEvent.setup();
        render(<ContactForm onSubmit={jest.fn()} />);
        
        const emailInput = screen.getByLabelText(/email/i);
        const submitButton = screen.getByRole('button', { name: /submit/i });
        
        await user.type(emailInput, 'invalid-email');
        await user.click(submitButton);
        
        expect(screen.getByText('Invalid email format')).toBeInTheDocument();
    });
    
    test('submits form with valid data', async () => {
        const user = userEvent.setup();
        const mockOnSubmit = jest.fn().mockResolvedValue();
        
        render(<ContactForm onSubmit={mockOnSubmit} />);
        
        await user.type(screen.getByLabelText(/name/i), 'John Doe');
        await user.type(screen.getByLabelText(/email/i), 'john@example.com');
        await user.type(screen.getByLabelText(/message/i), 'Hello world');
        
        await user.click(screen.getByRole('button', { name: /submit/i }));
        
        expect(mockOnSubmit).toHaveBeenCalledWith({
            name: 'John Doe',
            email: 'john@example.com',
            message: 'Hello world'
        });
    });
    
    test('shows loading state during submission', async () => {
        const user = userEvent.setup();
        const mockOnSubmit = jest.fn(() => new Promise(resolve => setTimeout(resolve, 100)));
        
        render(<ContactForm onSubmit={mockOnSubmit} />);
        
        // Fill form
        await user.type(screen.getByLabelText(/name/i), 'John Doe');
        await user.type(screen.getByLabelText(/email/i), 'john@example.com');
        await user.type(screen.getByLabelText(/message/i), 'Hello world');
        
        const submitButton = screen.getByRole('button', { name: /submit/i });
        await user.click(submitButton);
        
        expect(screen.getByText('Submitting...')).toBeInTheDocument();
        expect(submitButton).toBeDisabled();
        
        await waitFor(() => {
            expect(screen.getByText('Submit')).toBeInTheDocument();
        });
    });
});

// 3. Testing components with Context
const ThemeContext = createContext();

function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    const toggleTheme = () => {
        setTheme(prev => prev === 'light' ? 'dark' : 'light');
    };
    
    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

function ThemedButton() {
    const { theme, toggleTheme } = useContext(ThemeContext);
    
    return (
        <button 
            className={`btn btn-${theme}`}
            onClick={toggleTheme}
        >
            Current theme: {theme}
        </button>
    );
}

// Context testing helper
function renderWithTheme(component, { initialTheme = 'light' } = {}) {
    const TestThemeProvider = ({ children }) => {
        const [theme, setTheme] = useState(initialTheme);
        
        const toggleTheme = () => {
            setTheme(prev => prev === 'light' ? 'dark' : 'light');
        };
        
        return (
            <ThemeContext.Provider value={{ theme, toggleTheme }}>
                {children}
            </ThemeContext.Provider>
        );
    };
    
    return render(component, { wrapper: TestThemeProvider });
}

describe('ThemedButton', () => {
    test('displays current theme', () => {
        renderWithTheme(<ThemedButton />);
        
        expect(screen.getByText('Current theme: light')).toBeInTheDocument();
    });
    
    test('toggles theme when clicked', async () => {
        const user = userEvent.setup();
        renderWithTheme(<ThemedButton />);
        
        const button = screen.getByRole('button');
        
        expect(screen.getByText('Current theme: light')).toBeInTheDocument();
        
        await user.click(button);
        
        expect(screen.getByText('Current theme: dark')).toBeInTheDocument();
    });
    
    test('starts with dark theme', () => {
        renderWithTheme(<ThemedButton />, { initialTheme: 'dark' });
        
        expect(screen.getByText('Current theme: dark')).toBeInTheDocument();
    });
});

// 4. Testing Async Components
function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchUser = async () => {
            try {
                setLoading(true);
                setError(null);
                
                const response = await fetch(`/api/users/${userId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch user');
                }
                
                const userData = await response.json();
                setUser(userData);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchUser();
    }, [userId]);
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    if (!user) return <div>User not found</div>;
    
    return (
        <div>
            <h1>{user.name}</h1>
            <p>{user.email}</p>
        </div>
    );
}

// Mock fetch pentru testing
global.fetch = jest.fn();

describe('UserProfile', () => {
    beforeEach(() => {
        fetch.mockClear();
    });
    
    test('shows loading state initially', () => {
        fetch.mockResolvedValue({
            ok: true,
            json: async () => ({ name: 'John Doe', email: 'john@example.com' })
        });
        
        render(<UserProfile userId="1" />);
        
        expect(screen.getByText('Loading...')).toBeInTheDocument();
    });
    
    test('displays user data after successful fetch', async () => {
        const mockUser = { name: 'John Doe', email: 'john@example.com' };
        
        fetch.mockResolvedValue({
            ok: true,
            json: async () => mockUser
        });
        
        render(<UserProfile userId="1" />);
        
        await waitFor(() => {
            expect(screen.getByText('John Doe')).toBeInTheDocument();
        });
        
        expect(screen.getByText('john@example.com')).toBeInTheDocument();
        expect(fetch).toHaveBeenCalledWith('/api/users/1');
    });
    
    test('displays error message on fetch failure', async () => {
        fetch.mockResolvedValue({
            ok: false
        });
        
        render(<UserProfile userId="1" />);
        
        await waitFor(() => {
            expect(screen.getByText('Error: Failed to fetch user')).toBeInTheDocument();
        });
    });
    
    test('refetches user data when userId changes', async () => {
        const mockUser1 = { name: 'User 1', email: 'user1@example.com' };
        const mockUser2 = { name: 'User 2', email: 'user2@example.com' };
        
        fetch
            .mockResolvedValueOnce({
                ok: true,
                json: async () => mockUser1
            })
            .mockResolvedValueOnce({
                ok: true,
                json: async () => mockUser2
            });
        
        const { rerender } = render(<UserProfile userId="1" />);
        
        await waitFor(() => {
            expect(screen.getByText('User 1')).toBeInTheDocument();
        });
        
        rerender(<UserProfile userId="2" />);
        
        await waitFor(() => {
            expect(screen.getByText('User 2')).toBeInTheDocument();
        });
        
        expect(fetch).toHaveBeenCalledTimes(2);
        expect(fetch).toHaveBeenNthCalledWith(1, '/api/users/1');
        expect(fetch).toHaveBeenNthCalledWith(2, '/api/users/2');
    });
});
        """, language="javascript")

    with components_tabs[7]:
        st.markdown("### Architecture și Design")

        st.markdown("#### Component Architecture Principles")

        st.code("""
// 1. Single Responsibility Principle
// Bad - component face prea multe lucruri
function UserDashboard({ userId }) {
    const [user, setUser] = useState(null);
    const [posts, setPosts] = useState([]);
    const [notifications, setNotifications] = useState([]);
    const [theme, setTheme] = useState('light');
    const [sidebarOpen, setSidebarOpen] = useState(false);
    
    // Multiple useEffect hooks for different responsibilities
    useEffect(() => { /* fetch user */ }, [userId]);
    useEffect(() => { /* fetch posts */ }, [userId]);
    useEffect(() => { /* fetch notifications */ }, [userId]);
    useEffect(() => { /* handle theme */ }, [theme]);
    
    // Lots of event handlers
    // Lots of render logic mixing different concerns
    
    return (
        <div>
            {/* Complex JSX mixing user, posts, notifications, theme logic */}
        </div>
    );
}

// Good - separate responsibilities
function UserDashboard({ userId }) {
    return (
        <DashboardLayout>
            <DashboardHeader userId={userId} />
            <DashboardSidebar userId={userId} />
            <DashboardMain userId={userId} />
            <NotificationCenter userId={userId} />
        </DashboardLayout>
    );
}

function DashboardHeader({ userId }) {
    const { user } = useUser(userId);
    const { theme, toggleTheme } = useTheme();
    
    return (
        <header className={`dashboard-header theme-${theme}`}>
            <UserAvatar user={user} />
            <ThemeToggle theme={theme} onToggle={toggleTheme} />
        </header>
    );
}

function DashboardMain({ userId }) {
    const { posts, loading, error } = useUserPosts(userId);
    
    if (loading) return <PostsSkeleton />;
    if (error) return <ErrorMessage error={error} />;
    
    return (
        <main className="dashboard-main">
            <PostsList posts={posts} />
        </main>
    );
}

// 2. Composition over Inheritance
// Bad - inheritance-like pattern
class BaseCard extends React.Component {
    render() {
        return (
            <div className="card">
                <div className="card-header">{this.renderHeader()}</div>
                <div className="card-body">{this.renderBody()}</div>
                <div className="card-footer">{this.renderFooter()}</div>
            </div>
        );
    }
    
    renderHeader() {
        throw new Error('Must implement renderHeader');
    }
    
    renderBody() {
        throw new Error('Must implement renderBody');
    }
    
    renderFooter() {
        return null;
    }
}

class UserCard extends BaseCard {
    renderHeader() {
        return <h3>{this.props.user.name}</h3>;
    }
    
    renderBody() {
        return <p>{this.props.user.email}</p>;
    }
}

// Good - composition pattern
function Card({ header, children, footer, className = '' }) {
    return (
        <div className={`card ${className}`}>
            {header && <div className="card-header">{header}</div>}
            <div className="card-body">{children}</div>
            {footer && <div className="card-footer">{footer}</div>}
        </div>
    );
}

function UserCard({ user, onEdit, onDelete }) {
    return (
        <Card
            header={<UserCardHeader user={user} />}
            footer={<UserCardActions onEdit={onEdit} onDelete={onDelete} />}
            className="user-card"
        >
            <UserCardBody user={user} />
        </Card>
    );
}

function UserCardHeader({ user }) {
    return (
        <div className="user-card-header">
            <UserAvatar user={user} size="small" />
            <h3>{user.name}</h3>
            <UserStatus status={user.status} />
        </div>
    );
}

// 3. Container/Presentational Pattern
// Container Component - handles logic and state
function UserListContainer() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [filters, setFilters] = useState({
        search: '',
        role: 'all',
        status: 'all'
    });
    const [sorting, setSorting] = useState({
        field: 'name',
        direction: 'asc'
    });
    
    // Data fetching logic
    const { data, loading: fetchLoading, error: fetchError } = useUsers({
        filters,
        sorting
    });
    
    // Event handlers
    const handleFilterChange = useCallback((newFilters) => {
        setFilters(prev => ({ ...prev, ...newFilters }));
    }, []);
    
    const handleSortChange = useCallback((field) => {
        setSorting(prev => ({
            field,
            direction: prev.field === field && prev.direction === 'asc' ? 'desc' : 'asc'
        }));
    }, []);
    
    const handleUserEdit = useCallback((userId) => {
        // Handle edit logic
    }, []);
    
    const handleUserDelete = useCallback((userId) => {
        // Handle delete logic
    }, []);
    
    // Pass everything to presentational component
    return (
        <UserListPresentation
            users={data}
            loading={fetchLoading}
            error={fetchError}
            filters={filters}
            sorting={sorting}
            onFilterChange={handleFilterChange}
            onSortChange={handleSortChange}
            onUserEdit={handleUserEdit}
            onUserDelete={handleUserDelete}
        />
    );
}

// Presentational Component - only UI and display logic
function UserListPresentation({
    users,
    loading,
    error,
    filters,
    sorting,
    onFilterChange,
    onSortChange,
    onUserEdit,
    onUserDelete
}) {
    if (error) {
        return <ErrorBoundary><ErrorMessage error={error} /></ErrorBoundary>;
    }
    
    return (
        <div className="user-list">
            <UserListHeader
                filters={filters}
                onFilterChange={onFilterChange}
                userCount={users?.length || 0}
            />
            
            <UserListTable
                users={users}
                loading={loading}
                sorting={sorting}
                onSortChange={onSortChange}
                onUserEdit={onUserEdit}
                onUserDelete={onUserDelete}
            />
        </div>
    );
}

// 4. Custom Hooks pentru Business Logic
function useUsers({ filters, sorting, pagination }) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const fetchUsers = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);
            
            const params = {
                ...filters,
                sortBy: sorting.field,
                sortOrder: sorting.direction,
                page: pagination?.page || 1,
                limit: pagination?.limit || 20
            };
            
            const response = await userService.getUsers(params);
            setData(response.data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    }, [filters, sorting, pagination]);
    
    useEffect(() => {
        fetchUsers();
    }, [fetchUsers]);
    
    const createUser = useCallback(async (userData) => {
        try {
            const newUser = await userService.createUser(userData);
            setData(prev => [newUser, ...prev]);
            return newUser;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);
    
    const updateUser = useCallback(async (userId, updates) => {
        try {
            const updatedUser = await userService.updateUser(userId, updates);
            setData(prev => prev.map(user => 
                user.id === userId ? updatedUser : user
            ));
            return updatedUser;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);
    
    const deleteUser = useCallback(async (userId) => {
        try {
            await userService.deleteUser(userId);
            setData(prev => prev.filter(user => user.id !== userId));
        } catch (err) {
            setError(err);
            throw err;
        }
    }, []);
    
    return {
        data,
        loading,
        error,
        refetch: fetchUsers,
        createUser,
        updateUser,
        deleteUser
    };
}

// 5. Error Boundaries și Error Handling
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            hasError: false, 
            error: null, 
            errorInfo: null,
            eventId: null
        };
    }
    
    static getDerivedStateFromError(error) {
        return { hasError: true };
    }
    
    componentDidCatch(error, errorInfo) {
        console.error('Error caught by boundary:', error, errorInfo);
        
        this.setState({
            error,
            errorInfo
        });
        
        // Log to error monitoring service
        if (window.Sentry) {
            const eventId = window.Sentry.captureException(error, {
                contexts: {
                    react: {
                        componentStack: errorInfo.componentStack
                    }
                }
            });
            this.setState({ eventId });
        }
        
        // Log to analytics
        if (window.gtag) {
            window.gtag('event', 'exception', {
                description: error.message,
                fatal: false
            });
        }
    }
    
    render() {
        if (this.state.hasError) {
            if (this.props.fallback) {
                return this.props.fallback(
                    this.state.error, 
                    this.state.errorInfo,
                    () => this.setState({ hasError: false, error: null, errorInfo: null })
                );
            }
            
            return (
                <div className="error-boundary">
                    <h2>Something went wrong</h2>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        <summary>Error details</summary>
                        {this.state.error && this.state.error.toString()}
                        <br />
                        {this.state.errorInfo.componentStack}
                    </details>
                    {this.state.eventId && (
                        <p>Error ID: {this.state.eventId}</p>
                    )}
                    <button 
                        onClick={() => this.setState({ 
                            hasError: false, 
                            error: null, 
                            errorInfo: null 
                        })}
                    >
                        Try again
                    </button>
                </div>
            );
        }
        
        return this.props.children;
    }
}

// Usage
function App() {
    return (
        <ErrorBoundary fallback={(error, errorInfo, retry) => (
            <CustomErrorFallback 
                error={error} 
                errorInfo={errorInfo} 
                onRetry={retry}
            />
        )}>
            <Router>
                <Routes>
                    <Route path="/users" element={
                        <ErrorBoundary>
                            <UserListContainer />
                        </ErrorBoundary>
                    } />
                    <Route path="/dashboard" element={
                        <ErrorBoundary>
                            <UserDashboard />
                        </ErrorBoundary>
                    } />
                </Routes>
            </Router>
        </ErrorBoundary>
    );
}

// 6. Performance Optimization Architecture
function OptimizedApp() {
    return (
        <React.StrictMode>
            <ErrorBoundary>
                <Suspense fallback={<AppLoadingSpinner />}>
                    <AppProviders>
                        <AppRouter />
                    </AppProviders>
                </Suspense>
            </ErrorBoundary>
        </React.StrictMode>
    );
}

function AppProviders({ children }) {
    return (
        <QueryClient>
            <AuthProvider>
                <ThemeProvider>
                    <NotificationProvider>
                        {children}
                    </NotificationProvider>
                </ThemeProvider>
            </AuthProvider>
        </QueryClient>
    );
}

// Lazy loaded routes pentru code splitting
const UserManagement = lazy(() => import('./pages/UserManagement'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));

function AppRouter() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/users" element={
                    <Suspense fallback={<PageSkeleton />}>
                        <UserManagement />
                    </Suspense>
                } />
                <Route path="/dashboard" element={
                    <Suspense fallback={<PageSkeleton />}>
                        <Dashboard />
                    </Suspense>
                } />
                <Route path="/settings" element={
                    <Suspense fallback={<PageSkeleton />}>
                        <Settings />
                    </Suspense>
                } />
            </Routes>
        </Router>
    );
}
        """, language="javascript")

    with components_tabs[8]:
        st.markdown("### Întrebări frecvente la interviuri Components")

        components_qa = [
            {
                "question": "Explică diferența între Class Components și Function Components și de ce Function Components sunt preferate acum",
                "answer": """
                **Class Components (Legacy approach):**
                - Folosesc sintaxa ES6 class și extind React.Component
                - Au acces la lifecycle methods (componentDidMount, componentDidUpdate, etc.)
                - State este gestionat cu this.state și this.setState()
                - This binding poate crea probleme de context
                - Mai mult boilerplate code

                **Function Components (Modern approach):**
                - Funcții JavaScript simple care returnează JSX
                - Folosesc Hooks pentru state și side effects (useState, useEffect)
                - Mai puțin cod, mai ușor de citit și testat
                - Performanță mai bună cu optimizările React
                - Composability mai bună prin custom hooks

                **De ce Function Components sunt preferate:**
                - Sintaxă mai simplă și mai puțin verbozitate
                - Hooks permit reutilizarea logicii între componente
                - Optimizări mai bune de la React team
                - Viitorul React development se concentrează pe function components
                - Easier to reason about și debug
                """
            },
            {
                "question": "Ce sunt Higher-Order Components (HOCs) și cum se compară cu Hooks?",
                "answer": """
                **Higher-Order Components (HOCs):**
                - Funcții care primesc o componentă și returnează o componentă nouă îmbogățită
                - Pattern pentru reutilizarea logicii între componente
                - Pot adăuga props, state sau behavior la componente existente

                **Exemple comune:**
                - withAuth(Component) - adaugă authentication logic
                - withLoading(Component) - adaugă loading states
                - withErrorBoundary(Component) - adaugă error handling

                **Probleme cu HOCs:**
                - Wrapper hell - multiple HOCs creează nesting profund
                - Props collision - HOCs pot suprascrie props existente
                - Static composition - nu pot fi schimbate dinamic
                - Debugging dificil - component tree complex

                **Hooks vs HOCs:**
                - Hooks permit sharing logic fără wrapper components
                - Composition dinamică în timpul runtime
                - Mai puțin complexity în component tree
                - Props nu se pierd sau se suprascriu
                - Mai ușor de testat și debug

                **Când să folosești fiecare:**
                - HOCs: Legacy codebases, cross-cutting concerns la nivel înalt
                - Hooks: New development, fine-grained logic sharing
                """
            },
            {
                "question": "Explică Compound Components pattern și avantajele sale",
                "answer": """
                **Compound Components pattern:**
                Pattern în care multiple componente cooperează pentru a forma o funcționalitate completă, similar cu HTML elements native (select/option, ul/li).

                **Cum funcționează:**
                - Parent component furnizează context prin React Context
                - Child components consumă acest context pentru coordonare
                - Components pot fi compuse flexibil de către developer

                **Avantaje:**
                - **Flexibility**: Developers pot aranja componentele cum doresc
                - **Separation of concerns**: Fiecare componentă are o responsabilitate specifică
                - **Implicit state sharing**: Context permite partajarea automată a state-ului
                - **Better API**: Interface mai intuitivă și declarativă

                **Dezavantaje:**
                - Complexity crescută în implementare
                - Context dependency poate face testing mai dificil
                - Child components trebuie să fie direct descendents (fără wrapper)

                **Use cases:**
                - UI libraries (Tabs, Modal, Dropdown, Form)
                - Când ai nevoie de flexibilitate în composition
                - Complex components cu multiple variante
                - Când vrei să oferi APIs intuitive pentru alți developeri
                """
            },
            {
                "question": "Ce este prop drilling și cum poate fi evitat?",
                "answer": """
                **Prop Drilling:**
                Situația în care props sunt transmise prin multiple nivele de componente doar pentru a ajunge la o componentă deeply nested care le folosește efectiv.

                **Probleme:**
                - Components intermediare primesc props pe care nu le folosesc
                - Refactoring devine dificil
                - Performance issues - componente inutile se re-renderează
                - Maintenance nightmare pentru aplicații mari

                **Soluții:**

                **1. React Context:**
                ```javascript
                const UserContext = createContext();
                // Provider la nivel înalt
                // Consumer la nivel jos - sare peste intermediate components
                ```

                **2. Component composition:**
                ```javascript
                // În loc să trimiți props în jos, compune componentele sus
                <Layout sidebar={<UserInfo user={user} />}>
                  <MainContent />
                </Layout>
                ```

                **3. Custom Hooks:**
                ```javascript
                // Logic shared prin hooks în loc de props
                const useUser = () => { /* fetch user logic */ };
                ```

                **4. State management libraries:**
                - Redux, Zustand, Jotai pentru global state
                - React Query pentru server state

                **Când să folosești fiecare:**
                - Context: Theme, auth, language - rare changes
                - Composition: Layout patterns, slot patterns
                - Custom hooks: Shared logic, API calls
                - State libraries: Complex global state, server state
                """
            },
            {
                "question": "Cum optimizezi performanța componentelor React?",
                "answer": """
                **1. Memoization Techniques:**
                - **React.memo()**: Previne re-renders pentru function components
                - **useMemo()**: Memoizează expensive computations
                - **useCallback()**: Memoizează functions pentru stable references
                - **PureComponent**: Pentru class components (shallow comparison)

                **2. Code Splitting:**
                - **React.lazy()**: Lazy loading pentru components
                - **Dynamic imports**: Bundle splitting la route level
                - **Suspense**: Loading states pentru lazy components

                **3. Virtualization:**
                - Pentru large lists: react-window, react-virtualized
                - Renderează doar visible items
                - Reduce DOM nodes dramatically

                **4. State Optimization:**
                - **State colocation**: Keep state close to where it's used
                - **State normalization**: Avoid nested objects/arrays
                - **Context splitting**: Multiple contexts pentru different concerns

                **5. Anti-patterns să eviți:**
                - Inline object/function creation în render
                - Mutating props or state directly
                - Missing dependency arrays în useEffect
                - Over-using Context pentru frequently changing data

                **6. Performance Monitoring:**
                - React DevTools Profiler
                - Performance API pentru measuring
                - Bundle analyzers pentru bundle size
                - Core Web Vitals tracking

                **7. Best Practices:**
                - Use production builds
                - Proper key props pentru lists
                - Debounce expensive operations
                - Error boundaries pentru graceful failures
                """
            }
        ]

        for qa in components_qa:
            with st.expander(f"❓ {qa['question']}"):
                st.markdown(qa['answer'])

    # Final summary
    st.markdown("---")
    st.markdown("""

    """, unsafe_allow_html=True)

def state_props_page():
    """State and Props"""
    st.markdown('<h1 class="chapter-header">State și Props</h1>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Props", "State"])

    with tab1:
        st.markdown('<h2 class="section-header">Props (Proprietăți)</h2>', unsafe_allow_html=True)
        # Add props content here

    with tab2:
        st.markdown('<h2 class="section-header">State (Starea)</h2>', unsafe_allow_html=True)
        # Add state content here


def events_page():
    """Event Handling"""
    st.markdown('<h1 class="chapter-header">Event Handling</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Evenimente în React</h3>
        <p>React folosește SyntheticEvents pentru comportament consistent.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add events content here


def hooks_page():
    """React Hooks"""
    st.markdown('<h1 class="chapter-header">Hooks în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Ce sunt Hooks-urile?</h3>
        <p>Hooks permit accesul la funcționalitățile React din componentele funcționale.</p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["useState", "useEffect", "useContext", "Custom Hooks"])
    # Add hooks content here


def blog_app_page():
    """Blog Application Project"""
    st.markdown('<h1 class="chapter-header">Aplicația Blog - Proiect Complet</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Ce vom construi:</h3>
        <p>O aplicație completă de blog cu funcționalități CRUD.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add blog app content here


def styling_page():
    """Styling in React"""
    st.markdown('<h1 class="chapter-header">Styling în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Modalități de stilizare în React:</h3>
        <p>React oferă multiple modalități de stilizare.</p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["CSS Clasic", "CSS Modules", "Styled Components", "Tailwind CSS"])
    # Add styling content here


def deploy_page():
    """Deployment"""
    st.markdown('<h1 class="chapter-header">Deploierea Aplicației</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Ce înseamnă deploy?</h3>
        <p>Deploy înseamnă să pui aplicația live pe internet.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add deployment content here


def glossary_page():
    """Glossary of terms"""
    st.markdown('<h1 class="chapter-header">Glosar de Termeni</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Dicționar complet al termenilor din React</h3>
        <p>Toate termenele importante cu explicații clare.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add glossary content here


def quiz_page():
    """Interactive quiz"""
    st.markdown('<h1 class="chapter-header">Quiz React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="quiz-container">
        <h2>Testează-ți cunoștințele!</h2>
        <p>Răspunde la întrebări pentru a-ți testa înțelegerea.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add quiz content here


def resources_page():
    """Additional resources"""
    st.markdown('<h1 class="chapter-header">Resurse și Legături Utile</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h2>Resurse pentru continuarea învățării</h2>
        <p>Toate resursele pentru a-ți continua călătoria în React.</p>
    </div>
    """, unsafe_allow_html=True)

    # Add resources content here


# MAIN APPLICATION
def main():
    """Main application function"""
    load_css()
    create_navigation()

    # Routing logic
    page = st.session_state.current_page

    # Page routing
    page_functions = {
        "home": home_page,
        "intro_web": intro_web_page,
        "html_css": html_css_page,
        "javascript": javascript_page,
        "intro_react": intro_react_page,
        "components": components_page,
        "state_props": state_props_page,
        "events": events_page,
        "hooks": hooks_page,
        "blog_app": blog_app_page,
        "styling": styling_page,
        "deploy": deploy_page,
        "glossary": glossary_page,
        "quiz": quiz_page,
        "resources": resources_page
    }

    # Execute the appropriate page function
    if page in page_functions:
        page_functions[page]()
    else:
        # Fallback for undefined pages
        st.markdown(f"<h1 class='chapter-header'>{page.replace('_', ' ').title()}</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div class="warning-box">
            <h3>Acest capitol este în dezvoltare!</h3>
            <p>Conținutul pentru acest capitol va fi adăugat în curând.</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
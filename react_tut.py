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
    "5.1 Componente Basic" :"components_basic",
    "5. Componente React": "components",
    "6. State și Props": "state_props",
    "7. Event Handling": "events",
    "8. Hooks React": "hooks",
    "9. Aplicația Blog": "blog_app",
    "10. Styling": "styling",
   
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

def components_basic_page():

        """React Components - Complete educational content"""
        st.markdown('<h1 class="chapter-header">Componentele React</h1>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
            <h3>Components - Building blocks ale aplicațiilor React</h3>
            <p>Componentele sunt fundamentul arhitecturii React. Ele încapsulează logica și interfața unei părți 
            specifice din aplicație, permitând reutilizarea și mentenabilitatea codului. Acest capitol acoperă 
            de la conceptele de bază până la patterns avansate folosite în aplicații enterprise de producție.</p>

            <h4>Ce vei învăța:</h4>
            <ul>
                <li><strong>Cum să construiești prima ta componentă</strong> - pas cu pas pentru începători</li>
                <li><strong>Tipurile de componente</strong> - Function vs Class Components</li>
                <li><strong>Comunicarea între componente</strong> - Props și callbacks</li>
                <li><strong>Patterns avansate</strong> - HOCs, Compound Components, Render Props</li>
                <li><strong>Performance și optimizare</strong> - React.memo, useMemo, useCallback</li>
                <li><strong>Testarea componentelor</strong> - React Testing Library</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Components Tabs
        components_tabs = st.tabs([
            "Prima ta Componentă",
            "Types & Fundamentals",

        ])

        with components_tabs[0]:
            st.markdown("### Construim prima ta componentă React - Tutorial pas cu pas")

            st.markdown("""
            Acest tutorial este destinat celor care sunt noi în React sau doresc să înțeleagă 
            în profunzime cum se construiește o componentă de la zero. Vei învăța conceptele 
            fundamentale prin practică, construind o componentă reală pas cu pas.
            """)

            st.markdown("#### Pasul 1: Înțelegem conceptul de componentă")

            st.markdown("""
            <div class="concept-highlight">
            O componentă React este o funcție JavaScript care returnează markup HTML (JSX)
            </div>

            **Analogia simplă:** O componentă este ca un șablon reutilizabil:
            - Poți să o folosești în mai multe locuri din aplicație
            - Poți să îi transmiți date diferite (proprietăți)
            - Poți să o combini cu alte componente pentru a crea interfețe complexe

            **De ce sunt importante componentele?**
            - **Reutilizabilitate:** Scrii o dată, folosești oriunde
            - **Mentenabilitate:** Modifici într-un loc, se actualizează peste tot
            - **Modularitate:** Împarți aplicația în părți mici și ușor de gestionat
            - **Testabilitate:** Poți testa fiecare componentă independent
            """, unsafe_allow_html=True)

            st.markdown("#### Pasul 2: Prima noastră componentă - Un buton simplu")

            st.code("""
    // Definim o componentă React simplă
    function MyButton() {
        // Această funcție returnează JSX (sintaxă similară HTML-ului)
        return <button>Click me</button>;
    }

    // Cum folosim componenta într-o aplicație
    function App() {
        return (
            <div>
                <h1>Aplicația mea React</h1>
                <MyButton />  {/* Folosim componenta ca un tag HTML */}
                <MyButton />  {/* O putem folosi de mai multe ori */}
                <MyButton />
            </div>
        );
    }

    // Exportăm componenta pentru a o putea folosi în alte fișiere
    export default MyButton;
            """, language="javascript")

            st.markdown("""
            **Explicația codului:**

            1. **`function MyButton()`** - Definim o funcție JavaScript cu numele componentei
            2. **`return <button>Click me</button>`** - Returnăm JSX (JavaScript XML)
            3. **JSX** - Sintaxă care arată ca HTML dar e procesată de JavaScript
            4. **`<MyButton />`** - Folosim componenta ca și cum ar fi un element HTML
            5. **`export default MyButton`** - Exportăm componenta pentru reutilizare

            **Reguli importante:**
            - Numele componentei trebuie să înceapă cu literă mare (MyButton, nu myButton)
            - O componentă poate returna doar un singur element părinte
            - JSX-ul trebuie să fie înfășurat în paranteze dacă e pe mai multe linii
            """)

            st.markdown("#### Pasul 3: Adăugăm proprietăți (Props)")

            st.markdown("""
            Props (proprietăți) sunt modalitatea prin care transmitem date către componente. 
            Ele fac componentele flexibile și reutilizabile.
            """)

            st.code("""
    // Componenta primește props ca parametru
    function MyButton(props) {
        // Accesăm proprietatea 'text' din obiectul props
        return <button>{props.text}</button>;
    }

    // Folosim componenta cu proprietăți diferite
    function App() {
        return (
            <div>
                <MyButton text="Click me" />
                <MyButton text="Submit Form" />
                <MyButton text="Cancel" />
                <MyButton text="Save Changes" />
            </div>
        );
    }

    // Varianta cu destructuring (mai elegantă)
    function MyButton({ text }) {
        // Extragem direct proprietatea 'text' din props
        return <button>{text}</button>;
    }

    // Putem avea mai multe props
    function MyButton({ text, color, size }) {
        return (
            <button 
                style={{ 
                    backgroundColor: color, 
                    fontSize: size 
                }}
            >
                {text}
            </button>
        );
    }

    // Folosire cu mai multe props
    function App() {
        return (
            <div>
                <MyButton text="Primary" color="blue" size="16px" />
                <MyButton text="Danger" color="red" size="14px" />
                <MyButton text="Success" color="green" size="18px" />
            </div>
        );
    }
            """, language="javascript")

            st.markdown("""
            **Concepte cheie despre Props:**

            - **Props sunt read-only** - nu le poți modifica în componentă
            - **Props sunt ca parametrii unei funcții** - transmit date de la părinte la copil
            - **Destructuring** - extragi proprietățile direct din obiectul props
            - **Default values** - poți seta valori implicite pentru props
            - **Props validation** - poți valida tipurile de date (cu PropTypes)

            **De ce sunt utile Props-urile:**
            - Fac componentele reutilizabile cu date diferite
            - Permit comunicarea de la componentă părinte la copil
            - Mențin componentele pure și predictibile
            """)

            st.markdown("#### Pasul 4: Adăugăm interactivitate cu evenimente")

            st.code("""
    // Componenta cu event handler
    function MyButton({ text, onClick }) {
        // onClick este o funcție primită prin props
        return (
            <button onClick={onClick}>
                {text}
            </button>
        );
    }

    // Definim funcțiile pentru evenimente în componenta părinte
    function App() {
        // Funcții care se execută la click
        const handleSaveClick = () => {
            alert('Datele au fost salvate!');
        };

        const handleDeleteClick = () => {
            if (confirm('Ești sigur că vrei să ștergi?')) {
                alert('Element șters!');
            }
        };

        const handleCancelClick = () => {
            console.log('Operația a fost anulată');
        };

        return (
            <div>
                <h1>Panoul de control</h1>
                <MyButton text="Save" onClick={handleSaveClick} />
                <MyButton text="Delete" onClick={handleDeleteClick} />
                <MyButton text="Cancel" onClick={handleCancelClick} />
            </div>
        );
    }

    // Variantă mai avansată cu parametri
    function ActionButton({ text, action, data }) {
        const handleClick = () => {
            // Transmitem data către funcția primită prin props
            action(data);
        };

        return <button onClick={handleClick}>{text}</button>;
    }

    // Folosire cu parametri
    function UserList() {
        const users = [
            { id: 1, name: 'John Doe' },
            { id: 2, name: 'Jane Smith' },
            { id: 3, name: 'Bob Johnson' }
        ];

        const handleDeleteUser = (user) => {
            console.log('Ștergem utilizatorul:', user.name);
            // Aici ar fi logica pentru ștergere
        };

        return (
            <div>
                {users.map(user => (
                    <div key={user.id}>
                        <span>{user.name}</span>
                        <ActionButton 
                            text="Delete" 
                            action={handleDeleteUser} 
                            data={user} 
                        />
                    </div>
                ))}
            </div>
        );
    }
            """, language="javascript")

            st.markdown("""
            **Concepte importante despre Events:**

            - **Event handlers** - funcții care se execută când se întâmplă ceva (click, hover, etc.)
            - **Callback props** - transmitem funcții prin props pentru a gestiona evenimente
            - **Separation of concerns** - componenta nu știe ce face, execută doar funcția primită
            - **Event delegation** - părintele gestionează logica, copilul doar declanșează evenimentul

            **Pattern-ul standard:**
            1. Definești funcția în componenta părinte
            2. O transmiți ca prop către copil
            3. Copilul o apelează când se întâmplă evenimentul
            """)

            st.markdown("#### Pasul 5: Adăugăm stare (State) componentei")

            st.markdown("""
            State-ul reprezintă datele interne ale unei componente care se pot schimba în timp. 
            Când state-ul se modifică, componenta se re-renderează automat.
            """)

            st.code("""
    import { useState } from 'react';

    // Componentă cu state intern
    function Counter() {
        // useState returnează o pereche: [valoare, funcție_de_setare]
        const [count, setCount] = useState(0);
        //      ↑         ↑            ↑
        //  valoarea  funcția    valoarea inițială
        //  curentă   setter

        // Funcții pentru modificarea state-ului
        const handleIncrement = () => {
            setCount(count + 1); // Incrementăm count-ul
        };

        const handleDecrement = () => {
            setCount(count - 1); // Decrementăm count-ul
        };

        const handleReset = () => {
            setCount(0); // Resetăm la valoarea inițială
        };

        return (
            <div>
                <h2>Counter: {count}</h2>
                <button onClick={handleIncrement}>+</button>
                <button onClick={handleDecrement}>-</button>
                <button onClick={handleReset}>Reset</button>
            </div>
        );
    }

    // Componentă cu state mai complex - un obiect
    function UserProfile() {
        const [user, setUser] = useState({
            name: '',
            email: '',
            age: 0
        });

        // Funcție pentru actualizarea unei proprietăți
        const handleNameChange = (event) => {
            setUser({
                ...user, // Păstrăm toate proprietățile existente
                name: event.target.value // Actualizăm doar name
            });
        };

        const handleEmailChange = (event) => {
            setUser({
                ...user,
                email: event.target.value
            });
        };

        // Funcție generică pentru orice proprietate
        const handleInputChange = (field) => (event) => {
            setUser({
                ...user,
                [field]: event.target.value
            });
        };

        return (
            <div>
                <h2>User Profile</h2>
                <input
                    type="text"
                    placeholder="Name"
                    value={user.name}
                    onChange={handleNameChange}
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={user.email}
                    onChange={handleEmailChange}
                />
                <input
                    type="number"
                    placeholder="Age"
                    value={user.age}
                    onChange={handleInputChange('age')}
                />

                <div>
                    <h3>Preview:</h3>
                    <p>Name: {user.name}</p>
                    <p>Email: {user.email}</p>
                    <p>Age: {user.age}</p>
                </div>
            </div>
        );
    }

    // Folosire în aplicație
    function App() {
        return (
            <div>
                <Counter />
                <hr />
                <UserProfile />
            </div>
        );
    }
            """, language="javascript")

            st.markdown("""
            **Concepte esențiale despre State:**

            - **useState hook** - funcția care ne permite să adăugăm state la componente
            - **Immutability** - nu modifici niciodată state-ul direct, ci creezi o copie nouă
            - **Re-rendering** - când state-ul se schimbă, componenta se re-desenează automat
            - **Local state** - fiecare instanță de componentă are propriul state
            - **Controlled components** - elemente de formular controlate de React state

            **Reguli importante:**
            - Nu modifica niciodată state-ul direct: `count++` (GREȘIT)
            - Folosește întotdeauna setter-ul: `setCount(count + 1)` (CORECT)
            - Pentru obiecte și array-uri, creează o copie nouă cu spread operator
            """)

            st.markdown("#### Pasul 6: Construim o componentă completă - TodoItem")

            st.code("""
    import { useState } from 'react';

    // Componentă completă pentru un element Todo
    function TodoItem({ initialText, onDelete, onToggle }) {
        // State local pentru textul elementului
        const [text, setText] = useState(initialText);
        // State pentru statusul completat/necompletat
        const [isCompleted, setIsCompleted] = useState(false);
        // State pentru modul de editare
        const [isEditing, setIsEditing] = useState(false);

        // Handler pentru salvarea textului editat
        const handleSave = () => {
            if (text.trim()) { // Verificăm că textul nu e gol
                setIsEditing(false);
            }
        };

        // Handler pentru anularea editării
        const handleCancel = () => {
            setText(initialText); // Resetăm la textul original
            setIsEditing(false);
        };

        // Handler pentru schimbarea statusului
        const handleToggleComplete = () => {
            const newStatus = !isCompleted;
            setIsCompleted(newStatus);
            onToggle(newStatus); // Informăm componenta părinte
        };

        // Handler pentru ștergere
        const handleDelete = () => {
            if (confirm('Ești sigur că vrei să ștergi acest element?')) {
                onDelete(); // Apelăm funcția primită prin props
            }
        };

        // Handler pentru tasta Enter în input
        const handleKeyPress = (event) => {
            if (event.key === 'Enter') {
                handleSave();
            } else if (event.key === 'Escape') {
                handleCancel();
            }
        };

        // Dacă suntem în modul de editare, afișăm input-ul
        if (isEditing) {
            return (
                <div className="todo-item editing">
                    <input
                        type="text"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        onKeyDown={handleKeyPress}
                        autoFocus // Focus automat pe input
                    />
                    <button onClick={handleSave} className="save-btn">
                        Save
                    </button>
                    <button onClick={handleCancel} className="cancel-btn">
                        Cancel
                    </button>
                </div>
            );
        }

        // Modul normal de afișare
        return (
            <div className={`todo-item ${isCompleted ? 'completed' : ''}`}>
                {/* Checkbox pentru completat/necompletat */}
                <input
                    type="checkbox"
                    checked={isCompleted}
                    onChange={handleToggleComplete}
                />

                {/* Textul elementului - click pentru editare */}
                <span 
                    className="todo-text"
                    onClick={() => setIsEditing(true)}
                    style={{
                        textDecoration: isCompleted ? 'line-through' : 'none',
                        color: isCompleted ? '#888' : '#000'
                    }}
                >
                    {text}
                </span>

                {/* Buton pentru ștergere */}
                <button onClick={handleDelete} className="delete-btn">
                    Delete
                </button>
            </div>
        );
    }

    // Componentă pentru lista completă de Todo-uri
    function TodoApp() {
        const [todos, setTodos] = useState([
            { id: 1, text: "Învață React" },
            { id: 2, text: "Construiește o aplicație" },
            { id: 3, text: "Deploy pe server" }
        ]);

        // Funcție pentru ștergerea unui todo
        const handleDeleteTodo = (id) => {
            setTodos(todos.filter(todo => todo.id !== id));
        };

        // Funcție pentru schimbarea statusului unui todo
        const handleToggleTodo = (id, isCompleted) => {
            console.log(`Todo ${id} is now ${isCompleted ? 'completed' : 'incomplete'}`);
            // Aici ai putea actualiza și state-ul global dacă e necesar
        };

        return (
            <div className="todo-app">
                <h1>My Todo List</h1>
                <div className="todo-list">
                    {todos.map(todo => (
                        <TodoItem
                            key={todo.id} // Key-ul e obligatoriu pentru liste
                            initialText={todo.text}
                            onDelete={() => handleDeleteTodo(todo.id)}
                            onToggle={(isCompleted) => handleToggleTodo(todo.id, isCompleted)}
                        />
                    ))}
                </div>

                {todos.length === 0 && (
                    <p className="empty-message">No todos yet. Add some!</p>
                )}
            </div>
        );
    }
            """, language="javascript")

            st.markdown("#### Pasul 7: Stilizarea componentei cu CSS")

            st.code("""
    /* styles.css */

    /* Stiluri pentru aplicația Todo */
    .todo-app {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .todo-app h1 {
        text-align: center;
        color: #333;
        margin-bottom: 30px;
    }

    /* Stiluri pentru lista de todo-uri */
    .todo-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* Stiluri pentru fiecare element todo */
    .todo-item {
        display: flex;
        align-items: center;
        padding: 15px;
        background: white;
        border: 1px solid #ddd;
        border-radius: 6px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }

    .todo-item:hover {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-1px);
    }

    /* Stiluri pentru elementul completat */
    .todo-item.completed {
        background-color: #f0f8f0;
        border-color: #c3d9c3;
    }

    /* Stiluri pentru modul de editare */
    .todo-item.editing {
        background-color: #e3f2fd;
        border-color: #90caf9;
    }

    /* Checkbox styling */
    .todo-item input[type="checkbox"] {
        margin-right: 12px;
        transform: scale(1.2);
    }

    /* Textul todo-ului */
    .todo-text {
        flex: 1;
        cursor: pointer;
        padding: 5px;
        border-radius: 3px;
        transition: background-color 0.2s ease;
    }

    .todo-text:hover {
        background-color: #f0f0f0;
    }

    /* Input pentru editare */
    .todo-item.editing input[type="text"] {
        flex: 1;
        padding: 8px;
        border: 2px solid #2196f3;
        border-radius: 4px;
        font-size: 14px;
        margin-right: 10px;
    }

    /* Butoane */
    .save-btn, .cancel-btn, .delete-btn {
        padding: 6px 12px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        transition: background-color 0.2s ease;
        margin-left: 5px;
    }

    .save-btn {
        background-color: #4caf50;
        color: white;
    }

    .save-btn:hover {
        background-color: #45a049;
    }

    .cancel-btn {
        background-color: #ff9800;
        color: white;
    }

    .cancel-btn:hover {
        background-color: #f57c00;
    }

    .delete-btn {
        background-color: #f44336;
        color: white;
    }

    .delete-btn:hover {
        background-color: #da190b;
    }

    /* Mesaj pentru lista goală */
    .empty-message {
        text-align: center;
        color: #666;
        font-style: italic;
        margin-top: 30px;
    }

    /* Responsive design */
    @media (max-width: 480px) {
        .todo-app {
            margin: 10px;
            padding: 15px;
        }

        .todo-item {
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
        }

        .todo-text {
            width: 100%;
        }
    }
            """, language="css")

            st.markdown("#### Pasul 8: Best Practices pentru început")

            st.markdown("""
            <div class="success-box">
            <h4>Practici recomandate (Do's):</h4>
            <ul>
                <li><strong>Nume descriptive pentru componente</strong> - UserProfile, TodoItem, NavigationBar</li>
                <li><strong>O responsabilitate per componentă</strong> - fiecare componentă să aibă un scop clar</li>
                <li><strong>Props pentru transmiterea datelor</strong> - păstrează componentele reutilizabile</li>
                <li><strong>State pentru datele ce se schimbă</strong> - folosește useState pentru interactivitate</li>
                <li><strong>Key prop pentru liste</strong> - întotdeauna pune key={item.id} la element</li>
                <li><strong>Comentarii în cod</strong> - explică logica complexă</li>
                <li><strong>Exportă componentele</strong> - export default ComponentName</li>
            </ul>
            </div>

            <div class="error-box">
            <h4>Greșeli de evitat (Don'ts):</h4>
            <ul>
                <li><strong>Nu modifica props-urile</strong> - sunt read-only întotdeauna</li>
                <li><strong>Nu modifica state-ul direct</strong> - folosește doar setter functions</li>
                <li><strong>Nu pune logica în JSX</strong> - extrage în funcții separate</li>
                <li><strong>Nu folosi index ca key</strong> - poate cauza bug-uri la reordonare</li>
                <li><strong>Nu amesteca stilurile inline cu CSS</strong> - alege o metodă și rămâi consistent</li>
                <li><strong>Nu uita de cleanup</strong> - elimină event listeners în componentWillUnmount</li>
                <li><strong>Nu ignora warning-urile</strong> - React îți spune când ceva nu e în regulă</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Exerciții practice pentru consolidare")

            st.markdown("""
            <div class="quiz-container">
            <h4>Challenge-uri pentru a-ți testa cunoștințele:</h4>

            <h5>Nivel Începător:</h5>
            <ul>
                <li><strong>UserCard</strong> - Componentă care afișează nume, email și avatar</li>
                <li><strong>SimpleButton</strong> - Buton cu text personalizabil și culori diferite</li>
                <li><strong>ToggleSwitch</strong> - Switch on/off cu callback la schimbare</li>
            </ul>

            <h5>Nivel Intermediar:</h5>
            <ul>
                <li><strong>SearchBox</strong> - Input cu rezultate filtrate în timp real</li>
                <li><strong>Counter cu limite</strong> - Counter cu valoare minimă și maximă</li>
                <li><strong>FormField</strong> - Input cu validare și mesaje de eroare</li>
            </ul>

            <h5>Nivel Avansat:</h5>
            <ul>
                <li><strong>Modal</strong> - Fereastră popup cu backdrop și buton de închidere</li>
                <li><strong>Tabs</strong> - Navigare între mai multe tab-uri cu conținut dinamic</li>
                <li><strong>DataTable</strong> - Tabel cu sortare și paginare</li>
            </ul>

            <p><strong>Sfat:</strong> Începe cu cea mai simplă componentă și adaugă funcționalități pas cu pas. 
            Nu încerca să faci totul dintr-o dată!</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Recapitulare concepte învățate")

            st.markdown("""
            În acest tutorial ai învățat:

            **1. Structura unei componente React**
            - Funcție care returnează JSX
            - Exportul pentru reutilizare
            - Convențiile de denumire

            **2. Props (Proprietăți)**
            - Transmiterea datelor între componente
            - Destructuring pentru cod mai curat
            - Props ca funcții pentru event handling

            **3. State (Starea)**
            - useState hook pentru stare locală
            - Immutability în actualizarea state-ului
            - Re-rendering automat la schimbări

            **4. Event Handling**
            - Callback functions prin props
            - Gestionarea evenimentelor DOM
            - Pattern-ul standard de comunicare

            **5. Styling**
            - CSS classes și inline styles
            - Stilizare condițională
            - Responsive design

            **6. Best Practices**
            - Separarea responsabilităților
            - Cod curat și comentat
            - Naming conventions

            **Următorul pas:** Continuă cu celelalte taburi pentru a învăța concepte mai avansate 
            precum lifecycle management, performance optimization și advanced patterns.
            """)

        with components_tabs[1]:
            st.markdown("### Tipuri de componente și evoluția lor")

            st.markdown("""
            React a evoluat semnificativ de-a lungul timpului, trecând de la Class Components 
            la Function Components cu hooks. Înțelegerea ambelor abordări este esențială pentru:

            **De ce să înveți ambele tipuri?**
            - **Legacy codebases** - multe aplicații existente folosesc Class Components
            - **Interviuri tehnice** - întrebări frecvente despre diferențe și migration
            - **Evoluția React** - înțelegerea istoriei și motivațiilor din spatele schimbărilor
            - **Debugging abilități** - capacitatea de a lucra cu cod existent
            - **Team collaboration** - lucrul în echipe cu codebases mixte
            """)

            st.markdown("#### Class Components - Fundamentele React vechi")

            st.markdown("""
            **Class Components** au fost modalitatea principală de a scrie componente React până în 2018.
            Deși sunt considerate legacy, înțelegerea lor rămâne crucială pentru dezvoltatorii React.

            **Caracteristici Class Components:**
            - Extind clasa React.Component
            - Folosesc metode de lifecycle
            - State gestionat prin this.state și this.setState()
            - Necesită binding pentru metodele custom
            - Mai verbose, dar foarte predictibile
            """)

            st.code("""
    import React from 'react';
    import PropTypes from 'prop-types';

    // Class Component completă cu toate funcționalitățile
    class UserProfile extends React.Component {
        constructor(props) {
            super(props);

            // Definim state-ul inițial
            this.state = {
                user: null,           // Datele utilizatorului
                loading: true,        // Status de încărcare
                error: null,          // Mesajele de eroare
                posts: [],           // Posts-urile utilizatorului
                isEditing: false,    // Mod de editare
                editData: {}         // Datele pentru editare
            };

            // Binding metodelor pentru context corect
            // Aceasta este necesară pentru că JavaScript nu bind-uiește automat 'this'
            this.handleEdit = this.handleEdit.bind(this);
            this.handleSave = this.handleSave.bind(this);
            this.handleCancel = this.handleCancel.bind(this);
        }

        // LIFECYCLE METHODS

        // 1. componentDidMount - se execută DUPĂ ce componenta a fost inserată în DOM
        componentDidMount() {
            console.log('UserProfile component mounted');

            // Aici facem operațiuni care necesită DOM sau API calls
            this.fetchUserData();
            this.setupEventListeners();

            // Focus pe primul input dacă există
            const firstInput = document.querySelector('input');
            if (firstInput) {
                firstInput.focus();
            }
        }

        // 2. componentDidUpdate - se execută după fiecare update (props sau state)
        componentDidUpdate(prevProps, prevState) {
            console.log('UserProfile component updated');

            // Re-fetch data dacă props-ul userId s-a schimbat
            if (prevProps.userId !== this.props.userId) {
                console.log('UserId changed from', prevProps.userId, 'to', this.props.userId);
                this.fetchUserData();
            }

            // Handle edit mode changes
            if (prevState.isEditing !== this.state.isEditing) {
                this.handleEditModeChange();
            }

            // Update document title când se încarcă user-ul
            if (prevState.user !== this.state.user && this.state.user) {
                document.title = `Profile: ${this.state.user.name}`;
            }
        }

        // 3. componentWillUnmount - se execută ÎNAINTE ca componenta să fie eliminată
        componentWillUnmount() {
            console.log('UserProfile component will unmount');

            // CRITICAL: Cleanup pentru a preveni memory leaks
            this.cleanupEventListeners();
            this.cancelPendingRequests();

            // Reset document title
            document.title = 'React App';

            // Clear any timers
            if (this.timeoutId) {
                clearTimeout(this.timeoutId);
            }
            if (this.intervalId) {
                clearInterval(this.intervalId);
            }
        }

        // 4. componentDidCatch - Error boundary functionality
        componentDidCatch(error, errorInfo) {
            console.error('Error caught in UserProfile:', error, errorInfo);

            // Update state pentru a afișa error UI
            this.setState({ 
                error: error.message,
                loading: false 
            });

            // Send error to monitoring service
            if (window.Sentry) {
                window.Sentry.captureException(error, {
                    contexts: { react: { componentStack: errorInfo.componentStack } }
                });
            }
        }

        // CUSTOM METHODS

        // Fetch user data from API
        fetchUserData = async () => {
            try {
                this.setState({ loading: true, error: null });

                // Simulăm call-uri API paralele
                const [userResponse, postsResponse] = await Promise.all([
                    fetch(`/api/users/${this.props.userId}`),
                    fetch(`/api/users/${this.props.userId}/posts`)
                ]);

                // Verificăm dacă response-urile sunt OK
                if (!userResponse.ok) {
                    throw new Error(`User fetch failed: ${userResponse.status}`);
                }
                if (!postsResponse.ok) {
                    throw new Error(`Posts fetch failed: ${postsResponse.status}`);
                }

                const user = await userResponse.json();
                const posts = await postsResponse.json();

                this.setState({ 
                    user, 
                    posts, 
                    loading: false,
                    editData: { ...user } // Pregătim datele pentru editare
                });

            } catch (error) {
                console.error('Fetch error:', error);
                this.setState({ 
                    error: error.message, 
                    loading: false 
                });
            }
        };

        // Event handlers - folosim arrow functions pentru auto-binding
        handleEdit = () => {
            this.setState({ 
                isEditing: true,
                editData: { ...this.state.user } // Copiem datele curente
            });
        };

        handleSave = async (formData) => {
            try {
                this.setState({ loading: true });

                const response = await fetch(`/api/users/${this.props.userId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${this.props.authToken}`
                    },
                    body: JSON.stringify(formData)
                });

                if (!response.ok) {
                    throw new Error(`Update failed: ${response.status}`);
                }

                const updatedUser = await response.json();

                this.setState({ 
                    user: updatedUser, 
                    isEditing: false,
                    loading: false,
                    editData: {}
                });

                // Callback către componenta părinte
                if (this.props.onUserUpdate) {
                    this.props.onUserUpdate(updatedUser);
                }

                // Show success message
                this.showNotification('User updated successfully!', 'success');

            } catch (error) {
                console.error('Save error:', error);
                this.setState({ 
                    error: error.message,
                    loading: false
                });
            }
        };

        handleCancel = () => {
            this.setState({ 
                isEditing: false,
                editData: {},
                error: null // Clear any errors
            });
        };

        // Helper methods
        setupEventListeners() {
            window.addEventListener('resize', this.handleResize);
            window.addEventListener('beforeunload', this.handleBeforeUnload);
        }

        cleanupEventListeners() {
            window.removeEventListener('resize', this.handleResize);
            window.removeEventListener('beforeunload', this.handleBeforeUnload);
        }

        handleResize = () => {
            // Debounce resize events pentru performance
            if (this.resizeTimeout) {
                clearTimeout(this.resizeTimeout);
            }

            this.resizeTimeout = setTimeout(() => {
                console.log('Window resized');
                // Handle responsive behavior here
                this.forceUpdate(); // Re-render pentru responsive changes
            }, 250);
        };

        handleBeforeUnload = (event) => {
            // Warn user dacă sunt schimbări nesalvate
            if (this.state.isEditing) {
                event.preventDefault();
                event.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
            }
        };

        handleEditModeChange() {
            if (this.state.isEditing) {
                // Focus primul input când intrăm în edit mode
                this.timeoutId = setTimeout(() => {
                    const firstInput = document.querySelector('.user-form input');
                    if (firstInput) {
                        firstInput.focus();
                        firstInput.select();
                    }
                }, 0);
            }
        }

        cancelPendingRequests() {
            // Cancel any pending fetch requests
            if (this.abortController) {
                this.abortController.abort();
            }
        }

        showNotification(message, type) {
            // Simple notification system
            console.log(`${type.toUpperCase()}: ${message}`);
            // În aplicații reale, ai folosi o bibliotecă de notificații
        }

        // RENDER METHOD - obligatoriu în Class Components
        render() {
            const { user, loading, error, posts, isEditing, editData } = this.state;
            const { className, onUserUpdate, ...otherProps } = this.props;

            // Early returns pentru cazuri speciale
            if (loading) {
                return (
                    <div className="user-profile-loading">
                        <div className="spinner"></div>
                        <p>Loading user profile...</p>
                    </div>
                );
            }

            if (error) {
                return (
                    <div className="user-profile-error">
                        <h3>Something went wrong</h3>
                        <p className="error-message">{error}</p>
                        <div className="error-actions">
                            <button onClick={this.fetchUserData} className="retry-btn">
                                Try Again
                            </button>
                            <button onClick={() => this.setState({ error: null })}>
                                Dismiss
                            </button>
                        </div>
                    </div>
                );
            }

            if (!user) {
                return (
                    <div className="user-profile-empty">
                        <h3>User not found</h3>
                        <p>The user with ID {this.props.userId} could not be found.</p>
                    </div>
                );
            }

            // Main render logic
            return (
                <div className={`user-profile ${className || ''}`} {...otherProps}>
                    {/* Header Section */}
                    <div className="user-profile-header">
                        <div className="user-avatar">
                            <img 
                                src={user.avatar || '/default-avatar.png'} 
                                alt={`${user.name}'s avatar`}
                                onError={(e) => {
                                    e.target.src = '/default-avatar.png';
                                }}
                            />
                            <span className={`status-indicator ${user.online ? 'online' : 'offline'}`}>
                                {user.online ? 'Online' : 'Offline'}
                            </span>
                        </div>

                        <div className="user-info">
                            {isEditing ? (
                                <UserEditForm
                                    user={editData}
                                    onSave={this.handleSave}
                                    onCancel={this.handleCancel}
                                    onChange={(field, value) => {
                                        this.setState({
                                            editData: {
                                                ...this.state.editData,
                                                [field]: value
                                            }
                                        });
                                    }}
                                />
                            ) : (
                                <div className="user-display">
                                    <h2>{user.name}</h2>
                                    <p className="user-email">{user.email}</p>
                                    <p className="user-role">{user.role}</p>
                                    <div className="user-actions">
                                        <button onClick={this.handleEdit} className="edit-btn">
                                            Edit Profile
                                        </button>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>

                    {/* Posts Section */}
                    <div className="user-posts">
                        <h3>Recent Posts ({posts.length})</h3>
                        {posts.length === 0 ? (
                            <p className="no-posts">No posts yet.</p>
                        ) : (
                            <div className="posts-list">
                                {posts.map(post => (
                                    <article key={post.id} className="post-item">
                                        <h4>{post.title}</h4>
                                        <p>{post.content}</p>
                                        <div className="post-meta">
                                            <time dateTime={post.createdAt}>
                                                {new Date(post.createdAt).toLocaleDateString()}
                                            </time>
                                            <span className="post-views">{post.views} views</span>
                                        </div>
                                    </article>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            );
        }
    }

    // PropTypes pentru type checking și documentație
    UserProfile.propTypes = {
        userId: PropTypes.string.isRequired,        // ID-ul utilizatorului (obligatoriu)
        className: PropTypes.string,                // CSS class suplimentar
        onUserUpdate: PropTypes.func,               // Callback la actualizare
        authToken: PropTypes.string                 // Token pentru autentificare
    };

    // Default props pentru valori implicite
    UserProfile.defaultProps = {
        className: '',
        onUserUpdate: null,
        authToken: ''
    };

    export default UserProfile;
            """, language="javascript")

            st.markdown("""
            **Concepte cheie în Class Components:**

            **1. Constructor și State**
            - `constructor(props)` - se execută la crearea instanței
            - `this.state = {}` - definești starea inițială
            - `this.setState()` - singura modalitate corectă de actualizare a state-ului

            **2. Lifecycle Methods**
            - `componentDidMount()` - după inserarea în DOM (pentru API calls, setup)
            - `componentDidUpdate()` - după fiecare actualizare (pentru side effects)
            - `componentWillUnmount()` - înainte de eliminare (pentru cleanup)

            **3. Method Binding**
            - `this.method = this.method.bind(this)` în constructor
            - Sau arrow functions: `method = () => {}` pentru auto-binding
            - Necesar pentru ca `this` să funcționeze în event handlers

            **4. Props și State Management**
            - `this.props` pentru accesarea proprietăților
            - `this.state` pentru starea locală
            - `prevProps` și `prevState` în componentDidUpdate pentru comparații
            """)

            st.markdown("""
            <div class="info-box">
            <h4>De ce sunt încă importante Class Components?</h4>
            <ul>
                <li><strong>Legacy code</strong> - multe aplicații existente le folosesc</li>
                <li><strong>Error boundaries</strong> - doar Class Components pot fi error boundaries</li>
                <li><strong>Interviuri</strong> - întrebări frecvente despre diferențe</li>
                <li><strong>Understanding React</strong> - înțelegerea evoluției și motivațiilor</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


def state_props_page():
    """State and Props - Tutorial Comprehensiv React"""
    st.markdown('<h1 class="chapter-header">State și Props în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-box">
    <h3>Introducere</h3>
    <p>State și Props sunt conceptele fundamentale care controlează fluxul de date în React. 
    Înțelegerea acestora este esențială pentru dezvoltarea aplicațiilor React eficiente și scalabile.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Props", "State", "State vs Props", "Cazuri Practice"])

    with tab1:
        st.markdown('<h2 class="section-header">Props (Proprietăți)</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Ce sunt Props-urile?

        Props (prescurtare pentru "properties") sunt argumentele pe care le primește o componentă React. 
        Ele permit transmiterea datelor de la o componentă părinte către o componentă copil.

        **Caracteristici cheie:**
        - Sunt **immutable** (nu pot fi modificate de componenta copil)
        - Sunt **read-only** (doar pentru citire)
        - Permit **comunicarea unidirecțională** (de la părinte la copil)
        - Pot conține orice tip de date: strings, numbers, objects, arrays, functions
        """)

        st.markdown("### Exemple Simple de Props")

        st.code("""
// Componentă simplă care primește props
function Greeting(props) {
    return <h1>Salut, {props.name}!</h1>;
}

// Utilizarea componentei cu props
function App() {
    return (
        <div>
            <Greeting name="Maria" />
            <Greeting name="Ion" />
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Destructuring Props")

        st.code("""
// Destructuring în parametrii funcției
function UserCard({ name, age, email, isActive }) {
    return (
        <div className="user-card">
            <h2>{name}</h2>
            <p>Vârsta: {age}</p>
            <p>Email: {email}</p>
            <span className={isActive ? "active" : "inactive"}>
                {isActive ? "Activ" : "Inactiv"}
            </span>
        </div>
    );
}

// Utilizare
function App() {
    return (
        <UserCard 
            name="Ana Popescu" 
            age={28} 
            email="ana@example.com" 
            isActive={true} 
        />
    );
}
        """, language="javascript")

        st.markdown("### Props cu Obiecte și Arrays")

        st.code("""
function ProductList({ products }) {
    return (
        <div>
            <h2>Lista Produse</h2>
            {products.map(product => (
                <ProductCard 
                    key={product.id}
                    product={product}
                />
            ))}
        </div>
    );
}

function ProductCard({ product }) {
    const { name, price, description, inStock } = product;

    return (
        <div className="product-card">
            <h3>{name}</h3>
            <p>{description}</p>
            <p className="price">{price} RON</p>
            <p className={inStock ? "in-stock" : "out-of-stock"}>
                {inStock ? "În stoc" : "Epuizat"}
            </p>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Props ca Funcții")

        st.code("""
function Button({ onClick, children, variant = "primary" }) {
    return (
        <button 
            className={`btn btn-${variant}`}
            onClick={onClick}
        >
            {children}
        </button>
    );
}

function App() {
    const handleSave = () => {
        console.log("Salvare efectuată!");
    };

    const handleCancel = () => {
        console.log("Operațiune anulată!");
    };

    return (
        <div>
            <Button onClick={handleSave} variant="success">
                Salvează
            </Button>
            <Button onClick={handleCancel} variant="danger">
                Anulează
            </Button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Children Prop")

        st.code("""
function Card({ title, children }) {
    return (
        <div className="card">
            <div className="card-header">
                <h3>{title}</h3>
            </div>
            <div className="card-body">
                {children}
            </div>
        </div>
    );
}

function App() {
    return (
        <Card title="Informații Utilizator">
            <p>Nume: Ion Popescu</p>
            <p>Email: ion@example.com</p>
            <button>Editează Profil</button>
        </Card>
    );
}
        """, language="javascript")

        st.markdown("### PropTypes și Validare")

        st.code("""
import PropTypes from 'prop-types';

function UserProfile({ name, age, email, hobbies, onEdit }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>Vârsta: {age}</p>
            <p>Email: {email}</p>
            <ul>
                {hobbies.map((hobby, index) => (
                    <li key={index}>{hobby}</li>
                ))}
            </ul>
            <button onClick={onEdit}>Editează</button>
        </div>
    );
}

UserProfile.propTypes = {
    name: PropTypes.string.isRequired,
    age: PropTypes.number.isRequired,
    email: PropTypes.string.isRequired,
    hobbies: PropTypes.arrayOf(PropTypes.string),
    onEdit: PropTypes.func
};

UserProfile.defaultProps = {
    hobbies: [],
    onEdit: () => {}
};
        """, language="javascript")

        st.markdown("### Props Spreading")

        st.code("""
function Input({ label, error, ...inputProps }) {
    return (
        <div className="form-group">
            <label>{label}</label>
            <input 
                {...inputProps}
                className={`form-input ${error ? 'error' : ''}`}
            />
            {error && <span className="error-text">{error}</span>}
        </div>
    );
}

function LoginForm() {
    return (
        <form>
            <Input 
                label="Email"
                type="email"
                name="email"
                placeholder="Introduceți email-ul"
                required
            />
            <Input 
                label="Parolă"
                type="password"
                name="password"
                placeholder="Introduceți parola"
                required
            />
        </form>
    );
}
        """, language="javascript")

    with tab2:
        st.markdown('<h2 class="section-header">State (Starea Componentei)</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Ce este State-ul?

        State-ul reprezintă datele private ale unei componente care se pot schimba în timpul execuției. 
        Spre deosebire de props, state-ul este **mutable** și poate fi modificat de componentă.

        **Caracteristici cheie:**
        - Este **mutable** (poate fi modificat)
        - Este **privat** componentei (nu poate fi accesat direct din exterior)
        - Modificările state-ului declanșează **re-renderarea** componentei
        - Se inițializează în componentă și se gestionează local
        """)

        st.markdown("### useState Hook - Exemplu Simplu")

        st.code("""
import React, { useState } from 'react';

function Counter() {
    // Declararea unei variabile de state numită "count"
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>Ai făcut clic de {count} ori</p>
            <button onClick={() => setCount(count + 1)}>
                Incrementează
            </button>
            <button onClick={() => setCount(count - 1)}>
                Decrementează
            </button>
            <button onClick={() => setCount(0)}>
                Resetează
            </button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### State cu Obiecte")

        st.code("""
function UserForm() {
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: ''
    });

    const handleInputChange = (event) => {
        const { name, value } = event.target;

        // Actualizarea state-ului cu spread operator
        setUser(prevUser => ({
            ...prevUser,
            [name]: value
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Date utilizator:', user);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="name"
                placeholder="Nume"
                value={user.name}
                onChange={handleInputChange}
            />
            <input
                type="email"
                name="email"
                placeholder="Email"
                value={user.email}
                onChange={handleInputChange}
            />
            <input
                type="number"
                name="age"
                placeholder="Vârsta"
                value={user.age}
                onChange={handleInputChange}
            />
            <button type="submit">Salvează</button>
        </form>
    );
}
        """, language="javascript")

        st.markdown("### State cu Arrays")

        st.code("""
function TodoList() {
    const [todos, setTodos] = useState([]);
    const [inputValue, setInputValue] = useState('');

    const addTodo = () => {
        if (inputValue.trim() !== '') {
            const newTodo = {
                id: Date.now(),
                text: inputValue,
                completed: false
            };

            setTodos(prevTodos => [...prevTodos, newTodo]);
            setInputValue('');
        }
    };

    const toggleTodo = (id) => {
        setTodos(prevTodos =>
            prevTodos.map(todo =>
                todo.id === id 
                    ? { ...todo, completed: !todo.completed }
                    : todo
            )
        );
    };

    const deleteTodo = (id) => {
        setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
    };

    return (
        <div>
            <div>
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="Adaugă o sarcină..."
                />
                <button onClick={addTodo}>Adaugă</button>
            </div>

            <ul>
                {todos.map(todo => (
                    <li key={todo.id}>
                        <span 
                            style={{ 
                                textDecoration: todo.completed ? 'line-through' : 'none' 
                            }}
                            onClick={() => toggleTodo(todo.id)}
                        >
                            {todo.text}
                        </span>
                        <button onClick={() => deleteTodo(todo.id)}>
                            Șterge
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### State Functional Updates")

        st.code("""
function AdvancedCounter() {
    const [count, setCount] = useState(0);

    // Update funcțional - recomandat pentru actualizări bazate pe starea anterioară
    const increment = () => {
        setCount(prevCount => prevCount + 1);
    };

    const incrementByAmount = (amount) => {
        setCount(prevCount => prevCount + amount);
    };

    // Multiple updates în aceeași funcție
    const multipleIncrements = () => {
        setCount(prevCount => prevCount + 1);
        setCount(prevCount => prevCount + 1);
        setCount(prevCount => prevCount + 1);
    };

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>+1</button>
            <button onClick={() => incrementByAmount(5)}>+5</button>
            <button onClick={multipleIncrements}>+3 (multiple)</button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Lifting State Up")

        st.code("""
// Componentă părinte care gestionează state-ul partajat
function ShoppingApp() {
    const [cart, setCart] = useState([]);

    const addToCart = (product) => {
        setCart(prevCart => [...prevCart, product]);
    };

    const removeFromCart = (productId) => {
        setCart(prevCart => prevCart.filter(item => item.id !== productId));
    };

    return (
        <div>
            <ProductList onAddToCart={addToCart} />
            <Cart 
                items={cart} 
                onRemoveFromCart={removeFromCart} 
            />
        </div>
    );
}

// Componentele copil primesc funcțiile prin props
function ProductList({ onAddToCart }) {
    const products = [
        { id: 1, name: "Laptop", price: 2500 },
        { id: 2, name: "Mouse", price: 50 }
    ];

    return (
        <div>
            {products.map(product => (
                <div key={product.id}>
                    <span>{product.name} - {product.price} RON</span>
                    <button onClick={() => onAddToCart(product)}>
                        Adaugă în coș
                    </button>
                </div>
            ))}
        </div>
    );
}

function Cart({ items, onRemoveFromCart }) {
    const total = items.reduce((sum, item) => sum + item.price, 0);

    return (
        <div>
            <h3>Coșul de cumpărături</h3>
            {items.map(item => (
                <div key={item.id}>
                    <span>{item.name}</span>
                    <button onClick={() => onRemoveFromCart(item.id)}>
                        Elimină
                    </button>
                </div>
            ))}
            <p>Total: {total} RON</p>
        </div>
    );
}
        """, language="javascript")

    with tab3:
        st.markdown('<h2 class="section-header">State vs Props - Diferențe și Utilizare</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Comparație State vs Props
        """)

        comparison_data = {
            "Caracteristică": [
                "Mutabilitate",
                "Proprietar",
                "Inițializare",
                "Actualizare",
                "Utilizare",
                "Declanșează re-render",
                "Accesibilitate"
            ],
            "State": [
                "Mutable (poate fi modificat)",
                "Componenta care îl definește",
                "În interiorul componentei",
                "Prin setState/useState",
                "Pentru date care se schimbă",
                "Da, când se modifică",
                "Privat componentei"
            ],
            "Props": [
                "Immutable (nu poate fi modificat)",
                "Componenta părinte",
                "Transmis de la părinte",
                "Nu poate fi actualizat direct",
                "Pentru comunicare părinte-copil",
                "Da, când se schimbă",
                "Transmis între componente"
            ]
        }

        st.table(comparison_data)

        st.markdown("### Exemple Comparative")

        st.code("""
// PROPS - Date transmise de la părinte la copil
function ParentComponent() {
    const userData = {
        name: "Maria Ionescu",
        role: "Developer"
    };

    return (
        <div>
            {/* Transmiterea datelor prin props */}
            <ChildComponent 
                userName={userData.name}
                userRole={userData.role}
                isActive={true}
            />
        </div>
    );
}

function ChildComponent({ userName, userRole, isActive }) {
    // Props sunt doar pentru citire - nu pot fi modificate
    // userName = "Alt nume"; // ❌ GREȘIT - nu modificați props-urile

    return (
        <div>
            <h2>{userName}</h2>
            <p>Rol: {userRole}</p>
            <span>{isActive ? "Activ" : "Inactiv"}</span>
        </div>
    );
}

// STATE - Date private care se pot schimba
function ComponentWithState() {
    // State poate fi modificat prin setter-ul său
    const [userName, setUserName] = useState("Maria Ionescu");
    const [isEditing, setIsEditing] = useState(false);

    const handleNameChange = (newName) => {
        setUserName(newName); // ✅ CORECT - modificarea state-ului
    };

    return (
        <div>
            {isEditing ? (
                <input 
                    value={userName}
                    onChange={(e) => handleNameChange(e.target.value)}
                />
            ) : (
                <h2>{userName}</h2>
            )}

            <button onClick={() => setIsEditing(!isEditing)}>
                {isEditing ? "Salvează" : "Editează"}
            </button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Când să folosim State vs Props")

        st.markdown("""
        **Folosește STATE când:**
        - Datele se pot schimba în timp (input-uri, contoare, toggle-uri)
        - Componenta trebuie să "își amintească" ceva
        - Vrei să declanșezi re-renderarea la schimbarea datelor
        - Datele sunt private componentei

        **Folosește PROPS când:**
        - Vrei să transmiți date de la părinte la copil
        - Datele sunt statice sau se schimbă rar
        - Vrei să configurezi comportamentul unei componente
        - Vrei să reutilizezi componenta cu date diferite
        """)

        st.code("""
// Exemplu complex care combină State și Props
function UserDashboard({ initialUser, onUserUpdate }) {
    // State pentru datele care se schimbă local
    const [user, setUser] = useState(initialUser);
    const [isEditing, setIsEditing] = useState(false);
    const [notifications, setNotifications] = useState([]);

    // Funcție care folosește și state și props
    const handleSaveUser = () => {
        setIsEditing(false);
        // Notifică componenta părinte prin props
        onUserUpdate(user);

        // Actualizează state-ul local
        setNotifications(prev => [...prev, "Profil actualizat cu succes!"]);
    };

    return (
        <div>
            <UserProfile 
                user={user}              // Props - date transmise
                isEditing={isEditing}    // Props - configurare comportament
                onUserChange={setUser}   // Props - callback function
                onSave={handleSaveUser}  // Props - callback function
            />

            <NotificationList 
                notifications={notifications}  // Props - date transmise
                onClear={() => setNotifications([])}  // Props - callback
            />
        </div>
    );
}
        """, language="javascript")

    with tab4:
        st.markdown('<h2 class="section-header">Cazuri Practice și Întrebări de Interviu</h2>', unsafe_allow_html=True)

        st.markdown("### Cazuri Practice Comune")

        with st.expander("1. Formulare Controlate vs Necontrolate"):
            st.code("""
// FORMULAR CONTROLAT (cu state)
function ControlledForm() {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        rememberMe: false
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: type === 'checkbox' ? checked : value
        }));
    };

    return (
        <form>
            <input
                name="email"
                value={formData.email}  // Controlat de state
                onChange={handleChange}
            />
            <input
                name="password"
                type="password"
                value={formData.password}  // Controlat de state
                onChange={handleChange}
            />
            <input
                name="rememberMe"
                type="checkbox"
                checked={formData.rememberMe}  // Controlat de state
                onChange={handleChange}
            />
        </form>
    );
}

// FORMULAR NECONTROLAT (cu refs)
function UncontrolledForm() {
    const emailRef = useRef();
    const passwordRef = useRef();

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(emailRef.current.value);
        console.log(passwordRef.current.value);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input ref={emailRef} name="email" />
            <input ref={passwordRef} name="password" type="password" />
        </form>
    );
}
            """, language="javascript")

        with st.expander("2. Prop Drilling și Soluții"):
            st.code("""
// PROBLEMĂ: Prop Drilling
function App() {
    const [user, setUser] = useState({ name: "Ion", theme: "dark" });

    return (
        <div>
            <Header user={user} />
            <MainContent user={user} setUser={setUser} />
            <Footer user={user} />
        </div>
    );
}

function MainContent({ user, setUser }) {
    return (
        <div>
            <Sidebar user={user} />
            <Content user={user} setUser={setUser} />
        </div>
    );
}

function Content({ user, setUser }) {
    return (
        <div>
            <UserProfile user={user} setUser={setUser} />
        </div>
    );
}

// SOLUȚIE 1: Context API
const UserContext = createContext();

function App() {
    const [user, setUser] = useState({ name: "Ion", theme: "dark" });

    return (
        <UserContext.Provider value={{ user, setUser }}>
            <div>
                <Header />
                <MainContent />
                <Footer />
            </div>
        </UserContext.Provider>
    );
}

function UserProfile() {
    const { user, setUser } = useContext(UserContext);

    return (
        <div>
            <h2>{user.name}</h2>
            <button onClick={() => setUser(prev => ({ ...prev, name: "Maria" }))}>
                Schimbă numele
            </button>
        </div>
    );
}

// SOLUȚIE 2: Custom Hook
function useUser() {
    const context = useContext(UserContext);
    if (!context) {
        throw new Error('useUser must be used within UserProvider');
    }
    return context;
}
            """, language="javascript")

        with st.expander("3. State Batching și Performance"):
            st.code("""
function OptimizedComponent() {
    const [count, setCount] = useState(0);
    const [name, setName] = useState('');
    const [items, setItems] = useState([]);

    // React 18+ - Automatic Batching
    const handleMultipleUpdates = () => {
        setCount(c => c + 1);      // \
        setName('New Name');        //  > Un singur re-render
        setItems(['item1']);       // /
    };

    // Pentru React 17 și anterior
    const handleLegacyBatching = () => {
        unstable_batchedUpdates(() => {
            setCount(c => c + 1);
            setName('New Name');
            setItems(['item1']);
        });
    };

    // Evitarea re-render-urilor inutile cu React.memo
    const ExpensiveChild = React.memo(({ data }) => {
        console.log('ExpensiveChild rendered');
        return <div>{data.value}</div>;
    });

    // State derivat - evită state-ul redundant
    const expensiveData = useMemo(() => {
        return items.map(item => ({ 
            ...item, 
            processed: item.value * 2 
        }));
    }, [items]);

    return (
        <div>
            <p>Count: {count}</p>
            <p>Name: {name}</p>
            <ExpensiveChild data={{ value: count }} />
            <button onClick={handleMultipleUpdates}>
                Update Multiple
            </button>
        </div>
    );
}
            """, language="javascript")

        st.markdown("### Întrebări Frecvente la Interviuri")

        with st.expander("Întrebarea 1: Care este diferența între state și props?"):
            st.markdown("""
            **Răspuns complet:**

            State și props sunt două concepte fundamentale pentru gestionarea datelor în React:

            **Props:**
            - Sunt immutable și read-only
            - Se transmit de la componenta părinte la componenta copil
            - Permit comunicarea unidirecțională
            - Nu pot fi modificate de componenta care le primește
            - Sunt ca argumentele unei funcții

            **State:**
            - Este mutable și poate fi modificat
            - Aparține componentei care îl definește
            - Modificările declanșează re-renderarea
            - Se gestionează local în componentă
            - Folosit pentru date care se schimbă în timp

            **Exemplu practic:** Props-urile sunt ca setările pe care le primești (culoarea unui buton), 
            iar state-ul este ca memoria componentei (dacă butonul a fost apăsat).
            """)

        with st.expander("Întrebarea 2: Cum actualizezi state-ul care depinde de valoarea anterioară?"):
            st.markdown("""
            **Răspuns:**

            Pentru actualizări care depind de state-ul anterior, folosește forma funcțională a setter-ului:

            ```javascript
            // ❌ GREȘIT - poate cauza probleme
            setCount(count + 1);

            // ✅ CORECT - folosește valoarea anterioară
            setCount(prevCount => prevCount + 1);
            ```

            **De ce este important:**
            - State-ul se actualizează asincron
            - Multiple actualizări simultane pot fi problematice
            - Forma funcțională garantează că folosești cea mai recentă valoare
            """)

        with st.expander("Întrebarea 3: Ce este prop drilling și cum îl rezolvi?"):
            st.markdown("""
            **Răspuns:**

            **Prop drilling** este procesul de transmitere a props-urilor prin multiple nivele de componente 
            pentru a ajunge la componenta care chiar le folosește.

            **Problemele:**
            - Cod greu de întreținut
            - Componente intermediare care nu folosesc props-urile
            - Dificultate în refactorizare

            **Soluții:**
            1. **Context API** - pentru state global
            2. **Component composition** - folosirea children
            3. **State management libraries** (Redux, Zustand)
            4. **Custom hooks** pentru logica reutilizabilă
            """)

        with st.expander("Întrebarea 4: Când folosești state local vs state global?"):
            st.markdown("""
            **State Local când:**
            - Datele sunt folosite doar într-o componentă
            - State-ul nu trebuie partajat
            - Logica este simplă și izolată
            - Exemple: form inputs, toggle states, local counters

            **State Global când:**
            - Datele sunt folosite în multiple componente
            - Componente îndepărtate trebuie să comunice
            - State-ul trebuie persistat între navigări
            - Exemple: user authentication, theme settings, shopping cart

            **Regula generală:** Începe cu state local și mută în global doar când este necesar.
            """)

        st.markdown("### Exerciții Practice")

        with st.expander("Exercițiul 1: Todo App Complet"):
            st.markdown("""
            Creează o aplicație Todo cu următoarele funcționalități:
            - Adăugare task-uri
            - Marcare ca complete/incomplete
            - Filtrare (toate, active, completate)
            - Șterge task-urile completate
            - Contorizare task-uri active

            **Provocări suplimentare:**
            - Persistă datele în localStorage
            - Adaugă drag & drop pentru reordonare
            - Implementează categorii pentru task-uri
            """)

        with st.expander("Exercițiul 2: Form Validation Complex"):
            st.markdown("""
            Construiește un formular de înregistrare cu:
            - Validare în timp real
            - Afișare erori specifice pentru fiecare câmp
            - Verificare strength parolă
            - Confirmare parolă
            - Checkbox pentru termeni și condiții

            **State-ul să includă:**
            - Valorile câmpurilor
            - Erorile pentru fiecare câmp
            - Status submit (loading, success, error)
            """)

        st.markdown("### Best Practices")

        st.markdown("""
        **Pentru Props:**
        1. Folosește destructuring pentru citire mai ușoară
        2. Definește PropTypes pentru validare
        3. Oferă valori default cu defaultProps
        4. Păstrează props-urile simple și focalizate
        5. Evită transmiterea de obiecte mari ca props

        **Pentru State:**
        1. Păstrează state-ul cât mai mic și focalizat
        2. Folosește multiple state variables în loc de un obiect mare
        3. Actualizează state-ul immutable
        4. Folosește functional updates pentru dependențe
        5. Consideră lifting state up când este necesar

        **General:**
        1. Preferă composition peste inheritance
        2. Folosește Context doar pentru state truly global
        3. Optimizează performance cu React.memo și useMemo
        4. Testează componentele cu diferite combinații de props și state
        """)

    st.markdown("""
    <div class="summary-box">
    <h3>Rezumat Capitol</h3>
    <p><strong>Props</strong> permit comunicarea între componente și configurarea comportamentului, 
    în timp ce <strong>State</strong> gestionează datele care se schimbă în cadrul unei componente. 
    Înțelegerea acestor concepte și a modului în care interacționează este fundamentală pentru 
    dezvoltarea aplicațiilor React eficiente și scalabile.</p>
    </div>
    """, unsafe_allow_html=True)


def events_page():
    """Event Handling - Tutorial Comprehensiv React"""
    st.markdown('<h1 class="chapter-header">Event Handling în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-box">
    <h3>Introducere</h3>
    <p>Event Handling este mecanismul prin care aplicațiile React răspund la acțiunile utilizatorului. 
    React folosește un sistem de evenimente sintetice care oferă o interfață consistentă 
    între diferite browsere și platforme.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Concepte de Bază",
        "SyntheticEvents",
        "Event Handling Avansat",
        "Performance & Optimizare",
        "Întrebări de Interviu"
    ])

    with tab1:
        st.markdown('<h2 class="section-header">Concepte Fundamentale</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Cum Funcționează Event Handling în React

        React nu atașează event listener-ii direct la elementele DOM. În schimb, folosește:
        - **Event Delegation** - Un singur listener pe root
        - **SyntheticEvents** - Wrapper peste evenimente native
        - **Event Pooling** - Reutilizarea obiectelor de evenimente (React 16 și anterior)
        """)

        st.markdown("### Exemple Simple de Event Handling")

        st.code("""
// Exemplu basic - Click Handler
function BasicButton() {
    const handleClick = () => {
        console.log('Butonul a fost apăsat!');
    };

    return (
        <button onClick={handleClick}>
            Apasă-mă
        </button>
    );
}

// Handler inline - Nu recomandat pentru logică complexă
function InlineHandler() {
    return (
        <button onClick={() => console.log('Click inline')}>
            Click Inline
        </button>
    );
}

// Handler cu parametri
function ButtonWithParams() {
    const handleClick = (message, event) => {
        console.log('Mesaj:', message);
        console.log('Event:', event);
    };

    return (
        <div>
            <button onClick={(e) => handleClick('Primul buton', e)}>
                Buton 1
            </button>
            <button onClick={(e) => handleClick('Al doilea buton', e)}>
                Buton 2
            </button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Event Handling cu State")

        st.code("""
function InteractiveForm() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    const [isSubmitting, setIsSubmitting] = useState(false);

    // Handler pentru input-uri text
    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData(prevData => ({
            ...prevData,
            [name]: value
        }));
    };

    // Handler pentru submit
    const handleSubmit = async (event) => {
        event.preventDefault(); // Previne comportamentul default
        setIsSubmitting(true);

        try {
            // Simulăm o cerere către server
            await new Promise(resolve => setTimeout(resolve, 1000));
            console.log('Date trimise:', formData);
            alert('Formular trimis cu succes!');

            // Reset formular
            setFormData({ name: '', email: '', message: '' });
        } catch (error) {
            console.error('Eroare la trimitere:', error);
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="name"
                placeholder="Numele tău"
                value={formData.name}
                onChange={handleInputChange}
                required
            />

            <input
                type="email"
                name="email"
                placeholder="Email-ul tău"
                value={formData.email}
                onChange={handleInputChange}
                required
            />

            <textarea
                name="message"
                placeholder="Mesajul tău"
                value={formData.message}
                onChange={handleInputChange}
                rows="4"
                required
            />

            <button type="submit" disabled={isSubmitting}>
                {isSubmitting ? 'Se trimite...' : 'Trimite'}
            </button>
        </form>
    );
}
        """, language="javascript")

        st.markdown("### Event Handling pentru Diferite Elemente")

        st.code("""
function EventExamples() {
    const [logs, setLogs] = useState([]);

    const addLog = (message) => {
        setLogs(prev => [...prev, `${new Date().toLocaleTimeString()}: ${message}`]);
    };

    // Mouse Events
    const handleMouseEnter = () => addLog('Mouse entered');
    const handleMouseLeave = () => addLog('Mouse left');
    const handleDoubleClick = () => addLog('Double clicked');

    // Keyboard Events
    const handleKeyDown = (event) => {
        addLog(`Key pressed: ${event.key}`);

        // Exemple de taste speciale
        if (event.key === 'Enter') {
            addLog('Enter key pressed!');
        }
        if (event.ctrlKey && event.key === 's') {
            event.preventDefault();
            addLog('Ctrl+S pressed (save shortcut)');
        }
    };

    // Focus Events
    const handleFocus = () => addLog('Input focused');
    const handleBlur = () => addLog('Input lost focus');

    // Change Events
    const handleSelectChange = (event) => {
        addLog(`Selected: ${event.target.value}`);
    };

    const handleCheckboxChange = (event) => {
        addLog(`Checkbox ${event.target.checked ? 'checked' : 'unchecked'}`);
    };

    return (
        <div>
            <div 
                onMouseEnter={handleMouseEnter}
                onMouseLeave={handleMouseLeave}
                onDoubleClick={handleDoubleClick}
                style={{
                    padding: '20px',
                    border: '2px dashed #ccc',
                    margin: '10px 0'
                }}
            >
                Zonă interactivă - hover și double-click
            </div>

            <input
                type="text"
                placeholder="Tastează ceva..."
                onKeyDown={handleKeyDown}
                onFocus={handleFocus}
                onBlur={handleBlur}
            />

            <select onChange={handleSelectChange}>
                <option value="">Selectează o opțiune</option>
                <option value="option1">Opțiunea 1</option>
                <option value="option2">Opțiunea 2</option>
                <option value="option3">Opțiunea 3</option>
            </select>

            <label>
                <input
                    type="checkbox"
                    onChange={handleCheckboxChange}
                />
                Bifează această opțiune
            </label>

            <div style={{ marginTop: '20px' }}>
                <h4>Log Evenimente:</h4>
                <div style={{ height: '200px', overflow: 'auto', border: '1px solid #ccc' }}>
                    {logs.map((log, index) => (
                        <div key={index}>{log}</div>
                    ))}
                </div>
                <button onClick={() => setLogs([])}>
                    Șterge Log-urile
                </button>
            </div>
        </div>
    );
}
        """, language="javascript")

    with tab2:
        st.markdown('<h2 class="section-header">SyntheticEvents în Detaliu</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Ce sunt SyntheticEvents?

        SyntheticEvents sunt wrapper-ele React peste evenimentele native DOM. Oferă:
        - **Cross-browser compatibility** - Același API pe toate browserele
        - **Performance optimizată** - Event pooling și delegation
        - **API consistent** - Metodele și proprietățile sunt standardizate

        ### Proprietăți Importante ale SyntheticEvents
        """)

        st.code("""
function SyntheticEventDemo() {
    const handleEvent = (syntheticEvent) => {
        console.log('=== SyntheticEvent Properties ===');

        // Proprietăți comune
        console.log('Type:', syntheticEvent.type);
        console.log('Target:', syntheticEvent.target);
        console.log('CurrentTarget:', syntheticEvent.currentTarget);
        console.log('TimeStamp:', syntheticEvent.timeStamp);

        // Verifică dacă este un MouseEvent
        if (syntheticEvent.type.startsWith('mouse')) {
            console.log('ClientX:', syntheticEvent.clientX);
            console.log('ClientY:', syntheticEvent.clientY);
            console.log('Button:', syntheticEvent.button);
            console.log('Buttons:', syntheticEvent.buttons);
        }

        // Verifică dacă este un KeyboardEvent
        if (syntheticEvent.type.startsWith('key')) {
            console.log('Key:', syntheticEvent.key);
            console.log('KeyCode:', syntheticEvent.keyCode);
            console.log('CharCode:', syntheticEvent.charCode);
            console.log('Ctrl Key:', syntheticEvent.ctrlKey);
            console.log('Shift Key:', syntheticEvent.shiftKey);
            console.log('Alt Key:', syntheticEvent.altKey);
        }

        // Accesarea evenimentului nativ
        const nativeEvent = syntheticEvent.nativeEvent;
        console.log('Native Event:', nativeEvent);

        // Metodele importante
        console.log('=== Metode Disponibile ===');
        console.log('preventDefault:', typeof syntheticEvent.preventDefault);
        console.log('stopPropagation:', typeof syntheticEvent.stopPropagation);
        console.log('persist:', typeof syntheticEvent.persist);
    };

    return (
        <div>
            <button 
                onClick={handleEvent}
                onMouseMove={handleEvent}
                onKeyDown={handleEvent}
            >
                Interacționează cu mine (vezi consola)
            </button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Event Persistence și Async Handling")

        st.code("""
function EventPersistenceDemo() {
    const [message, setMessage] = useState('');

    // ❌ PROBLEMĂ - Event pooling (React 16 și anterior)
    const handleAsyncWrong = (event) => {
        // În React 16, acest cod ar genera eroare
        setTimeout(() => {
            console.log(event.target.value); // Event pooled - eroare
        }, 1000);
    };

    // ✅ SOLUȚIE 1 - Persist event (React 16)
    const handleAsyncWithPersist = (event) => {
        event.persist(); // Previne event pooling
        setTimeout(() => {
            console.log('Persisted event:', event.target.value);
        }, 1000);
    };

    // ✅ SOLUȚIE 2 - Extract value (Recommended)
    const handleAsyncCorrect = (event) => {
        const value = event.target.value; // Extrage valoarea
        setTimeout(() => {
            console.log('Extracted value:', value);
            setMessage(`Processed: ${value}`);
        }, 1000);
    };

    // ✅ SOLUȚIE 3 - React 17+ (Nu mai e nevoie de persist)
    const handleAsyncModern = (event) => {
        // În React 17+, event pooling nu mai există
        setTimeout(() => {
            console.log('Modern handling:', event.target.value);
        }, 1000);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Tastează pentru test async..."
                onChange={handleAsyncCorrect}
            />
            <p>Status: {message}</p>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Custom Events și Event Creation")

        st.code("""
function CustomEventDemo() {
    const [eventLog, setEventLog] = useState([]);

    // Crearea și dispatch-ul unui eveniment custom
    const dispatchCustomEvent = () => {
        // Creează eveniment custom
        const customEvent = new CustomEvent('myCustomEvent', {
            detail: {
                message: 'Acesta este un eveniment custom',
                timestamp: Date.now(),
                data: { id: 1, name: 'Test Event' }
            },
            bubbles: true,
            cancelable: true
        });

        // Dispatch evenimentul
        document.dispatchEvent(customEvent);

        setEventLog(prev => [...prev, 'Custom event dispatched']);
    };

    // Listener pentru evenimentul custom
    useEffect(() => {
        const handleCustomEvent = (event) => {
            console.log('Custom event received:', event.detail);
            setEventLog(prev => [
                ...prev, 
                `Received: ${event.detail.message} at ${new Date(event.detail.timestamp).toLocaleTimeString()}`
            ]);
        };

        document.addEventListener('myCustomEvent', handleCustomEvent);

        // Cleanup
        return () => {
            document.removeEventListener('myCustomEvent', handleCustomEvent);
        };
    }, []);

    // Simularea unui eveniment de click programatic
    const triggerProgrammaticClick = () => {
        const button = document.getElementById('target-button');
        if (button) {
            button.click(); // Trigger click programmatic
        }
    };

    const handleTargetClick = () => {
        setEventLog(prev => [...prev, 'Button clicked programmatically']);
    };

    return (
        <div>
            <button onClick={dispatchCustomEvent}>
                Dispatch Custom Event
            </button>

            <button onClick={triggerProgrammaticClick}>
                Trigger Click Programmatic
            </button>

            <button 
                id="target-button" 
                onClick={handleTargetClick}
                style={{ display: 'none' }}
            >
                Target Button
            </button>

            <div style={{ marginTop: '20px' }}>
                <h4>Event Log:</h4>
                <ul>
                    {eventLog.map((log, index) => (
                        <li key={index}>{log}</li>
                    ))}
                </ul>
                <button onClick={() => setEventLog([])}>
                    Clear Log
                </button>
            </div>
        </div>
    );
}
        """, language="javascript")

    with tab3:
        st.markdown('<h2 class="section-header">Event Handling Avansat</h2>', unsafe_allow_html=True)

        st.markdown("### Event Delegation și Bubbling")

        st.code("""
function EventDelegationDemo() {
    const [clickedItem, setClickedItem] = useState(null);

    // Event delegation - Un singur handler pentru multiple elemente
    const handleContainerClick = (event) => {
        // Verifică dacă elementul target are clasa 'clickable-item'
        if (event.target.classList.contains('clickable-item')) {
            const itemId = event.target.dataset.itemId;
            const itemText = event.target.textContent;

            setClickedItem({ id: itemId, text: itemText });

            console.log('Clicked item:', { itemId, itemText });
        }
    };

    // Demonstrare event bubbling
    const handleBubblingDemo = (event, level) => {
        console.log(`Event reached ${level}`);
        // event.stopPropagation(); // Uncomment pentru a opri bubbling
    };

    return (
        <div>
            {/* Event Delegation Example */}
            <div 
                onClick={handleContainerClick}
                style={{ padding: '20px', border: '2px solid #ddd' }}
            >
                <h4>Click pe oricare item (Event Delegation):</h4>
                <div className="clickable-item" data-item-id="1">Item 1</div>
                <div className="clickable-item" data-item-id="2">Item 2</div>
                <div className="clickable-item" data-item-id="3">Item 3</div>
                <div>Item non-clickable</div>

                {clickedItem && (
                    <p>Ai ales: {clickedItem.text} (ID: {clickedItem.id})</p>
                )}
            </div>

            {/* Event Bubbling Demo */}
            <div 
                onClick={(e) => handleBubblingDemo(e, 'Container')}
                style={{ padding: '20px', border: '2px solid #f00', margin: '20px 0' }}
            >
                Container
                <div 
                    onClick={(e) => handleBubblingDemo(e, 'Middle')}
                    style={{ padding: '15px', border: '2px solid #0f0', margin: '10px' }}
                >
                    Middle
                    <button 
                        onClick={(e) => handleBubblingDemo(e, 'Button')}
                        style={{ padding: '10px' }}
                    >
                        Inner Button (vezi consola pentru bubbling)
                    </button>
                </div>
            </div>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Advanced Form Handling")

        st.code("""
function AdvancedFormHandling() {
    const [formState, setFormState] = useState({
        personalInfo: {
            firstName: '',
            lastName: '',
            email: ''
        },
        preferences: {
            newsletter: false,
            notifications: true,
            theme: 'light'
        },
        skills: []
    });

    const [errors, setErrors] = useState({});
    const [touchedFields, setTouchedFields] = useState(new Set());

    // Generic handler pentru nested objects
    const handleNestedChange = (section, field, value) => {
        setFormState(prev => ({
            ...prev,
            [section]: {
                ...prev[section],
                [field]: value
            }
        }));

        // Mark field as touched
        setTouchedFields(prev => new Set([...prev, `${section}.${field}`]));

        // Clear error when user starts typing
        if (errors[`${section}.${field}`]) {
            setErrors(prev => {
                const newErrors = { ...prev };
                delete newErrors[`${section}.${field}`];
                return newErrors;
            });
        }
    };

    // Handler pentru checkbox-uri multiple (skills)
    const handleSkillToggle = (skill) => {
        setFormState(prev => ({
            ...prev,
            skills: prev.skills.includes(skill)
                ? prev.skills.filter(s => s !== skill)
                : [...prev.skills, skill]
        }));
    };

    // Real-time validation
    const validateField = (section, field, value) => {
        const fieldKey = `${section}.${field}`;

        switch (fieldKey) {
            case 'personalInfo.email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return emailRegex.test(value) ? null : 'Email invalid';

            case 'personalInfo.firstName':
            case 'personalInfo.lastName':
                return value.length >= 2 ? null : 'Minim 2 caractere';

            default:
                return null;
        }
    };

    // Handler cu validare
    const handleValidatedChange = (event) => {
        const { name, value, type, checked } = event.target;
        const [section, field] = name.split('.');

        const actualValue = type === 'checkbox' ? checked : value;
        handleNestedChange(section, field, actualValue);

        // Validate if field is touched
        const fieldKey = `${section}.${field}`;
        if (touchedFields.has(fieldKey)) {
            const error = validateField(section, field, actualValue);
            if (error) {
                setErrors(prev => ({ ...prev, [fieldKey]: error }));
            }
        }
    };

    // Submit handler
    const handleSubmit = (event) => {
        event.preventDefault();

        // Validate all fields
        const newErrors = {};
        Object.keys(formState.personalInfo).forEach(field => {
            const error = validateField('personalInfo', field, formState.personalInfo[field]);
            if (error) {
                newErrors[`personalInfo.${field}`] = error;
            }
        });

        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
            return;
        }

        console.log('Form submitted:', formState);
    };

    // Dynamic form generation
    const renderFormField = (section, field, type = 'text', options = []) => {
        const fieldKey = `${section}.${field}`;
        const value = formState[section][field];
        const error = errors[fieldKey];
        const isTouched = touchedFields.has(fieldKey);

        const commonProps = {
            name: fieldKey,
            onChange: handleValidatedChange,
            onBlur: () => setTouchedFields(prev => new Set([...prev, fieldKey]))
        };

        switch (type) {
            case 'select':
                return (
                    <div key={fieldKey}>
                        <label>{field}:</label>
                        <select {...commonProps} value={value}>
                            {options.map(opt => (
                                <option key={opt.value} value={opt.value}>
                                    {opt.label}
                                </option>
                            ))}
                        </select>
                        {isTouched && error && <span className="error">{error}</span>}
                    </div>
                );

            case 'checkbox':
                return (
                    <div key={fieldKey}>
                        <label>
                            <input 
                                type="checkbox" 
                                {...commonProps} 
                                checked={value}
                            />
                            {field}
                        </label>
                    </div>
                );

            default:
                return (
                    <div key={fieldKey}>
                        <label>{field}:</label>
                        <input 
                            type={type} 
                            {...commonProps} 
                            value={value}
                            className={isTouched && error ? 'error' : ''}
                        />
                        {isTouched && error && <span className="error">{error}</span>}
                    </div>
                );
        }
    };

    const availableSkills = ['JavaScript', 'React', 'Node.js', 'Python', 'CSS'];

    return (
        <form onSubmit={handleSubmit}>
            <fieldset>
                <legend>Informații Personale</legend>
                {renderFormField('personalInfo', 'firstName')}
                {renderFormField('personalInfo', 'lastName')}
                {renderFormField('personalInfo', 'email', 'email')}
            </fieldset>

            <fieldset>
                <legend>Preferințe</legend>
                {renderFormField('preferences', 'newsletter', 'checkbox')}
                {renderFormField('preferences', 'notifications', 'checkbox')}
                {renderFormField('preferences', 'theme', 'select', [
                    { value: 'light', label: 'Light' },
                    { value: 'dark', label: 'Dark' },
                    { value: 'auto', label: 'Auto' }
                ])}
            </fieldset>

            <fieldset>
                <legend>Skills</legend>
                {availableSkills.map(skill => (
                    <label key={skill}>
                        <input
                            type="checkbox"
                            checked={formState.skills.includes(skill)}
                            onChange={() => handleSkillToggle(skill)}
                        />
                        {skill}
                    </label>
                ))}
            </fieldset>

            <button type="submit">Submit</button>

            <pre style={{ marginTop: '20px', fontSize: '12px' }}>
                {JSON.stringify(formState, null, 2)}
            </pre>
        </form>
    );
}
        """, language="javascript")

        st.markdown("### Drag and Drop Events")

        st.code("""
function DragDropDemo() {
    const [items, setItems] = useState([
        { id: 1, text: 'Item 1', category: 'todo' },
        { id: 2, text: 'Item 2', category: 'todo' },
        { id: 3, text: 'Item 3', category: 'todo' }
    ]);

    const [draggedItem, setDraggedItem] = useState(null);
    const [dropZones] = useState(['todo', 'inprogress', 'done']);

    // Drag events
    const handleDragStart = (event, item) => {
        setDraggedItem(item);
        event.dataTransfer.effectAllowed = 'move';
        event.dataTransfer.setData('text/html', event.target.outerHTML);
        event.dataTransfer.setData('text/plain', item.text);

        // Custom drag image
        const dragImage = event.target.cloneNode(true);
        dragImage.style.opacity = '0.8';
        dragImage.style.transform = 'rotate(5deg)';
        event.dataTransfer.setDragImage(dragImage, 0, 0);
    };

    const handleDragEnd = () => {
        setDraggedItem(null);
    };

    // Drop zone events
    const handleDragOver = (event) => {
        event.preventDefault(); // Permite drop
        event.dataTransfer.dropEffect = 'move';
    };

    const handleDragEnter = (event) => {
        event.preventDefault();
        event.target.classList.add('drag-over');
    };

    const handleDragLeave = (event) => {
        event.target.classList.remove('drag-over');
    };

    const handleDrop = (event, targetCategory) => {
        event.preventDefault();
        event.target.classList.remove('drag-over');

        if (draggedItem && draggedItem.category !== targetCategory) {
            setItems(prev => prev.map(item => 
                item.id === draggedItem.id 
                    ? { ...item, category: targetCategory }
                    : item
            ));
        }

        console.log('Dropped item:', draggedItem, 'in category:', targetCategory);
    };

    // Touch events pentru mobile support
    const handleTouchStart = (event, item) => {
        setDraggedItem(item);
    };

    const handleTouchMove = (event) => {
        event.preventDefault();
        const touch = event.touches[0];
        const elementBelow = document.elementFromPoint(touch.clientX, touch.clientY);

        // Highlight drop zones
        document.querySelectorAll('.drop-zone').forEach(zone => {
            zone.classList.remove('drag-over');
        });

        if (elementBelow && elementBelow.classList.contains('drop-zone')) {
            elementBelow.classList.add('drag-over');
        }
    };

    const handleTouchEnd = (event) => {
        const touch = event.changedTouches[0];
        const elementBelow = document.elementFromPoint(touch.clientX, touch.clientY);

        if (elementBelow && elementBelow.classList.contains('drop-zone')) {
            const category = elementBelow.dataset.category;
            handleDrop(event, category);
        }

        document.querySelectorAll('.drop-zone').forEach(zone => {
            zone.classList.remove('drag-over');
        });

        setDraggedItem(null);
    };

    return (
        <div style={{ display: 'flex', gap: '20px' }}>
            {dropZones.map(category => (
                <div
                    key={category}
                    className="drop-zone"
                    data-category={category}
                    onDragOver={handleDragOver}
                    onDragEnter={handleDragEnter}
                    onDragLeave={handleDragLeave}
                    onDrop={(e) => handleDrop(e, category)}
                    style={{
                        minHeight: '200px',
                        width: '200px',
                        border: '2px dashed #ccc',
                        padding: '10px',
                        backgroundColor: '#f9f9f9'
                    }}
                >
                    <h3>{category.toUpperCase()}</h3>
                    {items
                        .filter(item => item.category === category)
                        .map(item => (
                            <div
                                key={item.id}
                                draggable
                                onDragStart={(e) => handleDragStart(e, item)}
                                onDragEnd={handleDragEnd}
                                onTouchStart={(e) => handleTouchStart(e, item)}
                                onTouchMove={handleTouchMove}
                                onTouchEnd={handleTouchEnd}
                                style={{
                                    padding: '8px',
                                    margin: '5px 0',
                                    backgroundColor: '#fff',
                                    border: '1px solid #ddd',
                                    borderRadius: '4px',
                                    cursor: 'grab',
                                    opacity: draggedItem?.id === item.id ? 0.5 : 1
                                }}
                            >
                                {item.text}
                            </div>
                        ))
                    }
                </div>
            ))}
        </div>
    );
}
        """, language="javascript")

    with tab4:
        st.markdown('<h2 class="section-header">Performance și Optimizare</h2>', unsafe_allow_html=True)

        st.markdown("### Event Handler Optimization")

        st.code("""
// ❌ PROBLEMĂ - Handler recreat la fiecare render
function BadEventHandling() {
    const [count, setCount] = useState(0);
    const [items, setItems] = useState([]);

    return (
        <div>
            {items.map(item => (
                <button 
                    key={item.id}
                    onClick={() => {  // Funcție nouă la fiecare render
                        console.log('Clicked item:', item.id);
                        setCount(count + 1);  // Closure over stale value
                    }}
                >
                    {item.name}
                </button>
            ))}
        </div>
    );
}

// ✅ SOLUȚIE 1 - useCallback și functional updates
function OptimizedEventHandling() {
    const [count, setCount] = useState(0);
    const [items, setItems] = useState([
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' }
    ]);

    // Handler optimizat cu useCallback
    const handleItemClick = useCallback((itemId) => {
        console.log('Clicked item:', itemId);
        setCount(prevCount => prevCount + 1); // Functional update
    }, []); // Empty dependency array - funcția nu se schimbă

    return (
        <div>
            <p>Count: {count}</p>
            {items.map(item => (
                <OptimizedButton
                    key={item.id}
                    item={item}
                    onClick={handleItemClick}
                />
            ))}
        </div>
    );
}

// Component memo pentru a evita re-render-urile inutile
const OptimizedButton = React.memo(({ item, onClick }) => {
    console.log(`Rendering button for ${item.name}`);

    const handleClick = useCallback(() => {
        onClick(item.id);
    }, [item.id, onClick]);

    return (
        <button onClick={handleClick}>
            {item.name}
        </button>
    );
});

// ✅ SOLUȚIE 2 - Event delegation pentru liste mari
function EventDelegationOptimization() {
    const [items, setItems] = useState(
        Array.from({ length: 1000 }, (_, i) => ({
            id: i,
            name: `Item ${i}`,
            active: false
        }))
    );

    // Un singur event handler pentru toate item-urile
    const handleContainerClick = useCallback((event) => {
        const button = event.target.closest('button[data-item-id]');
        if (!button) return;

        const itemId = parseInt(button.dataset.itemId);
        const action = button.dataset.action;

        setItems(prevItems => prevItems.map(item => 
            item.id === itemId 
                ? { ...item, active: action === 'toggle' ? !item.active : true }
                : item
        ));
    }, []);

    return (
        <div onClick={handleContainerClick}>
            {items.slice(0, 10).map(item => (
                <div key={item.id} style={{ padding: '5px' }}>
                    <span>{item.name}</span>
                    <button 
                        data-item-id={item.id}
                        data-action="toggle"
                        style={{ 
                            marginLeft: '10px',
                            backgroundColor: item.active ? 'green' : 'gray'
                        }}
                    >
                        {item.active ? 'Active' : 'Inactive'}
                    </button>
                </div>
            ))}
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Debouncing și Throttling")

        st.code("""
// Custom hooks pentru debounce și throttle
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

function useThrottle(value, delay) {
    const [throttledValue, setThrottledValue] = useState(value);
    const lastRan = useRef(Date.now());

    useEffect(() => {
        const handler = setTimeout(() => {
            if (Date.now() - lastRan.current >= delay) {
                setThrottledValue(value);
                lastRan.current = Date.now();
            }
        }, delay - (Date.now() - lastRan.current));

        return () => {
            clearTimeout(handler);
        };
    }, [value, delay]);

    return throttledValue;
}

// Componente care folosesc debounce și throttle
function SearchWithDebounce() {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [isSearching, setIsSearching] = useState(false);

    // Debounce search term
    const debouncedSearchTerm = useDebounce(searchTerm, 500);

    // Effect pentru search
    useEffect(() => {
        if (debouncedSearchTerm) {
            setIsSearching(true);
            // Simulăm o cerere de search
            setTimeout(() => {
                const results = Array.from({ length: 5 }, (_, i) => 
                    `Result ${i + 1} for "${debouncedSearchTerm}"`
                );
                setSearchResults(results);
                setIsSearching(false);
            }, 300);
        } else {
            setSearchResults([]);
        }
    }, [debouncedSearchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Search... (debounced)"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

            {isSearching && <p>Searching...</p>}

            <ul>
                {searchResults.map((result, index) => (
                    <li key={index}>{result}</li>
                ))}
            </ul>
        </div>
    );
}

function ScrollTracker() {
    const [scrollPosition, setScrollPosition] = useState(0);
    const [throttledScrollPosition, setThrottledScrollPosition] = useState(0);

    // Handler normal (va fi apelat foarte des)
    const handleScroll = useCallback(() => {
        setScrollPosition(window.scrollY);
    }, []);

    // Handler throttled (apelat maxim o dată la 100ms)
    const handleThrottledScroll = useCallback(() => {
        setThrottledScrollPosition(window.scrollY);
    }, []);

    useEffect(() => {
        let throttleTimeout;
        const throttledHandler = () => {
            if (!throttleTimeout) {
                throttleTimeout = setTimeout(() => {
                    handleThrottledScroll();
                    throttleTimeout = null;
                }, 100);
            }
        };

        window.addEventListener('scroll', handleScroll);
        window.addEventListener('scroll', throttledHandler);

        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('scroll', throttledHandler);
            if (throttleTimeout) {
                clearTimeout(throttleTimeout);
            }
        };
    }, [handleScroll, handleThrottledScroll]);

    return (
        <div style={{ position: 'fixed', top: 0, right: 0, padding: '10px' }}>
            <div>Normal Scroll: {scrollPosition}px</div>
            <div>Throttled Scroll: {throttledScrollPosition}px</div>
        </div>
    );
}
        """, language="javascript")

    with tab5:
        st.markdown('<h2 class="section-header">Întrebări de Interviu - Event Handling</h2>', unsafe_allow_html=True)

        st.markdown("### Întrebări de Nivel Începător")

        with st.expander("1. Ce sunt SyntheticEvents în React?"):
            st.markdown("""
            **Răspuns complet:**

            SyntheticEvents sunt wrapper-ele React peste evenimentele native DOM. Ele oferă:

            **Avantaje:**
            - **Cross-browser compatibility** - Același API pe toate browserele
            - **Performance optimizată** - Prin event delegation și pooling
            - **API consistent** - Metodele și proprietățile sunt standardizate
            - **Funcționalități suplimentare** - Persist, pooling (în React 16)

            **Proprietăți importante:**
            - `event.target` - Elementul care a declanșat evenimentul
            - `event.currentTarget` - Elementul pe care este atașat handler-ul
            - `event.preventDefault()` - Previne comportamentul default
            - `event.stopPropagation()` - Oprește propagarea evenimentului
            - `event.nativeEvent` - Accesul la evenimentul nativ DOM

            **Exemplu:**
            ```javascript
            function Button({ onClick }) {
                const handleClick = (syntheticEvent) => {
                    console.log('SyntheticEvent:', syntheticEvent);
                    console.log('Native Event:', syntheticEvent.nativeEvent);
                    syntheticEvent.preventDefault();
                };

                return <button onClick={handleClick}>Click</button>;
            }
            ```
            """)

        with st.expander("2. Care este diferența între onClick și addEventListener?"):
            st.markdown("""
            **Diferențe principale:**

            **React onClick (Recomandat în React):**
            - Folosește event delegation automată
            - Handler-ii sunt atașați la nivelul root-ului
            - Cleanup automat când componenta se unmount-ează
            - Sintaxă declarativă și intuitivă
            - Integrare perfectă cu state-ul React

            **addEventListener (Imperative DOM):**
            - Atașează listener-ul direct la element
            - Necesită cleanup manual
            - Mai multă flexibilitate pentru eventi complecși
            - Folosit în useEffect pentru eventi care nu au echivalent JSX

            **Când folosești addEventListener:**
            ```javascript
            useEffect(() => {
                const handleResize = () => setWindowSize(window.innerWidth);

                window.addEventListener('resize', handleResize);

                return () => {
                    window.removeEventListener('resize', handleResize);
                };
            }, []);
            ```
            """)

        st.markdown("### Întrebări de Nivel Intermediar")

        with st.expander("3. Explică event bubbling și cum îl controlezi în React"):
            st.markdown("""
            **Event Bubbling** este procesul prin care un eveniment se propagă de la elementul target 
            către elementele părinte până la root.

            **Faze ale evenimentelor:**
            1. **Capture Phase** - De la root către target
            2. **Target Phase** - La elementul target
            3. **Bubble Phase** - De la target către root (default în React)

            **Controlul bubbling-ului:**

            ```javascript
            function BubblingDemo() {
                const handleContainer = (e) => {
                    console.log('Container clicked');
                };

                const handleButton = (e) => {
                    console.log('Button clicked');
                    e.stopPropagation(); // Oprește bubbling-ul
                };

                return (
                    <div onClick={handleContainer}>
                        <button onClick={handleButton}>
                            Click me (nu va ajunge la container)
                        </button>
                    </div>
                );
            }
            ```

            **Event Delegation cu bubbling:**
            ```javascript
            const handleListClick = (e) => {
                if (e.target.tagName === 'LI') {
                    console.log('List item clicked:', e.target.textContent);
                }
            };

            <ul onClick={handleListClick}>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
            ```
            """)

        with st.expander("4. Cum optimizezi event handler-ii pentru performance?"):
            st.markdown("""
            **Tehnici de optimizare:**

            **1. useCallback pentru handler-ii stabili:**
            ```javascript
            const handleClick = useCallback((id) => {
                setItems(prev => prev.filter(item => item.id !== id));
            }, []); // Dependencies goale = handler stabil
            ```

            **2. Event delegation pentru liste mari:**
            ```javascript
            const handleListClick = useCallback((e) => {
                const itemId = e.target.dataset.itemId;
                if (itemId) handleItemAction(itemId);
            }, []);

            <div onClick={handleListClick}>
                {items.map(item => (
                    <div key={item.id} data-item-id={item.id}>
                        {item.name}
                    </div>
                ))}
            </div>
            ```

            **3. Debouncing pentru evenimente frecvente:**
            ```javascript
            const debouncedSearch = useCallback(
                debounce((term) => performSearch(term), 300),
                []
            );
            ```

            **4. React.memo pentru componente care primesc handler-ii:**
            ```javascript
            const ListItem = React.memo(({ item, onClick }) => (
                <div onClick={() => onClick(item.id)}>
                    {item.name}
                </div>
            ));
            ```
            """)

        st.markdown("### Întrebări de Nivel Avansat")

        with st.expander("5. Explică event pooling și cum afectează handler-ii async"):
            st.markdown("""
            **Event Pooling (React 16 și anterior):**

            React reutiliza obiectele SyntheticEvent pentru performance. După ce handler-ul se executa,
            proprietățile evenimentului erau resetate.

            **Problema cu async handlers:**
            ```javascript
            // ❌ PROBLEMĂ în React 16
            const handleAsync = (event) => {
                setTimeout(() => {
                    console.log(event.target.value); // Error: pooled event
                }, 1000);
            };

            // ✅ SOLUȚIE 1: event.persist()
            const handleAsyncWithPersist = (event) => {
                event.persist(); // Previne pooling
                setTimeout(() => {
                    console.log(event.target.value); // OK
                }, 1000);
            };

            // ✅ SOLUȚIE 2: Extract values
            const handleAsyncCorrect = (event) => {
                const value = event.target.value;
                setTimeout(() => {
                    console.log(value); // OK
                }, 1000);
            };
            ```

            **React 17+ schimbări:**
            - Event pooling a fost eliminat complet
            - Nu mai e nevoie de `event.persist()`
            - Event-urile rămân accesibile în handler-ii async

            **De ce era folosit pooling-ul:**
            - Reducerea overhead-ului de creare obiecte
            - Îmbunătățirea performance-ului în aplicații mari
            - Gestionarea memoriei mai eficientă
            """)

        with st.expander("6. Cum implementezi custom event handling patterns?"):
            st.markdown("""
            **1. Custom Hook pentru Multiple Event Types:**
            ```javascript
            function useEventListener(eventName, handler, element = window) {
                const savedHandler = useRef();

                useEffect(() => {
                    savedHandler.current = handler;
                }, [handler]);

                useEffect(() => {
                    const eventListener = (event) => savedHandler.current(event);
                    element.addEventListener(eventName, eventListener);

                    return () => {
                        element.removeEventListener(eventName, eventListener);
                    };
                }, [eventName, element]);
            }

            // Usage
            function Component() {
                useEventListener('keydown', (e) => {
                    if (e.key === 'Escape') closeModal();
                });
            }
            ```

            **2. Event Bus Pattern:**
            ```javascript
            class EventBus {
                constructor() {
                    this.events = {};
                }

                on(event, callback) {
                    if (!this.events[event]) {
                        this.events[event] = [];
                    }
                    this.events[event].push(callback);
                }

                emit(event, data) {
                    if (this.events[event]) {
                        this.events[event].forEach(callback => callback(data));
                    }
                }

                off(event, callback) {
                    if (this.events[event]) {
                        this.events[event] = this.events[event].filter(cb => cb !== callback);
                    }
                }
            }

            const eventBus = new EventBus();

            // În componente
            useEffect(() => {
                const handler = (data) => console.log('Event received:', data);
                eventBus.on('customEvent', handler);

                return () => eventBus.off('customEvent', handler);
            }, []);
            ```

            **3. Gesture Handling pentru Touch:**
            ```javascript
            function useGestures(ref) {
                const [gesture, setGesture] = useState(null);

                useEffect(() => {
                    const element = ref.current;
                    let startTouch = null;

                    const handleTouchStart = (e) => {
                        startTouch = {
                            x: e.touches[0].clientX,
                            y: e.touches[0].clientY,
                            time: Date.now()
                        };
                    };

                    const handleTouchEnd = (e) => {
                        if (!startTouch) return;

                        const endTouch = {
                            x: e.changedTouches[0].clientX,
                            y: e.changedTouches[0].clientY,
                            time: Date.now()
                        };

                        const deltaX = endTouch.x - startTouch.x;
                        const deltaY = endTouch.y - startTouch.y;
                        const deltaTime = endTouch.time - startTouch.time;

                        if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > 50) {
                            setGesture({
                                type: 'swipe',
                                direction: deltaX > 0 ? 'right' : 'left',
                                velocity: Math.abs(deltaX) / deltaTime
                            });
                        }
                    };

                    element.addEventListener('touchstart', handleTouchStart);
                    element.addEventListener('touchend', handleTouchEnd);

                    return () => {
                        element.removeEventListener('touchstart', handleTouchStart);
                        element.removeEventListener('touchend', handleTouchEnd);
                    };
                }, []);

                return gesture;
            }
            ```
            """)

        st.markdown("### Exerciții Practice Avansate")

        with st.expander("Exercițiul 1: Modal System cu Keyboard Navigation"):
            st.markdown("""
            **Cerințe:**
            - Modal care se deschide/închide cu Escape
            - Tab navigation care rămâne în modal
            - Focus management automat
            - Click outside pentru închidere
            - Support pentru multiple modals (stacking)

            **Provocări suplimentare:**
            - Animații pentru deschidere/închidere
            - Prevent scroll pe body când modal e deschis
            - ARIA attributes pentru accessibility
            - Portal rendering pentru z-index management
            """)

        with st.expander("Exercițiul 2: Advanced Data Grid cu Event Handling"):
            st.markdown("""
            **Funcționalități:**
            - Click pentru selectare row/cell
            - Drag pentru selectare multiple
            - Keyboard navigation (arrow keys)
            - Right-click pentru context menu
            - Double-click pentru editare inline
            - Drag & drop pentru reordonare coloane

            **Event handling complex:**
            - Multiple event types pe același element
            - Event delegation pentru performance
            - State management pentru selectii
            - Optimization pentru liste mari (virtualization)
            """)

        st.markdown("### Best Practices - Event Handling")

        st.markdown("""
        **Performance:**
        1. Folosește `useCallback` pentru handler-ii care se transmit ca props
        2. Implementează event delegation pentru liste mari
        3. Debounce/throttle evenimentele frecvente (scroll, resize, input)
        4. Evită crearea de funcții inline în JSX pentru componente mari

        **Memory Management:**
        1. Cleanup event listener-ii în useEffect
        2. Folosește weak references pentru circular dependencies
        3. Evită closure-urile care capturează obiecte mari
        4. Remove handler-ii când componentele se unmount

        **Accessibility:**
        1. Suportă atât mouse cât și keyboard events
        2. Implementează ARIA attributes corespunzător
        3. Oferă feedback vizual pentru interacțiuni
        4. Testează cu screen readers

        **Security:**
        1. Sanitizează input-urile din evenimente
        2. Validează date-le pe client și server
        3. Evită eval() sau innerHTML cu date de la utilizatori
        4. Implementează rate limiting pentru evenimente critice
        """)

    st.markdown("""
    <div class="summary-box">
    <h3>Rezumat Capitol</h3>
    <p><strong>Event Handling</strong> în React combină puterea evenimentelor native DOM cu 
    optimizările și abstractizările React. Înțelegerea SyntheticEvents, event delegation, 
    și tehnicilor de optimizare este esențială pentru construirea aplicațiilor React 
    performante și interactive. Practică cu exemple reale și testează diferite scenarii 
    pentru a stăpâni complet acest concept fundamental.</p>
    </div>
    """, unsafe_allow_html=True)


def hooks_page():
    """React Hooks - Tutorial Comprehensiv"""
    st.markdown('<h1 class="chapter-header">React Hooks - Completul Ghid</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-box">
    <h3>Introducere în React Hooks</h3>
    <p>Hooks au revoluționat React prin permiterea folosirii state-ului și a lifecycle methods-urilor 
    în functional components. Introduse în React 16.8, Hooks oferă o modalitate mai elegantă și 
    flexibilă de a scrie componente React.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Hooks de Bază",
        "Built-in Hooks",
        "Custom Hooks",
        "Hooks Avansați",
        "Patterns & Best Practices",
        "Întrebări de Interviu"
    ])

    with tab1:
        st.markdown('<h2 class="section-header">Hooks Fundamentali</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Regulile Hooks-urilor

        **Reguli obligatorii:**
        1. Hooks se apelează DOAR la nivelul superior (nu în loop-uri, condiții sau funcții nested)
        2. Hooks se folosesc DOAR în React functional components sau custom hooks
        3. Ordinea apelării hooks-urilor trebuie să fie consistentă între render-uri

        **De ce aceste reguli:**
        - React se bazează pe ordinea apelării pentru a asocia state-ul cu hooks-urile
        - Ordinea inconsistentă poate cauza bug-uri subtile și hard-to-debug
        """)

        st.markdown("### useState - Gestionarea State-ului Local")

        st.code("""
import React, { useState } from 'react';

// Exemplu simplu - Counter
function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>+</button>
            <button onClick={() => setCount(count - 1)}>-</button>
            <button onClick={() => setCount(0)}>Reset</button>
        </div>
    );
}

// State cu obiecte - Form handling
function UserForm() {
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: 0
    });

    const [errors, setErrors] = useState({});

    const handleInputChange = (field, value) => {
        // Actualizare corectă cu spread operator
        setUser(prevUser => ({
            ...prevUser,
            [field]: value
        }));

        // Clear error când user tastează
        if (errors[field]) {
            setErrors(prevErrors => ({
                ...prevErrors,
                [field]: null
            }));
        }
    };

    const validateForm = () => {
        const newErrors = {};

        if (!user.name.trim()) {
            newErrors.name = 'Numele este obligatoriu';
        }

        if (!user.email.includes('@')) {
            newErrors.email = 'Email invalid';
        }

        if (user.age < 18) {
            newErrors.age = 'Vârsta minimă este 18 ani';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            console.log('Form valid:', user);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <input
                    type="text"
                    placeholder="Nume"
                    value={user.name}
                    onChange={(e) => handleInputChange('name', e.target.value)}
                />
                {errors.name && <span className="error">{errors.name}</span>}
            </div>

            <div>
                <input
                    type="email"
                    placeholder="Email"
                    value={user.email}
                    onChange={(e) => handleInputChange('email', e.target.value)}
                />
                {errors.email && <span className="error">{errors.email}</span>}
            </div>

            <div>
                <input
                    type="number"
                    placeholder="Vârsta"
                    value={user.age}
                    onChange={(e) => handleInputChange('age', parseInt(e.target.value))}
                />
                {errors.age && <span className="error">{errors.age}</span>}
            </div>

            <button type="submit">Trimite</button>
        </form>
    );
}

// State cu arrays - Todo List
function TodoList() {
    const [todos, setTodos] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [filter, setFilter] = useState('all'); // all, active, completed

    const addTodo = () => {
        if (inputValue.trim()) {
            const newTodo = {
                id: Date.now(),
                text: inputValue.trim(),
                completed: false,
                createdAt: new Date()
            };

            setTodos(prevTodos => [...prevTodos, newTodo]);
            setInputValue('');
        }
    };

    const toggleTodo = (id) => {
        setTodos(prevTodos =>
            prevTodos.map(todo =>
                todo.id === id 
                    ? { ...todo, completed: !todo.completed }
                    : todo
            )
        );
    };

    const deleteTodo = (id) => {
        setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
    };

    const clearCompleted = () => {
        setTodos(prevTodos => prevTodos.filter(todo => !todo.completed));
    };

    // Computed values
    const filteredTodos = todos.filter(todo => {
        if (filter === 'active') return !todo.completed;
        if (filter === 'completed') return todo.completed;
        return true;
    });

    const activeCount = todos.filter(todo => !todo.completed).length;
    const completedCount = todos.length - activeCount;

    return (
        <div>
            <div>
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && addTodo()}
                    placeholder="Adaugă o sarcină..."
                />
                <button onClick={addTodo}>Adaugă</button>
            </div>

            <div>
                <button 
                    onClick={() => setFilter('all')}
                    className={filter === 'all' ? 'active' : ''}
                >
                    Toate ({todos.length})
                </button>
                <button 
                    onClick={() => setFilter('active')}
                    className={filter === 'active' ? 'active' : ''}
                >
                    Active ({activeCount})
                </button>
                <button 
                    onClick={() => setFilter('completed')}
                    className={filter === 'completed' ? 'active' : ''}
                >
                    Completate ({completedCount})
                </button>
            </div>

            <ul>
                {filteredTodos.map(todo => (
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
                        <button onClick={() => deleteTodo(todo.id)}>Șterge</button>
                    </li>
                ))}
            </ul>

            {completedCount > 0 && (
                <button onClick={clearCompleted}>
                    Șterge Completate ({completedCount})
                </button>
            )}
        </div>
    );
}
        """, language="javascript")

        st.markdown("### useEffect - Side Effects și Lifecycle")

        st.code("""
// Exemplu 1: Effect fără dependencies - rulează după fiecare render
function ComponentWithEffect() {
    const [count, setCount] = useState(0);

    // ❌ Rulează după fiecare render - poate cauza probleme de performance
    useEffect(() => {
        console.log('Component rendered, count is:', count);
        document.title = `Count: ${count}`;
    });

    return (
        <div>
            <p>{count}</p>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}

// Exemplu 2: Effect cu dependencies - rulează doar când se schimbă dependencies
function TimerComponent() {
    const [seconds, setSeconds] = useState(0);
    const [isRunning, setIsRunning] = useState(false);

    useEffect(() => {
        let interval = null;

        if (isRunning) {
            interval = setInterval(() => {
                setSeconds(prevSeconds => prevSeconds + 1);
            }, 1000);
        }

        // Cleanup function - foarte important!
        return () => {
            if (interval) {
                clearInterval(interval);
            }
        };
    }, [isRunning]); // Rulează doar când isRunning se schimbă

    const handleStart = () => setIsRunning(true);
    const handleStop = () => setIsRunning(false);
    const handleReset = () => {
        setSeconds(0);
        setIsRunning(false);
    };

    return (
        <div>
            <h2>Timer: {seconds}s</h2>
            <button onClick={handleStart} disabled={isRunning}>Start</button>
            <button onClick={handleStop} disabled={!isRunning}>Stop</button>
            <button onClick={handleReset}>Reset</button>
        </div>
    );
}

// Exemplu 3: Effect cu cleanup pentru event listeners
function WindowSizeTracker() {
    const [windowSize, setWindowSize] = useState({
        width: window.innerWidth,
        height: window.innerHeight
    });

    useEffect(() => {
        const handleResize = () => {
            setWindowSize({
                width: window.innerWidth,
                height: window.innerHeight
            });
        };

        // Add event listener
        window.addEventListener('resize', handleResize);

        // Cleanup function
        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []); // Empty dependency array - rulează doar la mount/unmount

    return (
        <div>
            <p>Window size: {windowSize.width} x {windowSize.height}</p>
        </div>
    );
}

// Exemplu 4: Data fetching cu useEffect
function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Reset state când userId se schimbă
        setLoading(true);
        setError(null);
        setUser(null);

        // Simulare API call
        const fetchUser = async () => {
            try {
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
    }, [userId]); // Rulează când userId se schimbă

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    if (!user) return <div>User not found</div>;

    return (
        <div>
            <h2>{user.name}</h2>
            <p>Email: {user.email}</p>
            <p>Joined: {new Date(user.joinDate).toLocaleDateString()}</p>
        </div>
    );
}

// Exemplu 5: Multiple effects pentru separarea concerns
function Dashboard() {
    const [user, setUser] = useState(null);
    const [notifications, setNotifications] = useState([]);
    const [onlineStatus, setOnlineStatus] = useState(navigator.onLine);

    // Effect 1: Fetch user data
    useEffect(() => {
        fetchUserData().then(setUser);
    }, []);

    // Effect 2: Setup notifications
    useEffect(() => {
        const unsubscribe = subscribeToNotifications((notification) => {
            setNotifications(prev => [...prev, notification]);
        });

        return unsubscribe;
    }, []);

    // Effect 3: Track online status
    useEffect(() => {
        const handleOnline = () => setOnlineStatus(true);
        const handleOffline = () => setOnlineStatus(false);

        window.addEventListener('online', handleOnline);
        window.addEventListener('offline', handleOffline);

        return () => {
            window.removeEventListener('online', handleOnline);
            window.removeEventListener('offline', handleOffline);
        };
    }, []);

    return (
        <div>
            <div className={`status ${onlineStatus ? 'online' : 'offline'}`}>
                {onlineStatus ? 'Online' : 'Offline'}
            </div>

            {user && (
                <div>
                    <h1>Welcome, {user.name}!</h1>
                    <p>You have {notifications.length} notifications</p>
                </div>
            )}
        </div>
    );
}
        """, language="javascript")

    with tab2:
        st.markdown('<h2 class="section-header">Built-in Hooks Avansați</h2>', unsafe_allow_html=True)

        st.markdown("### useContext - Gestionarea State-ului Global")

        st.code("""
// 1. Crearea Context-ului
const ThemeContext = createContext();
const UserContext = createContext();

// 2. Provider Component
function AppProvider({ children }) {
    const [theme, setTheme] = useState('light');
    const [user, setUser] = useState(null);

    const toggleTheme = () => {
        setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
    };

    const login = (userData) => {
        setUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('user');
    };

    // Load user from localStorage on mount
    useEffect(() => {
        const savedUser = localStorage.getItem('user');
        if (savedUser) {
            setUser(JSON.parse(savedUser));
        }
    }, []);

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            <UserContext.Provider value={{ user, login, logout }}>
                <div className={`app-container ${theme}`}>
                    {children}
                </div>
            </UserContext.Provider>
        </ThemeContext.Provider>
    );
}

// 3. Custom hooks pentru ușurința utilizării
function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within a ThemeProvider');
    }
    return context;
}

function useUser() {
    const context = useContext(UserContext);
    if (!context) {
        throw new Error('useUser must be used within a UserProvider');
    }
    return context;
}

// 4. Componente care folosesc context
function Header() {
    const { theme, toggleTheme } = useTheme();
    const { user, logout } = useUser();

    return (
        <header className="header">
            <h1>My App</h1>

            <div className="header-controls">
                <button onClick={toggleTheme}>
                    Switch to {theme === 'light' ? 'dark' : 'light'} mode
                </button>

                {user ? (
                    <div>
                        <span>Welcome, {user.name}!</span>
                        <button onClick={logout}>Logout</button>
                    </div>
                ) : (
                    <LoginButton />
                )}
            </div>
        </header>
    );
}

function LoginButton() {
    const { login } = useUser();

    const handleLogin = () => {
        // Simulare login
        const userData = {
            id: 1,
            name: 'John Doe',
            email: 'john@example.com'
        };
        login(userData);
    };

    return <button onClick={handleLogin}>Login</button>;
}

// 5. App principală
function App() {
    return (
        <AppProvider>
            <Header />
            <MainContent />
        </AppProvider>
    );
}
        """, language="javascript")

        st.markdown("### useReducer - State Management Complex")

        st.code("""
// 1. Definirea action types și reducer-ului
const ACTION_TYPES = {
    ADD_ITEM: 'ADD_ITEM',
    REMOVE_ITEM: 'REMOVE_ITEM',
    UPDATE_QUANTITY: 'UPDATE_QUANTITY',
    CLEAR_CART: 'CLEAR_CART',
    APPLY_DISCOUNT: 'APPLY_DISCOUNT',
    SET_SHIPPING: 'SET_SHIPPING'
};

function cartReducer(state, action) {
    switch (action.type) {
        case ACTION_TYPES.ADD_ITEM: {
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
        }

        case ACTION_TYPES.REMOVE_ITEM:
            return {
                ...state,
                items: state.items.filter(item => item.id !== action.payload)
            };

        case ACTION_TYPES.UPDATE_QUANTITY:
            return {
                ...state,
                items: state.items.map(item =>
                    item.id === action.payload.id
                        ? { ...item, quantity: action.payload.quantity }
                        : item
                ).filter(item => item.quantity > 0)
            };

        case ACTION_TYPES.CLEAR_CART:
            return {
                ...state,
                items: [],
                discount: 0
            };

        case ACTION_TYPES.APPLY_DISCOUNT:
            return {
                ...state,
                discount: action.payload
            };

        case ACTION_TYPES.SET_SHIPPING:
            return {
                ...state,
                shipping: action.payload
            };

        default:
            throw new Error(`Unknown action type: ${action.type}`);
    }
}

// 2. Starea inițială
const initialCartState = {
    items: [],
    discount: 0,
    shipping: 0
};

// 3. Shopping Cart Component
function ShoppingCart() {
    const [cartState, dispatch] = useReducer(cartReducer, initialCartState);

    // Computed values
    const subtotal = cartState.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const discountAmount = subtotal * (cartState.discount / 100);
    const total = subtotal - discountAmount + cartState.shipping;
    const itemCount = cartState.items.reduce((sum, item) => sum + item.quantity, 0);

    // Action creators
    const addItem = (product) => {
        dispatch({
            type: ACTION_TYPES.ADD_ITEM,
            payload: product
        });
    };

    const removeItem = (itemId) => {
        dispatch({
            type: ACTION_TYPES.REMOVE_ITEM,
            payload: itemId
        });
    };

    const updateQuantity = (itemId, quantity) => {
        dispatch({
            type: ACTION_TYPES.UPDATE_QUANTITY,
            payload: { id: itemId, quantity }
        });
    };

    const applyDiscount = (percentage) => {
        dispatch({
            type: ACTION_TYPES.APPLY_DISCOUNT,
            payload: percentage
        });
    };

    const clearCart = () => {
        dispatch({ type: ACTION_TYPES.CLEAR_CART });
    };

    return (
        <div className="shopping-cart">
            <h2>Shopping Cart ({itemCount} items)</h2>

            {cartState.items.length === 0 ? (
                <p>Your cart is empty</p>
            ) : (
                <>
                    <div className="cart-items">
                        {cartState.items.map(item => (
                            <div key={item.id} className="cart-item">
                                <h4>{item.name}</h4>
                                <p>Price: ${item.price}</p>
                                <div className="quantity-controls">
                                    <button 
                                        onClick={() => updateQuantity(item.id, item.quantity - 1)}
                                    >
                                        -
                                    </button>
                                    <span>Quantity: {item.quantity}</span>
                                    <button 
                                        onClick={() => updateQuantity(item.id, item.quantity + 1)}
                                    >
                                        +
                                    </button>
                                </div>
                                <button onClick={() => removeItem(item.id)}>
                                    Remove Item
                                </button>
                                <p>Subtotal: ${item.price * item.quantity}</p>
                            </div>
                        ))}
                    </div>

                    <div className="cart-summary">
                        <p>Subtotal: ${subtotal.toFixed(2)}</p>
                        {cartState.discount > 0 && (
                            <p>Discount ({cartState.discount}%): -${discountAmount.toFixed(2)}</p>
                        )}
                        <p>Shipping: ${cartState.shipping}</p>
                        <h3>Total: ${total.toFixed(2)}</h3>

                        <div className="cart-actions">
                            <button onClick={() => applyDiscount(10)}>
                                Apply 10% Discount
                            </button>
                            <button onClick={clearCart}>Clear Cart</button>
                        </div>
                    </div>
                </>
            )}

            <ProductList onAddToCart={addItem} />
        </div>
    );
}

// 4. Exemplu de folosire a useReducer pentru form complex
const formReducer = (state, action) => {
    switch (action.type) {
        case 'SET_FIELD':
            return {
                ...state,
                fields: {
                    ...state.fields,
                    [action.field]: action.value
                },
                errors: {
                    ...state.errors,
                    [action.field]: null // Clear error când user tastează
                }
            };

        case 'SET_ERRORS':
            return {
                ...state,
                errors: action.errors
            };

        case 'SET_LOADING':
            return {
                ...state,
                isLoading: action.isLoading
            };

        case 'RESET_FORM':
            return action.initialState;

        default:
            return state;
    }
};

function ComplexForm() {
    const initialState = {
        fields: {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
            confirmPassword: '',
            terms: false
        },
        errors: {},
        isLoading: false
    };

    const [formState, dispatch] = useReducer(formReducer, initialState);

    const setField = (field, value) => {
        dispatch({ type: 'SET_FIELD', field, value });
    };

    const validateForm = () => {
        const errors = {};
        const { fields } = formState;

        if (!fields.firstName.trim()) errors.firstName = 'First name is required';
        if (!fields.lastName.trim()) errors.lastName = 'Last name is required';
        if (!fields.email.includes('@')) errors.email = 'Invalid email';
        if (fields.password.length < 6) errors.password = 'Password must be at least 6 characters';
        if (fields.password !== fields.confirmPassword) errors.confirmPassword = 'Passwords do not match';
        if (!fields.terms) errors.terms = 'You must accept the terms';

        dispatch({ type: 'SET_ERRORS', errors });
        return Object.keys(errors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!validateForm()) return;

        dispatch({ type: 'SET_LOADING', isLoading: true });

        try {
            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 2000));
            alert('Form submitted successfully!');
            dispatch({ type: 'RESET_FORM', initialState });
        } catch (error) {
            dispatch({ 
                type: 'SET_ERRORS', 
                errors: { submit: 'Submission failed. Please try again.' }
            });
        } finally {
            dispatch({ type: 'SET_LOADING', isLoading: false });
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Form fields implementation */}
            <input
                type="text"
                placeholder="First Name"
                value={formState.fields.firstName}
                onChange={(e) => setField('firstName', e.target.value)}
            />
            {formState.errors.firstName && <span className="error">{formState.errors.firstName}</span>}

            {/* Additional form fields... */}

            <button type="submit" disabled={formState.isLoading}>
                {formState.isLoading ? 'Submitting...' : 'Submit'}
            </button>
        </form>
    );
}
        """, language="javascript")

        st.markdown("### useMemo și useCallback - Optimizarea Performance-ului")

        st.code("""
// useMemo - Pentru expensive calculations
function ExpensiveComponent({ items, filter }) {
    // ❌ FĂRĂ useMemo - calculul se face la fiecare render
    const expensiveCalculation = items
        .filter(item => item.category === filter)
        .map(item => ({
            ...item,
            processedData: heavyProcessing(item)
        }))
        .sort((a, b) => a.score - b.score);

    // ✅ CU useMemo - calculul se face doar când dependencies se schimbă
    const optimizedCalculation = useMemo(() => {
        console.log('Performing expensive calculation...');
        return items
            .filter(item => item.category === filter)
            .map(item => ({
                ...item,
                processedData: heavyProcessing(item)
            }))
            .sort((a, b) => a.score - b.score);
    }, [items, filter]); // Se recalculeaza doar când items sau filter se schimbă

    return (
        <div>
            {optimizedCalculation.map(item => (
                <div key={item.id}>{item.name}</div>
            ))}
        </div>
    );
}

// useCallback - Pentru optimizarea handler-ilor
function ParentComponent({ users }) {
    const [selectedUsers, setSelectedUsers] = useState(new Set());
    const [searchTerm, setSearchTerm] = useState('');

    // ❌ FĂRĂ useCallback - funcția se recrează la fiecare render
    const handleUserSelectBad = (userId) => {
        setSelectedUsers(prev => {
            const newSet = new Set(prev);
            if (newSet.has(userId)) {
                newSet.delete(userId);
            } else {
                newSet.add(userId);
            }
            return newSet;
        });
    };

    // ✅ CU useCallback - funcția se recrează doar când este necesar
    const handleUserSelect = useCallback((userId) => {
        setSelectedUsers(prev => {
            const newSet = new Set(prev);
            if (newSet.has(userId)) {
                newSet.delete(userId);
            } else {
                newSet.add(userId);
            }
            return newSet;
        });
    }, []); // Empty dependencies - funcția nu se schimbă niciodată

    // Handler cu dependencies
    const handleUserAction = useCallback((userId, action) => {
        console.log(`Performing ${action} on user ${userId}`);
        // Logic specific pentru action
        if (action === 'delete') {
            // Remove from selected users
            setSelectedUsers(prev => {
                const newSet = new Set(prev);
                newSet.delete(userId);
                return newSet;
            });
        }
    }, []);

    // Filtered users cu useMemo
    const filteredUsers = useMemo(() => {
        return users.filter(user => 
            user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.email.toLowerCase().includes(searchTerm.toLowerCase())
        );
    }, [users, searchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Search users..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

            <p>Selected: {selectedUsers.size} users</p>

            <div>
                {filteredUsers.map(user => (
                    <UserCard
                        key={user.id}
                        user={user}
                        isSelected={selectedUsers.has(user.id)}
                        onSelect={handleUserSelect}
                        onAction={handleUserAction}
                    />
                ))}
            </div>
        </div>
    );
}

// Component optimizat cu React.memo
const UserCard = React.memo(({ user, isSelected, onSelect, onAction }) => {
    console.log(`Rendering UserCard for ${user.name}`);

    return (
        <div className={`user-card ${isSelected ? 'selected' : ''}`}>
            <h3>{user.name}</h3>
            <p>{user.email}</p>

            <button onClick={() => onSelect(user.id)}>
                {isSelected ? 'Deselect' : 'Select'}
            </button>

            <button onClick={() => onAction(user.id, 'edit')}>
                Edit
            </button>

            <button onClick={() => onAction(user.id, 'delete')}>
                Delete
            </button>
        </div>
    );
});

// Exemplu complex cu multiple optimizări
function DataVisualization({ rawData }) {
    const [chartType, setChartType] = useState('bar');
    const [dateRange, setDateRange] = useState({ start: null, end: null });
    const [selectedMetrics, setSelectedMetrics] = useState(new Set(['revenue']));

    // Expensive data processing cu useMemo
    const processedData = useMemo(() => {
        console.log('Processing data for visualization...');

        let filtered = rawData;

        // Filter by date range
        if (dateRange.start && dateRange.end) {
            filtered = filtered.filter(item => {
                const itemDate = new Date(item.date);
                return itemDate >= dateRange.start && itemDate <= dateRange.end;
            });
        }

        // Group and aggregate data
        const grouped = filtered.reduce((acc, item) => {
            const key = item.category;
            if (!acc[key]) {
                acc[key] = { category: key, revenue: 0, orders: 0, users: 0 };
            }
            acc[key].revenue += item.revenue;
            acc[key].orders += item.orders;
            acc[key].users += item.users;
            return acc;
        }, {});

        return Object.values(grouped);
    }, [rawData, dateRange]);

    // Chart configuration cu useMemo
    const chartConfig = useMemo(() => {
        console.log('Building chart configuration...');

        return {
            type: chartType,
            data: processedData,
            metrics: Array.from(selectedMetrics),
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    tooltip: { enabled: true }
                }
            }
        };
    }, [chartType, processedData, selectedMetrics]);

    // Event handlers cu useCallback
    const handleChartTypeChange = useCallback((type) => {
        setChartType(type);
    }, []);

    const handleMetricToggle = useCallback((metric) => {
        setSelectedMetrics(prev => {
            const newSet = new Set(prev);
            if (newSet.has(metric)) {
                newSet.delete(metric);
            } else {
                newSet.add(metric);
            }
            return newSet;
        });
    }, []);

    const handleDateRangeChange = useCallback((start, end) => {
        setDateRange({ start, end });
    }, []);

    return (
        <div className="data-visualization">
            <div className="controls">
                <ChartTypeSelector 
                    selectedType={chartType}
                    onTypeChange={handleChartTypeChange}
                />

                <MetricSelector
                    selectedMetrics={selectedMetrics}
                    onMetricToggle={handleMetricToggle}
                />

                <DateRangePicker
                    dateRange={dateRange}
                    onRangeChange={handleDateRangeChange}
                />
            </div>

            <Chart config={chartConfig} />
        </div>
    );
}
        """, language="javascript")

    with tab3:
        st.markdown('<h2 class="section-header">Custom Hooks - Reutilizarea Logicii</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### De ce Custom Hooks?

        Custom hooks permit:
        - **Reutilizarea logicii** între componente
        - **Separarea concerns** - logica de business separată de UI
        - **Testarea mai ușoară** - logica poate fi testată independent
        - **Cod mai curat și mai organizat**
        """)

        st.code("""
// 1. useLocalStorage - Persistent state management
function useLocalStorage(key, initialValue) {
    // State pentru stocarea valorii
    const [storedValue, setStoredValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            console.error(`Error reading localStorage key "${key}":`, error);
            return initialValue;
        }
    });

    // Function pentru setarea valorii
    const setValue = useCallback((value) => {
        try {
            // Allow value to be a function so we have the same API as useState
            const valueToStore = value instanceof Function ? value(storedValue) : value;

            setStoredValue(valueToStore);

            if (valueToStore === undefined) {
                window.localStorage.removeItem(key);
            } else {
                window.localStorage.setItem(key, JSON.stringify(valueToStore));
            }
        } catch (error) {
            console.error(`Error setting localStorage key "${key}":`, error);
        }
    }, [key, storedValue]);

    return [storedValue, setValue];
}

// Utilizare
function Settings() {
    const [theme, setTheme] = useLocalStorage('theme', 'light');
    const [language, setLanguage] = useLocalStorage('language', 'en');
    const [preferences, setPreferences] = useLocalStorage('preferences', {
        notifications: true,
        autoSave: false
    });

    return (
        <div>
            <select value={theme} onChange={(e) => setTheme(e.target.value)}>
                <option value="light">Light</option>
                <option value="dark">Dark</option>
            </select>

            <select value={language} onChange={(e) => setLanguage(e.target.value)}>
                <option value="en">English</option>
                <option value="ro">Română</option>
            </select>

            <label>
                <input
                    type="checkbox"
                    checked={preferences.notifications}
                    onChange={(e) => setPreferences(prev => ({
                        ...prev,
                        notifications: e.target.checked
                    }))}
                />
                Enable notifications
            </label>
        </div>
    );
}

// 2. useFetch - Data fetching cu loading și error states
function useFetch(url, options = {}) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Memoize options pentru a evita re-fetch-urile inutile
    const memoizedOptions = useMemo(() => options, [JSON.stringify(options)]);

    useEffect(() => {
        let isCancelled = false;

        const fetchData = async () => {
            try {
                setLoading(true);
                setError(null);

                const response = await fetch(url, memoizedOptions);

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();

                if (!isCancelled) {
                    setData(result);
                }
            } catch (err) {
                if (!isCancelled) {
                    setError(err.message);
                }
            } finally {
                if (!isCancelled) {
                    setLoading(false);
                }
            }
        };

        fetchData();

        // Cleanup function pentru a evita memory leaks
        return () => {
            isCancelled = true;
        };
    }, [url, memoizedOptions]);

    // Function pentru retry
    const retry = useCallback(() => {
        setError(null);
        setLoading(true);
        // Re-trigger effect prin schimbarea unui dependency
    }, []);

    return { data, loading, error, retry };
}

// Utilizare
function UserList() {
    const { data: users, loading, error, retry } = useFetch('/api/users', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (loading) return <div>Loading users...</div>;
    if (error) return (
        <div>
            <p>Error: {error}</p>
            <button onClick={retry}>Retry</button>
        </div>
    );

    return (
        <ul>
            {users?.map(user => (
                <li key={user.id}>{user.name} - {user.email}</li>
            ))}
        </ul>
    );
}

// 3. useDebounce - Pentru input optimization
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

// Hook pentru search cu debounce și caching
function useSearch(searchFunction, delay = 300) {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const debouncedQuery = useDebounce(query, delay);

    // Cache pentru rezultate
    const cache = useRef(new Map());

    useEffect(() => {
        if (!debouncedQuery) {
            setResults([]);
            return;
        }

        // Check cache first
        if (cache.current.has(debouncedQuery)) {
            setResults(cache.current.get(debouncedQuery));
            return;
        }

        const performSearch = async () => {
            try {
                setLoading(true);
                setError(null);

                const searchResults = await searchFunction(debouncedQuery);

                // Cache results
                cache.current.set(debouncedQuery, searchResults);
                setResults(searchResults);
            } catch (err) {
                setError(err.message);
                setResults([]);
            } finally {
                setLoading(false);
            }
        };

        performSearch();
    }, [debouncedQuery, searchFunction]);

    const clearCache = useCallback(() => {
        cache.current.clear();
    }, []);

    return {
        query,
        setQuery,
        results,
        loading,
        error,
        clearCache
    };
}

// Utilizare
function SearchComponent() {
    const searchUsers = useCallback(async (query) => {
        const response = await fetch(`/api/search/users?q=${encodeURIComponent(query)}`);
        return response.json();
    }, []);

    const { query, setQuery, results, loading, error } = useSearch(searchUsers);

    return (
        <div>
            <input
                type="text"
                placeholder="Search users..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />

            {loading && <div>Searching...</div>}
            {error && <div>Error: {error}</div>}

            <ul>
                {results.map(user => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
}

// 4. useFormValidation - Complex form handling
function useFormValidation(initialValues, validationRules) {
    const [values, setValues] = useState(initialValues);
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});
    const [isSubmitting, setIsSubmitting] = useState(false);

    // Function pentru validarea unui câmp
    const validateField = useCallback((name, value) => {
        const rules = validationRules[name];
        if (!rules) return null;

        for (const rule of rules) {
            const error = rule(value, values);
            if (error) return error;
        }

        return null;
    }, [validationRules, values]);

    // Function pentru setarea unei valori
    const setValue = useCallback((name, value) => {
        setValues(prev => ({ ...prev, [name]: value }));

        // Clear error when user starts typing
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: null }));
        }
    }, [errors]);

    // Function pentru marcarea unui câmp ca touched
    const setTouched = useCallback((name) => {
        setTouched(prev => ({ ...prev, [name]: true }));

        // Validate field when it loses focus
        const error = validateField(name, values[name]);
        if (error) {
            setErrors(prev => ({ ...prev, [name]: error }));
        }
    }, [validateField, values]);

    // Function pentru validarea întregului form
    const validateForm = useCallback(() => {
        const newErrors = {};

        Object.keys(validationRules).forEach(name => {
            const error = validateField(name, values[name]);
            if (error) {
                newErrors[name] = error;
            }
        });

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    }, [validationRules, validateField, values]);

    // Function pentru submit
    const handleSubmit = useCallback((onSubmit) => {
        return async (event) => {
            event.preventDefault();

            if (!validateForm()) {
                // Mark all fields as touched to show errors
                const allTouched = Object.keys(validationRules).reduce((acc, key) => {
                    acc[key] = true;
                    return acc;
                }, {});
                setTouched(allTouched);
                return;
            }

            setIsSubmitting(true);

            try {
                await onSubmit(values);
            } catch (error) {
                console.error('Form submission error:', error);
            } finally {
                setIsSubmitting(false);
            }
        };
    }, [validateForm, validationRules, values]);

    // Function pentru reset
    const reset = useCallback(() => {
        setValues(initialValues);
        setErrors({});
        setTouched({});
        setIsSubmitting(false);
    }, [initialValues]);

    return {
        values,
        errors,
        touched,
        isSubmitting,
        setValue,
        setTouched,
        handleSubmit,
        reset,
        isValid: Object.keys(errors).length === 0
    };
}

// Utilizare cu validation rules
function RegistrationForm() {
    const validationRules = {
        email: [
            (value) => !value ? 'Email is required' : null,
            (value) => !/\S+@\S+\.\S+/.test(value) ? 'Email is invalid' : null
        ],
        password: [
            (value) => !value ? 'Password is required' : null,
            (value) => value.length < 6 ? 'Password must be at least 6 characters' : null
        ],
        confirmPassword: [
            (value) => !value ? 'Please confirm your password' : null,
            (value, allValues) => value !== allValues.password ? 'Passwords do not match' : null
        ]
    };

    const {
        values,
        errors,
        touched,
        isSubmitting,
        setValue,
        setTouched,
        handleSubmit,
        reset
    } = useFormValidation({
        email: '',
        password: '',
        confirmPassword: ''
    }, validationRules);

    const onSubmit = async (formData) => {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000));
        console.log('Form submitted:', formData);
        alert('Registration successful!');
        reset();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div>
                <input
                    type="email"
                    placeholder="Email"
                    value={values.email}
                    onChange={(e) => setValue('email', e.target.value)}
                    onBlur={() => setTouched('email')}
                />
                {touched.email && errors.email && (
                    <span className="error">{errors.email}</span>
                )}
            </div>

            <div>
                <input
                    type="password"
                    placeholder="Password"
                    value={values.password}
                    onChange={(e) => setValue('password', e.target.value)}
                    onBlur={() => setTouched('password')}
                />
                {touched.password && errors.password && (
                    <span className="error">{errors.password}</span>
                )}
            </div>

            <div>
                <input
                    type="password"
                    placeholder="Confirm Password"
                    value={values.confirmPassword}
                    onChange={(e) => setValue('confirmPassword', e.target.value)}
                    onBlur={() => setTouched('confirmPassword')}
                />
                {touched.confirmPassword && errors.confirmPassword && (
                    <span className="error">{errors.confirmPassword}</span>
                )}
            </div>

            <button type="submit" disabled={isSubmitting}>
                {isSubmitting ? 'Registering...' : 'Register'}
            </button>
        </form>
    );
}
        """, language="javascript")

    with tab4:
        st.markdown('<h2 class="section-header">Hooks Avansați și Specializați</h2>', unsafe_allow_html=True)

        st.markdown("### useRef - Referințe și Mutarea Beyond State")

        st.code("""
// 1. DOM References și Imperative Actions
function FocusInput() {
    const inputRef = useRef(null);
    const [count, setCount] = useState(0);

    // Focus pe input la mount
    useEffect(() => {
        inputRef.current?.focus();
    }, []);

    const handleFocus = () => {
        inputRef.current?.focus();
    };

    const handleClear = () => {
        if (inputRef.current) {
            inputRef.current.value = '';
            inputRef.current.focus();
        }
    };

    return (
        <div>
            <input ref={inputRef} type="text" placeholder="Type something..." />
            <button onClick={handleFocus}>Focus Input</button>
            <button onClick={handleClear}>Clear & Focus</button>

            <p>Component rendered {count} times</p>
            <button onClick={() => setCount(count + 1)}>Re-render</button>
        </div>
    );
}

// 2. Storing Mutable Values (nu declanșează re-render)
function Timer() {
    const [seconds, setSeconds] = useState(0);
    const [isRunning, setIsRunning] = useState(false);

    // useRef pentru storing interval ID (nu se pierde la re-render)
    const intervalRef = useRef(null);

    // useRef pentru previous value tracking
    const prevSecondsRef = useRef();

    useEffect(() => {
        prevSecondsRef.current = seconds;
    });

    const prevSeconds = prevSecondsRef.current;

    useEffect(() => {
        if (isRunning) {
            intervalRef.current = setInterval(() => {
                setSeconds(prevSeconds => prevSeconds + 1);
            }, 1000);
        } else {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
                intervalRef.current = null;
            }
        }

        // Cleanup
        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, [isRunning]);

    const handleStart = () => setIsRunning(true);
    const handleStop = () => setIsRunning(false);
    const handleReset = () => {
        setSeconds(0);
        setIsRunning(false);
    };

    return (
        <div>
            <h2>Timer: {seconds}s</h2>
            <p>Previous: {prevSeconds}s</p>

            <button onClick={handleStart} disabled={isRunning}>
                Start
            </button>
            <button onClick={handleStop} disabled={!isRunning}>
                Stop
            </button>
            <button onClick={handleReset}>Reset</button>
        </div>
    );
}

// 3. Forward Refs pentru Custom Components
const CustomInput = forwardRef(({ label, error, ...props }, ref) => {
    return (
        <div className="form-group">
            <label>{label}</label>
            <input
                ref={ref}
                {...props}
                className={`form-input ${error ? 'error' : ''}`}
            />
            {error && <span className="error-text">{error}</span>}
        </div>
    );
});

function FormWithCustomInputs() {
    const emailRef = useRef(null);
    const passwordRef = useRef(null);

    const handleSubmit = (e) => {
        e.preventDefault();

        const email = emailRef.current?.value;
        const password = passwordRef.current?.value;

        if (!email) {
            emailRef.current?.focus();
            return;
        }

        if (!password) {
            passwordRef.current?.focus();
            return;
        }

        console.log('Submitted:', { email, password });
    };

    return (
        <form onSubmit={handleSubmit}>
            <CustomInput
                ref={emailRef}
                label="Email"
                type="email"
                required
            />

            <CustomInput
                ref={passwordRef}
                label="Password"
                type="password"
                required
            />

            <button type="submit">Login</button>
        </form>
    );
}

// 4. useRef pentru Measuring și Animations
function MeasureComponent() {
    const [dimensions, setDimensions] = useState({ width: 0, height: 0 });
    const elementRef = useRef(null);

    useEffect(() => {
        const updateDimensions = () => {
            if (elementRef.current) {
                const { offsetWidth, offsetHeight } = elementRef.current;
                setDimensions({ width: offsetWidth, height: offsetHeight });
            }
        };

        // Initial measurement
        updateDimensions();

        // Listen for resize
        window.addEventListener('resize', updateDimensions);

        return () => {
            window.removeEventListener('resize', updateDimensions);
        };
    }, []);

    return (
        <div>
            <div
                ref={elementRef}
                style={{
                    padding: '20px',
                    border: '2px solid #ccc',
                    resize: 'both',
                    overflow: 'auto',
                    minWidth: '200px',
                    minHeight: '100px'
                }}
            >
                <h3>Resizable Box</h3>
                <p>Try resizing this box or the window!</p>
                <p>Current dimensions: {dimensions.width}x{dimensions.height}</p>
            </div>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### useLayoutEffect - Synchronous Effects")

        st.code("""
// useLayoutEffect vs useEffect - Timing diferit
function LayoutEffectDemo() {
    const [color, setColor] = useState('red');
    const buttonRef = useRef(null);

    // useEffect - Rulează DUPĂ paint (asincron)
    useEffect(() => {
        console.log('useEffect - după paint');
    });

    // useLayoutEffect - Rulează ÎNAINTE de paint (sincron)
    useLayoutEffect(() => {
        console.log('useLayoutEffect - înainte de paint');

        // Exemplu: Ajustarea poziției unui element
        if (buttonRef.current) {
            const rect = buttonRef.current.getBoundingClientRect();
            console.log('Button position:', rect);

            // Modificări DOM care trebuie să fie vizibile imediat
            if (rect.right > window.innerWidth - 50) {
                buttonRef.current.style.position = 'absolute';
                buttonRef.current.style.right = '10px';
            }
        }
    });

    return (
        <div>
            <button
                ref={buttonRef}
                onClick={() => setColor(color === 'red' ? 'blue' : 'red')}
                style={{ backgroundColor: color }}
            >
                Click me - Color: {color}
            </button>
        </div>
    );
}

// Exemplu practic: Tooltip positioning
function TooltipDemo() {
    const [showTooltip, setShowTooltip] = useState(false);
    const [tooltipPosition, setTooltipPosition] = useState({ top: 0, left: 0 });
    const triggerRef = useRef(null);
    const tooltipRef = useRef(null);

    useLayoutEffect(() => {
        if (showTooltip && triggerRef.current && tooltipRef.current) {
            const triggerRect = triggerRef.current.getBoundingClientRect();
            const tooltipRect = tooltipRef.current.getBoundingClientRect();

            let top = triggerRect.bottom + 5;
            let left = triggerRect.left + (triggerRect.width / 2) - (tooltipRect.width / 2);

            // Adjust if tooltip goes outside viewport
            if (left < 0) {
                left = 5;
            } else if (left + tooltipRect.width > window.innerWidth) {
                left = window.innerWidth - tooltipRect.width - 5;
            }

            if (top + tooltipRect.height > window.innerHeight) {
                top = triggerRect.top - tooltipRect.height - 5;
            }

            setTooltipPosition({ top, left });
        }
    }, [showTooltip]);

    return (
        <div>
            <button
                ref={triggerRef}
                onMouseEnter={() => setShowTooltip(true)}
                onMouseLeave={() => setShowTooltip(false)}
                style={{ margin: '100px' }}
            >
                Hover for tooltip
            </button>

            {showTooltip && (
                <div
                    ref={tooltipRef}
                    style={{
                        position: 'fixed',
                        top: tooltipPosition.top,
                        left: tooltipPosition.left,
                        backgroundColor: 'black',
                        color: 'white',
                        padding: '8px',
                        borderRadius: '4px',
                        fontSize: '12px',
                        pointerEvents: 'none',
                        zIndex: 1000
                    }}
                >
                    This is a perfectly positioned tooltip!
                </div>
            )}
        </div>
    );
}
        """, language="javascript")

        st.markdown("### useImperativeHandle - Expunerea Metodelor Custom")

        st.code("""
// Custom Input Component cu metode exposed
const FancyInput = forwardRef((props, ref) => {
    const inputRef = useRef(null);
    const [isFocused, setIsFocused] = useState(false);
    const [value, setValue] = useState('');

    // Expose custom methods prin ref
    useImperativeHandle(ref, () => ({
        // Metode standard
        focus: () => {
            inputRef.current?.focus();
        },

        blur: () => {
            inputRef.current?.blur();
        },

        // Metode custom
        clear: () => {
            setValue('');
            inputRef.current?.focus();
        },

        getValue: () => {
            return value;
        },

        setValue: (newValue) => {
            setValue(newValue);
        },

        selectAll: () => {
            inputRef.current?.select();
        },

        // Getter pentru state intern
        get isFocused() {
            return isFocused;
        },

        // Animation methods
        shake: () => {
            if (inputRef.current) {
                inputRef.current.style.animation = 'shake 0.5s';
                setTimeout(() => {
                    inputRef.current.style.animation = '';
                }, 500);
            }
        },

        highlight: (duration = 1000) => {
            if (inputRef.current) {
                inputRef.current.style.backgroundColor = '#ffeb3b';
                setTimeout(() => {
                    inputRef.current.style.backgroundColor = '';
                }, duration);
            }
        }
    }), [isFocused, value]);

    const handleFocus = () => setIsFocused(true);
    const handleBlur = () => setIsFocused(false);
    const handleChange = (e) => setValue(e.target.value);

    return (
        <input
            ref={inputRef}
            value={value}
            onChange={handleChange}
            onFocus={handleFocus}
            onBlur={handleBlur}
            style={{
                border: isFocused ? '2px solid blue' : '1px solid gray',
                padding: '8px',
                borderRadius: '4px',
                outline: 'none'
            }}
            {...props}
        />
    );
});

// Component care folosește FancyInput
function FancyInputDemo() {
    const inputRef = useRef(null);
    const [log, setLog] = useState([]);

    const addLog = (message) => {
        setLog(prev => [...prev, `${new Date().toLocaleTimeString()}: ${message}`]);
    };

    const handleFocus = () => {
        inputRef.current?.focus();
        addLog('Input focused via ref');
    };

    const handleClear = () => {
        inputRef.current?.clear();
        addLog('Input cleared via ref');
    };

    const handleGetValue = () => {
        const value = inputRef.current?.getValue();
        addLog(`Current value: "${value}"`);
    };

    const handleSetValue = () => {
        inputRef.current?.setValue('Hello from parent!');
        addLog('Value set via ref');
    };

    const handleSelectAll = () => {
        inputRef.current?.selectAll();
        addLog('Text selected via ref');
    };

    const handleShake = () => {
        inputRef.current?.shake();
        addLog('Input shaken via ref');
    };

    const handleHighlight = () => {
        inputRef.current?.highlight(2000);
        addLog('Input highlighted via ref');
    };

    const handleCheckFocus = () => {
        const focused = inputRef.current?.isFocused;
        addLog(`Input is ${focused ? 'focused' : 'not focused'}`);
    };

    return (
        <div>
            <h3>Fancy Input with Imperative Handle</h3>

            <FancyInput
                ref={inputRef}
                placeholder="Type something..."
            />

            <div style={{ margin: '20px 0' }}>
                <button onClick={handleFocus}>Focus</button>
                <button onClick={handleClear}>Clear</button>
                <button onClick={handleGetValue}>Get Value</button>
                <button onClick={handleSetValue}>Set Value</button>
                <button onClick={handleSelectAll}>Select All</button>
                <button onClick={handleShake}>Shake</button>
                <button onClick={handleHighlight}>Highlight</button>
                <button onClick={handleCheckFocus}>Check Focus</button>
            </div>

            <div>
                <h4>Action Log:</h4>
                <div style={{ 
                    maxHeight: '200px', 
                    overflow: 'auto', 
                    border: '1px solid #ccc',
                    padding: '10px'
                }}>
                    {log.map((entry, index) => (
                        <div key={index}>{entry}</div>
                    ))}
                </div>
                <button onClick={() => setLog([])}>Clear Log</button>
            </div>
        </div>
    );
}

// Advanced example: Modal cu imperativ API
const Modal = forwardRef(({ children, title }, ref) => {
    const [isOpen, setIsOpen] = useState(false);
    const [position, setPosition] = useState({ x: 0, y: 0 });
    const modalRef = useRef(null);

    useImperativeHandle(ref, () => ({
        open: (options = {}) => {
            setIsOpen(true);

            if (options.position) {
                setPosition(options.position);
            }

            if (options.center) {
                // Center modal on screen
                setTimeout(() => {
                    if (modalRef.current) {
                        const rect = modalRef.current.getBoundingClientRect();
                        setPosition({
                            x: (window.innerWidth - rect.width) / 2,
                            y: (window.innerHeight - rect.height) / 2
                        });
                    }
                }, 0);
            }
        },

        close: () => {
            setIsOpen(false);
        },

        toggle: () => {
            setIsOpen(prev => !prev);
        },

        setPosition: (newPosition) => {
            setPosition(newPosition);
        },

        get isOpen() {
            return isOpen;
        }
    }), [isOpen]);

    if (!isOpen) return null;

    return (
        <div 
            style={{
                position: 'fixed',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                backgroundColor: 'rgba(0,0,0,0.5)',
                zIndex: 1000
            }}
            onClick={() => setIsOpen(false)}
        >
            <div
                ref={modalRef}
                style={{
                    position: 'absolute',
                    top: position.y,
                    left: position.x,
                    backgroundColor: 'white',
                    padding: '20px',
                    borderRadius: '8px',
                    minWidth: '300px'
                }}
                onClick={(e) => e.stopPropagation()}
            >
                <h3>{title}</h3>
                {children}
                <button onClick={() => setIsOpen(false)}>Close</button>
            </div>
        </div>
    );
});

function ModalDemo() {
    const modalRef = useRef(null);

    return (
        <div>
            <button onClick={() => modalRef.current?.open({ center: true })}>
                Open Centered Modal
            </button>

            <button onClick={() => modalRef.current?.open({ position: { x: 50, y: 50 } })}>
                Open at Position
            </button>

            <button onClick={() => modalRef.current?.toggle()}>
                Toggle Modal
            </button>

            <Modal ref={modalRef} title="Imperative Modal">
                <p>This modal can be controlled imperatively!</p>
                <p>It was opened using ref methods.</p>
            </Modal>
        </div>
    );
}
        """, language="javascript")

    with tab5:
        st.markdown('<h2 class="section-header">Patterns și Best Practices</h2>', unsafe_allow_html=True)

        st.markdown("### Compound Hooks Pattern")

        st.code("""
// Pattern pentru combining multiple related hooks
function useCounter(initialValue = 0, options = {}) {
    const { min = -Infinity, max = Infinity, step = 1 } = options;

    const [count, setCount] = useState(initialValue);
    const [history, setHistory] = useState([initialValue]);

    const increment = useCallback(() => {
        setCount(prev => {
            const newValue = Math.min(prev + step, max);
            if (newValue !== prev) {
                setHistory(prevHistory => [...prevHistory, newValue]);
            }
            return newValue;
        });
    }, [step, max]);

    const decrement = useCallback(() => {
        setCount(prev => {
            const newValue = Math.max(prev - step, min);
            if (newValue !== prev) {
                setHistory(prevHistory => [...prevHistory, newValue]);
            }
            return newValue;
        });
    }, [step, min]);

    const reset = useCallback(() => {
        setCount(initialValue);
        setHistory([initialValue]);
    }, [initialValue]);

    const setValue = useCallback((value) => {
        const clampedValue = Math.max(min, Math.min(max, value));
        setCount(clampedValue);
        setHistory(prev => [...prev, clampedValue]);
    }, [min, max]);

    const undo = useCallback(() => {
        if (history.length > 1) {
            const newHistory = history.slice(0, -1);
            setHistory(newHistory);
            setCount(newHistory[newHistory.length - 1]);
        }
    }, [history]);

    return {
        count,
        increment,
        decrement,
        reset,
        setValue,
        undo,
        history,
        canUndo: history.length > 1,
        isAtMin: count === min,
        isAtMax: count === max
    };
}

// Usage
function CounterComponent() {
    const counter = useCounter(0, { min: 0, max: 10, step: 2 });

    return (
        <div>
            <h2>Count: {counter.count}</h2>

            <button 
                onClick={counter.decrement} 
                disabled={counter.isAtMin}
            >
                -2
            </button>

            <button 
                onClick={counter.increment} 
                disabled={counter.isAtMax}
            >
                +2
            </button>

            <button onClick={counter.reset}>Reset</button>

            <button 
                onClick={counter.undo} 
                disabled={!counter.canUndo}
            >
                Undo
            </button>

            <div>
                <h4>History:</h4>
                <p>{counter.history.join(' → ')}</p>
            </div>
        </div>
    );
}

// Pattern pentru State Machine cu hooks
function useStateMachine(states, initialState) {
    const [currentState, setCurrentState] = useState(initialState);
    const [context, setContext] = useState({});

    const transition = useCallback((event, payload = {}) => {
        const stateConfig = states[currentState];
        if (!stateConfig || !stateConfig.on || !stateConfig.on[event]) {
            console.warn(`No transition for event "${event}" in state "${currentState}"`);
            return;
        }

        const transition = stateConfig.on[event];
        const nextState = typeof transition === 'string' ? transition : transition.target;

        // Update context if transition has actions
        if (typeof transition === 'object' && transition.actions) {
            setContext(prevContext => {
                const newContext = { ...prevContext };
                transition.actions.forEach(action => {
                    if (typeof action === 'function') {
                        action(newContext, payload);
                    }
                });
                return newContext;
            });
        }

        setCurrentState(nextState);
    }, [currentState, states]);

    const can = useCallback((event) => {
        const stateConfig = states[currentState];
        return !!(stateConfig && stateConfig.on && stateConfig.on[event]);
    }, [currentState, states]);

    return {
        state: currentState,
        context,
        transition,
        can,
        matches: (state) => currentState === state
    };
}

// Usage: Loading state machine
function LoadingExample() {
    const loadingMachine = useStateMachine({
        idle: {
            on: {
                LOAD: 'loading'
            }
        },
        loading: {
            on: {
                SUCCESS: {
                    target: 'success',
                    actions: [(context, payload) => {
                        context.data = payload.data;
                    }]
                },
                ERROR: {
                    target: 'error',
                    actions: [(context, payload) => {
                        context.error = payload.error;
                    }]
                }
            }
        },
        success: {
            on: {
                RELOAD: 'loading',
                RESET: 'idle'
            }
        },
        error: {
            on: {
                RETRY: 'loading',
                RESET: 'idle'
            }
        }
    }, 'idle');

    const handleLoad = async () => {
        loadingMachine.transition('LOAD');

        try {
            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 2000));
            const data = { message: 'Data loaded successfully!' };
            loadingMachine.transition('SUCCESS', { data });
        } catch (error) {
            loadingMachine.transition('ERROR', { error: error.message });
        }
    };

    return (
        <div>
            <h3>Current State: {loadingMachine.state}</h3>

            {loadingMachine.matches('idle') && (
                <button onClick={handleLoad}>Load Data</button>
            )}

            {loadingMachine.matches('loading') && (
                <div>Loading...</div>
            )}

            {loadingMachine.matches('success') && (
                <div>
                    <p>✅ {loadingMachine.context.data?.message}</p>
                    <button onClick={() => loadingMachine.transition('RELOAD')}>
                        Reload
                    </button>
                    <button onClick={() => loadingMachine.transition('RESET')}>
                        Reset
                    </button>
                </div>
            )}

            {loadingMachine.matches('error') && (
                <div>
                    <p>❌ Error: {loadingMachine.context.error}</p>
                    <button onClick={() => loadingMachine.transition('RETRY')}>
                        Retry
                    </button>
                    <button onClick={() => loadingMachine.transition('RESET')}>
                        Reset
                    </button>
                </div>
            )}
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Hook Composition și Advanced Patterns")

        st.code("""
// Higher-Order Hook Pattern
function withLoading(hook) {
    return function useHookWithLoading(...args) {
        const [loading, setLoading] = useState(false);
        const [error, setError] = useState(null);

        const hookResult = hook(...args);

        // Wrap async methods cu loading state
        const wrappedResult = useMemo(() => {
            const wrapped = { ...hookResult };

            Object.keys(hookResult).forEach(key => {
                if (typeof hookResult[key] === 'function') {
                    wrapped[key] = async (...fnArgs) => {
                        try {
                            setLoading(true);
                            setError(null);
                            const result = await hookResult[key](...fnArgs);
                            return result;
                        } catch (err) {
                            setError(err);
                            throw err;
                        } finally {
                            setLoading(false);
                        }
                    };
                }
            });

            return {
                ...wrapped,
                loading,
                error
            };
        }, [hookResult, loading, error]);

        return wrappedResult;
    };
}

// Basic hook pentru API operations
function useApi(baseUrl) {
    const get = useCallback(async (endpoint) => {
        const response = await fetch(`${baseUrl}${endpoint}`);
        if (!response.ok) throw new Error('API request failed');
        return response.json();
    }, [baseUrl]);

    const post = useCallback(async (endpoint, data) => {
        const response = await fetch(`${baseUrl}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('API request failed');
        return response.json();
    }, [baseUrl]);

    return { get, post };
}

// Enhanced hook cu loading
const useApiWithLoading = withLoading(useApi);

// Usage
function ApiComponent() {
    const api = useApiWithLoading('/api');
    const [data, setData] = useState(null);

    const handleLoad = async () => {
        try {
            const result = await api.get('/users');
            setData(result);
        } catch (error) {
            console.error('Failed to load data:', error);
        }
    };

    return (
        <div>
            <button onClick={handleLoad} disabled={api.loading}>
                {api.loading ? 'Loading...' : 'Load Data'}
            </button>

            {api.error && <p>Error: {api.error.message}</p>}
            {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
        </div>
    );
}

// Dependency Injection Pattern pentru hooks
const ApiContext = createContext();

function ApiProvider({ children, baseUrl }) {
    const api = useApi(baseUrl);
    return (
        <ApiContext.Provider value={api}>
            {children}
        </ApiContext.Provider>
    );
}

function useApiContext() {
    const context = useContext(ApiContext);
    if (!context) {
        throw new Error('useApiContext must be used within ApiProvider');
    }
    return context;
}

// Hook composition pentru complex state management
function useEntityManager(entityName, apiEndpoint) {
    const api = useApiContext();
    const [entities, setEntities] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [selectedId, setSelectedId] = useState(null);

    // CRUD operations
    const load = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);
            const data = await api.get(apiEndpoint);
            setEntities(data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    }, [api, apiEndpoint]);

    const create = useCallback(async (entityData) => {
        try {
            const newEntity = await api.post(apiEndpoint, entityData);
            setEntities(prev => [...prev, newEntity]);
            return newEntity;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, [api, apiEndpoint]);

    const update = useCallback(async (id, updates) => {
        try {
            const updatedEntity = await api.post(`${apiEndpoint}/${id}`, updates);
            setEntities(prev => prev.map(entity => 
                entity.id === id ? updatedEntity : entity
            ));
            return updatedEntity;
        } catch (err) {
            setError(err);
            throw err;
        }
    }, [api, apiEndpoint]);

    const remove = useCallback(async (id) => {
        try {
            await api.post(`${apiEndpoint}/${id}`, { method: 'DELETE' });
            setEntities(prev => prev.filter(entity => entity.id !== id));
            if (selectedId === id) {
                setSelectedId(null);
            }
        } catch (err) {
            setError(err);
            throw err;
        }
    }, [api, apiEndpoint, selectedId]);

    // Selection management
    const select = useCallback((id) => {
        setSelectedId(id);
    }, []);

    const clearSelection = useCallback(() => {
        setSelectedId(null);
    }, []);

    // Computed values
    const selectedEntity = useMemo(() => {
        return entities.find(entity => entity.id === selectedId) || null;
    }, [entities, selectedId]);

    const isEmpty = entities.length === 0;
    const hasSelection = selectedId !== null;

    // Load on mount
    useEffect(() => {
        load();
    }, [load]);

    return {
        // Data
        entities,
        selectedEntity,
        selectedId,

        // State
        loading,
        error,
        isEmpty,
        hasSelection,

        // Actions
        load,
        create,
        update,
        remove,
        select,
        clearSelection,

        // Utilities
        getById: (id) => entities.find(entity => entity.id === id),
        filter: (predicate) => entities.filter(predicate),
        find: (predicate) => entities.find(predicate)
    };
}

// Usage
function UserManager() {
    const users = useEntityManager('user', '/users');

    return (
        <div>
            <h2>User Manager</h2>

            {users.loading && <p>Loading users...</p>}
            {users.error && <p>Error: {users.error.message}</p>}

            <div>
                <button onClick={users.load}>Refresh</button>
                <button onClick={users.clearSelection}>Clear Selection</button>
            </div>

            {users.isEmpty ? (
                <p>No users found</p>
            ) : (
                <div>
                    <ul>
                        {users.entities.map(user => (
                            <li 
                                key={user.id}
                                onClick={() => users.select(user.id)}
                                style={{
                                    cursor: 'pointer',
                                    backgroundColor: users.selectedId === user.id ? '#e3f2fd' : 'transparent'
                                }}
                            >
                                {user.name} - {user.email}
                            </li>
                        ))}
                    </ul>

                    {users.hasSelection && (
                        <div>
                            <h3>Selected User:</h3>
                            <p>Name: {users.selectedEntity.name}</p>
                            <p>Email: {users.selectedEntity.email}</p>
                            <button onClick={() => users.remove(users.selectedId)}>
                                Delete User
                            </button>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

// Main app cu providers
function App() {
    return (
        <ApiProvider baseUrl="/api">
            <UserManager />
        </ApiProvider>
    );
}
        """, language="javascript")

    with tab6:
        st.markdown('<h2 class="section-header">Întrebări de Interviu - React Hooks</h2>', unsafe_allow_html=True)

        st.markdown("### Întrebări de Nivel Începător")

        with st.expander("1. Ce sunt React Hooks și care sunt avantajele lor?"):
            st.markdown("""
            **Răspuns complet:**

            React Hooks sunt funcții speciale care permit folosirea state-ului și a altor funcționalități React 
            în componente funcționale, fără a fi nevoie să le converți în class components.

            **Avantaje principale:**

            **1. Simplificare cod:**
            - Elimină complexitatea class components
            - Nu mai e nevoie de `this` binding
            - Sintaxă mai curată și mai puțin verbose

            **2. Reutilizarea logicii:**
            - Custom hooks pentru logica comună
            - Composition mai ușoară decât inheritance
            - Separarea concerns-urilor

            **3. Performance îmbunătățit:**
            - Bundle size mai mic
            - Optimizări mai ușoare cu useCallback și useMemo
            - Hot reloading mai bun

            **4. Testare mai ușoară:**
            - Funcții pure pentru custom hooks
            - Mock-ing mai simplu
            - Izolarea logicii de UI

            **Exemplu comparativ:**
            ```javascript
            // Class component (înainte)
            class Counter extends Component {
                constructor(props) {
                    super(props);
                    this.state = { count: 0 };
                    this.increment = this.increment.bind(this);
                }

                increment() {
                    this.setState({ count: this.state.count + 1 });
                }

                render() {
                    return (
                        <button onClick={this.increment}>
                            {this.state.count}
                        </button>
                    );
                }
            }

            // Functional component cu hooks (acum)
            function Counter() {
                const [count, setCount] = useState(0);

                return (
                    <button onClick={() => setCount(count + 1)}>
                        {count}
                    </button>
                );
            }
            ```
            """)

        with st.expander("2. Care sunt regulile Hooks-urilor și de ce există?"):
            st.markdown("""
            **Regulile Hooks-urilor:**

            **1. Apelează Hooks-urile doar la nivelul superior**
            - Nu în loop-uri, condiții sau funcții nested
            - Doar în componente React sau custom hooks

            **2. Ordinea trebuie să fie consistentă**
            - Același număr și aceeași ordine la fiecare render
            - React se bazează pe ordine pentru asocierea state-ului

            **De ce aceste reguli:**

            **React folosește un index intern:**
            ```javascript
            // React menține intern ceva similar cu:
            const hooks = [];
            let currentHookIndex = 0;

            function useState(initial) {
                const index = currentHookIndex++;
                if (hooks[index] === undefined) {
                    hooks[index] = initial;
                }
                return [hooks[index], (value) => hooks[index] = value];
            }
            ```

            **❌ Ce NU trebuie să faci:**
            ```javascript
            function BadComponent({ condition }) {
                if (condition) {
                    const [state, setState] = useState(0); // GREȘIT!
                }

                for (let i = 0; i < 3; i++) {
                    useEffect(() => {}); // GREȘIT!
                }

                return <div>...</div>;
            }
            ```

            **✅ Varianta corectă:**
            ```javascript
            function GoodComponent({ condition }) {
                const [state, setState] = useState(condition ? 0 : null);

                useEffect(() => {
                    // Logica condițională INSIDE hook
                    if (condition) {
                        // do something
                    }
                });

                return <div>...</div>;
            }
            ```
            """)

        st.markdown("### Întrebări de Nivel Intermediar")

        with st.expander("3. Explică diferența între useState și useReducer. Când folosești fiecare?"):
            st.markdown("""
            **useState vs useReducer:**

            | Criteriu | useState | useReducer |
            |----------|----------|------------|
            | **Complexitate state** | Simplu (primitive, obiecte mici) | Complex (obiecte mari, logică complexă) |
            | **Updates** | Directe | Prin actions și reducer |
            | **Predictibilitate** | Menos predictibil | Foarte predictibil |
            | **Testare** | Mai greu de testat | Ușor de testat (pure functions) |
            | **Performance** | OK pentru state simplu | Optimizat pentru state complex |

            **Când folosești useState:**
            ```javascript
            // State simplu - primitive values
            const [count, setCount] = useState(0);
            const [name, setName] = useState('');
            const [isVisible, setIsVisible] = useState(false);

            // Obiecte mici cu updates simple
            const [user, setUser] = useState({ name: '', email: '' });
            ```

            **Când folosești useReducer:**
            ```javascript
            // State complex cu multiple proprietăți interdependente
            const [state, dispatch] = useReducer(formReducer, {
                fields: { name: '', email: '', password: '' },
                errors: {},
                isSubmitting: false,
                submitCount: 0
            });

            // Logică complexă de actualizare
            function formReducer(state, action) {
                switch (action.type) {
                    case 'SET_FIELD':
                        return {
                            ...state,
                            fields: {
                                ...state.fields,
                                [action.field]: action.value
                            },
                            errors: {
                                ...state.errors,
                                [action.field]: null // Clear error
                            }
                        };

                    case 'SET_ERRORS':
                        return {
                            ...state,
                            errors: action.errors,
                            isSubmitting: false
                        };

                    case 'START_SUBMIT':
                        return {
                            ...state,
                            isSubmitting: true,
                            submitCount: state.submitCount + 1
                        };

                    default:
                        return state;
                }
            }
            ```

            **Regula generală:** Începe cu useState, migrează la useReducer când:
            - Ai mai mult de 3-4 state variables relacionate
            - Logica de update devine complexă
            - Ai nevoie de predictibilitate pentru debugging
            - Vrei să testezi logica separat de componente
            """)

        with st.expander("4. Cum funcționează dependency arrays în useEffect și de ce sunt importante?"):
            st.markdown("""
            **Dependency Arrays controlează când se re-execută efectele:**

            **1. Fără dependency array - rulează după fiecare render:**
            ```javascript
            useEffect(() => {
                console.log('Runs after every render');
                document.title = `Count: ${count}`;
            }); // Fără array - ATENȚIE la performance!
            ```

            **2. Array gol - rulează doar la mount/unmount:**
            ```javascript
            useEffect(() => {
                console.log('Runs only on mount');
                const interval = setInterval(() => {
                    // Logic here
                }, 1000);

                return () => clearInterval(interval); // Cleanup
            }, []); // Array gol
            ```

            **3. Cu dependencies - rulează când se schimbă dependencies:**
            ```javascript
            useEffect(() => {
                console.log('Runs when userId changes');
                fetchUserData(userId);
            }, [userId]); // Rulează când userId se schimbă
            ```

            **Probleme comune și soluții:**

            **❌ Missing dependencies (ESLint warning):**
            ```javascript
            function UserProfile({ userId }) {
                const [user, setUser] = useState(null);

                useEffect(() => {
                    fetchUser(userId).then(setUser); // userId e dependency!
                }, []); // GREȘIT - missing userId

                return <div>{user?.name}</div>;
            }
            ```

            **✅ Correct dependencies:**
            ```javascript
            function UserProfile({ userId }) {
                const [user, setUser] = useState(null);

                useEffect(() => {
                    fetchUser(userId).then(setUser);
                }, [userId]); // Correct - include userId

                return <div>{user?.name}</div>;
            }
            ```

            **Stale closures problem:**
            ```javascript
            // ❌ PROBLEMĂ - stale closure
            function Timer() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const interval = setInterval(() => {
                        setCount(count + 1); // count este "stale"
                    }, 1000);

                    return () => clearInterval(interval);
                }, []); // Empty deps - count nu se actualizează

                return <div>{count}</div>;
            }

            // ✅ SOLUȚIE - functional update
            function Timer() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const interval = setInterval(() => {
                        setCount(prevCount => prevCount + 1); // Functional update
                    }, 1000);

                    return () => clearInterval(interval);
                }, []); // OK - nu depinde de count

                return <div>{count}</div>;
            }
            ```

            **Object dependencies - atenție la referințe:**
            ```javascript
            // ❌ Object se recreează la fiecare render
            function SearchResults({ query }) {
                const searchOptions = { query, limit: 10, sort: 'date' };

                useEffect(() => {
                    search(searchOptions); // Effect se rulează la fiecare render!
                }, [searchOptions]);
            }

            // ✅ useMemo pentru object dependencies
            function SearchResults({ query }) {
                const searchOptions = useMemo(() => ({
                    query,
                    limit: 10,
                    sort: 'date'
                }), [query]);

                useEffect(() => {
                    search(searchOptions);
                }, [searchOptions]); // OK - object e memoized
            }
            ```
            """)

        with st.expander("5. Explică diferența între useMemo și useCallback cu exemple practice"):
            st.markdown("""
            **useMemo vs useCallback - Concepte:**

            - **useMemo**: Memoizează **valoarea rezultată** dintr-un calcul
            - **useCallback**: Memoizează **funcția în sine**

            **useMemo - Pentru expensive calculations:**
            ```javascript
            function ExpensiveComponent({ items, filter }) {
                // ❌ Fără useMemo - calculul se face la fiecare render
                const expensiveValue = items
                    .filter(item => item.category === filter)
                    .map(item => heavyProcessing(item))
                    .reduce((sum, value) => sum + value, 0);

                // ✅ Cu useMemo - calculul se face doar când dependencies se schimbă
                const optimizedValue = useMemo(() => {
                    console.log('Performing expensive calculation...');
                    return items
                        .filter(item => item.category === filter)
                        .map(item => heavyProcessing(item))
                        .reduce((sum, value) => sum + value, 0);
                }, [items, filter]);

                return <div>Result: {optimizedValue}</div>;
            }
            ```

            **useCallback - Pentru function references:**
            ```javascript
            function ParentComponent({ items }) {
                const [filter, setFilter] = useState('');

                // ❌ Fără useCallback - funcția se recrează la fiecare render
                const handleItemClick = (itemId) => {
                    console.log('Clicked:', itemId);
                    // Some logic here
                };

                // ✅ Cu useCallback - funcția se recrează doar când e necesar
                const optimizedHandleClick = useCallback((itemId) => {
                    console.log('Clicked:', itemId);
                    // Some logic here
                }, []); // Empty deps - funcția nu se schimbă niciodată

                return (
                    <div>
                        {items.map(item => (
                            <ItemComponent
                                key={item.id}
                                item={item}
                                onClick={optimizedHandleClick} // Referință stabilă
                            />
                        ))}
                    </div>
                );
            }

            // Component copil optimizat cu React.memo
            const ItemComponent = React.memo(({ item, onClick }) => {
                console.log(`Rendering ${item.name}`); // Se printează doar când e necesar

                return (
                    <div onClick={() => onClick(item.id)}>
                        {item.name}
                    </div>
                );
            });
            ```

            **Combinarea useMemo și useCallback:**
            ```javascript
            function SearchComponent({ users, onSelectionChange }) {
                const [searchTerm, setSearchTerm] = useState('');
                const [selectedUsers, setSelectedUsers] = useState(new Set());

                // useMemo pentru filtered data
                const filteredUsers = useMemo(() => {
                    console.log('Filtering users...');
                    return users.filter(user =>
                        user.name.toLowerCase().includes(searchTerm.toLowerCase())
                    );
                }, [users, searchTerm]);

                // useCallback pentru event handlers
                const handleUserToggle = useCallback((userId) => {
                    setSelectedUsers(prev => {
                        const newSet = new Set(prev);
                        if (newSet.has(userId)) {
                            newSet.delete(userId);
                        } else {
                            newSet.add(userId);
                        }
                        return newSet;
                    });
                }, []);

                // useCallback cu dependencies
                const handleSelectionComplete = useCallback(() => {
                    onSelectionChange(Array.from(selectedUsers));
                }, [selectedUsers, onSelectionChange]);

                // useMemo pentru computed values
                const selectionStats = useMemo(() => ({
                    total: filteredUsers.length,
                    selected: selectedUsers.size,
                    percentage: filteredUsers.length > 0 
                        ? (selectedUsers.size / filteredUsers.length * 100).toFixed(1)
                        : 0
                }), [filteredUsers.length, selectedUsers.size]);

                return (
                    <div>
                        <input
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            placeholder="Search users..."
                        />

                        <p>
                            Selected {selectionStats.selected} of {selectionStats.total} 
                            ({selectionStats.percentage}%)
                        </p>

                        {filteredUsers.map(user => (
                            <UserItem
                                key={user.id}
                                user={user}
                                isSelected={selectedUsers.has(user.id)}
                                onToggle={handleUserToggle}
                            />
                        ))}

                        <button onClick={handleSelectionComplete}>
                            Confirm Selection
                        </button>
                    </div>
                );
            }
            ```

            **Când să folosești fiecare:**

            **useMemo:**
            - Expensive calculations (filtering, sorting, complex math)
            - Creating objects/arrays care se transmit ca props
            - Computed values bazate pe multiple dependencies

            **useCallback:**
            - Event handlers care se transmit la componente copil
            - Functions care sunt dependencies în alte hooks
            - API calls sau async operations
            - Când vrei să previi re-render-uri inutile
            """)

        st.markdown("### Întrebări de Nivel Avansat")

        with st.expander("6. Cum creezi un custom hook complex și care sunt best practices?"):
            st.markdown("""
            **Principii pentru Custom Hooks de calitate:**

            **1. Single Responsibility Principle:**
            ```javascript
            // ❌ Hook care face prea multe lucruri
            function useBadHook() {
                const [user, setUser] = useState(null);
                const [notifications, setNotifications] = useState([]);
                const [theme, setTheme] = useState('light');
                const [cart, setCart] = useState([]);
                // ... prea multe responsabilități
            }

            // ✅ Hooks focalizate pe o singură responsabilitate
            function useUser() {
                const [user, setUser] = useState(null);
                const [loading, setLoading] = useState(false);

                const login = useCallback(async (credentials) => {
                    setLoading(true);
                    try {
                        const userData = await authAPI.login(credentials);
                        setUser(userData);
                        return userData;
                    } finally {
                        setLoading(false);
                    }
                }, []);

                const logout = useCallback(() => {
                    setUser(null);
                    authAPI.logout();
                }, []);

                return { user, loading, login, logout };
            }
            ```

            **2. Composition over Complexity:**
            ```javascript
            // Hook de bază pentru API calls
            function useApi() {
                const [loading, setLoading] = useState(false);
                const [error, setError] = useState(null);

                const execute = useCallback(async (apiCall) => {
                    try {
                        setLoading(true);
                        setError(null);
                        return await apiCall();
                    } catch (err) {
                        setError(err);
                        throw err;
                    } finally {
                        setLoading(false);
                    }
                }, []);

                return { loading, error, execute };
            }

            // Hook specializat care combină useApi cu cache
            function useApiWithCache(cacheKey) {
                const { loading, error, execute } = useApi();
                const cache = useRef(new Map());

                const cachedExecute = useCallback(async (apiCall, options = {}) => {
                    const { forceRefresh = false, cacheTime = 5 * 60 * 1000 } = options;

                    if (!forceRefresh && cache.current.has(cacheKey)) {
                        const cached = cache.current.get(cacheKey);
                        const isExpired = Date.now() - cached.timestamp > cacheTime;

                        if (!isExpired) {
                            return cached.data;
                        }
                    }

                    const result = await execute(apiCall);
                    cache.current.set(cacheKey, {
                        data: result,
                        timestamp: Date.now()
                    });

                    return result;
                }, [execute, cacheKey]);

                const clearCache = useCallback(() => {
                    cache.current.delete(cacheKey);
                }, [cacheKey]);

                return { loading, error, execute: cachedExecute, clearCache };
            }

            // Hook de nivel înalt pentru entities
            function useEntityCollection(entityName, apiEndpoint) {
                const [entities, setEntities] = useState([]);
                const [selectedId, setSelectedId] = useState(null);
                const { loading, error, execute } = useApiWithCache(entityName);

                const load = useCallback(() => {
                    return execute(() => fetch(apiEndpoint).then(r => r.json()))
                        .then(setEntities);
                }, [execute, apiEndpoint]);

                const create = useCallback(async (data) => {
                    const newEntity = await execute(() => 
                        fetch(apiEndpoint, {
                            method: 'POST',
                            body: JSON.stringify(data),
                            headers: { 'Content-Type': 'application/json' }
                        }).then(r => r.json())
                    );

                    setEntities(prev => [...prev, newEntity]);
                    return newEntity;
                }, [execute, apiEndpoint]);

                // Auto-load pe mount
                useEffect(() => {
                    load();
                }, [load]);

                return {
                    entities,
                    selectedId,
                    loading,
                    error,
                    load,
                    create,
                    select: setSelectedId,
                    selectedEntity: entities.find(e => e.id === selectedId)
                };
            }
            ```

            **3. Type Safety și Validation:**
            ```javascript
            // Hook cu TypeScript pentru type safety
            interface UseFormOptions<T> {
                initialValues: T;
                validationSchema?: Record<keyof T, (value: any) => string | null>;
                onSubmit?: (values: T) => Promise<void> | void;
            }

            function useForm<T extends Record<string, any>>(options: UseFormOptions<T>) {
                const [values, setValues] = useState<T>(options.initialValues);
                const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});
                const [touched, setTouched] = useState<Partial<Record<keyof T, boolean>>>({});
                const [isSubmitting, setIsSubmitting] = useState(false);

                const setValue = useCallback((field: keyof T, value: any) => {
                    setValues(prev => ({ ...prev, [field]: value }));

                    // Validate field
                    if (options.validationSchema?.[field]) {
                        const error = options.validationSchema[field](value);
                        setErrors(prev => ({ ...prev, [field]: error }));
                    }
                }, [options.validationSchema]);

                const setTouchedField = useCallback((field: keyof T) => {
                    setTouched(prev => ({ ...prev, [field]: true }));
                }, []);

                const handleSubmit = useCallback(async (e?: React.FormEvent) => {
                    e?.preventDefault();
                    setIsSubmitting(true);

                    try {
                        await options.onSubmit?.(values);
                    } finally {
                        setIsSubmitting(false);
                    }
                }, [options.onSubmit, values]);

                return {
                    values,
                    errors,
                    touched,
                    isSubmitting,
                    setValue,
                    setTouched: setTouchedField,
                    handleSubmit
                };
            }
            ```

            **4. Testing Strategy:**
            ```javascript
            // Hook testabil
            function useCounter(initialValue = 0, options = {}) {
                const { min = -Infinity, max = Infinity, step = 1 } = options;
                const [count, setCount] = useState(initialValue);

                const increment = useCallback(() => {
                    setCount(prev => Math.min(prev + step, max));
                }, [step, max]);

                const decrement = useCallback(() => {
                    setCount(prev => Math.max(prev - step, min));
                }, [step, min]);

                const reset = useCallback(() => {
                    setCount(initialValue);
                }, [initialValue]);

                return {
                    count,
                    increment,
                    decrement,
                    reset,
                    canIncrement: count < max,
                    canDecrement: count > min
                };
            }

            // Test pentru hook
            import { renderHook, act } from '@testing-library/react-hooks';

            describe('useCounter', () => {
                it('should increment within bounds', () => {
                    const { result } = renderHook(() => 
                        useCounter(0, { min: 0, max: 5, step: 2 })
                    );

                    act(() => {
                        result.current.increment();
                    });

                    expect(result.current.count).toBe(2);
                    expect(result.current.canIncrement).toBe(true);

                    act(() => {
                        result.current.increment();
                        result.current.increment(); // Should hit max
                    });

                    expect(result.current.count).toBe(5);
                    expect(result.current.canIncrement).toBe(false);
                });
            });
            ```

            **Best Practices Summary:**
            - **Naming**: Începe cu 'use' și folosește nume descriptive
            - **Dependencies**: Minimizează și optimizează dependency arrays
            - **Error Handling**: Include loading și error states
            - **Cleanup**: Returnează cleanup functions unde e necesar
            - **Documentation**: Documentează parametrii și return values
            - **Testing**: Scrie teste pentru logica complexă
            - **TypeScript**: Folosește typing pentru safety
            """)

        with st.expander("7. Explică conceptul de 'stale closures' și cum să le eviți"):
            st.markdown("""
            **Stale Closures - Problema:**

            Stale closures apar când o funcție "înghețată" în closure referențiază 
            o valoare veche a unei variabile care s-a schimbat între timp.

            **Exemplu clasic - Timer cu stale closure:**
            ```javascript
            // ❌ PROBLEMĂ - count este "stale" în setInterval
            function BrokenTimer() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const timer = setInterval(() => {
                        // count aici este întotdeauna 0!
                        setCount(count + 1); // Numai primul increment funcționează
                    }, 1000);

                    return () => clearInterval(timer);
                }, []); // Empty deps - effect rulează o singură dată

                return <div>Count: {count}</div>;
            }

            // ✅ SOLUȚIE 1 - Functional update
            function FixedTimer() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const timer = setInterval(() => {
                        // Folosește previous value din state
                        setCount(prevCount => prevCount + 1);
                    }, 1000);

                    return () => clearInterval(timer);
                }, []); // OK - nu depinde de count

                return <div>Count: {count}</div>;
            }

            // ✅ SOLUȚIE 2 - Include în dependencies
            function FixedTimer2() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const timer = setInterval(() => {
                        setCount(count + 1); // count este fresh
                    }, 1000);

                    return () => clearInterval(timer);
                }, [count]); // Include count în dependencies

                return <div>Count: {count}</div>;
            }
            ```

            **Problema cu event listeners:**
            ```javascript
            // ❌ PROBLEMĂ - handleClick capturează valoarea inițială
            function ProblematicComponent() {
                const [count, setCount] = useState(0);

                useEffect(() => {
                    const handleClick = () => {
                        console.log('Count is:', count); // Întotdeauna 0!
                        setCount(count + 1); // Nu va funcționa corect
                    };

                    document.addEventListener('click', handleClick);

                    return () => {
                        document.removeEventListener('click', handleClick);
                    };
                }, []); // Empty deps - count rămâne stale

                return <div>Count: {count}</div>;
            }

            // ✅ SOLUȚIE - useRef pentru current value
            function FixedComponent() {
                const [count, setCount] = useState(0);
                const countRef = useRef(count);

                // Păstrează ref-ul sincronizat
                useEffect(() => {
                    countRef.current = count;
                });

                useEffect(() => {
                    const handleClick = () => {
                        console.log('Count is:', countRef.current); // Întotdeauna fresh!
                        setCount(prevCount => prevCount + 1);
                    };

                    document.addEventListener('click', handleClick);

                    return () => {
                        document.removeEventListener('click', handleClick);
                    };
                }, []); // OK - handleClick nu depinde de count

                return <div>Count: {count}</div>;
            }
            ```

            **Custom hook pentru current value:**
            ```javascript
            // Hook util pentru a obține întotdeauna current value
            function useCurrentValue(value) {
                const ref = useRef(value);

                useEffect(() => {
                    ref.current = value;
                });

                return ref;
            }

            // Utilizare
            function ComponentWithCurrentValue() {
                const [count, setCount] = useState(0);
                const [name, setName] = useState('');

                const currentCount = useCurrentValue(count);
                const currentName = useCurrentValue(name);

                useEffect(() => {
                    const handleSomeEvent = () => {
                        // Folosește întotdeauna valorile curente
                        console.log('Current count:', currentCount.current);
                        console.log('Current name:', currentName.current);
                    };

                    someEventEmitter.on('event', handleSomeEvent);

                    return () => {
                        someEventEmitter.off('event', handleSomeEvent);
                    };
                }, []); // Nu e nevoie de dependencies

                return (
                    <div>
                        <p>Count: {count}</p>
                        <button onClick={() => setCount(c => c + 1)}>+</button>

                        <input 
                            value={name} 
                            onChange={(e) => setName(e.target.value)} 
                        />
                    </div>
                );
            }
            ```

            **Stale closures în async functions:**
            ```javascript
            // ❌ PROBLEMĂ - async function cu stale closure
            function AsyncProblem() {
                const [user, setUser] = useState(null);
                const [data, setData] = useState(null);

                useEffect(() => {
                    const fetchData = async () => {
                        // Dacă user se schimbă în timpul acestui request...
                        const result = await api.getData(user.id);

                        // ...user poate fi deja diferit aici!
                        if (result.userId === user.id) { // Verificare stale!
                            setData(result);
                        }
                    };

                    if (user) {
                        fetchData();
                    }
                }, [user]); // user în dependencies, dar tot e risc de stale closure

                return <div>{data?.content}</div>;
            }

            // ✅ SOLUȚIE - Cleanup cu AbortController
            function AsyncFixed() {
                const [user, setUser] = useState(null);
                const [data, setData] = useState(null);

                useEffect(() => {
                    if (!user) return;

                    const abortController = new AbortController();

                    const fetchData = async () => {
                        try {
                            const result = await api.getData(user.id, {
                                signal: abortController.signal
                            });

                            // Nu verificăm user.id - dacă ajungem aici,
                            // înseamnă că request-ul nu a fost abortat
                            setData(result);
                        } catch (error) {
                            if (error.name !== 'AbortError') {
                                console.error('Fetch error:', error);
                            }
                        }
                    };

                    fetchData();

                    // Cleanup - anulează request-ul dacă user se schimbă
                    return () => {
                        abortController.abort();
                    };
                }, [user]);

                return <div>{data?.content}</div>;
            }
            ```

            **Strategii de prevenire:**

            **1. Functional Updates:**
            ```javascript
            // Folosește funcții pentru a accesa previous state
            setState(prevState => prevState + 1);
            ```

            **2. useRef pentru Current Values:**
            ```javascript
            const currentValueRef = useRef(value);
            useEffect(() => { currentValueRef.current = value; });
            ```

            **3. Include în Dependencies:**
            ```javascript
            useEffect(() => {
                // Use value here
            }, [value]); // Include toate valorile folosite
            ```

            **4. AbortController pentru Async:**
            ```javascript
            useEffect(() => {
                const controller = new AbortController();
                fetchData(controller.signal);
                return () => controller.abort();
            }, [dependencies]);
            ```

            **5. Custom Hooks pentru Pattern-uri Comune:**
            ```javascript
            function useLatestValue(value) {
                const ref = useRef(value);
                ref.current = value;
                return ref;
            }
            ```
            """)

        st.markdown("### Exerciții Practice Complexe")

        with st.expander("Exercițiul 1: Construiește un useInfiniteScroll hook"):
            st.markdown("""
            **Cerințe:**
            - Detectează când user-ul ajunge aproape de sfârșitul listei
            - Încarcă mai multe date automat
            - Gestionează loading și error states
            - Suportă refresh și retry
            - Optimizat pentru performance

            **Funcționalități extra:**
            - Threshold configurabil pentru loading
            - Cache pentru pagini încărcate
            - Virtual scrolling pentru liste mari
            - Suport pentru search și filtering

            **Interfața hook-ului:**
            ```javascript
            const {
                items,
                loading,
                error,
                hasMore,
                loadMore,
                refresh,
                retry
            } = useInfiniteScroll(fetchFunction, options);
            ```
            """)

        with st.expander("Exercițiul 2: Implementează useUndoRedo cu complex state"):
            st.markdown("""
            **Cerințe:**
            - Suportă undo/redo pentru orice tip de state
            - Limit configurabil pentru history size
            - Branch handling pentru undo apoi modificare nouă
            - Serialization pentru persistence
            - Optimizații pentru performance cu state mari

            **Advanced features:**
            - Batch operations pentru multiple changes
            - Conditional checkpoints (nu salva fiecare keystroke)
            - Time-based auto checkpoints
            - Integration cu keyboard shortcuts

            **API Design:**
            ```javascript
            const {
                state,
                setState,
                undo,
                redo,
                canUndo,
                canRedo,
                history,
                clearHistory,
                createCheckpoint
            } = useUndoRedo(initialState, options);
            ```
            """)

        st.markdown("### Best Practices Finale")

        st.markdown("""
        **Performance Optimization:**
        1. **Folosește useCallback pentru event handlers** care se transmit ca props
        2. **useMemo pentru expensive calculations** și object/array dependencies
        3. **React.memo pentru componente** care primesc props stabile
        4. **Lazy initialization** pentru useState cu valori expensive

        **Code Organization:**
        1. **Custom hooks pentru logica reutilizabilă** - separă business logic de UI
        2. **Hook composition** pentru funcționalități complexe
        3. **TypeScript pentru type safety** și developer experience mai bună
        4. **Naming conventions** clare și consistente

        **Testing:**
        1. **Unit tests pentru custom hooks** cu renderHook
        2. **Integration tests** pentru hook interactions
        3. **Mocking dependencies** pentru isolated testing
        4. **Performance testing** pentru hooks cu expensive operations

        **Error Handling:**
        1. **Error boundaries** pentru hook-uri care pot crash
        2. **Graceful degradation** când hooks fail
        3. **Proper cleanup** pentru resources (timers, subscriptions)
        4. **User feedback** pentru loading și error states

        **Security:**
        1. **Input validation** în custom hooks
        2. **Sanitization** pentru data handling
        3. **Rate limiting** pentru API calls
        4. **Memory leak prevention** cu proper cleanup
        """)

    st.markdown("""
    <div class="summary-box">
    <h3>Rezumat Capitol</h3>
    <p><strong>React Hooks</strong> au transformat fundamental modul în care scriem componente React. 
    De la hooks-urile de bază (useState, useEffect) la custom hooks complexe și patterns avansate, 
    stăpânirea acestor concepte este esențială pentru dezvoltarea aplicațiilor React moderne. 
    Practică cu exemple reale, testează hook-urile tale custom și urmează best practices-urile 
    pentru a scrie cod React de înaltă calitate și performant.</p>
    </div>
    """, unsafe_allow_html=True)


def blog_app_page():
    """Aplicația de Blog - Tutorial Complet React"""
    st.markdown('<h1 class="chapter-header">Construirea unei Aplicații de Blog Complete</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-box">
    <h3>Obiectivele Aplicației</h3>
    <p>Vom construi o aplicație de blog completă care demonstrează toate conceptele React învățate: 
    State & Props, Event Handling, Hooks, data fetching, form handling și optimizarea performance-ului. 
    Aplicația va include autentificare, CRUD operations, search, comentarii și interfață responsive.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Planning & Arhitectură",
        "API & Data Layer",
        "Core Components",
        "State Management",
        "Advanced Features",
        "Deployment & Testing"
    ])

    with tab1:
        st.markdown('<h2 class="section-header">Planning și Arhitectura Aplicației</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Structura Aplicației

        **Features principale:**
        - 📝 **Posts Management** - Creare, editare, ștergere, vizualizare
        - 👤 **User Authentication** - Login, register, profile management
        - 💬 **Comments System** - Comentarii cu replies și reactions
        - 🔍 **Search & Filter** - Căutare după title, content, tags, autor
        - 📱 **Responsive Design** - Funcțional pe mobile și desktop
        - ⚡ **Real-time Updates** - Live notifications și updates
        """)

        st.code("""
// Structura de foldere a proiectului
src/
├── components/          # Componente reutilizabile
│   ├── ui/             # UI primitives (Button, Input, Modal)
│   ├── forms/          # Form components (PostForm, CommentForm)
│   ├── layout/         # Layout components (Header, Footer, Sidebar)
│   └── features/       # Feature-specific components
├── hooks/              # Custom hooks
│   ├── useApi.js       # API communication
│   ├── useAuth.js      # Authentication logic
│   ├── usePosts.js     # Posts management
│   └── useComments.js  # Comments logic
├── context/            # React Context providers
│   ├── AuthContext.js  # Authentication state
│   ├── ThemeContext.js # Theme management
│   └── NotificationContext.js
├── services/           # API services și utilities
│   ├── api.js          # API client
│   ├── auth.js         # Authentication service
│   └── storage.js      # Local storage utilities
├── utils/              # Helper functions
│   ├── validation.js   # Form validation
│   ├── formatting.js   # Date, text formatting
│   └── constants.js    # App constants
└── pages/              # Page components
    ├── HomePage.js      # Posts list și hero
    ├── PostPage.js      # Individual post view
    ├── CreatePost.js    # Create/Edit post
    ├── ProfilePage.js   # User profile
    └── LoginPage.js     # Authentication
        """, language="javascript")

        st.markdown("### Componente și Props Flow")

        st.code("""
// Diagramă conceptuală a componentelor și data flow

App
├── AuthProvider (Context: user, login, logout)
│   ├── ThemeProvider (Context: theme, toggleTheme)
│   │   ├── NotificationProvider (Context: notifications, addNotification)
│   │   │   ├── Router
│   │   │   │   ├── Header (Props: user, onLogout)
│   │   │   │   ├── Routes
│   │   │   │   │   ├── HomePage
│   │   │   │   │   │   ├── PostsList (Props: posts, loading, onLoadMore)
│   │   │   │   │   │   │   └── PostCard (Props: post, onLike, onShare)
│   │   │   │   │   │   ├── SearchFilters (Props: filters, onFilterChange)
│   │   │   │   │   │   └── CreatePostButton (Props: onClick)
│   │   │   │   │   ├── PostPage
│   │   │   │   │   │   ├── PostDetail (Props: post, onEdit, onDelete)
│   │   │   │   │   │   └── CommentsSection
│   │   │   │   │   │       ├── CommentsList (Props: comments, onReply)
│   │   │   │   │   │       └── CommentForm (Props: postId, onSubmit)
│   │   │   │   │   └── CreatePost
│   │   │   │   │       └── PostForm (Props: initialData, onSubmit, onCancel)
│   │   │   │   └── Footer
│   │   │   └── NotificationContainer

// Data Flow Patterns demonstrează:
// - Props drilling vs Context pentru state global
// - Event bubbling pentru user interactions
// - Custom hooks pentru business logic
// - State lifting pentru shared state
        """, language="javascript")

        st.markdown("### API Design și Mock Data")

        st.code("""
// API endpoints pentru aplicația noastră
const API_ENDPOINTS = {
    // Authentication
    LOGIN: '/api/auth/login',
    REGISTER: '/api/auth/register',
    LOGOUT: '/api/auth/logout',
    ME: '/api/auth/me',

    // Posts
    POSTS: '/api/posts',
    POST_BY_ID: (id) => `/api/posts/${id}`,
    POST_LIKE: (id) => `/api/posts/${id}/like`,
    POST_SEARCH: '/api/posts/search',

    // Comments
    COMMENTS: (postId) => `/api/posts/${postId}/comments`,
    COMMENT_BY_ID: (id) => `/api/comments/${id}`,
    COMMENT_REPLY: (id) => `/api/comments/${id}/reply`,

    // Users
    USERS: '/api/users',
    USER_PROFILE: (id) => `/api/users/${id}`,
    USER_POSTS: (id) => `/api/users/${id}/posts`
};

// Mock data structure pentru development
const MOCK_DATA = {
    users: [
        {
            id: 1,
            username: 'john_doe',
            email: 'john@example.com',
            firstName: 'John',
            lastName: 'Doe',
            avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=John',
            bio: 'Passionate developer și blogger',
            createdAt: '2024-01-15T10:00:00Z',
            postsCount: 12,
            followersCount: 150
        }
    ],

    posts: [
        {
            id: 1,
            title: 'Introducere în React Hooks',
            slug: 'introducere-react-hooks',
            content: 'React Hooks au revoluționat modul în care scriem componente...',
            excerpt: 'Învață cum să folosești React Hooks pentru componente mai curate și reutilizabile.',
            author: {
                id: 1,
                username: 'john_doe',
                firstName: 'John',
                lastName: 'Doe',
                avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=John'
            },
            tags: ['react', 'javascript', 'frontend', 'hooks'],
            coverImage: 'https://picsum.photos/800/400?random=1',
            publishedAt: '2024-08-01T10:00:00Z',
            updatedAt: '2024-08-01T10:00:00Z',
            readTime: 8,
            likesCount: 42,
            commentsCount: 7,
            isLiked: false,
            isPublished: true,
            category: 'Tutorial'
        }
    ],

    comments: [
        {
            id: 1,
            postId: 1,
            parentId: null, // null pentru top-level comments
            author: {
                id: 2,
                username: 'jane_smith',
                firstName: 'Jane',
                lastName: 'Smith',
                avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Jane'
            },
            content: 'Excelent tutorial! M-a ajutat să înțeleg useState mult mai bine.',
            createdAt: '2024-08-01T14:30:00Z',
            updatedAt: '2024-08-01T14:30:00Z',
            likesCount: 5,
            isLiked: true,
            replies: []
        }
    ]
};

// API Service Layer - abstractizează comunicarea cu serverul
class ApiService {
    constructor(baseURL = 'http://localhost:3001') {
        this.baseURL = baseURL;
        this.token = localStorage.getItem('authToken');
    }

    // Generic request method cu error handling
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };

        // Add auth token dacă există
        if (this.token) {
            headers.Authorization = `Bearer ${this.token}`;
        }

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            // Handle HTTP errors
            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.message || `HTTP ${response.status}: ${response.statusText}`);
            }

            // Handle empty responses
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.includes('application/json')) {
                return await response.json();
            }

            return response;
        } catch (error) {
            // Network errors, parsing errors, etc.
            console.error('API Request failed:', error);
            throw error;
        }
    }

    // Authentication methods
    async login(credentials) {
        const response = await this.request(API_ENDPOINTS.LOGIN, {
            method: 'POST',
            body: JSON.stringify(credentials)
        });

        if (response.token) {
            this.token = response.token;
            localStorage.setItem('authToken', response.token);
        }

        return response;
    }

    async logout() {
        try {
            await this.request(API_ENDPOINTS.LOGOUT, { method: 'POST' });
        } finally {
            this.token = null;
            localStorage.removeItem('authToken');
        }
    }

    // Posts methods
    async getPosts(params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const endpoint = queryString ? `${API_ENDPOINTS.POSTS}?${queryString}` : API_ENDPOINTS.POSTS;
        return this.request(endpoint);
    }

    async getPost(id) {
        return this.request(API_ENDPOINTS.POST_BY_ID(id));
    }

    async createPost(postData) {
        return this.request(API_ENDPOINTS.POSTS, {
            method: 'POST',
            body: JSON.stringify(postData)
        });
    }

    async updatePost(id, postData) {
        return this.request(API_ENDPOINTS.POST_BY_ID(id), {
            method: 'PUT',
            body: JSON.stringify(postData)
        });
    }

    async deletePost(id) {
        return this.request(API_ENDPOINTS.POST_BY_ID(id), {
            method: 'DELETE'
        });
    }

    async likePost(id) {
        return this.request(API_ENDPOINTS.POST_LIKE(id), {
            method: 'POST'
        });
    }
}

// Singleton instance
export const apiService = new ApiService();
        """, language="javascript")

    with tab2:
        st.markdown('<h2 class="section-header">API Integration și Data Layer</h2>', unsafe_allow_html=True)

        st.markdown("### Custom Hooks pentru Data Management")

        st.code("""
// hooks/useApi.js - Generic API hook cu loading și error handling
import { useState, useCallback, useRef } from 'react';

export function useApi() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // AbortController pentru cleanup
    const abortControllerRef = useRef(null);

    const execute = useCallback(async (apiCall, options = {}) => {
        const { 
            showLoading = true, 
            onSuccess, 
            onError,
            abortPrevious = true 
        } = options;

        try {
            // Abort previous request dacă e necesar
            if (abortPrevious && abortControllerRef.current) {
                abortControllerRef.current.abort();
            }

            // Create new AbortController
            abortControllerRef.current = new AbortController();

            if (showLoading) setLoading(true);
            setError(null);

            // Execute API call cu abort signal
            const result = await apiCall(abortControllerRef.current.signal);

            onSuccess?.(result);
            return result;

        } catch (err) {
            if (err.name !== 'AbortError') {
                setError(err);
                onError?.(err);
                throw err;
            }
        } finally {
            if (showLoading) setLoading(false);
        }
    }, []);

    // Cancel ongoing requests
    const cancel = useCallback(() => {
        if (abortControllerRef.current) {
            abortControllerRef.current.abort();
        }
    }, []);

    // Clear error
    const clearError = useCallback(() => {
        setError(null);
    }, []);

    return {
        loading,
        error,
        execute,
        cancel,
        clearError
    };
}

// hooks/useAuth.js - Authentication logic cu Context
import { createContext, useContext, useReducer, useEffect, useCallback } from 'react';
import { apiService } from '../services/api';

// Auth reducer pentru complex state management
const authReducer = (state, action) => {
    switch (action.type) {
        case 'LOGIN_START':
            return {
                ...state,
                loading: true,
                error: null
            };

        case 'LOGIN_SUCCESS':
            return {
                ...state,
                loading: false,
                isAuthenticated: true,
                user: action.payload.user,
                token: action.payload.token,
                error: null
            };

        case 'LOGIN_FAILURE':
            return {
                ...state,
                loading: false,
                isAuthenticated: false,
                user: null,
                token: null,
                error: action.payload
            };

        case 'LOGOUT':
            return {
                ...state,
                isAuthenticated: false,
                user: null,
                token: null,
                error: null
            };

        case 'UPDATE_USER':
            return {
                ...state,
                user: { ...state.user, ...action.payload }
            };

        case 'CLEAR_ERROR':
            return {
                ...state,
                error: null
            };

        default:
            return state;
    }
};

const initialAuthState = {
    isAuthenticated: false,
    user: null,
    token: null,
    loading: false,
    error: null
};

// Context pentru Auth
const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [state, dispatch] = useReducer(authReducer, initialAuthState);

    // Load user from localStorage la mount
    useEffect(() => {
        const token = localStorage.getItem('authToken');
        const userData = localStorage.getItem('userData');

        if (token && userData) {
            try {
                const user = JSON.parse(userData);
                dispatch({
                    type: 'LOGIN_SUCCESS',
                    payload: { user, token }
                });
                // Set token în api service
                apiService.token = token;
            } catch (error) {
                // Invalid stored data
                localStorage.removeItem('authToken');
                localStorage.removeItem('userData');
            }
        }
    }, []);

    // Login function
    const login = useCallback(async (credentials) => {
        dispatch({ type: 'LOGIN_START' });

        try {
            const response = await apiService.login(credentials);

            // Store în localStorage
            localStorage.setItem('authToken', response.token);
            localStorage.setItem('userData', JSON.stringify(response.user));

            dispatch({
                type: 'LOGIN_SUCCESS',
                payload: response
            });

            return response;
        } catch (error) {
            dispatch({
                type: 'LOGIN_FAILURE',
                payload: error.message
            });
            throw error;
        }
    }, []);

    // Logout function
    const logout = useCallback(async () => {
        try {
            await apiService.logout();
        } finally {
            // Clear storage indiferent de API response
            localStorage.removeItem('authToken');
            localStorage.removeItem('userData');
            dispatch({ type: 'LOGOUT' });
        }
    }, []);

    // Register function
    const register = useCallback(async (userData) => {
        dispatch({ type: 'LOGIN_START' });

        try {
            const response = await apiService.register(userData);

            localStorage.setItem('authToken', response.token);
            localStorage.setItem('userData', JSON.stringify(response.user));

            dispatch({
                type: 'LOGIN_SUCCESS',
                payload: response
            });

            return response;
        } catch (error) {
            dispatch({
                type: 'LOGIN_FAILURE',
                payload: error.message
            });
            throw error;
        }
    }, []);

    // Update user profile
    const updateProfile = useCallback(async (updates) => {
        try {
            const updatedUser = await apiService.updateProfile(updates);

            // Update localStorage
            localStorage.setItem('userData', JSON.stringify(updatedUser));

            dispatch({
                type: 'UPDATE_USER',
                payload: updatedUser
            });

            return updatedUser;
        } catch (error) {
            throw error;
        }
    }, []);

    const clearError = useCallback(() => {
        dispatch({ type: 'CLEAR_ERROR' });
    }, []);

    const value = {
        ...state,
        login,
        logout,
        register,
        updateProfile,
        clearError
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

// Custom hook pentru folosirea auth context
export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}

// hooks/usePosts.js - Posts management cu caching
import { useState, useCallback, useMemo } from 'react';
import { apiService } from '../services/api';
import { useApi } from './useApi';

export function usePosts() {
    const [posts, setPosts] = useState([]);
    const [currentPost, setCurrentPost] = useState(null);
    const [totalPages, setTotalPages] = useState(0);
    const [currentPage, setCurrentPage] = useState(1);
    const [filters, setFilters] = useState({
        search: '',
        category: '',
        tag: '',
        author: ''
    });

    const { loading, error, execute } = useApi();

    // Load posts cu pagination și filtering
    const loadPosts = useCallback(async (page = 1, newFilters = {}) => {
        const params = {
            page,
            limit: 10,
            ...filters,
            ...newFilters
        };

        const result = await execute(() => apiService.getPosts(params));

        if (page === 1) {
            setPosts(result.posts);
        } else {
            // Append pentru infinite scroll
            setPosts(prev => [...prev, ...result.posts]);
        }

        setCurrentPage(page);
        setTotalPages(result.totalPages);

        return result;
    }, [execute, filters]);

    // Load single post
    const loadPost = useCallback(async (id) => {
        const post = await execute(() => apiService.getPost(id));
        setCurrentPost(post);
        return post;
    }, [execute]);

    // Create new post
    const createPost = useCallback(async (postData) => {
        const newPost = await execute(() => apiService.createPost(postData));

        // Add la începutul listei
        setPosts(prev => [newPost, ...prev]);

        return newPost;
    }, [execute]);

    // Update post
    const updatePost = useCallback(async (id, updates) => {
        const updatedPost = await execute(() => apiService.updatePost(id, updates));

        // Update în listă
        setPosts(prev => prev.map(post => 
            post.id === id ? updatedPost : post
        ));

        // Update current post dacă e același
        if (currentPost?.id === id) {
            setCurrentPost(updatedPost);
        }

        return updatedPost;
    }, [execute, currentPost]);

    // Delete post
    const deletePost = useCallback(async (id) => {
        await execute(() => apiService.deletePost(id));

        // Remove din listă
        setPosts(prev => prev.filter(post => post.id !== id));

        // Clear current post dacă e același
        if (currentPost?.id === id) {
            setCurrentPost(null);
        }
    }, [execute, currentPost]);

    // Like/unlike post
    const toggleLike = useCallback(async (id) => {
        const result = await execute(() => apiService.likePost(id));

        // Update în listă
        setPosts(prev => prev.map(post => 
            post.id === id 
                ? { 
                    ...post, 
                    isLiked: result.isLiked,
                    likesCount: result.likesCount 
                }
                : post
        ));

        // Update current post
        if (currentPost?.id === id) {
            setCurrentPost(prev => ({
                ...prev,
                isLiked: result.isLiked,
                likesCount: result.likesCount
            }));
        }

        return result;
    }, [execute, currentPost]);

    // Update filters
    const updateFilters = useCallback((newFilters) => {
        setFilters(prev => ({ ...prev, ...newFilters }));
        // Reset la prima pagină când schimbăm filtrele
        setCurrentPage(1);
    }, []);

    // Load more pentru infinite scroll
    const loadMore = useCallback(() => {
        if (currentPage < totalPages && !loading) {
            return loadPosts(currentPage + 1);
        }
    }, [currentPage, totalPages, loading, loadPosts]);

    // Refresh posts
    const refresh = useCallback(() => {
        return loadPosts(1, filters);
    }, [loadPosts, filters]);

    // Computed values
    const hasMore = currentPage < totalPages;
    const isEmpty = posts.length === 0 && !loading;

    return {
        // Data
        posts,
        currentPost,
        filters,

        // Pagination
        currentPage,
        totalPages,
        hasMore,

        // State
        loading,
        error,
        isEmpty,

        // Actions
        loadPosts,
        loadPost,
        createPost,
        updatePost,
        deletePost,
        toggleLike,
        updateFilters,
        loadMore,
        refresh,

        // Utilities
        getPostById: (id) => posts.find(post => post.id === id),
        searchPosts: (query) => posts.filter(post => 
            post.title.toLowerCase().includes(query.toLowerCase()) ||
            post.content.toLowerCase().includes(query.toLowerCase())
        )
    };
}
        """, language="javascript")

        st.markdown("### Error Handling și Loading States")

        st.code("""
// components/ui/ErrorBoundary.js - Error boundary pentru catching JS errors
import React from 'react';

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
            error,
            errorInfo
        });

        // Log error pentru monitoring
        console.error('Error caught by boundary:', error, errorInfo);

        // Send error la logging service în production
        if (process.env.NODE_ENV === 'production') {
            // logErrorToService(error, errorInfo);
        }
    }

    render() {
        if (this.state.hasError) {
            if (this.props.fallback) {
                return this.props.fallback(this.state.error, this.state.errorInfo);
            }

            return (
                <div className="error-boundary">
                    <h2>😵 Something went wrong</h2>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        <summary>Error details (pentru development)</summary>
                        {this.state.error && this.state.error.toString()}
                        <br />
                        {this.state.errorInfo.componentStack}
                    </details>
                    <button 
                        onClick={() => this.setState({ hasError: false, error: null, errorInfo: null })}
                    >
                        Try Again
                    </button>
                </div>
            );
        }

        return this.props.children;
    }
}

// components/ui/LoadingSpinner.js - Reusable loading component
export function LoadingSpinner({ size = 'medium', text = 'Loading...' }) {
    const sizeClasses = {
        small: 'w-4 h-4',
        medium: 'w-8 h-8',
        large: 'w-12 h-12'
    };

    return (
        <div className="flex items-center justify-center space-x-2">
            <div className={`animate-spin rounded-full border-2 border-gray-300 border-t-blue-600 ${sizeClasses[size]}`}></div>
            {text && <span className="text-gray-600">{text}</span>}
        </div>
    );
}

// components/ui/ErrorMessage.js - Error display cu retry functionality
export function ErrorMessage({ error, onRetry, className = '' }) {
    const getErrorMessage = (error) => {
        if (typeof error === 'string') return error;
        if (error?.message) return error.message;
        if (error?.error) return error.error;
        return 'An unexpected error occurred';
    };

    const isNetworkError = error?.message?.includes('fetch') || 
                          error?.name === 'NetworkError' ||
                          error?.code === 'NETWORK_ERROR';

    return (
        <div className={`bg-red-50 border border-red-200 rounded-lg p-4 ${className}`}>
            <div className="flex items-start">
                <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                </div>

                <div className="ml-3 flex-1">
                    <h3 className="text-sm font-medium text-red-800">
                        {isNetworkError ? 'Connection Error' : 'Error'}
                    </h3>
                    <p className="mt-1 text-sm text-red-700">
                        {getErrorMessage(error)}
                    </p>

                    {isNetworkError && (
                        <p className="mt-1 text-xs text-red-600">
                            Please check your internet connection and try again.
                        </p>
                    )}

                    {onRetry && (
                        <div className="mt-3">
                            <button
                                onClick={onRetry}
                                className="bg-red-100 hover:bg-red-200 text-red-800 px-3 py-1 rounded text-sm font-medium transition-colors"
                            >
                                Try Again
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

// hooks/useErrorHandler.js - Global error handling
import { useCallback } from 'react';
import { useNotification } from './useNotification';

export function useErrorHandler() {
    const { addNotification } = useNotification();

    const handleError = useCallback((error, options = {}) => {
        const {
            showNotification = true,
            notificationType = 'error',
            customMessage,
            logError = true
        } = options;

        // Log error pentru debugging
        if (logError) {
            console.error('Error handled:', error);
        }

        // Show user-friendly notification
        if (showNotification) {
            const message = customMessage || getErrorMessage(error);
            addNotification({
                type: notificationType,
                message,
                duration: 5000
            });
        }

        // Report error la monitoring service în production
        if (process.env.NODE_ENV === 'production') {
            // reportError(error);
        }

        return error;
    }, [addNotification]);

    const getErrorMessage = (error) => {
        // Network errors
        if (error?.message?.includes('fetch') || error?.name === 'NetworkError') {
            return 'Connection error. Please check your internet and try again.';
        }

        // Authentication errors
        if (error?.status === 401 || error?.message?.includes('unauthorized')) {
            return 'Session expired. Please log in again.';
        }

        // Permission errors
        if (error?.status === 403) {
            return 'You do not have permission to perform this action.';
        }

        // Not found errors
        if (error?.status === 404) {
            return 'The requested resource was not found.';
        }

        // Server errors
        if (error?.status >= 500) {
            return 'Server error. Please try again later.';
        }

        // Custom error messages
        if (error?.message) {
            return error.message;
        }

        return 'An unexpected error occurred. Please try again.';
    };

    return { handleError };
}

// Wrapper component pentru automatic error handling
export function withErrorHandling(WrappedComponent) {
    return function ErrorHandledComponent(props) {
        const { handleError } = useErrorHandler();

        return (
            <ErrorBoundary
                fallback={(error, errorInfo) => (
                    <ErrorMessage 
                        error={error} 
                        onRetry={() => window.location.reload()}
                    />
                )}
            >
                <WrappedComponent 
                    {...props} 
                    onError={handleError}
                />
            </ErrorBoundary>
        );
    };
}
        """, language="javascript")

    with tab3:
        st.markdown('<h2 class="section-header">Core Components Implementation</h2>', unsafe_allow_html=True)

        st.markdown("### Layout Components cu Context Integration")

        st.code("""
// components/layout/Header.js - Main navigation cu authentication
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth';
import { useTheme } from '../../hooks/useTheme';

export function Header() {
    const { user, isAuthenticated, logout } = useAuth();
    const { theme, toggleTheme } = useTheme();
    const navigate = useNavigate();

    const handleLogout = async () => {
        try {
            await logout();
            navigate('/');
        } catch (error) {
            console.error('Logout failed:', error);
        }
    };

    return (
        <header className="bg-white dark:bg-gray-800 shadow-md border-b border-gray-200 dark:border-gray-700">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">
                    {/* Logo și Navigation */}
                    <div className="flex items-center space-x-8">
                        <Link 
                            to="/" 
                            className="flex items-center space-x-2 text-xl font-bold text-gray-900 dark:text-white"
                        >
                            <svg className="w-8 h-8 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span>DevBlog</span>
                        </Link>

                        <nav className="hidden md:flex space-x-6">
                            <Link 
                                to="/" 
                                className="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                            >
                                Home
                            </Link>
                            <Link 
                                to="/posts" 
                                className="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                            >
                                Posts
                            </Link>
                            {isAuthenticated && (
                                <Link 
                                    to="/create" 
                                    className="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                                >
                                    Write
                                </Link>
                            )}
                        </nav>
                    </div>

                    {/* Search Bar */}
                    <div className="hidden md:block flex-1 max-w-lg mx-8">
                        <SearchBar />
                    </div>

                    {/* User Actions */}
                    <div className="flex items-center space-x-4">
                        {/* Theme Toggle */}
                        <button
                            onClick={toggleTheme}
                            className="p-2 rounded-lg bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
                            aria-label="Toggle theme"
                        >
                            {theme === 'light' ? (
                                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
                                </svg>
                            ) : (
                                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clipRule="evenodd" />
                                </svg>
                            )}
                        </button>

                        {isAuthenticated ? (
                            <UserMenu user={user} onLogout={handleLogout} />
                        ) : (
                            <div className="flex items-center space-x-2">
                                <Link
                                    to="/login"
                                    className="px-4 py-2 text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                                >
                                    Login
                                </Link>
                                <Link
                                    to="/register"
                                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                                >
                                    Sign Up
                                </Link>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
}

// UserMenu component cu dropdown
function UserMenu({ user, onLogout }) {
    const [isOpen, setIsOpen] = useState(false);
    const menuRef = useRef(null);

    // Close menu când se face click outside
    useEffect(() => {
        function handleClickOutside(event) {
            if (menuRef.current && !menuRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        }

        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    return (
        <div className="relative" ref={menuRef}>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="flex items-center space-x-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
            >
                <img
                    src={user.avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${user.username}`}
                    alt={user.username}
                    className="w-8 h-8 rounded-full"
                />
                <span className="hidden md:block text-gray-700 dark:text-gray-300">
                    {user.firstName || user.username}
                </span>
                <svg 
                    className={`w-4 h-4 text-gray-500 transition-transform ${isOpen ? 'rotate-180' : ''}`}
                    fill="currentColor" 
                    viewBox="0 0 20 20"
                >
                    <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
            </button>

            {isOpen && (
                <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 py-1 z-50">
                    <Link
                        to={`/profile/${user.id}`}
                        className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                        onClick={() => setIsOpen(false)}
                    >
                        Profile
                    </Link>
                    <Link
                        to="/settings"
                        className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                        onClick={() => setIsOpen(false)}
                    >
                        Settings
                    </Link>
                    <Link
                        to="/my-posts"
                        className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                        onClick={() => setIsOpen(false)}
                    >
                        My Posts
                    </Link>
                    <hr className="my-1 border-gray-200 dark:border-gray-600" />
                    <button
                        onClick={() => {
                            setIsOpen(false);
                            onLogout();
                        }}
                        className="block w-full text-left px-4 py-2 text-red-600 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                    >
                        Logout
                    </button>
                </div>
            )}
        </div>
    );
}

// components/features/SearchBar.js - Search cu debounce
import { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDebounce } from '../../hooks/useDebounce';

function SearchBar() {
    const [query, setQuery] = useState('');
    const [isOpen, setIsOpen] = useState(false);
    const [suggestions, setSuggestions] = useState([]);
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();
    const debouncedQuery = useDebounce(query, 300);

    // Load suggestions când query se schimbă
    useEffect(() => {
        if (debouncedQuery.length >= 2) {
            loadSuggestions(debouncedQuery);
        } else {
            setSuggestions([]);
            setIsOpen(false);
        }
    }, [debouncedQuery]);

    const loadSuggestions = async (searchQuery) => {
        try {
            setLoading(true);
            const response = await apiService.searchSuggestions(searchQuery);
            setSuggestions(response.suggestions);
            setIsOpen(response.suggestions.length > 0);
        } catch (error) {
            console.error('Failed to load suggestions:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (query.trim()) {
            navigate(`/search?q=${encodeURIComponent(query.trim())}`);
            setIsOpen(false);
        }
    };

    const handleSuggestionClick = (suggestion) => {
        setQuery(suggestion.title);
        setIsOpen(false);

        if (suggestion.type === 'post') {
            navigate(`/posts/${suggestion.id}`);
        } else if (suggestion.type === 'user') {
            navigate(`/profile/${suggestion.id}`);
        } else {
            navigate(`/search?q=${encodeURIComponent(suggestion.title)}`);
        }
    };

    return (
        <div className="relative">
            <form onSubmit={handleSubmit} className="relative">
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search posts, authors..."
                    className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg className="h-5 w-5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd" />
                    </svg>
                </div>
                {loading && (
                    <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
                        <div className="animate-spin rounded-full h-4 w-4 border-2 border-gray-300 border-t-blue-600"></div>
                    </div>
                )}
            </form>

            {isOpen && suggestions.length > 0 && (
                <div className="absolute z-50 w-full mt-1 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 max-h-96 overflow-y-auto">
                    {suggestions.map((suggestion, index) => (
                        <button
                            key={index}
                            onClick={() => handleSuggestionClick(suggestion)}
                            className="w-full px-4 py-3 text-left hover:bg-gray-50 dark:hover:bg-gray-700 border-b border-gray-100 dark:border-gray-600 last:border-b-0 transition-colors"
                        >
                            <div className="flex items-center space-x-3">
                                {suggestion.type === 'post' && (
                                    <svg className="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clipRule="evenodd" />
                                    </svg>
                                )}
                                {suggestion.type === 'user' && (
                                    <svg className="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                                    </svg>
                                )}
                                <div className="flex-1 min-w-0">
                                    <p className="text-sm font-medium text-gray-900 dark:text-gray-100 truncate">
                                        {suggestion.title}
                                    </p>
                                    {suggestion.subtitle && (
                                        <p className="text-xs text-gray-500 dark:text-gray-400 truncate">
                                            {suggestion.subtitle}
                                        </p>
                                    )}
                                </div>
                            </div>
                        </button>
                    ))}
                </div>
            )}
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Posts Components cu Event Handling")

        st.code("""
// components/features/PostCard.js - Individual post card cu interactions
import React, { useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { formatDistanceToNow } from 'date-fns';
import { useAuth } from '../../hooks/useAuth';

export function PostCard({ 
    post, 
    onLike, 
    onShare, 
    onDelete, 
    showActions = true,
    className = '' 
}) {
    const { user, isAuthenticated } = useAuth();
    const [isLiking, setIsLiking] = useState(false);
    const [showShareMenu, setShowShareMenu] = useState(false);

    // Like/unlike functionality cu optimistic updates
    const handleLike = useCallback(async (e) => {
        e.preventDefault(); // Prevent navigation dacă e în Link

        if (!isAuthenticated) {
            // Redirect to login sau show modal
            return;
        }

        if (isLiking) return; // Prevent double clicks

        try {
            setIsLiking(true);
            await onLike(post.id);
        } catch (error) {
            console.error('Failed to like post:', error);
        } finally {
            setIsLiking(false);
        }
    }, [post.id, onLike, isAuthenticated, isLiking]);

    // Share functionality
    const handleShare = useCallback((platform) => {
        const url = `${window.location.origin}/posts/${post.id}`;
        const text = `Check out this post: ${post.title}`;

        switch (platform) {
            case 'twitter':
                window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`);
                break;
            case 'facebook':
                window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`);
                break;
            case 'linkedin':
                window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`);
                break;
            case 'copy':
                navigator.clipboard.writeText(url);
                // Show toast notification
                break;
            default:
                onShare?.(post.id, platform);
        }

        setShowShareMenu(false);
    }, [post.id, post.title, onShare]);

    // Delete cu confirmation
    const handleDelete = useCallback(async () => {
        if (window.confirm('Are you sure you want to delete this post?')) {
            try {
                await onDelete(post.id);
            } catch (error) {
                console.error('Failed to delete post:', error);
            }
        }
    }, [post.id, onDelete]);

    const canEdit = user?.id === post.author.id;
    const isLiked = post.isLiked;
    const likesCount = post.likesCount;

    return (
        <article className={`bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 overflow-hidden ${className}`}>
            {/* Cover Image */}
            {post.coverImage && (
                <Link to={`/posts/${post.id}`}>
                    <img
                        src={post.coverImage}
                        alt={post.title}
                        className="w-full h-48 object-cover hover:scale-105 transition-transform duration-200"
                    />
                </Link>
            )}

            <div className="p-6">
                {/* Author și Date */}
                <div className="flex items-center space-x-3 mb-4">
                    <Link to={`/profile/${post.author.id}`}>
                        <img
                            src={post.author.avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${post.author.username}`}
                            alt={post.author.username}
                            className="w-10 h-10 rounded-full hover:ring-2 hover:ring-blue-500 transition-all"
                        />
                    </Link>
                    <div className="flex-1 min-w-0">
                        <Link 
                            to={`/profile/${post.author.id}`}
                            className="text-sm font-medium text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                        >
                            {post.author.firstName} {post.author.lastName}
                        </Link>
                        <p className="text-xs text-gray-500 dark:text-gray-400">
                            {formatDistanceToNow(new Date(post.publishedAt), { addSuffix: true })} 
                            {post.readTime && ` • ${post.readTime} min read`}
                        </p>
                    </div>

                    {/* More options pentru author */}
                    {canEdit && (
                        <div className="relative">
                            <DropdownMenu
                                trigger={
                                    <button className="p-2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                                        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                                            <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
                                        </svg>
                                    </button>
                                }
                                items={[
                                    {
                                        label: 'Edit',
                                        icon: 'edit',
                                        onClick: () => navigate(`/posts/${post.id}/edit`)
                                    },
                                    {
                                        label: 'Delete',
                                        icon: 'delete',
                                        onClick: handleDelete,
                                        className: 'text-red-600 hover:bg-red-50'
                                    }
                                ]}
                            />
                        </div>
                    )}
                </div>

                {/* Title și Content */}
                <Link to={`/posts/${post.id}`} className="block group">
                    <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors mb-2 line-clamp-2">
                        {post.title}
                    </h2>
                    <p className="text-gray-600 dark:text-gray-300 mb-4 line-clamp-3">
                        {post.excerpt}
                    </p>
                </Link>

                {/* Tags */}
                {post.tags && post.tags.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-4">
                        {post.tags.slice(0, 3).map(tag => (
                            <Link
                                key={tag}
                                to={`/posts?tag=${tag}`}
                                className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 text-xs rounded-full hover:bg-blue-100 dark:hover:bg-blue-900 hover:text-blue-700 dark:hover:text-blue-300 transition-colors"
                            >
                                #{tag}
                            </Link>
                        ))}
                        {post.tags.length > 3 && (
                            <span className="px-2 py-1 text-gray-500 text-xs">
                                +{post.tags.length - 3} more
                            </span>
                        )}
                    </div>
                )}

                {/* Actions Bar */}
                {showActions && (
                    <div className="flex items-center justify-between pt-4 border-t border-gray-200 dark:border-gray-700">
                        <div className="flex items-center space-x-4">
                            {/* Like Button */}
                            <button
                                onClick={handleLike}
                                disabled={isLiking || !isAuthenticated}
                                className={`flex items-center space-x-1 px-3 py-1 rounded-full transition-colors ${
                                    isLiked 
                                        ? 'text-red-600 bg-red-50 dark:bg-red-900/20' 
                                        : 'text-gray-500 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20'
                                } ${isLiking ? 'opacity-50 cursor-not-allowed' : ''}`}
                            >
                                <svg 
                                    className={`w-4 h-4 ${isLiked ? 'fill-current' : 'stroke-current fill-none'}`} 
                                    viewBox="0 0 24 24"
                                >
                                    <path 
                                        strokeLinecap="round" 
                                        strokeLinejoin="round" 
                                        strokeWidth={2} 
                                        d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" 
                                    />
                                </svg>
                                <span className="text-sm">{likesCount}</span>
                            </button>

                            {/* Comments */}
                            <Link
                                to={`/posts/${post.id}#comments`}
                                className="flex items-center space-x-1 px-3 py-1 text-gray-500 hover:text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-full transition-colors"
                            >
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                                </svg>
                                <span className="text-sm">{post.commentsCount}</span>
                            </Link>
                        </div>

                        {/* Share Button */}
                        <div className="relative">
                            <button
                                onClick={() => setShowShareMenu(!showShareMenu)}
                                className="p-2 text-gray-500 hover:text-gray-700 dark:hover:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full transition-colors"
                                aria-label="Share post"
                            >
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z" />
                                </svg>
                            </button>

                            {showShareMenu && (
                                <div className="absolute right-0 bottom-full mb-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 py-1 z-10">
                                    <button
                                        onClick={() => handleShare('twitter')}
                                        className="w-full px-4 py-2 text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                                    >
                                        Share on Twitter
                                    </button>
                                    <button
                                        onClick={() => handleShare('facebook')}
                                        className="w-full px-4 py-2 text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                                    >
                                        Share on Facebook
                                    </button>
                                    <button
                                        onClick={() => handleShare('linkedin')}
                                        className="w-full px-4 py-2 text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                                    >
                                        Share on LinkedIn
                                    </button>
                                    <button
                                        onClick={() => handleShare('copy')}
                                        className="w-full px-4 py-2 text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                                    >
                                        Copy Link
                                    </button>
                                </div>
                            )}
                        </div>
                    </div>
                )}
            </div>
        </article>
    );
}

// components/features/PostsList.js - Lista de posts cu infinite scroll
import { useEffect, useRef, useCallback } from 'react';
import { usePosts } from '../../hooks/usePosts';
import { LoadingSpinner } from '../ui/LoadingSpinner';
import { ErrorMessage } from '../ui/ErrorMessage';

export function PostsList({ filters = {}, className = '' }) {
    const {
        posts,
        loading,
        error,
        hasMore,
        loadPosts,
        loadMore,
        toggleLike,
        refresh
    } = usePosts();

    // Ref pentru intersection observer
    const loadMoreRef = useRef();

    // Load posts la mount și când se schimbă filters
    useEffect(() => {
        loadPosts(1, filters);
    }, [loadPosts, filters]);

    // Intersection Observer pentru infinite scroll
    useEffect(() => {
        const observer = new IntersectionObserver(
            (entries) => {
                if (entries[0].isIntersecting && hasMore && !loading) {
                    loadMore();
                }
            },
            { threshold: 0.1 }
        );

        if (loadMoreRef.current) {
            observer.observe(loadMoreRef.current);
        }

        return () => {
            if (loadMoreRef.current) {
                observer.unobserve(loadMoreRef.current);
            }
        };
    }, [hasMore, loading, loadMore]);

    const handleLike = useCallback(async (postId) => {
        try {
            await toggleLike(postId);
        } catch (error) {
            console.error('Failed to toggle like:', error);
        }
    }, [toggleLike]);

    if (error && posts.length === 0) {
        return (
            <ErrorMessage 
                error={error} 
                onRetry={refresh}
                className="max-w-md mx-auto"
            />
        );
    }

    return (
        <div className={`space-y-6 ${className}`}>
            {posts.length === 0 && !loading ? (
                <div className="text-center py-12">
                    <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <h3 className="mt-2 text-sm font-medium text-gray-900 dark:text-gray-100">No posts found</h3>
                    <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                        {Object.keys(filters).length > 0 
                            ? 'Try adjusting your search or filters.' 
                            : 'Get started by creating a new post.'
                        }
                    </p>
                </div>
            ) : (
                <>
                    {posts.map(post => (
                        <PostCard
                            key={post.id}
                            post={post}
                            onLike={handleLike}
                        />
                    ))}

                    {/* Infinite scroll trigger */}
                    {hasMore && (
                        <div ref={loadMoreRef} className="flex justify-center py-8">
                            {loading && <LoadingSpinner text="Loading more posts..." />}
                        </div>
                    )}

                    {!hasMore && posts.length > 0 && (
                        <div className="text-center py-8 text-gray-500 dark:text-gray-400">
                            You've reached the end! 🎉
                        </div>
                    )}
                </>
            )}
        </div>
    );
}
        """, language="javascript")

    with tab4:
        st.markdown('<h2 class="section-header">State Management și Form Handling</h2>', unsafe_allow_html=True)

        st.markdown("### Advanced Form Components cu Validation")

        st.code("""
// components/forms/PostForm.js - Form complex pentru post creation/editing
import React, { useState, useEffect, useCallback, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useFormValidation } from '../../hooks/useFormValidation';
import { useAuth } from '../../hooks/useAuth';
import { LoadingSpinner } from '../ui/LoadingSpinner';
import { ErrorMessage } from '../ui/ErrorMessage';

// Validation rules pentru post form
const postValidationRules = {
    title: [
        (value) => !value?.trim() ? 'Title is required' : null,
        (value) => value?.length < 5 ? 'Title must be at least 5 characters' : null,
        (value) => value?.length > 100 ? 'Title must be less than 100 characters' : null
    ],
    content: [
        (value) => !value?.trim() ? 'Content is required' : null,
        (value) => value?.length < 50 ? 'Content must be at least 50 characters' : null
    ],
    excerpt: [
        (value) => value && value.length > 200 ? 'Excerpt must be less than 200 characters' : null
    ],
    tags: [
        (value) => Array.isArray(value) && value.length > 10 ? 'Maximum 10 tags allowed' : null
    ],
    category: [
        (value) => !value ? 'Category is required' : null
    ]
};

export function PostForm({ 
    initialData = null, 
    mode = 'create', // 'create' or 'edit'
    onSubmit, 
    onCancel 
}) {
    const { user } = useAuth();
    const navigate = useNavigate();

    // Initial form values
    const initialValues = {
        title: initialData?.title || '',
        content: initialData?.content || '',
        excerpt: initialData?.excerpt || '',
        coverImage: initialData?.coverImage || '',
        tags: initialData?.tags || [],
        category: initialData?.category || '',
        isPublished: initialData?.isPublished ?? true
    };

    const {
        values,
        errors,
        touched,
        isSubmitting,
        setValue,
        setTouched: setFieldTouched,
        handleSubmit,
        isValid
    } = useFormValidation(initialValues, postValidationRules);

    const [tagInput, setTagInput] = useState('');
    const [imagePreview, setImagePreview] = useState(initialData?.coverImage || '');
    const [autoSaving, setAutoSaving] = useState(false);
    const [lastSaved, setLastSaved] = useState(null);

    // Auto-save functionality
    const autoSaveTimeoutRef = useRef();
    const isInitialMount = useRef(true);

    // Auto-save effect
    useEffect(() => {
        // Skip auto-save pe prima render
        if (isInitialMount.current) {
            isInitialMount.current = false;
            return;
        }

        // Clear existing timeout
        if (autoSaveTimeoutRef.current) {
            clearTimeout(autoSaveTimeoutRef.current);
        }

        // Set new timeout pentru auto-save
        autoSaveTimeoutRef.current = setTimeout(() => {
            if (mode === 'edit' && isValid && values.title.trim() && values.content.trim()) {
                autoSave();
            }
        }, 2000); // Auto-save după 2 secunde de inactivitate

        return () => {
            if (autoSaveTimeoutRef.current) {
                clearTimeout(autoSaveTimeoutRef.current);
            }
        };
    }, [values, isValid, mode]);

    const autoSave = async () => {
        try {
            setAutoSaving(true);

            const draftData = {
                ...values,
                isDraft: true,
                lastModified: new Date().toISOString()
            };

            // Save ca draft
            await onSubmit(draftData, { isDraft: true });
            setLastSaved(new Date());
        } catch (error) {
            console.error('Auto-save failed:', error);
        } finally {
            setAutoSaving(false);
        }
    };

    // Tag handling
    const addTag = useCallback((tag) => {
        const normalizedTag = tag.trim().toLowerCase();
        if (normalizedTag && !values.tags.includes(normalizedTag)) {
            setValue('tags', [...values.tags, normalizedTag]);
        }
        setTagInput('');
    }, [values.tags, setValue]);

    const removeTag = useCallback((tagToRemove) => {
        setValue('tags', values.tags.filter(tag => tag !== tagToRemove));
    }, [values.tags, setValue]);

    const handleTagKeyPress = (e) => {
        if (e.key === 'Enter' || e.key === ',') {
            e.preventDefault();
            addTag(tagInput);
        }
    };

    // Image handling
    const handleImageUpload = useCallback(async (file) => {
        try {
            // Create preview
            const reader = new FileReader();
            reader.onload = (e) => setImagePreview(e.target.result);
            reader.readAsDataURL(file);

            // Upload to server (mock implementation)
            const formData = new FormData();
            formData.append('image', file);

            // const response = await apiService.uploadImage(formData);
            // setValue('coverImage', response.url);

            // Pentru demo, folosim preview URL
            setValue('coverImage', URL.createObjectURL(file));
        } catch (error) {
            console.error('Image upload failed:', error);
        }
    }, [setValue]);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            if (file.size > 5 * 1024 * 1024) { // 5MB limit
                alert('Image size must be less than 5MB');
                return;
            }

            if (!file.type.startsWith('image/')) {
                alert('Please select a valid image file');
                return;
            }

            handleImageUpload(file);
        }
    };

    // Submit handling
    const handleFormSubmit = handleSubmit(async (formData) => {
        try {
            const submitData = {
                ...formData,
                author: user.id,
                publishedAt: formData.isPublished ? new Date().toISOString() : null,
                updatedAt: new Date().toISOString()
            };

            await onSubmit(submitData);

            // Navigate după success
            navigate(mode === 'create' ? '/posts' : `/posts/${initialData.id}`);
        } catch (error) {
            console.error('Form submission failed:', error);
        }
    });

    // Content statistics
    const contentStats = {
        characters: values.content.length,
        words: values.content.trim() ? values.content.trim().split(/\s+/).length : 0,
        readTime: Math.ceil((values.content.trim().split(/\s+/).length || 0) / 200) // 200 words per minute
    };

    return (
        <form onSubmit={handleFormSubmit} className="max-w-4xl mx-auto space-y-6">
            {/* Header cu save status */}
            <div className="flex items-center justify-between">
                <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">
                    {mode === 'create' ? 'Create New Post' : 'Edit Post'}
                </h1>

                <div className="flex items-center space-x-4">
                    {/* Auto-save status */}
                    <div className="text-sm text-gray-500 dark:text-gray-400">
                        {autoSaving && (
                            <span className="flex items-center space-x-1">
                                <div className="animate-spin rounded-full h-3 w-3 border border-gray-400 border-t-transparent"></div>
                                <span>Saving...</span>
                            </span>
                        )}
                        {lastSaved && !autoSaving && (
                            <span>
                                Saved {formatDistanceToNow(lastSaved, { addSuffix: true })}
                            </span>
                        )}
                    </div>

                    {/* Action buttons */}
                    <button
                        type="button"
                        onClick={onCancel}
                        className="px-4 py-2 text-gray-700 dark:text-gray-300 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                    >
                        Cancel
                    </button>

                    <button
                        type="submit"
                        disabled={!isValid || isSubmitting}
                        className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                        {isSubmitting ? (
                            <span className="flex items-center space-x-2">
                                <LoadingSpinner size="small" />
                                <span>{mode === 'create' ? 'Creating...' : 'Saving...'}</span>
                            </span>
                        ) : (
                            mode === 'create' ? 'Publish Post' : 'Save Changes'
                        )}
                    </button>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Main content */}
                <div className="lg:col-span-2 space-y-6">
                    {/* Title */}
                    <div>
                        <input
                            type="text"
                            placeholder="Post title..."
                            value={values.title}
                            onChange={(e) => setValue('title', e.target.value)}
                            onBlur={() => setFieldTouched('title')}
                            className={`w-full text-3xl font-bold bg-transparent border-none outline-none resize-none placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-gray-100 ${
                                touched.title && errors.title ? 'text-red-600' : ''
                            }`}
                        />
                        {touched.title && errors.title && (
                            <p className="mt-1 text-sm text-red-600">{errors.title}</p>
                        )}
                    </div>

                    {/* Cover Image */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                            Cover Image
                        </label>

                        {imagePreview ? (
                            <div className="relative">
                                <img
                                    src={imagePreview}
                                    alt="Cover preview"
                                    className="w-full h-64 object-cover rounded-lg"
                                />
                                <button
                                    type="button"
                                    onClick={() => {
                                        setImagePreview('');
                                        setValue('coverImage', '');
                                    }}
                                    className="absolute top-2 right-2 p-1 bg-red-600 text-white rounded-full hover:bg-red-700 transition-colors"
                                >
                                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                        ) : (
                            <div className="border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg p-6 text-center">
                                <input
                                    type="file"
                                    accept="image/*"
                                    onChange={handleImageChange}
                                    className="hidden"
                                    id="cover-image"
                                />
                                <label
                                    htmlFor="cover-image"
                                    className="cursor-pointer flex flex-col items-center space-y-2"
                                >
                                    <svg className="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 48 48">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" />
                                    </svg>
                                    <div className="text-sm text-gray-600 dark:text-gray-400">
                                        <span className="font-medium text-blue-600 hover:text-blue-500">Upload an image</span>
                                        <span> or drag and drop</span>
                                    </div>
                                    <p className="text-xs text-gray-500">PNG, JPG, GIF up to 5MB</p>
                                </label>
                            </div>
                        )}
                    </div>

                    {/* Content */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                            Content
                        </label>
                        <textarea
                            placeholder="Tell your story..."
                            value={values.content}
                            onChange={(e) => setValue('content', e.target.value)}
                            onBlur={() => setFieldTouched('content')}
                            rows={20}
                            className={`w-full p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical ${
                                touched.content && errors.content ? 'border-red-500' : ''
                            }`}
                        />
                        {touched.content && errors.content && (
                            <p className="mt-1 text-sm text-red-600">{errors.content}</p>
                        )}

                        {/* Content stats */}
                        <div className="mt-2 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
                            <span>{contentStats.characters} characters</span>
                            <span>{contentStats.words} words</span>
                            <span>{contentStats.readTime} min read</span>
                        </div>
                    </div>
                </div>

                {/* Sidebar */}
                <div className="space-y-6">
                    {/* Publish settings */}
                    <div className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
                        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">Publish Settings</h3>

                        <div className="space-y-4">
                            {/* Published status */}
                            <label className="flex items-center space-x-3">
                                <input
                                    type="checkbox"
                                    checked={values.isPublished}
                                    onChange={(e) => setValue('isPublished', e.target.checked)}
                                    className="rounded border-gray-300 dark:border-gray-600 text-blue-600 focus:ring-blue-500"
                                />
                                <span className="text-sm text-gray-700 dark:text-gray-300">
                                    Publish immediately
                                </span>
                            </label>

                            {/* Category */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                    Category
                                </label>
                                <select
                                    value={values.category}
                                    onChange={(e) => setValue('category', e.target.value)}
                                    onBlur={() => setFieldTouched('category')}
                                    className={`w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
                                        touched.category && errors.category ? 'border-red-500' : ''
                                    }`}
                                >
                                    <option value="">Select category</option>
                                    <option value="tutorial">Tutorial</option>
                                    <option value="opinion">Opinion</option>
                                    <option value="news">News</option>
                                    <option value="review">Review</option>
                                    <option value="case-study">Case Study</option>
                                </select>
                                {touched.category && errors.category && (
                                    <p className="mt-1 text-sm text-red-600">{errors.category}</p>
                                )}
                            </div>
                        </div>
                    </div>

                    {/* Tags */}
                    <div className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                            Tags
                        </label>

                        <div className="space-y-2">
                            <input
                                type="text"
                                placeholder="Add tags..."
                                value={tagInput}
                                onChange={(e) => setTagInput(e.target.value)}
                                onKeyPress={handleTagKeyPress}
                                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                            />

                            <div className="flex flex-wrap gap-2">
                                {values.tags.map(tag => (
                                    <span
                                        key={tag}
                                        className="inline-flex items-center px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-sm rounded-full"
                                    >
                                        #{tag}
                                        <button
                                            type="button"
                                            onClick={() => removeTag(tag)}
                                            className="ml-1 text-blue-600 hover:text-blue-800 dark:text-blue-300 dark:hover:text-blue-100"
                                        >
                                            <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                                                <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
                                            </svg>
                                        </button>
                                    </span>
                                ))}
                            </div>

                            {touched.tags && errors.tags && (
                                <p className="text-sm text-red-600">{errors.tags}</p>
                            )}
                        </div>
                    </div>

                    {/* Excerpt */}
                    <div className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4">
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                            Excerpt
                        </label>
                        <textarea
                            placeholder="Brief description of your post..."
                            value={values.excerpt}
                            onChange={(e) => setValue('excerpt', e.target.value)}
                            onBlur={() => setFieldTouched('excerpt')}
                            rows={3}
                            className={`w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical ${
                                touched.excerpt && errors.excerpt ? 'border-red-500' : ''
                            }`}
                        />
                        {touched.excerpt && errors.excerpt && (
                            <p className="mt-1 text-sm text-red-600">{errors.excerpt}</p>
                        )}
                    </div>
                </div>
            </div>
        </form>
    );
}
        """, language="javascript")

    with tab5:
        st.markdown('<h2 class="section-header">Advanced Features și Performance</h2>', unsafe_allow_html=True)

        st.markdown("### Comments System cu Real-time Updates")

        st.code("""
// components/features/CommentsSection.js - Sistema complexă de comentarii
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { formatDistanceToNow } from 'date-fns';
import { useAuth } from '../../hooks/useAuth';
import { useComments } from '../../hooks/useComments';
import { LoadingSpinner } from '../ui/LoadingSpinner';
import { ErrorMessage } from '../ui/ErrorMessage';

export function CommentsSection({ postId, className = '' }) {
    const { user, isAuthenticated } = useAuth();
    const {
        comments,
        loading,
        error,
        loadComments,
        addComment,
        updateComment,
        deleteComment,
        toggleLike
    } = useComments(postId);

    const [newComment, setNewComment] = useState('');
    const [replyingTo, setReplyingTo] = useState(null);
    const [editingComment, setEditingComment] = useState(null);
    const [submitting, setSubmitting] = useState(false);

    // Load comments la mount
    useEffect(() => {
        loadComments();
    }, [loadComments]);

    // Organizarea comentariilor în thread-uri
    const organizedComments = useMemo(() => {
        const topLevel = comments.filter(comment => !comment.parentId);
        const replies = comments.filter(comment => comment.parentId);

        return topLevel.map(comment => ({
            ...comment,
            replies: replies.filter(reply => reply.parentId === comment.id)
                .sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt))
        })).sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    }, [comments]);

    // Submit new comment
    const handleSubmitComment = useCallback(async (content, parentId = null) => {
        if (!content.trim() || submitting) return;

        try {
            setSubmitting(true);
            await addComment({
                content: content.trim(),
                parentId,
                postId
            });

            // Reset form
            if (parentId) {
                setReplyingTo(null);
            } else {
                setNewComment('');
            }
        } catch (error) {
            console.error('Failed to submit comment:', error);
        } finally {
            setSubmitting(false);
        }
    }, [addComment, postId, submitting]);

    // Update comment
    const handleUpdateComment = useCallback(async (commentId, content) => {
        if (!content.trim()) return;

        try {
            await updateComment(commentId, { content: content.trim() });
            setEditingComment(null);
        } catch (error) {
            console.error('Failed to update comment:', error);
        }
    }, [updateComment]);

    // Delete comment cu confirmation
    const handleDeleteComment = useCallback(async (commentId) => {
        if (window.confirm('Are you sure you want to delete this comment?')) {
            try {
                await deleteComment(commentId);
            } catch (error) {
                console.error('Failed to delete comment:', error);
            }
        }
    }, [deleteComment]);

    // Like/unlike comment
    const handleToggleLike = useCallback(async (commentId) => {
        if (!isAuthenticated) return;

        try {
            await toggleLike(commentId);
        } catch (error) {
            console.error('Failed to toggle like:', error);
        }
    }, [toggleLike, isAuthenticated]);

    if (error) {
        return <ErrorMessage error={error} onRetry={loadComments} />;
    }

    return (
        <section id="comments" className={`bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 ${className}`}>
            <div className="border-b border-gray-200 dark:border-gray-700 pb-4 mb-6">
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100">
                    Comments ({comments.length})
                </h2>
            </div>

            {/* New comment form */}
            {isAuthenticated ? (
                <CommentForm
                    onSubmit={(content) => handleSubmitComment(content)}
                    submitting={submitting}
                    placeholder="Share your thoughts..."
                    buttonText="Post Comment"
                />
            ) : (
                <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4 text-center mb-6">
                    <p className="text-gray-600 dark:text-gray-400 mb-2">
                        Join the conversation!
                    </p>
                    <Link
                        to="/login"
                        className="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 font-medium"
                    >
                        Sign in to comment
                    </Link>
                </div>
            )}

            {/* Comments list */}
            {loading && comments.length === 0 ? (
                <div className="flex justify-center py-8">
                    <LoadingSpinner text="Loading comments..." />
                </div>
            ) : (
                <div className="space-y-6">
                    {organizedComments.length === 0 ? (
                        <div className="text-center py-8">
                            <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                            </svg>
                            <h3 className="mt-2 text-sm font-medium text-gray-900 dark:text-gray-100">
                                No comments yet
                            </h3>
                            <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                                Be the first to share your thoughts!
                            </p>
                        </div>
                    ) : (
                        organizedComments.map(comment => (
                            <CommentThread
                                key={comment.id}
                                comment={comment}
                                currentUser={user}
                                isAuthenticated={isAuthenticated}
                                replyingTo={replyingTo}
                                editingComment={editingComment}
                                onReply={setReplyingTo}
                                onEdit={setEditingComment}
                                onDelete={handleDeleteComment}
                                onLike={handleToggleLike}
                                onSubmitReply={handleSubmitComment}
                                onSubmitEdit={handleUpdateComment}
                                submitting={submitting}
                            />
                        ))
                    )}
                </div>
            )}
        </section>
    );
}

// Individual comment component
function CommentThread({
    comment,
    currentUser,
    isAuthenticated,
    replyingTo,
    editingComment,
    onReply,
    onEdit,
    onDelete,
    onLike,
    onSubmitReply,
    onSubmitEdit,
    submitting
}) {
    const isAuthor = currentUser?.id === comment.author.id;
    const isReplying = replyingTo === comment.id;
    const isEditing = editingComment === comment.id;

    return (
        <div className="flex space-x-3">
            {/* Avatar */}
            <img
                src={comment.author.avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${comment.author.username}`}
                alt={comment.author.username}
                className="w-10 h-10 rounded-full flex-shrink-0"
            />

            <div className="flex-1 min-w-0">
                {/* Comment header */}
                <div className="flex items-center space-x-2 mb-1">
                    <span className="text-sm font-medium text-gray-900 dark:text-gray-100">
                        {comment.author.firstName} {comment.author.lastName}
                    </span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">
                        @{comment.author.username}
                    </span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">•</span>
                    <time className="text-xs text-gray-500 dark:text-gray-400">
                        {formatDistanceToNow(new Date(comment.createdAt), { addSuffix: true })}
                    </time>
                    {comment.updatedAt !== comment.createdAt && (
                        <span className="text-xs text-gray-400">(edited)</span>
                    )}
                </div>

                {/* Comment content */}
                {isEditing ? (
                    <CommentForm
                        initialValue={comment.content}
                        onSubmit={(content) => onSubmitEdit(comment.id, content)}
                        onCancel={() => onEdit(null)}
                        submitting={submitting}
                        placeholder="Edit your comment..."
                        buttonText="Save Changes"
                        showCancel
                    />
                ) : (
                    <div className="text-gray-700 dark:text-gray-300 mb-2 whitespace-pre-wrap">
                        {comment.content}
                    </div>
                )}

                {/* Comment actions */}
                {!isEditing && (
                    <div className="flex items-center space-x-4 text-sm">
                        {/* Like button */}
                        <button
                            onClick={() => onLike(comment.id)}
                            disabled={!isAuthenticated}
                            className={`flex items-center space-x-1 px-2 py-1 rounded-full transition-colors ${
                                comment.isLiked
                                    ? 'text-red-600 bg-red-50 dark:bg-red-900/20'
                                    : 'text-gray-500 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20'
                            } ${!isAuthenticated ? 'opacity-50 cursor-not-allowed' : ''}`}
                        >
                            <svg 
                                className={`w-4 h-4 ${comment.isLiked ? 'fill-current' : 'stroke-current fill-none'}`}
                                viewBox="0 0 24 24"
                            >
                                <path 
                                    strokeLinecap="round" 
                                    strokeLinejoin="round" 
                                    strokeWidth={2} 
                                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" 
                                />
                            </svg>
                            <span>{comment.likesCount}</span>
                        </button>

                        {/* Reply button */}
                        {isAuthenticated && (
                            <button
                                onClick={() => onReply(isReplying ? null : comment.id)}
                                className="text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                            >
                                {isReplying ? 'Cancel' : 'Reply'}
                            </button>
                        )}

                        {/* Edit/Delete pentru author */}
                        {isAuthor && (
                            <>
                                <button
                                    onClick={() => onEdit(comment.id)}
                                    className="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300 transition-colors"
                                >
                                    Edit
                                </button>
                                <button
                                    onClick={() => onDelete(comment.id)}
                                    className="text-gray-500 hover:text-red-600 transition-colors"
                                >
                                    Delete
                                </button>
                            </>
                        )}
                    </div>
                )}

                {/* Reply form */}
                {isReplying && (
                    <div className="mt-3">
                        <CommentForm
                            onSubmit={(content) => onSubmitReply(content, comment.id)}
                            onCancel={() => onReply(null)}
                            submitting={submitting}
                            placeholder={`Reply to ${comment.author.firstName}...`}
                            buttonText="Post Reply"
                            showCancel
                        />
                    </div>
                )}

                {/* Replies */}
                {comment.replies && comment.replies.length > 0 && (
                    <div className="mt-4 space-y-4">
                        {comment.replies.map(reply => (
                            <CommentThread
                                key={reply.id}
                                comment={reply}
                                currentUser={currentUser}
                                isAuthenticated={isAuthenticated}
                                replyingTo={replyingTo}
                                editingComment={editingComment}
                                onReply={onReply}
                                onEdit={onEdit}
                                onDelete={onDelete}
                                onLike={onLike}
                                onSubmitReply={onSubmitReply}
                                onSubmitEdit={onSubmitEdit}
                                submitting={submitting}
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

// Reusable comment form
function CommentForm({
    initialValue = '',
    onSubmit,
    onCancel,
    submitting,
    placeholder,
    buttonText,
    showCancel = false
}) {
    const [content, setContent] = useState(initialValue);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (content.trim()) {
            onSubmit(content);
            if (!showCancel) {
                setContent('');
            }
        }
    };

    const handleCancel = () => {
        setContent(initialValue);
        onCancel?.();
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-3">
            <textarea
                value={content}
                onChange={(e) => setContent(e.target.value)}
                placeholder={placeholder}
                rows={3}
                className="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical"
                disabled={submitting}
            />

            <div className="flex items-center space-x-2">
                <button
                    type="submit"
                    disabled={!content.trim() || submitting}
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                    {submitting ? (
                        <span className="flex items-center space-x-2">
                            <div className="animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"></div>
                            <span>Posting...</span>
                        </span>
                    ) : (
                        buttonText
                    )}
                </button>

                {showCancel && (
                    <button
                        type="button"
                        onClick={handleCancel}
                        className="px-4 py-2 text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200 transition-colors"
                    >
                        Cancel
                    </button>
                )}
            </div>
        </form>
    );
}

// hooks/useComments.js - Comments management hook
import { useState, useCallback } from 'react';
import { apiService } from '../services/api';
import { useApi } from './useApi';

export function useComments(postId) {
    const [comments, setComments] = useState([]);
    const { loading, error, execute } = useApi();

    // Load comments pentru post
    const loadComments = useCallback(async () => {
        const result = await execute(() => apiService.getComments(postId));
        setComments(result);
        return result;
    }, [execute, postId]);

    // Add new comment
    const addComment = useCallback(async (commentData) => {
        const newComment = await execute(() => apiService.createComment(commentData));

        // Add la lista locală
        setComments(prev => {
            if (commentData.parentId) {
                // Reply la comment existent
                return prev.map(comment => 
                    comment.id === commentData.parentId
                        ? { ...comment, replies: [...(comment.replies || []), newComment] }
                        : comment
                );
            } else {
                // New top-level comment
                return [newComment, ...prev];
            }
        });

        return newComment;
    }, [execute]);

    // Update comment
    const updateComment = useCallback(async (commentId, updates) => {
        const updatedComment = await execute(() => apiService.updateComment(commentId, updates));

        // Update în lista locală
        const updateCommentInTree = (comments) => {
            return comments.map(comment => {
                if (comment.id === commentId) {
                    return { ...comment, ...updatedComment };
                }
                if (comment.replies) {
                    return {
                        ...comment,
                        replies: updateCommentInTree(comment.replies)
                    };
                }
                return comment;
            });
        };

        setComments(prev => updateCommentInTree(prev));

        return updatedComment;
    }, [execute]);

    // Delete comment
    const deleteComment = useCallback(async (commentId) => {
        await execute(() => apiService.deleteComment(commentId));

        // Remove din lista locală
        const removeCommentFromTree = (comments) => {
            return comments.filter(comment => {
                if (comment.id === commentId) {
                    return false;
                }
                if (comment.replies) {
                    comment.replies = removeCommentFromTree(comment.replies);
                }
                return true;
            });
        };

        setComments(prev => removeCommentFromTree(prev));
    }, [execute]);

    // Toggle like
    const toggleLike = useCallback(async (commentId) => {
        const result = await execute(() => apiService.toggleCommentLike(commentId));

        // Update în lista locală
        const updateLikeInTree = (comments) => {
            return comments.map(comment => {
                if (comment.id === commentId) {
                    return {
                        ...comment,
                        isLiked: result.isLiked,
                        likesCount: result.likesCount
                    };
                }
                if (comment.replies) {
                    return {
                        ...comment,
                        replies: updateLikeInTree(comment.replies)
                    };
                }
                return comment;
            });
        };

        setComments(prev => updateLikeInTree(prev));

        return result;
    }, [execute]);

    return {
        comments,
        loading,
        error,
        loadComments,
        addComment,
        updateComment,
        deleteComment,
        toggleLike
    };
}
        """, language="javascript")

        st.markdown("### Performance Optimizations și Virtual Scrolling")

        st.code("""
// hooks/useVirtualScrolling.js - Virtual scrolling pentru liste mari
import { useState, useEffect, useCallback, useMemo } from 'react';

export function useVirtualScrolling({
    items = [],
    itemHeight = 80,
    containerHeight = 600,
    overscan = 5
}) {
    const [scrollTop, setScrollTop] = useState(0);

    // Calculează ce items sunt vizibile
    const visibleRange = useMemo(() => {
        const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan);
        const endIndex = Math.min(
            items.length - 1,
            Math.floor((scrollTop + containerHeight) / itemHeight) + overscan
        );

        return { startIndex, endIndex };
    }, [scrollTop, itemHeight, containerHeight, overscan, items.length]);

    // Items vizibile cu offset pentru poziționare
    const visibleItems = useMemo(() => {
        const { startIndex, endIndex } = visibleRange;
        const visible = [];

        for (let i = startIndex; i <= endIndex; i++) {
            if (items[i]) {
                visible.push({
                    index: i,
                    item: items[i],
                    offsetY: i * itemHeight
                });
            }
        }

        return visible;
    }, [visibleRange, items, itemHeight]);

    // Total height pentru scrollbar
    const totalHeight = items.length * itemHeight;

    // Scroll handler
    const onScroll = useCallback((e) => {
        setScrollTop(e.target.scrollTop);
    }, []);

    return {
        visibleItems,
        totalHeight,
        onScroll,
        containerProps: {
            style: {
                height: containerHeight,
                overflow: 'auto'
            },
            onScroll
        }
    };
}

// components/ui/VirtualList.js - Virtual list component
export function VirtualList({
    items,
    renderItem,
    itemHeight = 80,
    height = 400,
    className = '',
    ...props
}) {
    const {
        visibleItems,
        totalHeight,
        containerProps
    } = useVirtualScrolling({
        items,
        itemHeight,
        containerHeight: height
    });

    return (
        <div
            {...containerProps}
            className={`relative ${className}`}
            {...props}
        >
            {/* Spacer pentru total height */}
            <div style={{ height: totalHeight, position: 'relative' }}>
                {/* Visible items */}
                {visibleItems.map(({ index, item, offsetY }) => (
                    <div
                        key={index}
                        style={{
                            position: 'absolute',
                            top: offsetY,
                            width: '100%',
                            height: itemHeight
                        }}
                    >
                        {renderItem(item, index)}
                    </div>
                ))}
            </div>
        </div>
    );
}

// hooks/useInfiniteScroll.js - Infinite scroll cu virtual scrolling
export function useInfiniteScroll({
    fetchMore,
    hasMore,
    threshold = 100
}) {
    const [isFetching, setIsFetching] = useState(false);

    const handleScroll = useCallback((e) => {
        const { scrollTop, scrollHeight, clientHeight } = e.target;

        // Check dacă user-ul e aproape de bottom
        if (scrollHeight - scrollTop - clientHeight < threshold && hasMore && !isFetching) {
            setIsFetching(true);

            fetchMore()
                .then(() => setIsFetching(false))
                .catch(() => setIsFetching(false));
        }
    }, [fetchMore, hasMore, isFetching, threshold]);

    return { isFetching, handleScroll };
}

// components/features/OptimizedPostsList.js - Posts list cu virtual scrolling
import React, { useMemo } from 'react';
import { VirtualList } from '../ui/VirtualList';
import { PostCard } from './PostCard';
import { useInfiniteScroll } from '../../hooks/useInfiniteScroll';

export function OptimizedPostsList({ posts, onLoadMore, hasMore, onLike }) {
    const { isFetching, handleScroll } = useInfiniteScroll({
        fetchMore: onLoadMore,
        hasMore,
        threshold: 200
    });

    // Memoize post card renderer pentru performance
    const renderPost = useMemo(() => (post, index) => (
        <div className="px-4 py-2">
            <PostCard
                post={post}
                onLike={onLike}
                className="h-full"
            />
        </div>
    ), [onLike]);

    return (
        <div className="space-y-4">
            <VirtualList
                items={posts}
                renderItem={renderPost}
                itemHeight={320} // Approximate height pentru post card
                height={800}
                onScroll={handleScroll}
                className="space-y-4"
            />

            {isFetching && (
                <div className="flex justify-center py-4">
                    <LoadingSpinner text="Loading more posts..." />
                </div>
            )}

            {!hasMore && posts.length > 0 && (
                <div className="text-center py-4 text-gray-500">
                    You've reached the end! 🎉
                </div>
            )}
        </div>
    );
}

// hooks/usePerformanceMonitor.js - Performance monitoring
export function usePerformanceMonitor(componentName) {
    const renderStartTime = useRef(performance.now());
    const renderCount = useRef(0);

    useEffect(() => {
        renderCount.current += 1;
        const renderTime = performance.now() - renderStartTime.current;

        // Log performance metrics
        if (process.env.NODE_ENV === 'development') {
            console.log(`${componentName} render #${renderCount.current}: ${renderTime.toFixed(2)}ms`);
        }

        // Report la analytics în production
        if (process.env.NODE_ENV === 'production' && renderTime > 16) { // Slower than 60fps
            // analytics.track('slow_render', {
            //     component: componentName,
            //     renderTime,
            //     renderCount: renderCount.current
            // });
        }

        renderStartTime.current = performance.now();
    });

    return { renderCount: renderCount.current };
}

// components/features/PerformantPostCard.js - Optimized post card
const PerformantPostCard = React.memo(({ post, onLike, onShare }) => {
    usePerformanceMonitor('PostCard');

    // Memoize expensive computations
    const formattedDate = useMemo(() => 
        formatDistanceToNow(new Date(post.publishedAt), { addSuffix: true }),
        [post.publishedAt]
    );

    const readTime = useMemo(() => 
        Math.ceil((post.content?.split(' ').length || 0) / 200),
        [post.content]
    );

    // Stable event handlers
    const handleLike = useCallback(() => {
        onLike(post.id);
    }, [post.id, onLike]);

    const handleShare = useCallback((platform) => {
        onShare(post.id, platform);
    }, [post.id, onShare]);

    return (
        <article className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow">
            {/* Post content */}
            <PostCardContent
                post={post}
                formattedDate={formattedDate}
                readTime={readTime}
                onLike={handleLike}
                onShare={handleShare}
            />
        </article>
    );
}, (prevProps, nextProps) => {
    // Custom comparison function pentru React.memo
    return (
        prevProps.post.id === nextProps.post.id &&
        prevProps.post.likesCount === nextProps.post.likesCount &&
        prevProps.post.isLiked === nextProps.post.isLiked &&
        prevProps.post.commentsCount === nextProps.post.commentsCount
    );
});

// Lazy loading pentru images
function LazyImage({ src, alt, className, ...props }) {
    const [loaded, setLoaded] = useState(false);
    const [inView, setInView] = useState(false);
    const imgRef = useRef();

    useEffect(() => {
        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) {
                    setInView(true);
                    observer.disconnect();
                }
            },
            { threshold: 0.1 }
        );

        if (imgRef.current) {
            observer.observe(imgRef.current);
        }

        return () => observer.disconnect();
    }, []);

    return (
        <div ref={imgRef} className={className} {...props}>
            {inView && (
                <img
                    src={src}
                    alt={alt}
                    className={`transition-opacity duration-300 ${loaded ? 'opacity-100' : 'opacity-0'}`}
                    onLoad={() => setLoaded(true)}
                    loading="lazy"
                />
            )}
            {!loaded && inView && (
                <div className="bg-gray-200 dark:bg-gray-700 animate-pulse w-full h-full flex items-center justify-center">
                    <svg className="w-8 h-8 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clipRule="evenodd" />
                    </svg>
                </div>
            )}
        </div>
    );
}

// Service Worker pentru caching
// public/sw.js
const CACHE_NAME = 'blog-app-v1';
const urlsToCache = [
    '/',
    '/static/js/bundle.js',
    '/static/css/main.css',
    '/manifest.json'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cached version or fetch from network
                return response || fetch(event.request);
            })
    );
});

// utils/performance.js - Performance utilities
export const performanceUtils = {
    // Debounce function pentru search
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Throttle function pentru scroll events
    throttle: (func, limit) => {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    // Lazy load components
    lazyLoad: (importFunc) => {
        return React.lazy(() => {
            return new Promise(resolve => {
                setTimeout(() => resolve(importFunc()), 100);
            });
        });
    },

    // Bundle size analyzer
    analyzeBundleSize: () => {
        if (process.env.NODE_ENV === 'development') {
            import('webpack-bundle-analyzer').then(({ BundleAnalyzerPlugin }) => {
                // Analysis logic
            });
        }
    }
};
        """, language="javascript")

    with tab6:
        st.markdown('<h2 class="section-header">Deployment, Testing și Finalizare</h2>', unsafe_allow_html=True)

        st.markdown("### Testing Strategy Completă")

        st.code("""
// tests/components/PostCard.test.js - Unit tests pentru components
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from '../../context/AuthContext';
import { PostCard } from '../../components/features/PostCard';

// Mock data
const mockPost = {
    id: 1,
    title: 'Test Post Title',
    excerpt: 'This is a test excerpt for the post.',
    content: 'Full post content here...',
    author: {
        id: 1,
        username: 'testuser',
        firstName: 'Test',
        lastName: 'User',
        avatar: 'https://example.com/avatar.jpg'
    },
    tags: ['react', 'testing', 'javascript'],
    publishedAt: '2024-08-01T10:00:00Z',
    readTime: 5,
    likesCount: 42,
    commentsCount: 7,
    isLiked: false,
    coverImage: 'https://example.com/cover.jpg'
};

const mockUser = {
    id: 1,
    username: 'testuser',
    firstName: 'Test',
    lastName: 'User'
};

// Test wrapper cu providers
const TestWrapper = ({ children, user = mockUser }) => (
    <BrowserRouter>
        <AuthProvider initialUser={user}>
            {children}
        </AuthProvider>
    </BrowserRouter>
);

describe('PostCard Component', () => {
    const mockOnLike = jest.fn();
    const mockOnShare = jest.fn();
    const mockOnDelete = jest.fn();

    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('renders post information correctly', () => {
        render(
            <TestWrapper>
                <PostCard post={mockPost} onLike={mockOnLike} />
            </TestWrapper>
        );

        // Check dacă toate elementele sunt afișate
        expect(screen.getByText(mockPost.title)).toBeInTheDocument();
        expect(screen.getByText(mockPost.excerpt)).toBeInTheDocument();
        expect(screen.getByText(`${mockPost.author.firstName} ${mockPost.author.lastName}`)).toBeInTheDocument();
        expect(screen.getByText(mockPost.likesCount.toString())).toBeInTheDocument();
        expect(screen.getByText(mockPost.commentsCount.toString())).toBeInTheDocument();

        // Check tags
        mockPost.tags.slice(0, 3).forEach(tag => {
            expect(screen.getByText(`#${tag}`)).toBeInTheDocument();
        });
    });

    test('handles like interaction correctly', async () => {
        const user = userEvent.setup();

        render(
            <TestWrapper>
                <PostCard post={mockPost} onLike={mockOnLike} />
            </TestWrapper>
        );

        const likeButton = screen.getByRole('button', { name: /like/i });
        await user.click(likeButton);

        expect(mockOnLike).toHaveBeenCalledWith(mockPost.id);
    });

    test('shows edit/delete options for post author', () => {
        render(
            <TestWrapper user={mockUser}>
                <PostCard 
                    post={mockPost} 
                    onLike={mockOnLike}
                    onDelete={mockOnDelete}
                />
            </TestWrapper>
        );

        // Buttons should be visible pentru author
        expect(screen.getByRole('button', { name: /edit/i })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /delete/i })).toBeInTheDocument();
    });

    test('does not show edit/delete options for other users', () => {
        const otherUser = { ...mockUser, id: 2 };

        render(
            <TestWrapper user={otherUser}>
                <PostCard post={mockPost} onLike={mockOnLike} />
            </TestWrapper>
        );

        // Buttons should not be visible pentru non-author
        expect(screen.queryByRole('button', { name: /edit/i })).not.toBeInTheDocument();
        expect(screen.queryByRole('button', { name: /delete/i })).not.toBeInTheDocument();
    });

    test('handles delete with confirmation', async () => {
        const user = userEvent.setup();

        // Mock window.confirm
        const confirmSpy = jest.spyOn(window, 'confirm').mockReturnValue(true);

        render(
            <TestWrapper user={mockUser}>
                <PostCard 
                    post={mockPost} 
                    onLike={mockOnLike}
                    onDelete={mockOnDelete}
                />
            </TestWrapper>
        );

        const deleteButton = screen.getByRole('button', { name: /delete/i });
        await user.click(deleteButton);

        expect(confirmSpy).toHaveBeenCalledWith('Are you sure you want to delete this post?');
        expect(mockOnDelete).toHaveBeenCalledWith(mockPost.id);

        confirmSpy.mockRestore();
    });

    test('handles share functionality', async () => {
        const user = userEvent.setup();

        render(
            <TestWrapper>
                <PostCard 
                    post={mockPost} 
                    onLike={mockOnLike}
                    onShare={mockOnShare}
                />
            </TestWrapper>
        );

        // Open share menu
        const shareButton = screen.getByLabelText(/share post/i);
        await user.click(shareButton);

        // Check dacă share options sunt visible
        expect(screen.getByText('Share on Twitter')).toBeInTheDocument();
        expect(screen.getByText('Share on Facebook')).toBeInTheDocument();

        // Click pe Twitter share
        const twitterShare = screen.getByText('Share on Twitter');
        await user.click(twitterShare);

        // Note: În real test, ar trebui să verifici dacă window.open e apelat
    });

    test('displays loading state for like button', async () => {
        const slowMockOnLike = jest.fn(() => new Promise(resolve => setTimeout(resolve, 1000)));

        render(
            <TestWrapper>
                <PostCard post={mockPost} onLike={slowMockOnLike} />
            </TestWrapper>
        );

        const likeButton = screen.getByRole('button', { name: /like/i });
        fireEvent.click(likeButton);

        // Check loading state
        expect(likeButton).toBeDisabled();
        expect(likeButton).toHaveClass('opacity-50');
    });
});

// tests/hooks/usePosts.test.js - Custom hooks testing
import { renderHook, act } from '@testing-library/react-hooks';
import { usePosts } from '../../hooks/usePosts';
import { apiService } from '../../services/api';

// Mock API service
jest.mock('../../services/api');

describe('usePosts Hook', () => {
    const mockPosts = [
        { id: 1, title: 'Post 1', likesCount: 5 },
        { id: 2, title: 'Post 2', likesCount: 10 }
    ];

    beforeEach(() => {
        jest.clearAllMocks();
        apiService.getPosts.mockResolvedValue({
            posts: mockPosts,
            totalPages: 2
        });
    });

    test('loads posts on mount', async () => {
        const { result, waitForNextUpdate } = renderHook(() => usePosts());

        act(() => {
            result.current.loadPosts();
        });

        await waitForNextUpdate();

        expect(result.current.posts).toEqual(mockPosts);
        expect(result.current.loading).toBe(false);
        expect(apiService.getPosts).toHaveBeenCalledWith({
            page: 1,
            limit: 10
        });
    });

    test('handles like toggle correctly', async () => {
        apiService.likePost.mockResolvedValue({
            isLiked: true,
            likesCount: 6
        });

        const { result, waitForNextUpdate } = renderHook(() => usePosts());

        // Load posts first
        act(() => {
            result.current.loadPosts();
        });
        await waitForNextUpdate();

        // Toggle like
        act(() => {
            result.current.toggleLike(1);
        });
        await waitForNextUpdate();

        expect(result.current.posts[0].likesCount).toBe(6);
        expect(result.current.posts[0].isLiked).toBe(true);
    });

    test('handles errors gracefully', async () => {
        const errorMessage = 'Network error';
        apiService.getPosts.mockRejectedValue(new Error(errorMessage));

        const { result, waitForNextUpdate } = renderHook(() => usePosts());

        act(() => {
            result.current.loadPosts();
        });

        await waitForNextUpdate();

        expect(result.current.error).toBeTruthy();
        expect(result.current.error.message).toBe(errorMessage);
        expect(result.current.posts).toEqual([]);
    });
});

// tests/integration/BlogFlow.test.js - Integration tests
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { BrowserRouter } from 'react-router-dom';
import { App } from '../../App';
import { server } from '../mocks/server';

// Setup MSW pentru API mocking
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('Blog Application Flow', () => {
    test('complete user journey from login to post creation', async () => {
        const user = userEvent.setup();

        render(
            <BrowserRouter>
                <App />
            </BrowserRouter>
        );

        // 1. User navigates to login
        const loginButton = screen.getByText('Login');
        await user.click(loginButton);

        // 2. User fills login form
        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/password/i);
        const submitButton = screen.getByRole('button', { name: /sign in/i });

        await user.type(emailInput, 'test@example.com');
        await user.type(passwordInput, 'password123');
        await user.click(submitButton);

        // 3. Wait pentru successful login
        await waitFor(() => {
            expect(screen.getByText('Welcome back!')).toBeInTheDocument();
        });

        // 4. Navigate to create post
        const createButton = screen.getByText('Write');
        await user.click(createButton);

        // 5. Fill post form
        const titleInput = screen.getByPlaceholderText(/post title/i);
        const contentInput = screen.getByPlaceholderText(/tell your story/i);

        await user.type(titleInput, 'My Test Post');
        await user.type(contentInput, 'This is the content of my test post. It needs to be long enough to meet the minimum requirements for posting.');

        // 6. Add tags
        const tagInput = screen.getByPlaceholderText(/add tags/i);
        await user.type(tagInput, 'react{enter}');
        await user.type(tagInput, 'testing{enter}');

        // 7. Select category
        const categorySelect = screen.getByLabelText(/category/i);
        await user.selectOptions(categorySelect, 'tutorial');

        // 8. Submit post
        const publishButton = screen.getByRole('button', { name: /publish post/i });
        await user.click(publishButton);

        // 9. Verify post creation success
        await waitFor(() => {
            expect(screen.getByText('Post published successfully!')).toBeInTheDocument();
        });

        // 10. Verify redirect to posts page
        expect(screen.getByText('My Test Post')).toBeInTheDocument();
    });
});

// tests/mocks/server.js - MSW setup pentru API mocking
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const handlers = [
    // Auth endpoints
    rest.post('/api/auth/login', (req, res, ctx) => {
        return res(
            ctx.json({
                user: {
                    id: 1,
                    username: 'testuser',
                    email: 'test@example.com',
                    firstName: 'Test',
                    lastName: 'User'
                },
                token: 'mock-jwt-token'
            })
        );
    }),

    // Posts endpoints
    rest.get('/api/posts', (req, res, ctx) => {
        return res(
            ctx.json({
                posts: [
                    {
                        id: 1,
                        title: 'Test Post',
                        excerpt: 'Test excerpt',
                        author: {
                            id: 1,
                            username: 'testuser',
                            firstName: 'Test',
                            lastName: 'User'
                        },
                        likesCount: 0,
                        commentsCount: 0,
                        isLiked: false,
                        publishedAt: new Date().toISOString()
                    }
                ],
                totalPages: 1
            })
        );
    }),

    rest.post('/api/posts', (req, res, ctx) => {
        return res(
            ctx.json({
                id: 2,
                title: 'My Test Post',
                content: 'This is the content...',
                author: {
                    id: 1,
                    username: 'testuser',
                    firstName: 'Test',
                    lastName: 'User'
                }
            })
        );
    })
];

export const server = setupServer(...handlers);
        """, language="javascript")

        st.markdown("### Deployment Configuration")

        st.code("""
// package.json - Scripts și dependencies pentru production
{
    "name": "react-blog-app",
    "version": "1.0.0",
    "private": true,
    "dependencies": {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-router-dom": "^6.8.0",
        "date-fns": "^2.29.3",
        "@headlessui/react": "^1.7.0",
        "@heroicons/react": "^2.0.0"
    },
    "devDependencies": {
        "@testing-library/jest-dom": "^5.16.5",
        "@testing-library/react": "^13.4.0",
        "@testing-library/user-event": "^14.4.3",
        "msw": "^1.0.0",
        "tailwindcss": "^3.2.4",
        "webpack-bundle-analyzer": "^4.7.0"
    },
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "test:coverage": "react-scripts test --coverage --watchAll=false",
        "test:ci": "CI=true react-scripts test --coverage --watchAll=false",
        "eject": "react-scripts eject",
        "analyze": "npm run build && npx webpack-bundle-analyzer build/static/js/*.js",
        "deploy": "npm run build && npm run deploy:netlify",
        "deploy:netlify": "netlify deploy --prod --dir=build",
        "deploy:vercel": "vercel --prod",
        "lint": "eslint src/ --ext .js,.jsx,.ts,.tsx",
        "lint:fix": "eslint src/ --ext .js,.jsx,.ts,.tsx --fix",
        "format": "prettier --write src/**/*.{js,jsx,ts,tsx,json,css,md}"
    },
    "eslintConfig": {
        "extends": [
            "react-app",
            "react-app/jest"
        ]
    },
    "browserslist": {
        "production": [
            ">0.2%",
            "not dead",
            "not op_mini all"
        ],
        "development": [
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version"
        ]
    },
    "jest": {
        "collectCoverageFrom": [
            "src/**/*.{js,jsx}",
            "!src/index.js",
            "!src/reportWebVitals.js",
            "!src/**/*.test.{js,jsx}"
        ],
        "coverageThreshold": {
            "global": {
                "branches": 80,
                "functions": 80,
                "lines": 80,
                "statements": 80
            }
        }
    }
}

// netlify.toml - Netlify deployment configuration
[build]
  publish = "build"
  command = "npm run build"

[build.environment]
  NODE_VERSION = "18"
  NPM_VERSION = "8"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true

# vercel.json - Vercel deployment configuration
{
    "version": 2,
    "builds": [
        {
            "src": "package.json",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "build"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "headers": {
                "cache-control": "public, max-age=31536000, immutable"
            }
        },
        {
            "src": "/(.*)",
            "dest": "/index.html"
        }
    ],
    "env": {
        "REACT_APP_API_URL": "@api-url",
        "REACT_APP_ENV": "production"
    }
}

# Dockerfile - Pentru containerization
FROM node:18-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build aplicația
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built app
COPY --from=build /app/build /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# nginx.conf - Nginx configuration pentru production
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied expired no-cache no-store private must-revalidate auth;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/javascript
        application/xml+rss
        application/json;

    server {
        listen 80;
        server_name localhost;
        root /usr/share/nginx/html;
        index index.html;

        # Cache static assets
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
            expires 1y;
            add_header Cache-Control "public, immutable";
        }

        # Handle React Router
        location / {
            try_files $uri $uri/ /index.html;
        }

        # Security headers
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    }
}

# .github/workflows/ci.yml - GitHub Actions pentru CI/CD
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [16.x, 18.x]

    steps:
    - uses: actions/checkout@v3

    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Run linting
      run: npm run lint

    - name: Run tests
      run: npm run test:ci

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage/lcov.info

    - name: Build application
      run: npm run build

    - name: Run bundle analyzer
      run: npm run analyze

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v3

    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Build for production
      run: npm run build
      env:
        REACT_APP_API_URL: ${{ secrets.API_URL }}
        REACT_APP_ENV: production

    - name: Deploy to Netlify
      uses: nwtgck/actions-netlify@v2.0
      with:
        publish-dir: './build'
        production-branch: main
        github-token: ${{ secrets.GITHUB_TOKEN }}
        deploy-message: "Deploy from GitHub Actions"
      env:
        NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
        NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}

# .env.example - Environment variables template
# API Configuration
REACT_APP_API_URL=http://localhost:3001
REACT_APP_WS_URL=ws://localhost:3001

# Authentication
REACT_APP_JWT_SECRET=your-jwt-secret-here

# External Services
REACT_APP_GOOGLE_ANALYTICS_ID=GA-XXXXXXXXX
REACT_APP_SENTRY_DSN=https://your-sentry-dsn

# Feature Flags
REACT_APP_ENABLE_COMMENTS=true
REACT_APP_ENABLE_DARK_MODE=true
REACT_APP_ENABLE_PWA=true

# Development
REACT_APP_DEBUG=false
REACT_APP_MOCK_API=false
        """, language="bash")

        st.markdown("### Performance Monitoring și Analytics")

        st.code("""
// utils/analytics.js - Analytics și monitoring setup
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

class Analytics {
    constructor() {
        this.isProduction = process.env.NODE_ENV === 'production';
        this.userId = null;
        this.sessionId = this.generateSessionId();

        if (this.isProduction) {
            this.initializeAnalytics();
            this.trackWebVitals();
        }
    }

    generateSessionId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }

    initializeAnalytics() {
        // Google Analytics 4
        if (window.gtag && process.env.REACT_APP_GOOGLE_ANALYTICS_ID) {
            window.gtag('config', process.env.REACT_APP_GOOGLE_ANALYTICS_ID, {
                session_id: this.sessionId,
                custom_map: { custom_dimension_1: 'user_type' }
            });
        }

        // Sentry pentru error tracking
        if (process.env.REACT_APP_SENTRY_DSN) {
            import('@sentry/react').then(Sentry => {
                Sentry.init({
                    dsn: process.env.REACT_APP_SENTRY_DSN,
                    environment: process.env.NODE_ENV,
                    tracesSampleRate: 0.1,
                    beforeSend: (event, hint) => {
                        // Filter out development errors
                        if (process.env.NODE_ENV === 'development') {
                            return null;
                        }
                        return event;
                    }
                });
            });
        }
    }

    trackWebVitals() {
        const sendToAnalytics = (metric) => {
            // Send la Google Analytics
            if (window.gtag) {
                window.gtag('event', metric.name, {
                    event_category: 'Web Vitals',
                    event_label: metric.id,
                    value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
                    non_interaction: true
                });
            }

            // Send la custom analytics endpoint
            this.track('web_vital', {
                metric: metric.name,
                value: metric.value,
                id: metric.id,
                page: window.location.pathname
            });
        };

        getCLS(sendToAnalytics);
        getFID(sendToAnalytics);
        getFCP(sendToAnalytics);
        getLCP(sendToAnalytics);
        getTTFB(sendToAnalytics);
    }

    // Track page views
    trackPageView(page, title) {
        if (!this.isProduction) return;

        if (window.gtag) {
            window.gtag('config', process.env.REACT_APP_GOOGLE_ANALYTICS_ID, {
                page_title: title,
                page_location: window.location.href,
                page_path: page
            });
        }

        this.track('page_view', {
            page,
            title,
            url: window.location.href,
            referrer: document.referrer
        });
    }

    // Track custom events
    trackEvent(action, category, label, value) {
        if (!this.isProduction) return;

        if (window.gtag) {
            window.gtag('event', action, {
                event_category: category,
                event_label: label,
                value: value
            });
        }

        this.track('event', {
            action,
            category,
            label,
            value
        });
    }

    // Track user interactions
    trackInteraction(element, action, context = {}) {
        this.trackEvent(action, 'User Interaction', element, 1);

        this.track('interaction', {
            element,
            action,
            timestamp: Date.now(),
            sessionId: this.sessionId,
            ...context
        });
    }

    // Track errors
    trackError(error, context = {}) {
        if (window.gtag) {
            window.gtag('event', 'exception', {
                description: error.message,
                fatal: false
            });
        }

        this.track('error', {
            message: error.message,
            stack: error.stack,
            page: window.location.pathname,
            userAgent: navigator.userAgent,
            timestamp: Date.now(),
            ...context
        });
    }

    // Track performance metrics
    trackPerformance(metrics) {
        this.track('performance', {
            ...metrics,
            page: window.location.pathname,
            timestamp: Date.now(),
            sessionId: this.sessionId
        });
    }

    // Set user information
    setUser(userId, properties = {}) {
        this.userId = userId;

        if (window.gtag) {
            window.gtag('config', process.env.REACT_APP_GOOGLE_ANALYTICS_ID, {
                user_id: userId
            });
        }

        this.track('user_identify', {
            userId,
            ...properties
        });
    }

    // Generic track method
    track(event, properties = {}) {
        if (!this.isProduction) {
            console.log('Analytics Event:', event, properties);
            return;
        }

        // Send to custom analytics endpoint
        fetch('/api/analytics', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                event,
                properties: {
                    ...properties,
                    userId: this.userId,
                    sessionId: this.sessionId,
                    timestamp: Date.now(),
                    url: window.location.href,
                    userAgent: navigator.userAgent
                }
            })
        }).catch(error => {
            console.error('Analytics tracking failed:', error);
        });
    }
}

// Singleton instance
export const analytics = new Analytics();

// React hook pentru analytics
export function useAnalytics() {
    const location = useLocation();

    useEffect(() => {
        analytics.trackPageView(location.pathname, document.title);
    }, [location]);

    return {
        trackEvent: analytics.trackEvent.bind(analytics),
        trackInteraction: analytics.trackInteraction.bind(analytics),
        trackError: analytics.trackError.bind(analytics),
        setUser: analytics.setUser.bind(analytics)
    };
}

// Higher-order component pentru automatic tracking
export function withAnalytics(WrappedComponent, componentName) {
    return function AnalyticsWrappedComponent(props) {
        const { trackInteraction } = useAnalytics();

        const handleClick = useCallback((event) => {
            trackInteraction(componentName, 'click', {
                target: event.target.tagName,
                text: event.target.textContent?.substring(0, 50)
            });

            props.onClick?.(event);
        }, [trackInteraction, props.onClick]);

        return (
            <WrappedComponent
                {...props}
                onClick={handleClick}
            />
        );
    };
}

// utils/monitoring.js - Application monitoring
export class PerformanceMonitor {
    constructor() {
        this.metrics = new Map();
        this.observers = [];

        this.initializeObservers();
    }

    initializeObservers() {
        // Performance Observer pentru navigation timing
        if ('PerformanceObserver' in window) {
            const navObserver = new PerformanceObserver((list) => {
                list.getEntries().forEach((entry) => {
                    this.recordMetric('navigation', {
                        type: entry.type,
                        duration: entry.duration,
                        startTime: entry.startTime
                    });
                });
            });

            navObserver.observe({ entryTypes: ['navigation'] });
            this.observers.push(navObserver);

            // Long Task Observer
            const longTaskObserver = new PerformanceObserver((list) => {
                list.getEntries().forEach((entry) => {
                    this.recordMetric('long-task', {
                        duration: entry.duration,
                        startTime: entry.startTime
                    });

                    analytics.trackEvent('long_task', 'Performance', 'Long Task Detected', entry.duration);
                });
            });

            try {
                longTaskObserver.observe({ entryTypes: ['longtask'] });
                this.observers.push(longTaskObserver);
            } catch (e) {
                console.warn('Long Task Observer not supported');
            }
        }

        // Memory usage monitoring
        this.monitorMemoryUsage();

        // Network information
        this.monitorNetworkInfo();
    }

    recordMetric(name, data) {
        if (!this.metrics.has(name)) {
            this.metrics.set(name, []);
        }

        this.metrics.get(name).push({
            ...data,
            timestamp: Date.now()
        });

        // Send la analytics
        analytics.trackPerformance({
            metric: name,
            ...data
        });
    }

    monitorMemoryUsage() {
        if ('memory' in performance) {
            setInterval(() => {
                this.recordMetric('memory', {
                    used: performance.memory.usedJSHeapSize,
                    total: performance.memory.totalJSHeapSize,
                    limit: performance.memory.jsHeapSizeLimit
                });
            }, 30000); // Every 30 seconds
        }
    }

    monitorNetworkInfo() {
        if ('connection' in navigator) {
            const connection = navigator.connection;

            this.recordMetric('network', {
                effectiveType: connection.effectiveType,
                downlink: connection.downlink,
                rtt: connection.rtt,
                saveData: connection.saveData
            });

            connection.addEventListener('change', () => {
                this.recordMetric('network-change', {
                    effectiveType: connection.effectiveType,
                    downlink: connection.downlink,
                    rtt: connection.rtt
                });
            });
        }
    }

    getMetrics(name) {
        return this.metrics.get(name) || [];
    }

    getAverageMetric(name, property) {
        const metrics = this.getMetrics(name);
        if (metrics.length === 0) return 0;

        const sum = metrics.reduce((acc, metric) => acc + (metric[property] || 0), 0);
        return sum / metrics.length;
    }

    exportMetrics() {
        const exported = {};
        this.metrics.forEach((value, key) => {
            exported[key] = value;
        });
        return exported;
    }

    cleanup() {
        this.observers.forEach(observer => observer.disconnect());
        this.metrics.clear();
    }
}

// Initialize monitoring
export const performanceMonitor = new PerformanceMonitor();

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    performanceMonitor.cleanup();
});
        """, language="javascript")

        st.markdown("### Rezumat și Concepte Învățate")

        st.markdown("""
        ### Concepte React Demonstrate în Aplicație

        **1. State & Props Management:**
        - **useState** pentru form state, UI state (modals, dropdowns)
        - **useReducer** pentru complex state (auth, posts management)
        - **Props drilling** vs **Context API** pentru state partajare
        - **Prop validation** cu PropTypes și TypeScript

        **2. Event Handling Avansat:**
        - **SyntheticEvents** pentru cross-browser compatibility
        - **Event delegation** pentru performance (comments system)
        - **Custom event handlers** cu useCallback pentru optimization
        - **Form events** cu validation și error handling
        - **Keyboard events** pentru accessibility (Escape pentru modal close)

        **3. Hooks Mastery:**
        - **Built-in hooks**: useState, useEffect, useContext, useMemo, useCallback, useRef
        - **Custom hooks**: useAuth, usePosts, useComments, useFormValidation, useDebounce
        - **Hook composition** pentru functionality complex
        - **Dependencies optimization** pentru performance

        **4. Performance Optimization:**
        - **React.memo** pentru component memoization
        - **useMemo/useCallback** pentru expensive operations
        - **Virtual scrolling** pentru liste mari
        - **Lazy loading** pentru images și components
        - **Code splitting** cu React.lazy

        **5. Real-world Patterns:**
        - **Error boundaries** pentru graceful error handling
        - **Loading states** și **optimistic updates**
        - **Infinite scrolling** cu intersection observer
        - **Search cu debouncing** pentru API efficiency
        - **Form handling** cu complex validation

        **6. Architecture Patterns:**
        - **Component composition** peste inheritance
        - **Container/Presentational** component pattern
        - **Custom hooks** pentru business logic separation
        - **Service layer** pentru API communication
        - **Context providers** pentru global state

        **7. Testing Strategy:**
        - **Unit tests** pentru individual components
        - **Integration tests** pentru user flows
        - **Custom hooks testing** cu renderHook
        - **MSW** pentru API mocking
        - **Coverage reporting** și CI/CD integration

        **8. Production Readiness:**
        - **Bundle optimization** cu webpack analyzer
        - **PWA capabilities** cu service worker
        - **SEO optimization** cu meta tags
        - **Performance monitoring** cu web vitals
        - **Analytics integration** pentru user tracking
        - **Error tracking** cu Sentry
        - **Deployment** cu Netlify/Vercel

        ### Key Takeaways pentru Interview Preparation

        **Demonstrates Deep React Knowledge:**
        - Proper use of all major hooks cu real-world examples
        - Performance optimization techniques în production scenarios
        - Error handling și user experience considerations
        - Testing strategies pentru maintainable code

        **Shows Architecture Skills:**
        - Separation of concerns între UI și business logic
        - Scalable folder structure și component organization
        - Proper state management strategy selection
        - API integration cu error handling și loading states

        **Production Experience:**
        - Deployment pipeline setup cu CI/CD
        - Performance monitoring și analytics integration
        - Security considerations (XSS protection, auth handling)
        - Accessibility features și responsive design

        Această aplicație demonstrează toate conceptele React necesare pentru poziții senior de frontend development și oferă exemple concrete pentru discuții tehnice în interviuri.
        """)

    st.markdown("""
    <div class="summary-box">
    <h3>Finalizarea Proiectului</h3>
    <p>Ai construit o aplicație completă de blog care demonstrează toate conceptele React învățate: 
    de la hooks fundamentali la optimizări avansate de performance. Aplicația include authentication, 
    CRUD operations, real-time comments, search functionality și este deployment-ready cu testing complet. 
    Această implementare te pregătește pentru interviuri tehnice și dezvoltarea aplicațiilor React la nivel profesionist.</p>
    <p><strong>Next Steps:</strong> Extinde aplicația cu notificații real-time, editor de text avansat, 
    sistem de categorii, și integrations cu servicii externe pentru o experiență completă de production.</p>
    </div>
    """, unsafe_allow_html=True)


def styling_page():
    """Styling in React - Tutorial Complet"""
    st.markdown('<h1 class="chapter-header">Styling în React</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-box">
    <h3>Modalități de stilizare în React</h3>
    <p>React oferă multiple modalități de stilizare, fiecare cu propriile avantaje și cazuri de utilizare. 
    De la CSS tradițional la soluții moderne CSS-in-JS, vei învăța când și cum să folosești fiecare metodă 
    pentru aplicații scalabile și maintainable.</p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["CSS Clasic", "CSS Modules", "Styled Components", "Tailwind CSS"])

    with tabs[0]:
        st.markdown('<h2 class="section-header">CSS Clasic în React</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### CSS Traditional cu React

        Cea mai directă metodă de stilizare în React este folosirea CSS-ului tradițional.
        React suportă atât **clase CSS** cât și **inline styles**.
        """)

        st.markdown("### 1. Inline Styles")

        st.code("""
// Inline styles în React - obiecte JavaScript
function InlineStylesExample() {
    // Styles ca obiecte JavaScript
    const containerStyle = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '20px',
        backgroundColor: '#f0f2f5',
        borderRadius: '8px',
        boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)'
    };

    const titleStyle = {
        fontSize: '2rem',
        fontWeight: 'bold',
        color: '#1a365d',
        marginBottom: '16px',
        textAlign: 'center'
    };

    const buttonStyle = {
        backgroundColor: '#3182ce',
        color: 'white',
        border: 'none',
        padding: '12px 24px',
        borderRadius: '6px',
        fontSize: '16px',
        cursor: 'pointer',
        transition: 'all 0.2s ease-in-out',
        ':hover': { // Pseudo-selectors nu funcționează direct în inline styles
            backgroundColor: '#2c5aa0'
        }
    };

    return (
        <div style={containerStyle}>
            <h1 style={titleStyle}>Inline Styles Example</h1>
            <button style={buttonStyle}>
                Click Me
            </button>
        </div>
    );
}

// Dynamic inline styles bazate pe props/state
function DynamicInlineStyles({ isActive, theme = 'light' }) {
    const [isHovered, setIsHovered] = useState(false);

    // Styles calculaţi dinamic
    const dynamicStyles = {
        container: {
            padding: '16px',
            backgroundColor: theme === 'dark' ? '#2d3748' : '#ffffff',
            color: theme === 'dark' ? '#ffffff' : '#2d3748',
            border: `2px solid ${isActive ? '#48bb78' : '#e2e8f0'}`,
            borderRadius: '8px',
            transition: 'all 0.3s ease',
            transform: isHovered ? 'scale(1.02)' : 'scale(1)',
            cursor: 'pointer'
        },
        status: {
            display: 'inline-block',
            padding: '4px 8px',
            borderRadius: '4px',
            fontSize: '14px',
            fontWeight: 'bold',
            backgroundColor: isActive ? '#c6f6d5' : '#fed7d7',
            color: isActive ? '#22543d' : '#742a2a'
        }
    };

    return (
        <div 
            style={dynamicStyles.container}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            <h3>Dynamic Component</h3>
            <span style={dynamicStyles.status}>
                {isActive ? 'Active' : 'Inactive'}
            </span>
            <p>Theme: {theme}</p>
        </div>
    );
}

// Avantaje inline styles:
// ✅ Styling dinamic foarte uşor
// ✅ Scoped automat la componentă
// ✅ JavaScript variables în styles
// ✅ Nu există CSS class name conflicts

// Dezavantaje inline styles:
// ❌ Nu există pseudo-selectors (:hover, :focus)
// ❌ Nu există media queries
// ❌ Performance mai slab pentru styles complexe
// ❌ Dificil de maintainit pentru aplicaţii mari
        """, language="javascript")

        st.markdown("### 2. CSS Classes cu className")

        st.code("""
/* styles.css - CSS tradițional */
.card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 24px;
    margin: 16px 0;
    transition: transform 0.2s ease-in-out;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}

.card__title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2d3748;
    margin-bottom: 12px;
}

.card__content {
    color: #4a5568;
    line-height: 1.6;
    margin-bottom: 16px;
}

.card__actions {
    display: flex;
    gap: 12px;
    justify-content: flex-end;
}

.btn {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn--primary {
    background-color: #3182ce;
    color: white;
}

.btn--primary:hover {
    background-color: #2c5aa0;
}

.btn--secondary {
    background-color: #e2e8f0;
    color: #4a5568;
}

.btn--secondary:hover {
    background-color: #cbd5e0;
}

/* Responsive design */
@media (max-width: 768px) {
    .card {
        padding: 16px;
        margin: 8px 0;
    }

    .card__actions {
        flex-direction: column;
    }

    .btn {
        width: 100%;
    }
}

/* Dark theme support */
.dark .card {
    background-color: #2d3748;
    color: #ffffff;
}

.dark .card__title {
    color: #ffffff;
}

.dark .card__content {
    color: #a0aec0;
}
        """, language="css")

        st.code("""
// Component folosind CSS classes
import React, { useState } from 'react';
import './styles.css'; // Import CSS file

function ClassNamesExample({ title, content, onSave, onCancel }) {
    const [isDarkMode, setIsDarkMode] = useState(false);

    // Conditional class names
    const containerClass = `card ${isDarkMode ? 'dark' : ''}`;

    return (
        <div className={containerClass}>
            <h2 className="card__title">{title}</h2>
            <p className="card__content">{content}</p>

            <div className="card__actions">
                <button className="btn btn--secondary" onClick={onCancel}>
                    Cancel
                </button>
                <button className="btn btn--primary" onClick={onSave}>
                    Save
                </button>
            </div>

            <button 
                onClick={() => setIsDarkMode(!isDarkMode)}
                className="btn btn--secondary"
                style={{ marginTop: '12px' }}
            >
                Toggle {isDarkMode ? 'Light' : 'Dark'} Mode
            </button>
        </div>
    );
}

// Dynamic class names cu conditionals
function DynamicClasses({ isLoading, hasError, isSuccess }) {
    // Multiple ways să construieşti class names

    // 1. Template literals
    const statusClass = `status ${isLoading ? 'status--loading' : ''} ${hasError ? 'status--error' : ''} ${isSuccess ? 'status--success' : ''}`;

    // 2. Array join
    const statusClassArray = [
        'status',
        isLoading && 'status--loading',
        hasError && 'status--error', 
        isSuccess && 'status--success'
    ].filter(Boolean).join(' ');

    // 3. Object cu keys
    const statusClasses = {
        'status': true,
        'status--loading': isLoading,
        'status--error': hasError,
        'status--success': isSuccess
    };

    const statusClassFromObject = Object.keys(statusClasses)
        .filter(key => statusClasses[key])
        .join(' ');

    return (
        <div>
            <div className={statusClass}>Template Literal Method</div>
            <div className={statusClassArray}>Array Method</div>
            <div className={statusClassFromObject}>Object Method</div>
        </div>
    );
}

// Helper library: classnames pentru managementul claslor
// npm install classnames
import classNames from 'classnames';

function ClassNamesLibrary({ isActive, isDisabled, variant = 'primary' }) {
    const buttonClass = classNames('btn', {
        'btn--active': isActive,
        'btn--disabled': isDisabled,
        [`btn--${variant}`]: variant
    });

    const iconClass = classNames('icon', {
        'icon--spin': isActive && !isDisabled
    });

    return (
        <button className={buttonClass} disabled={isDisabled}>
            <span className={iconClass}>⚡</span>
            Button Text
        </button>
    );
}

// CSS cu CSS Variables pentru theming
function CSSVariablesExample() {
    const [primaryColor, setPrimaryColor] = useState('#3182ce');

    // Setăm CSS variables dinamic
    const cssVariables = {
        '--primary-color': primaryColor,
        '--primary-color-hover': darkenColor(primaryColor, 10),
        '--border-radius': '8px',
        '--spacing-unit': '8px'
    };

    return (
        <div style={cssVariables} className="css-variables-container">
            <h3>CSS Variables Example</h3>
            <input 
                type="color" 
                value={primaryColor}
                onChange={(e) => setPrimaryColor(e.target.value)}
            />
            <button className="themed-button">Themed Button</button>
        </div>
    );
}

function darkenColor(color, percent) {
    // Helper function pentru culori mai închise
    const amount = Math.round(2.55 * percent);
    const num = parseInt(color.replace("#", ""), 16);
    return "#" + (0x1000000 + (Math.max(0, Math.min(255, (num >> 16) - amount)) << 16) +
        (Math.max(0, Math.min(255, (num >> 8 & 0x00FF) - amount)) << 8) +
        Math.max(0, Math.min(255, (num & 0x0000FF) - amount))).toString(16).slice(1);
}
        """, language="javascript")

        st.code("""
/* CSS Variables pentru theming */
.css-variables-container {
    --primary-color: #3182ce;
    --primary-color-hover: #2c5aa0;
    --secondary-color: #718096;
    --background-color: #ffffff;
    --text-color: #2d3748;
    --border-radius: 8px;
    --spacing-unit: 8px;
    --transition-speed: 0.2s;
}

.themed-button {
    background-color: var(--primary-color);
    color: white;
    border: none;
    padding: calc(var(--spacing-unit) * 1.5) calc(var(--spacing-unit) * 3);
    border-radius: var(--border-radius);
    font-size: 16px;
    cursor: pointer;
    transition: background-color var(--transition-speed) ease;
}

.themed-button:hover {
    background-color: var(--primary-color-hover);
}

/* Dark theme override */
.css-variables-container.dark {
    --background-color: #2d3748;
    --text-color: #ffffff;
    --secondary-color: #a0aec0;
}

/* Responsive spacing cu CSS variables */
@media (max-width: 768px) {
    .css-variables-container {
        --spacing-unit: 4px;
        --border-radius: 4px;
    }
}
        """, language="css")

        st.markdown("### 3. SASS/SCSS în React")

        st.code("""
// Installation: npm install sass

/* styles.scss - SASS/SCSS features */

// Variables
$primary-color: #3182ce;
$secondary-color: #718096;
$border-radius: 8px;
$spacing-base: 8px;

// Mixins
@mixin flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

@mixin button-variant($bg-color, $text-color: white) {
    background-color: $bg-color;
    color: $text-color;
    border: none;
    padding: ($spacing-base * 1.5) ($spacing-base * 3);
    border-radius: $border-radius;
    cursor: pointer;
    transition: all 0.2s ease;

    &:hover {
        background-color: darken($bg-color, 10%);
        transform: translateY(-1px);
    }

    &:active {
        transform: translateY(0);
    }

    &:disabled {
        background-color: lighten($bg-color, 20%);
        cursor: not-allowed;
        transform: none;
    }
}

@mixin responsive($breakpoint) {
    @if $breakpoint == mobile {
        @media (max-width: 767px) { @content; }
    }
    @if $breakpoint == tablet {
        @media (min-width: 768px) and (max-width: 1023px) { @content; }
    }
    @if $breakpoint == desktop {
        @media (min-width: 1024px) { @content; }
    }
}

// Nested selectors cu SASS
.card {
    background: white;
    border-radius: $border-radius;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: $spacing-base * 3;
    margin: $spacing-base * 2 0;

    &__header {
        @include flex-center;
        margin-bottom: $spacing-base * 2;

        &--centered {
            text-align: center;
        }
    }

    &__title {
        font-size: 1.5rem;
        font-weight: 600;
        color: $primary-color;
        margin: 0;

        &--large {
            font-size: 2rem;
        }
    }

    &__content {
        color: $secondary-color;
        line-height: 1.6;
        margin-bottom: $spacing-base * 2;

        p {
            margin-bottom: $spacing-base;

            &:last-child {
                margin-bottom: 0;
            }
        }
    }

    &__actions {
        display: flex;
        gap: $spacing-base * 1.5;
        justify-content: flex-end;

        @include responsive(mobile) {
            flex-direction: column;
            gap: $spacing-base;
        }
    }

    // State classes
    &--loading {
        opacity: 0.7;
        pointer-events: none;
    }

    &--error {
        border-left: 4px solid #e53e3e;
    }

    &--success {
        border-left: 4px solid #38a169;
    }
}

// Button variants cu mixins
.btn {
    &--primary {
        @include button-variant($primary-color);
    }

    &--secondary {
        @include button-variant($secondary-color);
    }

    &--danger {
        @include button-variant(#e53e3e);
    }

    &--outline {
        background: transparent;
        border: 2px solid $primary-color;
        color: $primary-color;
        padding: ($spacing-base * 1.5 - 2px) ($spacing-base * 3 - 2px);

        &:hover {
            background: $primary-color;
            color: white;
        }
    }
}

// Functions în SASS
@function px-to-rem($px, $base: 16px) {
    @return ($px / $base) * 1rem;
}

.typography {
    &--small { font-size: px-to-rem(12px); }
    &--normal { font-size: px-to-rem(16px); }
    &--large { font-size: px-to-rem(20px); }
    &--xl { font-size: px-to-rem(24px); }
}

// Advanced SASS features
%flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal {
    @extend %flex-center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);

    &__content {
        background: white;
        border-radius: $border-radius;
        padding: $spacing-base * 4;
        max-width: 500px;
        width: 90%;

        @include responsive(mobile) {
            padding: $spacing-base * 2;
            margin: $spacing-base * 2;
        }
    }
}
        """, language="scss")

        st.code("""
// Component folosind SASS
import React, { useState } from 'react';
import './styles.scss'; // Import SASS file

function SASSExample() {
    const [isLoading, setIsLoading] = useState(false);
    const [status, setStatus] = useState('normal'); // normal, error, success

    const cardClasses = [
        'card',
        isLoading && 'card--loading',
        status === 'error' && 'card--error',
        status === 'success' && 'card--success'
    ].filter(Boolean).join(' ');

    const handleAction = (actionType) => {
        setIsLoading(true);

        setTimeout(() => {
            setIsLoading(false);
            setStatus(actionType === 'success' ? 'success' : 'error');

            // Reset status după 3 secunde
            setTimeout(() => setStatus('normal'), 3000);
        }, 2000);
    };

    return (
        <div className={cardClasses}>
            <div className="card__header card__header--centered">
                <h2 className="card__title card__title--large">
                    SASS Example Card
                </h2>
            </div>

            <div className="card__content">
                <p>Această componentă folosește SASS pentru styling avansat.</p>
                <p>Include nested selectors, mixins, variables și responsive design.</p>
                <p className="typography--small">
                    Status current: {status}
                </p>
            </div>

            <div className="card__actions">
                <button 
                    className="btn btn--secondary"
                    onClick={() => handleAction('error')}
                    disabled={isLoading}
                >
                    Trigger Error
                </button>
                <button 
                    className="btn btn--primary"
                    onClick={() => handleAction('success')}
                    disabled={isLoading}
                >
                    {isLoading ? 'Loading...' : 'Trigger Success'}
                </button>
                <button className="btn btn--outline">
                    Outline Button
                </button>
            </div>
        </div>
    );
}

export default SASSExample;
        """, language="javascript")

    with tabs[1]:
        st.markdown('<h2 class="section-header">CSS Modules</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Ce sunt CSS Modules?

        CSS Modules oferă **scoped CSS** prin generarea automată de class names unice. 
        Acest lucru elimină conflictele de nume și permite modularizarea stilurilor.
        """)

        st.markdown("### Configurare și Utilizare de Bază")

        st.code("""
/* Button.module.css - Fișier CSS Module */
.container {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.button {
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    position: relative;
    overflow: hidden;
}

.button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5);
}

/* Button variants */
.primary {
    background-color: #3182ce;
    color: white;
}

.primary:hover:not(:disabled) {
    background-color: #2c5aa0;
    transform: translateY(-1px);
}

.secondary {
    background-color: #e2e8f0;
    color: #4a5568;
}

.secondary:hover:not(:disabled) {
    background-color: #cbd5e0;
}

.danger {
    background-color: #e53e3e;
    color: white;
}

.danger:hover:not(:disabled) {
    background-color: #c53030;
}

.outline {
    background-color: transparent;
    border: 2px solid #3182ce;
    color: #3182ce;
}

.outline:hover:not(:disabled) {
    background-color: #3182ce;
    color: white;
}

/* Size variants */
.small {
    padding: 8px 16px;
    font-size: 14px;
}

.large {
    padding: 16px 32px;
    font-size: 18px;
}

.fullWidth {
    width: 100%;
    justify-content: center;
}

/* Loading state */
.loading {
    pointer-events: none;
}

.spinner {
    display: inline-block;
    width: 16px;
    height: 16px;
    border: 2px solid transparent;
    border-top: 2px solid currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
}
        """, language="css")

        st.code("""
// Button.jsx - Component folosind CSS Modules
import React from 'react';
import styles from './Button.module.css'; // Import ca obiect

function Button({
    children,
    variant = 'primary',
    size = 'medium',
    fullWidth = false,
    loading = false,
    disabled = false,
    icon,
    onClick,
    ...props
}) {
    // Construirea class names folosind CSS Modules
    const buttonClasses = [
        styles.button,              // styles.button = "Button_button__a1b2c3"
        styles[variant],            // styles.primary = "Button_primary__d4e5f6"
        size !== 'medium' && styles[size],
        fullWidth && styles.fullWidth,
        loading && styles.loading
    ].filter(Boolean).join(' ');

    const containerClasses = [
        styles.container,
        fullWidth && styles.fullWidth
    ].filter(Boolean).join(' ');

    return (
        <div className={containerClasses}>
            <button
                className={buttonClasses}
                disabled={disabled || loading}
                onClick={onClick}
                {...props}
            >
                {loading ? (
                    <span className={styles.spinner} />
                ) : icon ? (
                    <span className={styles.icon}>{icon}</span>
                ) : null}

                {children}
            </button>
        </div>
    );
}

export default Button;

// Utilizarea componentei
function App() {
    const [loading, setLoading] = useState(false);

    const handleClick = () => {
        setLoading(true);
        setTimeout(() => setLoading(false), 2000);
    };

    return (
        <div>
            <Button variant="primary" onClick={handleClick} loading={loading}>
                Primary Button
            </Button>

            <Button variant="secondary" size="small">
                Small Secondary
            </Button>

            <Button variant="danger" size="large" icon="🗑️">
                Delete
            </Button>

            <Button variant="outline" fullWidth>
                Full Width Outline
            </Button>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Composition Pattern cu CSS Modules")

        st.code("""
/* Card.module.css - Complex component styling */
.card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    overflow: hidden;
    transition: all 0.3s ease;
    border: 1px solid #e2e8f0;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.header {
    padding: 24px 24px 0 24px;
}

.headerWithImage {
    padding: 0;
}

.image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.content {
    padding: 24px;
}

.contentWithHeader {
    padding-top: 16px;
}

.title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2d3748;
    margin: 0 0 8px 0;
    line-height: 1.3;
}

.subtitle {
    font-size: 0.875rem;
    color: #718096;
    margin: 0 0 16px 0;
}

.description {
    color: #4a5568;
    line-height: 1.6;
    margin: 0 0 16px 0;
}

.footer {
    padding: 0 24px 24px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footerActions {
    display: flex;
    gap: 12px;
}

.metadata {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.metadataItem {
    font-size: 0.75rem;
    color: #718096;
}

/* Card variants */
.elevated {
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.outlined {
    border: 2px solid #3182ce;
    box-shadow: none;
}

.ghost {
    background: transparent;
    box-shadow: none;
    border: 1px dashed #cbd5e0;
}

/* Responsive design */
@media (max-width: 768px) {
    .header,
    .content,
    .footer {
        padding-left: 16px;
        padding-right: 16px;
    }

    .footer {
        flex-direction: column;
        gap: 12px;
        align-items: stretch;
    }

    .footerActions {
        justify-content: center;
    }
}
        """, language="css")

        st.code("""
// Card.jsx - Complex component cu CSS Modules
import React from 'react';
import styles from './Card.module.css';
import Button from './Button'; // Assume că avem componenta Button

function Card({
    title,
    subtitle,
    description,
    image,
    actions,
    metadata,
    variant = 'default',
    className,
    children,
    ...props
}) {
    const cardClasses = [
        styles.card,
        variant !== 'default' && styles[variant],
        className
    ].filter(Boolean).join(' ');

    const contentClasses = [
        styles.content,
        (title || subtitle) && styles.contentWithHeader
    ].filter(Boolean).join(' ');

    const headerClasses = [
        styles.header,
        image && styles.headerWithImage
    ].filter(Boolean).join(' ');

    return (
        <div className={cardClasses} {...props}>
            {image && (
                <img src={image} alt={title} className={styles.image} />
            )}

            {(title || subtitle) && (
                <div className={headerClasses}>
                    {title && <h3 className={styles.title}>{title}</h3>}
                    {subtitle && <p className={styles.subtitle}>{subtitle}</p>}
                </div>
            )}

            <div className={contentClasses}>
                {description && (
                    <p className={styles.description}>{description}</p>
                )}
                {children}
            </div>

            {(actions || metadata) && (
                <div className={styles.footer}>
                    {metadata && (
                        <div className={styles.metadata}>
                            {metadata.map((item, index) => (
                                <span key={index} className={styles.metadataItem}>
                                    {item}
                                </span>
                            ))}
                        </div>
                    )}

                    {actions && (
                        <div className={styles.footerActions}>
                            {actions}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

// Usage examples
function CardExamples() {
    return (
        <div style={{ display: 'grid', gap: '24px', maxWidth: '800px' }}>
            {/* Basic card */}
            <Card
                title="Basic Card"
                description="This is a basic card with title and description."
                actions={[
                    <Button key="1" variant="primary" size="small">Action</Button>
                ]}
            />

            {/* Card with image */}
            <Card
                title="Card with Image"
                subtitle="Beautiful landscape"
                description="This card includes an image at the top."
                image="https://picsum.photos/400/200?random=1"
                metadata={['Photography', 'Nature', '2024']}
                actions={[
                    <Button key="1" variant="secondary" size="small">View</Button>,
                    <Button key="2" variant="primary" size="small">Download</Button>
                ]}
            />

            {/* Elevated variant */}
            <Card
                variant="elevated"
                title="Elevated Card"
                description="This card has more prominent shadow."
            />

            {/* Outlined variant */}
            <Card
                variant="outlined"
                title="Outlined Card"
                description="This card has a colored border instead of shadow."
            />

            {/* Card with custom content */}
            <Card
                title="Custom Content Card"
                subtitle="Advanced example"
                actions={[
                    <Button key="1" variant="danger" size="small" icon="🗑️">
                        Delete
                    </Button>
                ]}
            >
                <div style={{ 
                    background: '#f7fafc', 
                    padding: '16px', 
                    borderRadius: '8px',
                    marginBottom: '16px'
                }}>
                    <strong>Custom content area</strong>
                    <p style={{ margin: '8px 0 0 0', fontSize: '14px' }}>
                        You can add any custom content here.
                    </p>
                </div>

                <ul style={{ margin: 0, paddingLeft: '20px' }}>
                    <li>Feature 1</li>
                    <li>Feature 2</li>
                    <li>Feature 3</li>
                </ul>
            </Card>
        </div>
    );
}

export default CardExamples;
        """, language="javascript")

        st.markdown("### Composition și Global Styles")

        st.code("""
/* global.module.css - Global utilities cu CSS Modules */
/* Typography */
.textXs { font-size: 0.75rem; }
.textSm { font-size: 0.875rem; }
.textBase { font-size: 1rem; }
.textLg { font-size: 1.125rem; }
.textXl { font-size: 1.25rem; }
.text2xl { font-size: 1.5rem; }
.text3xl { font-size: 1.875rem; }

.fontThin { font-weight: 100; }
.fontLight { font-weight: 300; }
.fontNormal { font-weight: 400; }
.fontMedium { font-weight: 500; }
.fontSemibold { font-weight: 600; }
.fontBold { font-weight: 700; }

/* Colors */
.textGray100 { color: #f7fafc; }
.textGray500 { color: #a0aec0; }
.textGray900 { color: #1a202c; }
.textBlue500 { color: #4299e1; }
.textGreen500 { color: #48bb78; }
.textRed500 { color: #f56565; }

.bgWhite { background-color: #ffffff; }
.bgGray50 { background-color: #f7fafc; }
.bgGray100 { background-color: #edf2f7; }
.bgBlue500 { background-color: #4299e1; }

/* Spacing */
.m0 { margin: 0; }
.m1 { margin: 0.25rem; }
.m2 { margin: 0.5rem; }
.m4 { margin: 1rem; }
.m8 { margin: 2rem; }

.p0 { padding: 0; }
.p1 { padding: 0.25rem; }
.p2 { padding: 0.5rem; }
.p4 { padding: 1rem; }
.p8 { padding: 2rem; }

.mt0 { margin-top: 0; }
.mt2 { margin-top: 0.5rem; }
.mt4 { margin-top: 1rem; }
.mb2 { margin-bottom: 0.5rem; }
.mb4 { margin-bottom: 1rem; }

.px2 { padding-left: 0.5rem; padding-right: 0.5rem; }
.px4 { padding-left: 1rem; padding-right: 1rem; }
.py2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.py4 { padding-top: 1rem; padding-bottom: 1rem; }

/* Layout */
.flex { display: flex; }
.inlineFlex { display: inline-flex; }
.block { display: block; }
.inlineBlock { display: inline-block; }
.hidden { display: none; }

.flexCol { flex-direction: column; }
.flexRow { flex-direction: row; }

.itemsCenter { align-items: center; }
.itemsStart { align-items: flex-start; }
.itemsEnd { align-items: flex-end; }

.justifyCenter { justify-content: center; }
.justifyBetween { justify-content: space-between; }
.justifyAround { justify-content: space-around; }
.justifyStart { justify-content: flex-start; }
.justifyEnd { justify-content: flex-end; }

.gap1 { gap: 0.25rem; }
.gap2 { gap: 0.5rem; }
.gap4 { gap: 1rem; }
.gap8 { gap: 2rem; }

/* Borders */
.rounded { border-radius: 0.25rem; }
.roundedMd { border-radius: 0.375rem; }
.roundedLg { border-radius: 0.5rem; }
.roundedXl { border-radius: 0.75rem; }
.rounded2xl { border-radius: 1rem; }
.roundedFull { border-radius: 9999px; }

.border { border: 1px solid #e2e8f0; }
.border2 { border: 2px solid #e2e8f0; }
.borderGray200 { border-color: #edf2f7; }
.borderBlue500 { border-color: #4299e1; }

/* Shadows */
.shadowSm { box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); }
.shadow { box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); }
.shadowMd { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07); }
.shadowLg { box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1); }

/* Position */
.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }

.top0 { top: 0; }
.right0 { right: 0; }
.bottom0 { bottom: 0; }
.left0 { left: 0; }

/* Width & Height */
.wFull { width: 100%; }
.hFull { height: 100%; }
.w32 { width: 8rem; }
.h32 { height: 8rem; }

/* Responsive utilities */
@media (max-width: 640px) {
    .smHidden { display: none; }
    .smBlock { display: block; }
    .smFlex { display: flex; }
    .smFlexCol { flex-direction: column; }
}

@media (min-width: 768px) {
    .mdBlock { display: block; }
    .mdFlex { display: flex; }
    .mdFlexRow { flex-direction: row; }
}

@media (min-width: 1024px) {
    .lgBlock { display: block; }
    .lgFlex { display: flex; }
}
        """, language="css")

        st.code("""
// utils/classNames.js - Helper pentru CSS Modules
import globalStyles from '../styles/global.module.css';

// Helper function pentru combining CSS Modules classes
export function cn(...classNames) {
    return classNames
        .flat()
        .filter(Boolean)
        .join(' ');
}

// Helper pentru global utility classes
export function createUtilityClass(utilityName) {
    return globalStyles[utilityName] || '';
}

// Bulk utility class creator
export function utils(utilityNames) {
    if (typeof utilityNames === 'string') {
        return utilityNames.split(' ').map(name => globalStyles[name] || '').join(' ');
    }

    if (Array.isArray(utilityNames)) {
        return utilityNames.map(name => globalStyles[name] || '').join(' ');
    }

    return '';
}

// Advanced composition helper
export function composeStyles(baseStyles, ...additionalStyles) {
    const base = typeof baseStyles === 'string' ? baseStyles : 
                 Object.values(baseStyles).join(' ');

    const additional = additionalStyles
        .flat()
        .filter(Boolean)
        .map(style => typeof style === 'string' ? style : Object.values(style).join(' '))
        .join(' ');

    return cn(base, additional);
}

// Usage în components
import React from 'react';
import styles from './UtilityExample.module.css';
import { cn, utils, composeStyles } from '../utils/classNames';

function UtilityExample() {
    return (
        <div className={cn(
            styles.container,
            utils('flex flexCol gap4 p8 bgGray50 rounded2xl shadow')
        )}>
            <h2 className={utils('text2xl fontBold textGray900 mb4')}>
                Utility Classes Example
            </h2>

            <div className={utils('flex gap4 itemsCenter')}>
                <button className={composeStyles(
                    styles.button,
                    utils('px4 py2 bgBlue500 textWhite roundedMd shadow')
                )}>
                    Primary Action
                </button>

                <button className={cn(
                    styles.button,
                    utils('px4 py2 border borderGray200 textGray900 roundedMd')
                )}>
                    Secondary Action
                </button>
            </div>

            <div className={utils('grid gridCols2 gap4 mt8 mdGridCols4')}>
                {[1, 2, 3, 4].map(num => (
                    <div 
                        key={num}
                        className={utils('p4 bgWhite rounded border shadowSm')}
                    >
                        <div className={utils('w8 h8 bgBlue500 roundedFull mb2')} />
                        <h3 className={utils('fontSemibold textGray900')}>
                            Item {num}
                        </h3>
                        <p className={utils('textSm textGray500 mt1')}>
                            Description for item {num}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
}
        """, language="javascript")

    with tabs[2]:
        st.markdown('<h2 class="section-header">Styled Components</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### CSS-in-JS cu Styled Components

        Styled Components este o bibliotecă CSS-in-JS care permite scrierea CSS-ului direct în JavaScript, 
        oferind **dynamic styling**, **theming** și **component-based architecture**.
        """)

        st.markdown("### Installation și Setup")

        st.code("""
# Installation
npm install styled-components

# TypeScript support (opțional)
npm install --save-dev @types/styled-components

# Babel plugin pentru optimizare (opțional)
npm install --save-dev babel-plugin-styled-components
        """, language="bash")

        st.markdown("### Basic Styled Components")

        st.code("""
// Basic styled components examples
import styled from 'styled-components';

// Basic styled component
const Button = styled.button`
    background-color: #3182ce;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease-in-out;

    &:hover {
        background-color: #2c5aa0;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    &:active {
        transform: translateY(0);
    }

    &:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5);
    }

    &:disabled {
        background-color: #a0aec0;
        cursor: not-allowed;
        transform: none;

        &:hover {
            background-color: #a0aec0;
            transform: none;
            box-shadow: none;
        }
    }
`;

// Styled component cu props
const DynamicButton = styled.button`
    background-color: ${props => {
        switch (props.variant) {
            case 'primary': return '#3182ce';
            case 'secondary': return '#718096';
            case 'danger': return '#e53e3e';
            case 'success': return '#38a169';
            default: return '#3182ce';
        }
    }};

    color: ${props => props.variant === 'secondary' ? '#2d3748' : 'white'};
    border: ${props => props.outline ? `2px solid ${props.color || '#3182ce'}` : 'none'};
    background-color: ${props => props.outline ? 'transparent' : undefined};
    color: ${props => props.outline ? (props.color || '#3182ce') : undefined};

    padding: ${props => {
        switch (props.size) {
            case 'small': return '8px 16px';
            case 'large': return '16px 32px';
            default: return '12px 24px';
        }
    }};

    font-size: ${props => {
        switch (props.size) {
            case 'small': return '14px';
            case 'large': return '18px';
            default: return '16px';
        }
    }};

    width: ${props => props.fullWidth ? '100%' : 'auto'};

    border-radius: 6px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;

    &:hover:not(:disabled) {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);

        ${props => props.outline && `
            background-color: ${props.color || '#3182ce'};
            color: white;
        `}
    }

    &:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none;
    }

    ${props => props.loading && `
        pointer-events: none;
        opacity: 0.8;
    `}
`;

// Extending styled components
const IconButton = styled(DynamicButton)`
    padding: ${props => {
        switch (props.size) {
            case 'small': return '8px';
            case 'large': return '16px';
            default: return '12px';
        }
    }};

    border-radius: 50%;
    aspect-ratio: 1;
`;

// Container components
const Container = styled.div`
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 16px;

    @media (min-width: 768px) {
        padding: 0 24px;
    }

    @media (min-width: 1024px) {
        padding: 0 32px;
    }
`;

const Card = styled.div`
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    padding: 24px;
    margin: 16px 0;
    transition: all 0.3s ease;
    border: 1px solid #e2e8f0;

    &:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }

    ${props => props.variant === 'outlined' && `
        border: 2px solid #3182ce;
        box-shadow: none;
    `}

    ${props => props.variant === 'elevated' && `
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
    `}
`;

const CardHeader = styled.div`
    margin-bottom: 16px;

    ${props => props.centered && `
        text-align: center;
    `}
`;

const CardTitle = styled.h3`
    font-size: 1.25rem;
    font-weight: 600;
    color: #2d3748;
    margin: 0 0 8px 0;
    line-height: 1.3;

    ${props => props.size === 'large' && `
        font-size: 1.5rem;
    `}

    ${props => props.size === 'small' && `
        font-size: 1rem;
    `}
`;

const CardContent = styled.div`
    color: #4a5568;
    line-height: 1.6;
    margin-bottom: 16px;

    p {
        margin-bottom: 12px;

        &:last-child {
            margin-bottom: 0;
        }
    }
`;

// Usage example
function StyledComponentsBasic() {
    const [loading, setLoading] = useState(false);

    const handleClick = () => {
        setLoading(true);
        setTimeout(() => setLoading(false), 2000);
    };

    return (
        <Container>
            <Card>
                <CardHeader centered>
                    <CardTitle size="large">Styled Components Example</CardTitle>
                </CardHeader>

                <CardContent>
                    <p>Această componentă demonstrează puterea Styled Components pentru styling dinamic și flexibil.</p>
                </CardContent>

                <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
                    <DynamicButton variant="primary" onClick={handleClick} loading={loading}>
                        {loading ? 'Loading...' : 'Primary'}
                    </DynamicButton>

                    <DynamicButton variant="secondary" size="small">
                        Secondary Small
                    </DynamicButton>

                    <DynamicButton variant="danger" outline>
                        Danger Outline
                    </DynamicButton>

                    <DynamicButton variant="success" size="large" fullWidth>
                        Success Full Width
                    </DynamicButton>

                    <IconButton variant="primary" size="small">
                        ⚙️
                    </IconButton>
                </div>
            </Card>

            <Card variant="outlined">
                <CardTitle>Outlined Card Variant</CardTitle>
                <CardContent>
                    <p>Această variantă de card are o bordură colorată în loc de umbră.</p>
                </CardContent>
            </Card>
        </Container>
    );
}
        """, language="javascript")

        st.markdown("### Theming System cu Styled Components")

        st.code("""
// theme.js - Definirea theme-ului
export const lightTheme = {
    colors: {
        primary: '#3182ce',
        primaryHover: '#2c5aa0',
        secondary: '#718096',
        secondaryHover: '#4a5568',
        success: '#38a169',
        successHover: '#2f855a',
        danger: '#e53e3e',
        dangerHover: '#c53030',
        warning: '#dd6b20',
        warningHover: '#c05621',

        // Grays
        gray50: '#f7fafc',
        gray100: '#edf2f7',
        gray200: '#e2e8f0',
        gray300: '#cbd5e0',
        gray400: '#a0aec0',
        gray500: '#718096',
        gray600: '#4a5568',
        gray700: '#2d3748',
        gray800: '#1a202c',
        gray900: '#171923',

        // Semantic colors
        background: '#ffffff',
        surface: '#f7fafc',
        text: '#2d3748',
        textSecondary: '#4a5568',
        textMuted: '#718096',
        border: '#e2e8f0',

        // Status colors
        info: '#3182ce',
        infoLight: '#bee3f8',
        successLight: '#c6f6d5',
        warningLight: '#faf089',
        dangerLight: '#fed7d7'
    },

    fonts: {
        body: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        heading: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        mono: 'SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace'
    },

    fontSizes: {
        xs: '0.75rem',
        sm: '0.875rem',
        base: '1rem',
        lg: '1.125rem',
        xl: '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
        '5xl': '3rem'
    },

    fontWeights: {
        thin: 100,
        light: 300,
        normal: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
        extrabold: 800,
        black: 900
    },

    lineHeights: {
        tight: 1.25,
        snug: 1.375,
        normal: 1.5,
        relaxed: 1.625,
        loose: 2
    },

    space: {
        0: '0',
        1: '0.25rem',
        2: '0.5rem',
        3: '0.75rem',
        4: '1rem',
        5: '1.25rem',
        6: '1.5rem',
        8: '2rem',
        10: '2.5rem',
        12: '3rem',
        16: '4rem',
        20: '5rem',
        24: '6rem',
        32: '8rem'
    },

    sizes: {
        xs: '20rem',
        sm: '24rem',
        md: '28rem',
        lg: '32rem',
        xl: '36rem',
        '2xl': '42rem',
        '3xl': '48rem',
        '4xl': '56rem',
        '5xl': '64rem',
        '6xl': '72rem',
        full: '100%'
    },

    radii: {
        none: '0',
        sm: '0.125rem',
        base: '0.25rem',
        md: '0.375rem',
        lg: '0.5rem',
        xl: '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
        full: '9999px'
    },

    shadows: {
        xs: '0 0 0 1px rgba(0, 0, 0, 0.05)',
        sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        base: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
        outline: '0 0 0 3px rgba(66, 153, 225, 0.5)',
        none: 'none'
    },

    breakpoints: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px'
    },

    zIndices: {
        hide: -1,
        auto: 'auto',
        base: 0,
        docked: 10,
        dropdown: 1000,
        sticky: 1100,
        banner: 1200,
        overlay: 1300,
        modal: 1400,
        popover: 1500,
        skipLink: 1600,
        toast: 1700,
        tooltip: 1800
    }
};

export const darkTheme = {
    ...lightTheme,
    colors: {
        ...lightTheme.colors,
        primary: '#4299e1',
        primaryHover: '#3182ce',

        // Dark mode specific colors
        background: '#1a202c',
        surface: '#2d3748',
        text: '#ffffff',
        textSecondary: '#e2e8f0',
        textMuted: '#a0aec0',
        border: '#4a5568',

        // Adjusted grays for dark mode
        gray50: '#171923',
        gray100: '#1a202c',
        gray200: '#2d3748',
        gray300: '#4a5568',
        gray400: '#718096',
        gray500: '#a0aec0',
        gray600: '#cbd5e0',
        gray700: '#e2e8f0',
        gray800: '#edf2f7',
        gray900: '#f7fafc'
    }
};
        """, language="javascript")

        st.code("""
// ThemeProvider setup și themed components
import React, { useState, createContext, useContext } from 'react';
import styled, { ThemeProvider, createGlobalStyle } from 'styled-components';
import { lightTheme, darkTheme } from './theme';

// Global styles cu theme support
const GlobalStyle = createGlobalStyle`
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: ${props => props.theme.fonts.body};
        background-color: ${props => props.theme.colors.background};
        color: ${props => props.theme.colors.text};
        line-height: ${props => props.theme.lineHeights.normal};
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: ${props => props.theme.fonts.heading};
        font-weight: ${props => props.theme.fontWeights.semibold};
        line-height: ${props => props.theme.lineHeights.tight};
    }

    button {
        font-family: inherit;
    }

    a {
        color: ${props => props.theme.colors.primary};
        text-decoration: none;

        &:hover {
            color: ${props => props.theme.colors.primaryHover};
        }
    }
`;

// Theme context pentru theme switching
const ThemeContext = createContext();

export function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within a ThemeProvider');
    }
    return context;
}

export function CustomThemeProvider({ children }) {
    const [isDark, setIsDark] = useState(false);
    const theme = isDark ? darkTheme : lightTheme;

    const toggleTheme = () => setIsDark(!isDark);

    return (
        <ThemeContext.Provider value={{ isDark, toggleTheme, theme }}>
            <ThemeProvider theme={theme}>
                <GlobalStyle />
                {children}
            </ThemeProvider>
        </ThemeContext.Provider>
    );
}

// Themed components
const ThemedButton = styled.button`
    background-color: ${props => props.theme.colors[props.variant || 'primary']};
    color: ${props => {
        if (props.variant === 'secondary') return props.theme.colors.text;
        return 'white';
    }};
    border: ${props => props.outline ? `2px solid ${props.theme.colors[props.variant || 'primary']}` : 'none'};
    background-color: ${props => props.outline ? 'transparent' : undefined};
    color: ${props => props.outline ? props.theme.colors[props.variant || 'primary'] : undefined};

    padding: ${props => props.theme.space[props.size === 'small' ? 2 : props.size === 'large' ? 4 : 3]} 
             ${props => props.theme.space[props.size === 'small' ? 4 : props.size === 'large' ? 6 : 5]};

    border-radius: ${props => props.theme.radii[props.rounded || 'base']};
    font-size: ${props => props.theme.fontSizes[props.fontSize || 'base']};
    font-weight: ${props => props.theme.fontWeights.medium};
    font-family: ${props => props.theme.fonts.body};

    cursor: pointer;
    transition: all 0.2s ease-in-out;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: ${props => props.theme.space[2]};

    &:hover:not(:disabled) {
        background-color: ${props => props.outline 
            ? props.theme.colors[props.variant || 'primary']
            : props.theme.colors[`${props.variant || 'primary'}Hover`]
        };
        color: ${props => props.outline ? 'white' : undefined};
        transform: translateY(-1px);
        box-shadow: ${props => props.theme.shadows.md};
    }

    &:focus {
        outline: none;
        box-shadow: ${props => props.theme.shadows.outline};
    }

    &:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none;
    }

    ${props => props.fullWidth && 'width: 100%;'}
`;

const ThemedCard = styled.div`
    background-color: ${props => props.theme.colors.surface};
    border: 1px solid ${props => props.theme.colors.border};
    border-radius: ${props => props.theme.radii[props.rounded || 'lg']};
    box-shadow: ${props => props.theme.shadows[props.shadow || 'base']};
    padding: ${props => props.theme.space[props.padding || 6]};
    margin: ${props => props.theme.space[props.margin || 4]} 0;
    transition: all 0.3s ease;

    &:hover {
        transform: translateY(-2px);
        box-shadow: ${props => props.theme.shadows.lg};
    }

    @media (max-width: ${props => props.theme.breakpoints.md}) {
        padding: ${props => props.theme.space[4]};
        margin: ${props => props.theme.space[2]} 0;
    }
`;

const ThemedTitle = styled.h2`
    font-size: ${props => props.theme.fontSizes[props.size || '2xl']};
    font-weight: ${props => props.theme.fontWeights[props.weight || 'semibold']};
    color: ${props => props.theme.colors.text};
    margin-bottom: ${props => props.theme.space[props.mb || 4]};
    line-height: ${props => props.theme.lineHeights.tight};

    ${props => props.centered && 'text-align: center;'}
`;

const ThemedText = styled.p`
    font-size: ${props => props.theme.fontSizes[props.size || 'base']};
    color: ${props => props.color ? props.theme.colors[props.color] : props.theme.colors.textSecondary};
    line-height: ${props => props.theme.lineHeights[props.lineHeight || 'normal']};
    margin-bottom: ${props => props.theme.space[props.mb || 4]};

    &:last-child {
        margin-bottom: 0;
    }
`;

// Usage example cu theming
function ThemedComponents() {
    const { isDark, toggleTheme } = useTheme();

    return (
        <div style={{ padding: '20px' }}>
            <ThemedCard shadow="lg" rounded="xl">
                <ThemedTitle size="3xl" centered mb={6}>
                    Themed Components Example
                </ThemedTitle>

                <ThemedText size="lg" color="textMuted" mb={6}>
                    Aceste componente se adaptează automat la tema curentă. 
                    Încearcă să schimbi tema pentru a vedea diferența!
                </ThemedText>

                <div style={{ 
                    display: 'grid', 
                    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                    gap: '16px',
                    marginBottom: '24px'
                }}>
                    <ThemedButton variant="primary">Primary Button</ThemedButton>
                    <ThemedButton variant="secondary" outline>Secondary Outline</ThemedButton>
                    <ThemedButton variant="success" size="small">Small Success</ThemedButton>
                    <ThemedButton variant="danger" size="large" rounded="full">Large Danger</ThemedButton>
                </div>

                <ThemedButton 
                    variant={isDark ? 'warning' : 'info'} 
                    fullWidth 
                    onClick={toggleTheme}
                >
                    🌙 Switch to {isDark ? 'Light' : 'Dark'} Theme
                </ThemedButton>
            </ThemedCard>

            <ThemedCard>
                <ThemedTitle size="xl">Card cu Theme Adaptat</ThemedTitle>
                <ThemedText>
                    Această carte se schimbă automat între light și dark mode, 
                    inclusiv culorile, shadows și border-urile.
                </ThemedText>
                <ThemedText size="sm" color="textMuted">
                    Toate valorile vin din obiectul theme centralizat.
                </ThemedText>
            </ThemedCard>
        </div>
    );
}

// Main App cu ThemeProvider
export function App() {
    return (
        <CustomThemeProvider>
            <ThemedComponents />
        </CustomThemeProvider>
    );
}
        """, language="javascript")

    with tabs[3]:
        st.markdown('<h2 class="section-header">Tailwind CSS</h2>', unsafe_allow_html=True)

        st.markdown("""
        ### Utility-First CSS Framework

        Tailwind CSS este un framework CSS utility-first care permite construirea rapidă 
        a interfețelor prin componerea claselor mici și reutilizabile.
        """)

        st.markdown("### Installation și Configurare")

        st.code("""
# Installation în proiect React
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Sau folosind Create React App
npm install -D tailwindcss
npx tailwindcss init
        """, language="bash")

        st.code("""
// tailwind.config.js - Configurare customizată
module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
        "./public/index.html"
    ],
    darkMode: 'class', // sau 'media' pentru system preference
    theme: {
        extend: {
            // Custom colors
            colors: {
                brand: {
                    50: '#eff6ff',
                    100: '#dbeafe',
                    200: '#bfdbfe',
                    300: '#93c5fd',
                    400: '#60a5fa',
                    500: '#3b82f6',
                    600: '#2563eb',
                    700: '#1d4ed8',
                    800: '#1e40af',
                    900: '#1e3a8a',
                },
                gray: {
                    50: '#f9fafb',
                    100: '#f3f4f6',
                    200: '#e5e7eb',
                    300: '#d1d5db',
                    400: '#9ca3af',
                    500: '#6b7280',
                    600: '#4b5563',
                    700: '#374151',
                    800: '#1f2937',
                    900: '#111827',
                }
            },

            // Custom spacing
            spacing: {
                '18': '4.5rem',
                '88': '22rem',
                '128': '32rem'
            },

            // Custom font families
            fontFamily: {
                'sans': ['Inter', 'system-ui', 'sans-serif'],
                'serif': ['Georgia', 'serif'],
                'mono': ['Fira Code', 'monospace']
            },

            // Custom font sizes
            fontSize: {
                'xs': ['0.75rem', { lineHeight: '1rem' }],
                'sm': ['0.875rem', { lineHeight: '1.25rem' }],
                'base': ['1rem', { lineHeight: '1.5rem' }],
                'lg': ['1.125rem', { lineHeight: '1.75rem' }],
                'xl': ['1.25rem', { lineHeight: '1.75rem' }],
                '2xl': ['1.5rem', { lineHeight: '2rem' }],
                '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
                '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
                '5xl': ['3rem', { lineHeight: '1' }],
                '6xl': ['3.75rem', { lineHeight: '1' }],
            },

            // Custom breakpoints
            screens: {
                'xs': '475px',
                'sm': '640px',
                'md': '768px',
                'lg': '1024px',
                'xl': '1280px',
                '2xl': '1536px',
                '3xl': '1920px'
            },

            // Custom animations
            animation: {
                'fade-in': 'fadeIn 0.5s ease-in-out',
                'slide-up': 'slideUp 0.3s ease-out',
                'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'bounce-gentle': 'bounceGentle 2s infinite'
            },

            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' }
                },
                slideUp: {
                    '0%': { transform: 'translateY(10px)', opacity: '0' },
                    '100%': { transform: 'translateY(0)', opacity: '1' }
                },
                bounceGentle: {
                    '0%, 100%': { transform: 'translateY(-5%)' },
                    '50%': { transform: 'translateY(0)' }
                }
            },

            // Custom box shadows
            boxShadow: {
                'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
                'medium': '0 4px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
                'hard': '0 10px 40px -10px rgba(0, 0, 0, 0.2)',
                'inner-soft': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)'
            },

            // Custom border radius
            borderRadius: {
                'none': '0',
                'sm': '0.125rem',
                'DEFAULT': '0.25rem',
                'md': '0.375rem',
                'lg': '0.5rem',
                'xl': '0.75rem',
                '2xl': '1rem',
                '3xl': '1.5rem',
                'full': '9999px'
            }
        }
    },
    plugins: [
        require('@tailwindcss/forms'),      // Form styling
        require('@tailwindcss/typography'), // Typography plugin
        require('@tailwindcss/aspect-ratio'), // Aspect ratio utilities
        require('@tailwindcss/line-clamp')   // Line clamp utilities
    ]
}
        """, language="javascript")

        st.code("""
/* src/index.css - Import Tailwind */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom base styles */
@layer base {
    html {
        scroll-behavior: smooth;
    }

    body {
        @apply font-sans antialiased;
    }

    h1, h2, h3, h4, h5, h6 {
        @apply font-semibold text-gray-900 dark:text-gray-100;
    }

    h1 { @apply text-4xl md:text-5xl; }
    h2 { @apply text-3xl md:text-4xl; }
    h3 { @apply text-2xl md:text-3xl; }
    h4 { @apply text-xl md:text-2xl; }
    h5 { @apply text-lg md:text-xl; }
    h6 { @apply text-base md:text-lg; }
}

/* Custom component classes */
@layer components {
    .btn {
        @apply inline-flex items-center justify-center px-4 py-2 border border-transparent 
               text-sm font-medium rounded-md shadow-sm transition-all duration-200 
               focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 
               disabled:cursor-not-allowed;
    }

    .btn-primary {
        @apply btn bg-brand-600 text-white hover:bg-brand-700 focus:ring-brand-500;
    }

    .btn-secondary {
        @apply btn bg-gray-600 text-white hover:bg-gray-700 focus:ring-gray-500;
    }

    .btn-outline {
        @apply btn border-gray-300 text-gray-700 bg-white hover:bg-gray-50 
               focus:ring-brand-500 dark:bg-gray-800 dark:text-gray-300 
               dark:border-gray-600 dark:hover:bg-gray-700;
    }

    .btn-sm {
        @apply px-3 py-1.5 text-xs;
    }

    .btn-lg {
        @apply px-6 py-3 text-base;
    }

    .card {
        @apply bg-white dark:bg-gray-800 rounded-lg shadow-soft 
               border border-gray-200 dark:border-gray-700 
               transition-all duration-300;
    }

    .card-hover {
        @apply hover:shadow-medium hover:-translate-y-1;
    }

    .input {
        @apply block w-full px-3 py-2 border border-gray-300 rounded-md 
               shadow-sm placeholder-gray-400 
               focus:outline-none focus:ring-brand-500 focus:border-brand-500 
               dark:bg-gray-700 dark:border-gray-600 dark:text-white 
               dark:placeholder-gray-400 dark:focus:ring-brand-400 
               dark:focus:border-brand-400;
    }

    .input-error {
        @apply border-red-300 text-red-900 placeholder-red-300 
               focus:outline-none focus:ring-red-500 focus:border-red-500 
               dark:border-red-600 dark:text-red-400 dark:placeholder-red-400;
    }
}

/* Custom utilities */
@layer utilities {
    .text-gradient {
        @apply bg-gradient-to-r from-brand-600 to-purple-600 bg-clip-text text-transparent;
    }

    .bg-gradient-primary {
        @apply bg-gradient-to-r from-brand-500 to-purple-600;
    }

    .bg-gradient-secondary {
        @apply bg-gradient-to-r from-gray-700 to-gray-900;
    }

    .animation-delay-200 {
        animation-delay: 200ms;
    }

    .animation-delay-400 {
        animation-delay: 400ms;
    }

    .scrollbar-hide {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }

    .scrollbar-hide::-webkit-scrollbar {
        display: none;
    }
}
        """, language="css")

        st.markdown("### Complex Components cu Tailwind")

        st.code("""
// Components folosind Tailwind utility classes
import React, { useState } from 'react';

// Button component cu multiple variants
function TailwindButton({ 
    children, 
    variant = 'primary', 
    size = 'md', 
    loading = false, 
    disabled = false,
    fullWidth = false,
    icon,
    ...props 
}) {
    const baseClasses = 'inline-flex items-center justify-center font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed';

    const variantClasses = {
        primary: 'bg-brand-600 text-white hover:bg-brand-700 focus:ring-brand-500 shadow-sm hover:shadow-md',
        secondary: 'bg-gray-600 text-white hover:bg-gray-700 focus:ring-gray-500 shadow-sm hover:shadow-md',
        outline: 'border-2 border-brand-600 text-brand-600 hover:bg-brand-50 focus:ring-brand-500 dark:border-brand-400 dark:text-brand-400 dark:hover:bg-brand-900/10',
        ghost: 'text-gray-700 hover:bg-gray-100 focus:ring-gray-500 dark:text-gray-300 dark:hover:bg-gray-800',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500 shadow-sm hover:shadow-md',
        success: 'bg-green-600 text-white hover:bg-green-700 focus:ring-green-500 shadow-sm hover:shadow-md'
    };

    const sizeClasses = {
        sm: 'px-3 py-1.5 text-xs',
        md: 'px-4 py-2 text-sm',
        lg: 'px-6 py-3 text-base',
        xl: 'px-8 py-4 text-lg'
    };

    const classes = [
        baseClasses,
        variantClasses[variant],
        sizeClasses[size],
        fullWidth && 'w-full',
        loading && 'pointer-events-none'
    ].filter(Boolean).join(' ');

    return (
        <button
            className={classes}
            disabled={disabled || loading}
            {...props}
        >
            {loading ? (
                <>
                    <svg className="animate-spin -ml-1 mr-2 h-4 w-4" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Loading...
                </>
            ) : (
                <>
                    {icon && <span className="mr-2">{icon}</span>}
                    {children}
                </>
            )}
        </button>
    );
}

// Card component cu multiple variants
function TailwindCard({ 
    title, 
    subtitle, 
    children, 
    image, 
    actions, 
    variant = 'default',
    hover = true,
    className = '',
    ...props 
}) {
    const baseClasses = 'bg-white dark:bg-gray-800 rounded-xl shadow-soft border border-gray-200 dark:border-gray-700 overflow-hidden transition-all duration-300';

    const variantClasses = {
        default: '',
        elevated: 'shadow-medium',
        outlined: 'border-2 border-brand-200 dark:border-brand-800 shadow-none',
        ghost: 'bg-transparent shadow-none border-dashed'
    };

    const hoverClasses = hover ? 'hover:shadow-medium hover:-translate-y-1' : '';

    const cardClasses = [
        baseClasses,
        variantClasses[variant],
        hoverClasses,
        className
    ].filter(Boolean).join(' ');

    return (
        <div className={cardClasses} {...props}>
            {image && (
                <div className="aspect-w-16 aspect-h-9">
                    <img 
                        src={image} 
                        alt={title} 
                        className="w-full h-48 object-cover"
                    />
                </div>
            )}

            <div className="p-6">
                {(title || subtitle) && (
                    <div className="mb-4">
                        {title && (
                            <h3 className="text-xl font-semibold text-gray-900 dark:text-gray-100 mb-2">
                                {title}
                            </h3>
                        )}
                        {subtitle && (
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                                {subtitle}
                            </p>
                        )}
                    </div>
                )}

                <div className="text-gray-700 dark:text-gray-300">
                    {children}
                </div>

                {actions && (
                    <div className="mt-6 flex flex-wrap gap-3">
                        {actions}
                    </div>
                )}
            </div>
        </div>
    );
}

// Modal component cu Tailwind
function TailwindModal({ isOpen, onClose, title, children, size = 'md' }) {
    const sizeClasses = {
        sm: 'max-w-md',
        md: 'max-w-lg',
        lg: 'max-w-2xl',
        xl: 'max-w-4xl',
        full: 'max-w-7xl'
    };

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-50 overflow-y-auto">
            {/* Backdrop */}
            <div 
                className="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
                onClick={onClose}
            />

            {/* Modal */}
            <div className="flex min-h-full items-center justify-center p-4">
                <div className={`relative w-full ${sizeClasses[size]} bg-white dark:bg-gray-800 rounded-xl shadow-xl transform transition-all`}>
                    {/* Header */}
                    <div className="flex items-center justify-between p-6 border-b border-gray-200 dark:border-gray-700">
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
                            {title}
                        </h3>
                        <button
                            onClick={onClose}
                            className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors"
                        >
                            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    {/* Content */}
                    <div className="p-6">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    );
}

// Complex Dashboard Layout
function TailwindDashboard() {
    const [darkMode, setDarkMode] = useState(false);
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const [modalOpen, setModalOpen] = useState(false);
    const [loading, setLoading] = useState(false);

    const handleAction = () => {
        setLoading(true);
        setTimeout(() => setLoading(false), 2000);
    };

    return (
        <div className={darkMode ? 'dark' : ''}>
            <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
                {/* Sidebar */}
                <div className={`fixed inset-y-0 left-0 z-50 w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 transform transition-transform lg:translate-x-0 ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}>
                    <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
                        <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100">Dashboard</h2>
                        <button
                            onClick={() => setSidebarOpen(false)}
                            className="lg:hidden text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
                        >
                            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    <nav className="p-4 space-y-2">
                        {['Dashboard', 'Analytics', 'Projects', 'Settings'].map((item, index) => (
                            <a
                                key={item}
                                href="#"
                                className={`flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors ${
                                    index === 0 
                                        ? 'bg-brand-100 text-brand-700 dark:bg-brand-900/50 dark:text-brand-300' 
                                        : 'text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700'
                                }`}
                            >
                                {item}
                            </a>
                        ))}
                    </nav>
                </div>

                {/* Main Content */}
                <div className="lg:pl-64">
                    {/* Top Bar */}
                    <header className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-3">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center space-x-4">
                                <button
                                    onClick={() => setSidebarOpen(true)}
                                    className="lg:hidden text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
                                >
                                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                                    </svg>
                                </button>
                                <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Analytics Overview</h1>
                            </div>

                            <div className="flex items-center space-x-4">
                                {/* Search */}
                                <div className="relative hidden md:block">
                                    <input
                                        type="text"
                                        placeholder="Search..."
                                        className="input w-64"
                                    />
                                    <svg className="absolute right-3 top-2.5 w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                    </svg>
                                </div>

                                {/* Dark mode toggle */}
                                <button
                                    onClick={() => setDarkMode(!darkMode)}
                                    className="p-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                                >
                                    {darkMode ? '🌞' : '🌙'}
                                </button>

                                {/* Profile */}
                                <div className="w-8 h-8 bg-brand-500 rounded-full flex items-center justify-center text-white font-medium">
                                    JD
                                </div>
                            </div>
                        </div>
                    </header>

                    {/* Page Content */}
                    <main className="p-6">
                        {/* Stats Grid */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                            {[
                                { label: 'Total Users', value: '12,345', change: '+12%', color: 'text-green-600' },
                                { label: 'Revenue', value: '$45,678', change: '+8%', color: 'text-green-600' },
                                { label: 'Orders', value: '1,234', change: '-3%', color: 'text-red-600' },
                                { label: 'Conversion', value: '3.24%', change: '+5%', color: 'text-green-600' }
                            ].map((stat, index) => (
                                <div key={index} className="card p-6">
                                    <div className="flex items-center justify-between">
                                        <div>
                                            <p className="text-sm font-medium text-gray-600 dark:text-gray-400">
                                                {stat.label}
                                            </p>
                                            <p className="text-2xl font-bold text-gray-900 dark:text-gray-100">
                                                {stat.value}
                                            </p>
                                        </div>
                                        <div className={`text-sm font-medium ${stat.color}`}>
                                            {stat.change}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* Content Grid */}
                        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                            {/* Cards Example */}
                            <div className="lg:col-span-2 space-y-6">
                                <TailwindCard
                                    title="Project Analytics"
                                    subtitle="Real-time insights"
                                    image="https://picsum.photos/400/200?random=1"
                                    variant="elevated"
                                    actions={[
                                        <TailwindButton key="1" variant="outline" size="sm">
                                            View Details
                                        </TailwindButton>,
                                        <TailwindButton key="2" variant="primary" size="sm" loading={loading} onClick={handleAction}>
                                            Generate Report
                                        </TailwindButton>
                                    ]}
                                >
                                    <p className="mb-4">
                                        Monitor your project performance with real-time analytics 
                                        and insights. Track user engagement, conversion rates, 
                                        and revenue metrics.
                                    </p>
                                    <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                                        <h4 className="font-medium text-gray-900 dark:text-gray-100 mb-2">
                                            Key Metrics
                                        </h4>
                                        <ul className="space-y-1 text-sm text-gray-600 dark:text-gray-400">
                                            <li>• Active Users: 2,345</li>
                                            <li>• Page Views: 45,678</li>
                                            <li>• Bounce Rate: 23%</li>
                                        </ul>
                                    </div>
                                </TailwindCard>

                                <TailwindCard
                                    title="Recent Activity"
                                    variant="outlined"
                                    hover={false}
                                >
                                    <div className="space-y-4">
                                        {[
                                            { user: 'John Doe', action: 'created a new project', time: '2 hours ago' },
                                            { user: 'Jane Smith', action: 'updated dashboard settings', time: '4 hours ago' },
                                            { user: 'Mike Johnson', action: 'completed task review', time: '6 hours ago' }
                                        ].map((activity, index) => (
                                            <div key={index} className="flex items-start space-x-3 p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                                                <div className="w-8 h-8 bg-brand-100 dark:bg-brand-900 text-brand-600 dark:text-brand-400 rounded-full flex items-center justify-center text-sm font-medium">
                                                    {activity.user.split(' ').map(n => n[0]).join('')}
                                                </div>
                                                <div className="flex-1 min-w-0">
                                                    <p className="text-sm text-gray-900 dark:text-gray-100">
                                                        <span className="font-medium">{activity.user}</span> {activity.action}
                                                    </p>
                                                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                                                        {activity.time}
                                                    </p>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </TailwindCard>
                            </div>

                            {/* Sidebar Cards */}
                            <div className="space-y-6">
                                <TailwindCard
                                    title="Quick Actions"
                                    variant="ghost"
                                >
                                    <div className="space-y-3">
                                        <TailwindButton 
                                            variant="primary" 
                                            fullWidth 
                                            icon="+"
                                            onClick={() => setModalOpen(true)}
                                        >
                                            Create Project
                                        </TailwindButton>
                                        <TailwindButton variant="outline" fullWidth icon="📊">
                                            View Reports
                                        </TailwindButton>
                                        <TailwindButton variant="ghost" fullWidth icon="⚙️">
                                            Settings
                                        </TailwindButton>
                                    </div>
                                </TailwindCard>

                                <TailwindCard title="Team Members">
                                    <div className="space-y-3">
                                        {['Alice Cooper', 'Bob Wilson', 'Carol Davis'].map((member, index) => (
                                            <div key={index} className="flex items-center space-x-3">
                                                <div className="w-8 h-8 bg-gradient-to-r from-brand-400 to-purple-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                                                    {member.split(' ').map(n => n[0]).join('')}
                                                </div>
                                                <div className="flex-1">
                                                    <p className="text-sm font-medium text-gray-900 dark:text-gray-100">
                                                        {member}
                                                    </p>
                                                    <p className="text-xs text-gray-500 dark:text-gray-400">
                                                        Online
                                                    </p>
                                                </div>
                                                <div className="w-2 h-2 bg-green-400 rounded-full"></div>
                                            </div>
                                        ))}
                                    </div>
                                </TailwindCard>
                            </div>
                        </div>
                    </main>
                </div>

                {/* Modal Example */}
                <TailwindModal
                    isOpen={modalOpen}
                    onClose={() => setModalOpen(false)}
                    title="Create New Project"
                    size="lg"
                >
                    <form className="space-y-6">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                Project Name
                            </label>
                            <input
                                type="text"
                                className="input"
                                placeholder="Enter project name..."
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                Description
                            </label>
                            <textarea
                                rows={4}
                                className="input resize-none"
                                placeholder="Project description..."
                            />
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Category
                                </label>
                                <select className="input">
                                    <option>Web Development</option>
                                    <option>Mobile App</option>
                                    <option>Design</option>
                                    <option>Marketing</option>
                                </select>
                            </div>

                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Priority
                                </label>
                                <select className="input">
                                    <option>High</option>
                                    <option>Medium</option>
                                    <option>Low</option>
                                </select>
                            </div>
                        </div>

                        <div className="flex justify-end space-x-3 pt-4">
                            <TailwindButton 
                                variant="outline" 
                                onClick={() => setModalOpen(false)}
                            >
                                Cancel
                            </TailwindButton>
                            <TailwindButton variant="primary">
                                Create Project
                            </TailwindButton>
                        </div>
                    </form>
                </TailwindModal>
            </div>
        </div>
    );
}

export default TailwindDashboard;
        """, language="javascript")

        st.markdown("### Advanced Tailwind Patterns")

        st.code("""
// Advanced Tailwind patterns și techniques

// 1. Responsive Design cu Tailwind
function ResponsiveGrid() {
    return (
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            {/* Grid care se adaptează la toate screen sizes */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6 lg:gap-8">
                {Array.from({ length: 8 }).map((_, index) => (
                    <div 
                        key={index}
                        className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-4 sm:p-6 
                                   hover:shadow-lg transition-shadow duration-300
                                   transform hover:-translate-y-1"
                    >
                        <div className="aspect-w-16 aspect-h-9 mb-4">
                            <img 
                                src={`https://picsum.photos/300/200?random=${index}`}
                                alt={`Image ${index}`}
                                className="w-full h-32 sm:h-40 object-cover rounded"
                            />
                        </div>
                        <h3 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-gray-100 mb-2">
                            Card Title {index + 1}
                        </h3>
                        <p className="text-sm sm:text-base text-gray-600 dark:text-gray-300 mb-4">
                            This is a responsive card that adapts to different screen sizes.
                        </p>
                        <button className="w-full sm:w-auto btn-primary">
                            Learn More
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

// 2. Dark Mode Implementation
function DarkModeToggle() {
    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {
        // Load saved preference
        const saved = localStorage.getItem('darkMode');
        if (saved) {
            setDarkMode(JSON.parse(saved));
        }
    }, []);

    useEffect(() => {
        // Apply dark mode class to html element
        if (darkMode) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }

        // Save preference
        localStorage.setItem('darkMode', JSON.stringify(darkMode));
    }, [darkMode]);

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
            <div className="container mx-auto px-4 py-8">
                {/* Header cu dark mode toggle */}
                <header className="flex justify-between items-center mb-8">
                    <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100">
                        Dark Mode Example
                    </h1>

                    <button
                        onClick={() => setDarkMode(!darkMode)}
                        className="relative inline-flex h-6 w-11 items-center rounded-full 
                                   bg-gray-200 dark:bg-gray-700 transition-colors duration-300
                                   focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2"
                    >
                        <span
                            className={`inline-block h-4 w-4 transform rounded-full bg-white 
                                       transition-transform duration-300 ${
                                           darkMode ? 'translate-x-6' : 'translate-x-1'
                                       }`}
                        />
                        <span className="sr-only">Toggle dark mode</span>
                    </button>
                </header>

                {/* Content care se adaptează la dark mode */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 
                                    border border-gray-200 dark:border-gray-700">
                        <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100 mb-4">
                            Card Title
                        </h2>
                        <p className="text-gray-600 dark:text-gray-300 mb-4">
                            This card automatically adapts its colors based on the current theme.
                        </p>
                        <div className="flex space-x-2">
                            <button className="btn-primary">Primary</button>
                            <button className="btn-outline">Secondary</button>
                        </div>
                    </div>

                    <div className="bg-gradient-to-br from-brand-500 to-purple-600 rounded-lg p-6 text-white">
                        <h2 className="text-xl font-semibold mb-4">Gradient Card</h2>
                        <p className="mb-4 opacity-90">
                            Gradient backgrounds work well in both light and dark modes.
                        </p>
                        <button className="bg-white/20 hover:bg-white/30 text-white px-4 py-2 rounded-lg transition-colors">
                            Gradient Button
                        </button>
                    </div>

                    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
                        <div className="flex items-center mb-4">
                            <div className="w-12 h-12 bg-brand-100 dark:bg-brand-900 rounded-full flex items-center justify-center">
                                <svg className="w-6 h-6 text-brand-600 dark:text-brand-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
                                </svg>
                            </div>
                            <div className="ml-4">
                                <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100">
                                    Icon Card
                                </h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400">
                                    With adaptive colors
                                </p>
                            </div>
                        </div>
                        <p className="text-gray-600 dark:text-gray-300">
                            Icons and backgrounds adapt automatically to the current theme.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}

// 3. Animation și Motion cu Tailwind
function AnimatedComponents() {
    const [isVisible, setIsVisible] = useState(false);
    const [currentTab, setCurrentTab] = useState(0);

    const tabs = ['Dashboard', 'Analytics', 'Reports', 'Settings'];

    return (
        <div className="container mx-auto px-4 py-8 space-y-8">
            {/* Animated Cards */}
            <section>
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">
                    Animated Cards
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    {[0, 1, 2].map((index) => (
                        <div
                            key={index}
                            className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 
                                       transform transition-all duration-500 hover:scale-105 
                                       hover:shadow-xl animate-fade-in"
                            style={{ animationDelay: `${index * 200}ms` }}
                        >
                            <div className="w-12 h-12 bg-gradient-to-r from-brand-400 to-purple-500 
                                           rounded-lg flex items-center justify-center mb-4
                                           animate-bounce-gentle">
                                <span className="text-white font-bold text-xl">{index + 1}</span>
                            </div>
                            <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
                                Feature {index + 1}
                            </h3>
                            <p className="text-gray-600 dark:text-gray-300">
                                This card has smooth hover animations and staggered entrance effects.
                            </p>
                        </div>
                    ))}
                </div>
            </section>

            {/* Animated Tabs */}
            <section>
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">
                    Animated Tabs
                </h2>

                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
                    <div className="flex border-b border-gray-200 dark:border-gray-700 relative">
                        {tabs.map((tab, index) => (
                            <button
                                key={tab}
                                onClick={() => setCurrentTab(index)}
                                className={`flex-1 px-6 py-3 text-sm font-medium transition-colors relative
                                           ${currentTab === index 
                                               ? 'text-brand-600 dark:text-brand-400' 
                                               : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
                                           }`}
                            >
                                {tab}
                            </button>
                        ))}

                        {/* Animated indicator */}
                        <div
                            className="absolute bottom-0 h-0.5 bg-brand-600 dark:bg-brand-400 transition-all duration-300"
                            style={{
                                left: `${currentTab * (100 / tabs.length)}%`,
                                width: `${100 / tabs.length}%`
                            }}
                        />
                    </div>

                    <div className="p-6">
                        <div className="animate-slide-up">
                            <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">
                                {tabs[currentTab]} Content
                            </h3>
                            <p className="text-gray-600 dark:text-gray-300 mb-4">
                                This is the content for the {tabs[currentTab].toLowerCase()} tab. 
                                The content slides in smoothly when switching tabs.
                            </p>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                                    <h4 className="font-medium text-gray-900 dark:text-gray-100 mb-2">
                                        Metric 1
                                    </h4>
                                    <p className="text-2xl font-bold text-brand-600 dark:text-brand-400">
                                        {Math.floor(Math.random() * 1000)}
                                    </p>
                                </div>
                                <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                                    <h4 className="font-medium text-gray-900 dark:text-gray-100 mb-2">
                                        Metric 2
                                    </h4>
                                    <p className="text-2xl font-bold text-green-600 dark:text-green-400">
                                        {Math.floor(Math.random() * 100)}%
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Loading States */}
            <section>
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">
                    Loading States
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* Skeleton Loader */}
                    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">
                            Skeleton Loader
                        </h3>
                        <div className="animate-pulse space-y-4">
                            <div className="flex space-x-4">
                                <div className="rounded-full bg-gray-200 dark:bg-gray-700 h-12 w-12"></div>
                                <div className="flex-1 space-y-2 py-1">
                                    <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-3/4"></div>
                                    <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-1/2"></div>
                                </div>
                            </div>
                            <div className="space-y-3">
                                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded"></div>
                                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-5/6"></div>
                                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-4/6"></div>
                            </div>
                        </div>
                    </div>

                    {/* Spinner */}
                    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 flex flex-col items-center justify-center">
                        <div className="animate-spin rounded-full h-12 w-12 border-4 border-gray-200 border-t-brand-600 mb-4"></div>
                        <p className="text-gray-600 dark:text-gray-300">Loading content...</p>
                    </div>
                </div>
            </section>

            {/* Hover Effects */}
            <section>
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">
                    Interactive Elements
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    {['Hover me', 'Click me', 'Focus me', 'Active state'].map((text, index) => (
                        <button
                            key={index}
                            className="group relative overflow-hidden bg-gradient-to-r from-brand-500 to-purple-600 
                                       text-white px-6 py-3 rounded-lg font-medium
                                       transform transition-all duration-300
                                       hover:scale-105 hover:shadow-lg
                                       focus:outline-none focus:ring-4 focus:ring-brand-300
                                       active:scale-95"
                        >
                            <span className="relative z-10">{text}</span>
                            <div className="absolute inset-0 bg-white opacity-0 group-hover:opacity-20 transition-opacity duration-300"></div>
                            <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-brand-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        </button>
                    ))}
                </div>
            </section>
        </div>
    );
}

// 4. Form Components cu Tailwind
function TailwindForms() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: '',
        category: '',
        notifications: false,
        newsletter: true
    });

    const [errors, setErrors] = useState({});

    const handleChange = (field, value) => {
        setFormData(prev => ({ ...prev, [field]: value }));
        // Clear error când user începe să tasteze
        if (errors[field]) {
            setErrors(prev => ({ ...prev, [field]: null }));
        }
    };

    const validateForm = () => {
        const newErrors = {};

        if (!formData.name.trim()) {
            newErrors.name = 'Name is required';
        }

        if (!formData.email.trim()) {
            newErrors.email = 'Email is required';
        } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
            newErrors.email = 'Email is invalid';
        }

        if (!formData.message.trim()) {
            newErrors.message = 'Message is required';
        } else if (formData.message.length < 10) {
            newErrors.message = 'Message must be at least 10 characters';
        }

        if (!formData.category) {
            newErrors.category = 'Please select a category';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            console.log('Form submitted:', formData);
            // Reset form
            setFormData({
                name: '', email: '', message: '', category: '',
                notifications: false, newsletter: true
            });
        }
    };

    return (
        <div className="max-w-2xl mx-auto bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">
                Contact Form
            </h2>

            <form onSubmit={handleSubmit} className="space-y-6">
                {/* Name Field */}
                <div>
                    <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                        Full Name
                    </label>
                    <input
                        type="text"
                        id="name"
                        value={formData.name}
                        onChange={(e) => handleChange('name', e.target.value)}
                        className={`input ${errors.name ? 'input-error' : ''}`}
                        placeholder="Enter your full name"
                    />
                    {errors.name && (
                        <p className="mt-1 text-sm text-red-600 dark:text-red-400">
                            {errors.name}
                        </p>
                    )}
                </div>

                {/* Email Field */}
                <div>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                        Email Address
                    </label>
                    <input
                        type="email"
                        id="email"
                        value={formData.email}
                        onChange={(e) => handleChange('email', e.target.value)}
                        className={`input ${errors.email ? 'input-error' : ''}`}
                        placeholder="Enter your email address"
                    />
                    {errors.email && (
                        <p className="mt-1 text-sm text-red-600 dark:text-red-400">
                            {errors.email}
                        </p>
                    )}
                </div>

                {/* Category Select */}
                <div>
                    <label htmlFor="category" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                        Category
                    </label>
                    <select
                        id="category"
                        value={formData.category}
                        onChange={(e) => handleChange('category', e.target.value)}
                        className={`input ${errors.category ? 'input-error' : ''}`}
                    >
                        <option value="">Select a category</option>
                        <option value="general">General Inquiry</option>
                        <option value="support">Technical Support</option>
                        <option value="billing">Billing Question</option>
                        <option value="feedback">Feedback</option>
                    </select>
                    {errors.category && (
                        <p className="mt-1 text-sm text-red-600 dark:text-red-400">
                            {errors.category}
                        </p>
                    )}
                </div>

                {/* Message Textarea */}
                <div>
                    <label htmlFor="message" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                        Message
                    </label>
                    <textarea
                        id="message"
                        rows={4}
                        value={formData.message}
                        onChange={(e) => handleChange('message', e.target.value)}
                        className={`input resize-none ${errors.message ? 'input-error' : ''}`}
                        placeholder="Enter your message..."
                    />
                    {errors.message && (
                        <p className="mt-1 text-sm text-red-600 dark:text-red-400">
                            {errors.message}
                        </p>
                    )}
                    <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                        {formData.message.length}/500 characters
                    </p>
                </div>

                {/* Checkboxes */}
                <div className="space-y-4">
                    <div className="flex items-start">
                        <input
                            id="notifications"
                            type="checkbox"
                            checked={formData.notifications}
                            onChange={(e) => handleChange('notifications', e.target.checked)}
                            className="mt-1 h-4 w-4 text-brand-600 border-gray-300 rounded focus:ring-brand-500"
                        />
                        <label htmlFor="notifications" className="ml-3 text-sm text-gray-700 dark:text-gray-300">
                            Send me notifications about updates and important announcements
                        </label>
                    </div>

                    <div className="flex items-start">
                        <input
                            id="newsletter"
                            type="checkbox"
                            checked={formData.newsletter}
                            onChange={(e) => handleChange('newsletter', e.target.checked)}
                            className="mt-1 h-4 w-4 text-brand-600 border-gray-300 rounded focus:ring-brand-500"
                        />
                        <label htmlFor="newsletter" className="ml-3 text-sm text-gray-700 dark:text-gray-300">
                            Subscribe to our newsletter for tips, tutorials, and product updates
                        </label>
                    </div>
                </div>

                {/* Submit Button */}
                <div className="flex justify-end space-x-4">
                    <button
                        type="button"
                        className="btn-outline"
                        onClick={() => setFormData({
                            name: '', email: '', message: '', category: '',
                            notifications: false, newsletter: true
                        })}
                    >
                        Reset
                    </button>
                    <button
                        type="submit"
                        className="btn-primary"
                    >
                        Send Message
                    </button>
                </div>
            </form>
        </div>
    );
}
        """, language="javascript")

        st.markdown("### Comparația Metodelor de Styling")

        comparison_data = {
            "Aspect": [
                "Curba de învățare",
                "Performanță",
                "Bundle size",
                "Customizare",
                "Maintainabilitate",
                "Scoping",
                "Dynamic styling",
                "Responsive design",
                "Dark mode",
                "Team collaboration",
                "Debugging",
                "Production ready"
            ],
            "CSS Clasic": [
                "🟢 Ușor", "🟢 Excelent", "🟢 Mic", "🟡 Mediu",
                "🔴 Dificil", "🔴 Global", "🔴 Limitat", "🟢 Excelent",
                "🟡 Manual", "🟡 Mediu", "🟡 CSS DevTools", "🟢 Da"
            ],
            "CSS Modules": [
                "🟡 Mediu", "🟢 Excelent", "🟡 Mic", "🟢 Bun",
                "🟢 Bun", "🟢 Scoped", "🔴 Limitat", "🟢 Excelent",
                "🟡 Manual", "🟢 Bun", "🟢 Ușor", "🟢 Da"
            ],
            "Styled Components": [
                "🟡 Mediu", "🟡 Bun", "🔴 Mare", "🟢 Excelent",
                "🟢 Bun", "🟢 Scoped", "🟢 Excelent", "🟢 Excelent",
                "🟢 Ușor", "🟢 Bun", "🟢 React DevTools", "🟢 Da"
            ],
            "Tailwind CSS": [
                "🔴 Dificil", "🟢 Excelent", "🟡 Optimizat", "🟢 Excelent",
                "🟢 Bun", "🟢 Utility", "🟡 Limitat", "🟢 Excelent",
                "🟢 Built-in", "🟢 Excelent", "🟢 Browser DevTools", "🟢 Da"
            ]
        }

        st.table(comparison_data)

        st.markdown("### Recomandări pentru Alegerea Metodei")

        st.markdown("""
        **CSS Clasic - Când să folosești:**
        - Proiecte mici și simple
        - Echipe cu experiență CSS mare
        - Când ai nevoie de control total asupra CSS-ului
        - Aplicații cu cerințe specifice de styling

        **CSS Modules - Când să folosești:**
        - Proiecte medii și mari
        - Când vrei scoping automat fără overhead-ul CSS-in-JS
        - Echipe care preferă CSS tradițional dar vor modularitate
        - Când performanța este critică

        **Styled Components - Când să folosești:**
        - Aplicații React cu styling dinamic complex
        - Când vrei theming avansat
        - Echipe care preferă JavaScript pentru styling
        - Aplicații cu multe componente reutilizabile

        **Tailwind CSS - Când să folosești:**
        - Prototipare rapidă
        - Echipe care vor consistență în design
        - Proiecte cu design system bine definit
        - Când vrei productivitate maximă în dezvoltare

        ### Best Practices Generale

        **Performance:**
        - Minimizează CSS-ul nefolosit
        - Folosește CSS-in-JS doar când e necesar
        - Optimizează pentru Critical CSS
        - Compresia și caching pentru assets

        **Maintainabilitate:**
        - Organizează CSS-ul în module logice
        - Folosește naming conventions consistente
        - Documentează componentele complexe
        - Evită nested selectors prea adânci

        **Accessibility:**
        - Asigură-te că focus states sunt vizibile
        - Folosește culori cu contrast suficient
        - Testează cu screen readers
        - Respectă WCAG guidelines

        **Responsive Design:**
        - Mobile-first approach
        - Testează pe device-uri reale
        - Optimizează pentru touch interfaces
        - Consideră performance pe conexiuni lente
        """)

    st.markdown("""
    <div class="summary-box">
    <h3>Rezumat Styling în React</h3>
    <p>Ai învățat toate metodele principale de stilizare în React: de la CSS clasic la soluții moderne 
    ca Styled Components și Tailwind CSS. Fiecare metodă are avantajele și cazurile sale de utilizare. 
    Alegerea depinde de complexitatea proiectului, preferințele echipei și cerințele de performance. 
    Pentru majoritatea proiectelor moderne, o combinație între CSS Modules pentru componente de bază 
    și Tailwind pentru rapid prototyping oferă cel mai bun echilibru între productivitate și maintainabilitate.</p>
    </div>
    """, unsafe_allow_html=True)


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
        "components_basic": components_basic_page,
        "state_props": state_props_page,
        "events": events_page,
        "hooks": hooks_page,
        "blog_app": blog_app_page,
        "styling": styling_page,
        "deploy": deploy_page,

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
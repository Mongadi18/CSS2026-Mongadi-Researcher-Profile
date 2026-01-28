import streamlit as st 
import pandas as pd

# Page config
st.set_page_config(page_title="Itumeleng Lucky Mongadi - CV", page_icon="🧪", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

    .main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;}
    h1, h2, h3 {font-family: 'Montserrat', sans-serif; color: #ffd700 !important;}
    p, li {font-size: 1.05rem; line-height: 1.6;}
    .stButton>button {background: #ffd700; color: #764ba2; font-weight: 600;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🧭 Navigation")
    page = st.radio("", ["Home", "Education", "Experience", "Research", "Skills", "Contact"])
    st.info("**Location:** Pretoria, SA\n\n**Field:** Chemistry & Chemical Technology")

# HOME PAGE
if page == "Home":
    st.title("ITUMELENG LUCKY MONGADI")
    st.subheader("Chemist | Researcher | Educator | AI Specialist")

    col1, col2, col3 = st.columns(3)
    col1.metric("Degrees", "3", "BSc, Honours, MSc")
    col2.metric("Teaching", "2.5+ Years", "Laboratory & Lectures")
    col3.metric("Funding", "R315k", "NRF Research Grant")

    st.markdown("---")
    st.subheader("About Me")
    st.write("""
    Passionate researcher specializing in **Analytical Chemistry** and **Computational Toxicology**.
    Expertise in environmental contaminant analysis, machine learning applications in chemistry,
    and scientific education. Currently focused on plasticizer contamination assessment in drinking
    water using GC-MS and AI-driven toxicity prediction.
    """)

    st.subheader("Career Highlights")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**🔬 Research**")
        st.write("- NRF-funded plasticizer research")
        st.write("- Published peer-reviewed articles")
        st.write("- GC-MS & ML toxicity modeling")
    with col2:
        st.write("**👨‍🏫 Teaching**")
        st.write("- Assistant Lecturer (2025)")
        st.write("- Lab Demonstrator & Tutor")
        st.write("- Supervised 2 Honours students")

# EDUCATION PAGE
elif page == "Education":
    st.title("🎓 Education")

    st.subheader("MSc Chemistry and Chemical Technology (2025)")
    st.write("**Sefako Makgatho Health Sciences University** | Completed, awaiting results")
    with st.expander("View Research Details"):
        st.write("**Project:** Plasticizer contamination in tap water (Limpopo & Northern Cape)")
        st.write("**Funding:** NRF - R105k/year for 3 years")
        st.write("**Methods:** SALLE-GC/MS, Machine Learning (Random Forest, XGBoost, CatBoost)")
        st.write("**Focus:** Health risk assessment, toxicity prediction (pIC50)")

    st.markdown("---")
    st.subheader("BSc Honours Chemistry (2022)")
    st.write("**Sefako Makgatho Health Sciences University** | 1 Distinction")

    st.markdown("---")
    st.subheader("BSc Chemistry (2021)")
    st.write("**Sefako Makgatho Health Sciences University** | 1 Distinction")

    st.markdown("---")
    st.subheader("Professional Development")
    events = ["Tuks Young Research Leadership Program (2025)", "SMU Research Day (2025)",
              "MIND Seminar: Human & AI", "Webinar: Biomarkers in Neurological Disorders"]
    for event in events:
        st.write(f"✓ {event}")

# EXPERIENCE PAGE
elif page == "Experience":
    st.title("💼 Professional Experience")

    st.subheader("Assistant Lecturer (Jul 2025 - Nov 2025)")
    st.write("**Sefako Makgatho Health Sciences University**")
    st.write("- Lectured General Chemistry to health science students")
    st.write("- Developed tutorials and assessments")
    st.write("- Taught: Medicine, Physiotherapy, Dental, Nursing programs")

    st.markdown("---")
    st.subheader("Laboratory Demonstrator & Tutor (Feb 2023 - Jul 2025)")
    st.write("**Sefako Makgatho Health Sciences University**")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Lab Demonstrator:**")
        st.write("- Conducted lab sessions (1st-3rd year)")
        st.write("- Demonstrated GC-MS & analytical techniques")
        st.write("- Supervised experiments & safety")
    with col2:
        st.write("**Tutor:**")
        st.write("- General Chemistry")
        st.write("- Organic Chemistry")
        st.write("- Analytical Chemistry")
        st.write("- Inorganic Chemistry")

    st.markdown("---")
    st.subheader("Student Supervision")
    df = pd.DataFrame({
        "Student": ["Mr. Bongumusa Nkamana", "Ms. Reitumetse Pearl Matseke"],
        "Degree": ["Honours", "Honours"],
        "Role": ["Co-supervisor", "Primary Supervisor"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# RESEARCH PAGE
elif page == "Research":
    st.title("🔬 Research Profile")

    st.subheader("Current Project: Plasticizer Contamination in Tap Water")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("**Focus:** Environmental Analytical Chemistry & Computational Toxicology")
        st.write("**Regions:** Limpopo & Northern Cape provinces")
        st.write("**Funding:** NRF - R315k total (R105k/year × 3 years)")
    with col2:
        st.metric("Total Funding", "R315k")
        st.metric("Duration", "3 Years")

    st.markdown("---")
    st.subheader("Research Methodology")

    tab1, tab2, tab3 = st.tabs(["Analytical", "Computational", "Risk Assessment"])

    with tab1:
        st.write("**SALLE-GC/MS Method**")
        st.write("- Salting-out Assisted Liquid-Liquid Extraction")
        st.write("- Gas Chromatography-Mass Spectrometry")
        st.write("- Quantified phthalates & bisphenols")
        st.write("- Method validation (MDL/MQL, recovery, precision)")

    with tab2:
        st.write("**Machine Learning Models**")
        st.write("- Random Forest, CatBoost, XGBoost, LightGBM, KNN")
        st.write("- Predicted pIC50 for CYP19A1 aromatase")
        st.write("- QSAR modeling with RDKit & Mordred")

    with tab3:
        st.write("**Health Risk Assessment**")
        st.write("- EDI (Estimated Daily Intake)")
        st.write("- CDI (Chronic Daily Intake)")
        st.write("- HQ (Hazard Quotient)")
        st.write("- Adult & child exposure pathways")

    st.markdown("---")
    st.subheader("Publications")
    st.write("""
    **MAHLANGU, W.B., MASEKO, B.R., MONGADI, I.L., et al. (2023)**
    "Quantitative analysis and health risk assessment of bisphenols in selected canned foods"
    *Food Packaging and Shelf Life*, 37, 101078
    """)

# SKILLS PAGE
elif page == "Skills":
    st.title("💻 Technical Skills")

    st.subheader("🐍 Python Programming")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Scientific Computing**")
        st.write("- NumPy, SciPy, Pandas")
        st.write("- Matplotlib, Seaborn")
        st.write("- statsmodels")
    with col2:
        st.write("**Machine Learning**")
        st.write("- scikit-learn")
        st.write("- XGBoost, LightGBM")
        st.write("- CatBoost")
    with col3:
        st.write("**Cheminformatics**")
        st.write("- RDKit, Mordred")
        st.write("- DeepChem")
        st.write("- PubChemPy")

    st.markdown("---")
    st.subheader("🔬 Analytical Chemistry")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- Gas Chromatography-Mass Spectrometry (GC-MS)")
        st.write("- SALLE extraction method")
        st.write("- Method development & validation")
    with col2:
        st.write("- Environmental contamination analysis")
        st.write("- Water quality monitoring")
        st.write("- Sample preparation & optimization")

    st.markdown("---")
    st.subheader("🤖 AI & Prompt Engineering")
    st.write("- Design domain-specific prompts for chemistry")
    st.write("- Evaluate AI model accuracy & scientific depth")
    st.write("- Review and correct model outputs")
    st.write("- Establish scoring standards for responses")

    st.markdown("---")
    st.subheader("Skill Proficiency")
    df = pd.DataFrame({
        "Skill": ["Python", "Machine Learning", "GC-MS", "Data Analysis", "Teaching"],
        "Proficiency": ["90%", "85%", "95%", "92%", "90%"],
        "Experience": ["3 years", "2.5 years", "3 years", "3 years", "2.5 years"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# CONTACT PAGE
elif page == "Contact":
    st.title("📧 Contact Information")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Personal Details")
        st.write("**Name:** Itumeleng Lucky Mongadi")
        st.write("**Email:** luckyitumeleng234@gmail.com")
        st.write("**Phone:** 072 920 5189")
        st.write("**Location:** Pretoria, Gauteng, South Africa")
        st.write("**Date of Birth:** 12 January 1998")

    with col2:
        st.subheader("Professional")
        st.write("**Department:** Chemistry and Chemical Technology")
        st.write("**Institution:** Sefako Makgatho Health Sciences University")
        st.write("**Position:** Researcher & Former Assistant Lecturer")

    st.markdown("---")
    st.subheader("References")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Dr. JN Oyourou**")
        st.write("Faculty of Applied Sciences, Eduvos")
        st.write("📞 +27 73 974 3747")
        st.write("✉️ Jean.Oyourou@eduvos.com")

    with col2:
        st.write("**Mr. WB Mahlangu**")
        st.write("Faculty of Applied Sciences, Eduvos")
        st.write("📞 +27 68 457 5957")
        st.write("✉️ bonkemahlangu@gmail.com")

    with col3:
        st.write("**Dr. D Molefe**")
        st.write("Dept. of Chemistry, SMU")
        st.write("📞 +27 82 202 2095")
        st.write("✉️ dan.molefe@smu.ac.za")

# Footer
st.markdown("---")
st.markdown("*© 2026 Itumeleng Lucky Mongadi | Built with Streamlit*")

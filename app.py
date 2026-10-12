"""Academic CV and digital profile for doctoral applications."""

from pathlib import Path

import streamlit as st

NAME = "Jayanath Jayarathna"
FULL_NAME = "Jayanath Jayarathna"
TITLE = "Doctoral Applicant | Artificial Intelligence"
TAGLINE = "AI research interests · Data science · Intelligent automation · Software systems"
EMAIL = "jayanathsha@gmail.com"
PHONE = ""
LOCATION = ""
GITHUB = ""
LINKEDIN = ""
CONTACT_INFO = " · ".join(value for value in (EMAIL, PHONE, LOCATION) if value)

PROFILE = (
    "Railway operations professional with 22 years of experience in Sri Lanka Railways, "
    "supported by postgraduate education in data science and practical experience in "
    "software development, machine learning, AI automation, and business information systems. "
    "Experienced in developing interactive web applications, ERP and business management "
    "systems, employee and accounting management solutions, and AI-powered workflows using "
    "React.js, Next.js, Node.js, n8n, local large language models, and retrieval-augmented "
    "generation (RAG). Interested in researching how artificial intelligence can improve "
    "operational decision-making, workflow automation, information retrieval, and complex "
    "transportation systems."
)

RESEARCH_TITLE = "Artificial Intelligence-Based Decision Support for Railway Operations and Service Reliability"
RESEARCH_SUMMARY = (
    "Preliminary direction: investigate whether predictive models and operational data can "
    "support disruption analysis, service reliability, and operational decision-making. "
    "The research questions, data access, methodology, and evaluation plan require a literature "
    "review and discussion with a prospective supervisor. This is a proposed topic, not completed research."
)

EDUCATION = [
    {
        "qualification": "MBA in Data Science (certificate wording to verify)",
        "institution": "Business and Hospitality School, Switzerland",
        "dates": "2023–2024",
    },
    {
        "qualification": "Bachelor of Computer Science (certificate wording to verify)",
        "institution": "University of Kelaniya, Sri Lanka",
        "dates": "2002–2006",
    },
    {
        "qualification": "Advanced National Diploma in Business Management",
        "institution": "Management Qualifications, UK",
        "dates": "2015–2016",
    },
]

SKILLS = {
    "AI and data science": ["Python", "Pandas", "NumPy", "scikit-learn", "Machine learning", "NLP", "Model evaluation"],
    "AI agents and automation": ["n8n", "Ollama", "LLM applications", "RAG", "Agent workflows", "Retrieval pipelines"],
    "Software development": ["React.js", "Next.js", "Node.js", "APIs", "Interactive web applications"],
    "Databases": ["Supabase / PostgreSQL", "MongoDB", "MySQL"],
    "Deployment": ["Hostinger VPS", "CloudPanel", "Application deployment and maintenance"],
}

EXPERIENCE = [
    {
        "role": "Railway Guard (official English designation to confirm)",
        "organisation": "Sri Lanka Railways",
        "period": "22 years of service; dates to confirm",
        "details": [
            "Professional experience in railway operations, with practical exposure to operational decision-making and safety-sensitive work.",
            "Coordinates operational work and communication in a complex transportation environment.",
            "Brings frontline railway context to potential research in service reliability and AI decision support.",
        ],
    },
    {
        "role": "Software and AI projects",
        "organisation": "Independent project work",
        "period": "Dates and professional status to confirm",
        "details": [
            "Developed web applications and business information systems, including ERP, accounting, and employee-management solutions.",
            "Worked with modern web technologies and databases, and explored AI-enabled workflows using n8n, local language models, and RAG.",
        ],
    },
]

PROJECTS = [
    ("Breast cancer prediction", "Built a Streamlit classification application with logistic regression and scikit-learn using a Kaggle dataset. Add the dataset citation, validation design, evaluation metrics, and limitations; accuracy is omitted pending verification."),
    ("Customer feedback analysis", "Applied NLTK and TextBlob sentiment analysis with trend visualisation. Add the data source, preprocessing, evaluation method, and limitations; no business impact is claimed."),
    ("Customer churn prediction", "Completed a churn-prediction exercise through the BCG Data Science Job Simulation on Forage. Confirm the exact programme title and describe the workflow and evaluation without an unverified score."),
    ("Business and management systems", "ERP, accounting, employee-management, and business applications; add individual project links and your contribution."),
    ("AI agent and RAG workflows", "AI automation experiments using n8n, Ollama, and document retrieval; include a demo or technical write-up where available."),
]

st.set_page_config(page_title=f"{NAME} | Doctoral CV", page_icon="📄", layout="wide")
st.markdown("""
<style>
:root { --ink:#17252b; --muted:#526269; --accent:#087e78; --accent-soft:#e5f2ef; --line:#d6e1dd; }
.block-container { max-width:1080px; padding-top:2.2rem; }
.cv-hero { background:linear-gradient(115deg,#17343b,#087e78); color:#fff; padding:2rem 2.2rem; border-radius:8px; margin-bottom:1.2rem; }
.cv-hero h1 { color:#fff; margin:0; font-size:2.15rem; }
.cv-hero h3 { color:#d3ebe5; margin:.45rem 0; font-weight:500; }
.cv-hero p { color:#eaf5f1; margin:0; }
.cv-card { border:1px solid var(--line); border-radius:6px; padding:1rem 1.1rem; margin-bottom:.7rem; }
.cv-card h4 { margin:0 0 .35rem; color:var(--ink); }
.cv-kicker { color:var(--accent); text-transform:uppercase; font-size:.78rem; font-weight:700; letter-spacing:.08em; }
.cv-muted { color:var(--muted); }
.cv-chip { display:inline-block; background:var(--accent-soft); color:#155550; border-radius:3px; padding:.25rem .55rem; margin:.12rem; font-size:.86rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    photo = Path(__file__).parent / "profile.jpg"
    if photo.exists():
        st.image(str(photo), use_container_width=True)
    st.markdown(f"### {NAME}")
    st.caption(TITLE)
    st.markdown(f"[Email](mailto:{EMAIL})")
    if PHONE:
        st.caption(PHONE)
    if LOCATION:
        st.caption(LOCATION)
    if GITHUB:
        st.markdown(f"[GitHub]({GITHUB})")
    if LINKEDIN:
        st.markdown(f"[LinkedIn]({LINKEDIN})")
    st.divider()
    cv_markdown = f"""# {FULL_NAME}\n\n**{TITLE}**\n\n{TAGLINE}\n\n{CONTACT_INFO}\n\n## Professional Profile\n{PROFILE}\n\n## Research Interests\n{RESEARCH_TITLE}\n\n{RESEARCH_SUMMARY}\n\n## Academic Preparation\n"""
    for education in EDUCATION:
        cv_markdown += f"- **{education['qualification']}** — {education['institution']} ({education['dates']})\n"
    cv_markdown += "\n## Professional Experience\n"
    for job in EXPERIENCE:
        cv_markdown += f"\n### {job['role']} | {job['organisation']}\n{job['period']}\n"
        cv_markdown += "".join(f"\n- {detail}" for detail in job["details"]) + "\n"
    cv_markdown += "\n## Selected Projects\n" + "".join(f"\n- **{name}:** {detail}" for name, detail in PROJECTS)
    cv_markdown += "\n\n## Technical Skills\n" + "".join(f"\n- **{group}:** {', '.join(skills)}" for group, skills in SKILLS.items())
    st.download_button("Download CV draft (.md)", cv_markdown, file_name="Jayanath_Jayarathna_Doctoral_CV.md", mime="text/markdown", use_container_width=True)

st.markdown(f"""
<div class="cv-hero">
  <div class="cv-kicker" style="color:#bce4db">Doctoral application · Artificial Intelligence</div>
  <h1>{NAME}</h1>
  <h3>{TITLE}</h3>
  <p>{TAGLINE}</p>
</div>
""", unsafe_allow_html=True)

st.info("Application draft: verify award titles against certificates, confirm dates and official job title, and add public project evidence before submitting.")

tab_cv, tab_research, tab_projects, tab_skills = st.tabs(["Academic CV", "Research direction", "Projects", "Technical skills"])

with tab_cv:
    st.markdown('<div class="cv-kicker">Professional profile</div>', unsafe_allow_html=True)
    st.write(PROFILE)
    st.markdown('<div class="cv-kicker">Academic preparation</div>', unsafe_allow_html=True)
    for education in EDUCATION:
        st.markdown(f"**{education['qualification']}**  \n{education['institution']} · {education['dates']}")
    st.markdown('<div class="cv-kicker">Professional experience</div>', unsafe_allow_html=True)
    for job in EXPERIENCE:
        st.markdown(f"#### {job['role']}\n**{job['organisation']}** · {job['period']}")
        for detail in job["details"]:
            st.markdown(f"- {detail}")

with tab_research:
    st.markdown('<div class="cv-kicker">Preliminary research direction</div>', unsafe_allow_html=True)
    st.header(RESEARCH_TITLE)
    st.write(RESEARCH_SUMMARY)
    st.markdown("**Potential focus**")
    st.markdown("- Decision support for disruption analysis and service reliability.\n- Responsible use of operational data in safety-sensitive transportation settings.\n- Evaluation of model usefulness, reliability, and limitations with domain stakeholders.")
    st.caption("A research proposal still needs a focused literature review, research questions, methodology, and confirmed access to suitable data.")

with tab_projects:
    st.markdown('<div class="cv-kicker">Selected project areas</div>', unsafe_allow_html=True)
    for name, detail in PROJECTS:
        st.markdown(f'<div class="cv-card"><h4>{name}</h4><span class="cv-muted">{detail}</span></div>', unsafe_allow_html=True)
    st.caption("Add repositories, live demonstrations, technical documentation, and verified evaluation results to strengthen these entries.")

with tab_skills:
    for group, skills in SKILLS.items():
        st.markdown(f"#### {group}")
        st.markdown("".join(f'<span class="cv-chip">{skill}</span>' for skill in skills), unsafe_allow_html=True)

with st.expander("Details to confirm before sending this CV"):
    st.markdown("- Exact official title and awarding institution for each qualification; ensure postgraduate award wording matches the certificate.\n- Railway designation in English and Sinhala, service dates, current employment status, and any specific responsibilities you can substantiate.\n- Current contact details and professional profile links.\n- For each project: your contribution, data source, methods, evaluation, limitations, and accessible evidence.\n- Add languages, certifications, publications, presentations, and research work only where accurate.")

st.caption(f"{NAME} · Doctoral CV draft")

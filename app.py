from pathlib import Path 

import streamlit as st
from PIL import Image

# ---PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jayanath Rangika"
PAGE_ICON = ":wave:"
NAME = "Jayanath Rangika"
DESCRIPTION = """
Experienced data science and date analyst professional with a background in physical science and data science
"""
EMAIL = "jayanathsha@gmail.com"
SOCIAL_MEDIA = {
    "YouTube":"https://www.youtube.com/@jayanathjayarathna5983",
    "GitHub": "https://github.com/Rangikaj80",
    "LinkedIn":"https://www.linkedin.com/in/jayanath-jayarathna-178b19228/",
}
PROJECTS = {
    
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://www.novypro.com/profile_projects/jayanathjayarathna",
    "🏆 Retail Shop Profit DashBoard - Python streamlit": "https://sbmprofitdashboard.streamlit.app/",
    "🏆 Business Management System - Python streamlit and sqlight": "https://sbmstcom-gn.streamlit.app/",
    "🏆 Brest Cancer Prediction - Python streamlit machine learning radar chart": "https://canserapp.streamlit.app/",
    }

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#--- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)




# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        )
    st.write("📫", EMAIL)
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- EXPERIENCE & QUAILIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas,Streamlit), SQL, VBA 
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Google Sheet
- 📚 Modeling: Logistic regression, linear regression, Random forest, XGboost
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 🤖 Deep Learning: Genarative AI, Langchain, RAG, ollama
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("___")

# --- JOB 1
st.write("🚧", "**Deport Master | Sri Lanka Railway department**")
st.write("08/2002 - 04/2023")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations 
- ► Coordination with Other Departments: They work closely with other departments, such as maintenance, dispatch, and logistics, 
    to address operational needs, resolve issues, and ensure seamless communication across teams
- ► Inventory and Resource Management, Documentation and Reporting 
"""
)

# --- JOB 3
st.write('\n')
st.write('🚧', "**retail shop owner | Saheli Beauty Mart**")
st.write("04/2015 - present")
st.write(
    """
- ► Market Analysis:assesses market trends, customer preferences, and competitor activities to identify 
        growth opportunities and areas for improvement. And use this information to adapt our product offerings or services
- ► Sales and Financial Analysis: Monitoring sales data, profit margins, and inventory turnover helps the owner understand 
        what products are performing well and where to adjust pricing or stock levels. And use KPIs to measure store  
        performance and set financial goals.
- ► Customer Insights: By analyzing customer feedback, purchase patterns, and demographics, can better understand 
        the needs of their target market and tailor products or services accordingly.
    """
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accoplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
# --- CERTIFICATES ---
st.write("\n")
st.subheader("Certificates")
st.write("---")

CERTIFICATES = {
    "Certificate 1 Mba in data science": current_dir / "assets" / "mba_data_science.pdf",
    "Certificate 2: Degree of Statistic & Computer Science": current_dir / "assets" / "degree_certificate.pdf",
    "Certificate 3: Business Management": current_dir / "assets" / "BusinessManagement.pdf",
    "Certificate 4: Other Certification & Achievements": current_dir / "assets" / "otherCertificates.pdf",
}

for cert_name, cert_path in CERTIFICATES.items():
    with open(cert_path, "rb") as cert_file:
        cert_data = cert_file.read()
        st.download_button(
            label=f"📄 {cert_name}",
            data=cert_data,
            file_name=cert_path.name,
            mime="application/pdf"
        )
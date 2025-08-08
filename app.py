import streamlit as st

st.set_page_config(page_title="Chat with Surya", page_icon="🤖")
st.title("🤖 Chat with Surya Tatikayala's Assistant")

st.markdown("Ask me anything about Surya — his experience, projects, skills, or certifications.")

query = st.text_input("💬 Ask your question here:")

def get_response(query):
    query = query.lower()

    if "name" in query or "who are you" in query:
        return "I am Surya Tatikayala's virtual assistant. Surya is an Associate DevOps & AI/ML Engineer based in Bangalore."

    elif "experience" in query or "job" in query:
        return (
            "Surya has 3+ years of experience as a DevOps Engineer at Kyndryl. "
            "He has architected and deployed multi-cloud infrastructure (AWS, Azure, IBM Cloud), "
            "automated using Terraform, Ansible, Jenkins, and GitHub Actions."
        )

    elif "project" in query:
        return (
            "Surya has led several AI/ML projects:\n"
            "1. **SRE AIOps Dashboard** – Forecasts incidents using ARIMA and Mistral AI insights.\n"
            "2. **Ansible Log Detector** – ML-powered tool to analyze Ansible logs and suggest solutions.\n"
            "3. **Speaker Recognition System** – Voice-based gender and speaker ID using TensorFlow.\n"
            "All hosted on GitHub and Hugging Face!"
        )

    elif "skill" in query:
        return (
            "Surya's technical skills include:\n"
            "- **Cloud**: AWS, Azure, IBM Cloud\n"
            "- **IaC & Automation**: Terraform, Ansible, Ansible Tower\n"
            "- **CI/CD**: Jenkins, GitHub Actions, Azure DevOps\n"
            "- **Programming**: Python, YAML, Bash\n"
            "- **AI/ML**: TensorFlow, Scikit-learn, Statsmodels, Hugging Face, Gradio\n"
            "- **Containers**: Docker, basic Kubernetes"
        )

    elif "certification" in query or "certified" in query:
        return (
            "Surya holds the following certifications:\n"
            "- AWS Certified Cloud Practitioner\n"
            "- Microsoft Azure Fundamentals (AZ-900)\n"
            "- Microsoft Azure Administrator (AZ-104)\n"
            "- Terraform Associate (002)\n"
            "- Certified AI Engineer – Reva University"
        )

    elif "contact" in query or "email" in query:
        return (
            "You can contact Surya at: sudheertatikayala111@gmail.com\n"
            "Phone: +91 9398743330\n"
            "LinkedIn: https://www.linkedin.com/in/surya-tatikayala1/\n"
            "GitHub: https://github.com/suryaT1"
        )

    elif "education" in query:
        return (
            "Surya completed:\n"
            "- **Bachelor of Computer Science** (2019–2022) – Adikavi Nannaya University\n"
            "- **Master of Computer Science** (2022–2024) – Adikavi Nannaya University"
        )

    elif "tools" in query or "ms tools" in query:
        return "MS tools Surya uses: Power Automate, Planner, SharePoint, Power Apps."

    else:
        return "I'm not sure about that. You can ask me about Surya's skills, projects, certifications, or experience."

if query:
    st.write("🤖", get_response(query))

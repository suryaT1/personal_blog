import streamlit as st

st.set_page_config(page_title="Chat with Surya", page_icon="🤖")
st.title("🤖 Chat with Surya Tatikayala's Assistant")

# Show default greeting
with st.chat_message("assistant"):
    st.markdown("Hi there! 👋 I'm Surya's virtual assistant. You can ask me about his skills, projects, experience, and more.")

# Show sample questions
with st.expander("💡 Sample Questions"):
    st.markdown("""
    - What are Surya's technical skills?
    - Tell me about his AI/ML projects.
    - What certifications does Surya hold?
    - How can I contact him?
    - What is his work experience?
    """)

# Input box (chat-style)
user_query = st.chat_input("Ask me anything about Surya...")

def get_response(query):
    query = query.lower()

    if query in ["hi", "hello", "hey"]:
        return "Hello! 👋 I'm here to answer questions about Surya Tatikayala. Try asking about his projects or skills!"

    elif "name" in query or "who are you" in query:
        return "I’m Surya Tatikayala's virtual assistant. Surya is an Associate DevOps & AI/ML Engineer based in Bangalore."

    elif "experience" in query or "job" in query:
        return (
            "Surya has over 3 years of experience at Kyndryl. He works with AWS, Azure, Terraform, Ansible, Jenkins, and containerized apps using Docker & Kubernetes."
        )

    elif "project" in query:
        return (
            "**Surya’s Top AI/ML Projects:**\n"
            "1. **SRE AIOPS Dashboard** – ARIMA forecasting + Mistral AI insights.\n"
            "2. **Ansible Log Detector** – ML tool for error detection in Ansible logs.\n"
            "3. **Speaker Recognition System** – Gender + speaker ID via voice using TensorFlow.\n"
            "Live demos on GitHub & Hugging Face!"
        )

    elif "skill" in query:
        return (
            "**Technical Skills:**\n"
            "- Cloud: AWS, Azure, IBM Cloud\n"
            "- IaC: Terraform, Ansible, Ansible Tower\n"
            "- CI/CD: Jenkins, GitHub Actions, Azure DevOps\n"
            "- ML: TensorFlow, Scikit-learn, Hugging Face, Gradio\n"
            "- Containers: Docker, Kubernetes\n"
            "- Scripting: Python, YAML, Bash"
        )

    elif "certification" in query or "certified" in query:
        return (
            "**Certifications:**\n"
            "- AWS Cloud Practitioner\n"
            "- Microsoft Azure (AZ-900, AZ-104)\n"
            "- Terraform Associate (002)\n"
            "- Certified AI Engineer – Reva University"
        )

    elif "contact" in query or "email" in query:
        return (
            "**Contact Surya:**\n"
            "- 📧 sudheertatikayala111@gmail.com\n"
            "- 📞 +91 9398743330\n"
            "- [LinkedIn](https://www.linkedin.com/in/surya-tatikayala1/) | [GitHub](https://github.com/suryaT1)"
        )

    elif "education" in query:
        return (
            "Surya completed:\n"
            "- **B.Sc. in Computer Science** (2019–2022)\n"
            "- **M.Sc. in Computer Science** (2022–2024)\n"
            "at Adikavi Nannaya University."
        )

    elif "tools" in query or "ms tools" in query:
        return (
            "Surya uses various MS tools including:\n"
            "- Power Automate, Power Apps, SharePoint, and Planner."
        )

    else:
        return (
            "I'm not sure how to answer that 🤔. Try asking about Surya’s skills, projects, certifications, or contact info."
        )

# Display response
if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        response = get_response(user_query)
        st.markdown(response)

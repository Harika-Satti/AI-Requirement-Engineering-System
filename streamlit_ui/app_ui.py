import streamlit as st
import requests
import os

API_URL = "http://127.0.0.1:8000"

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Requirement Engineering System",
    layout="wide"
)

st.title("AI Requirement Engineering Platform")

# ==========================
# Sidebar Navigation
# ==========================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Generate Project",
        "View Projects",
        "Ask AI (RAG)"
    ]
)

# ==========================
# Generate Project
# ==========================

if menu == "Generate Project":

    st.header("Generate New Project")

    project_name = st.text_input("Project Name")

    requirement = st.text_area(
        "Enter Requirement",
        height=250
    )

    if st.button("Generate"):

        payload = {
            "project_name": project_name,
            "requirement": requirement
        }

        response = requests.post(
            f"{API_URL}/generate",
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.success(
                "Project Generated Successfully!"
            )

            # Tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "Analysis",
                    "User Stories",
                    "Use Cases",
                    "SRS",
                    "Review"
                ]
            )

            with tab1:
                st.write(data.get("analysis", "No analysis available"))

            with tab2:
                st.write(data.get("user_stories", "No user stories available"))

            with tab3:
                st.write(data.get("use_cases", "No use cases available"))

            with tab4:
                st.markdown(data.get("srs", "No SRS generated"))

            with tab5:
                st.write(data.get("review", "No review available"))

            # File paths
            st.divider()

            st.subheader("Generated Files")

            st.write("PDF Location:")
            st.code(data.get("pdf", "Not generated"))

            st.write("DOCX Location:")
            st.code(data.get("docx", "Not generated"))

            # Downloads
            st.divider()

            st.subheader("Download SRS Documents")

            pdf_path = data.get("pdf")
            docx_path = data.get("docx")

            # PDF Download
            if pdf_path and os.path.exists(pdf_path):

                with open(pdf_path, "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download PDF",
                        data=pdf_file.read(),
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )

            else:
                st.warning("PDF file not found")

            # DOCX Download
            if docx_path and os.path.exists(docx_path):

                with open(docx_path, "rb") as docx_file:

                    st.download_button(
                        label="📝 Download DOCX",
                        data=docx_file.read(),
                        file_name=os.path.basename(docx_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

            else:
                st.warning("DOCX file not found")

        else:
            st.error("Something went wrong")

# ==========================
# View Projects
# ==========================

elif menu == "View Projects":

    st.header("Stored Projects")

    response = requests.get(
        f"{API_URL}/projects"
    )

    if response.status_code == 200:

        projects = response.json()["projects"]

        for p in projects:

            st.subheader(
                f"Project ID: {p[0]}"
            )

            st.write(f"Name: {p[1]}")
            st.write(f"Requirement: {p[2]}")
            st.write("---")

    else:
        st.error(
            "Failed to fetch projects"
        )

# ==========================
# Ask AI (RAG)
# ==========================

elif menu == "Ask AI (RAG)":

    st.header(
        "Ask AI About Your Project"
    )

    query = st.text_input(
        "Ask a question"
    )

    if st.button("Search"):

        payload = {
            "query": query
        }

        response = requests.post(
            f"{API_URL}/ask",
            json=payload
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            st.success(answer)

        else:
            st.error(
                "Failed to get answer"
            )
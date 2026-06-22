from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from graph.workflow import workflow
from rag.retriever import answer_query

from database.db import create_tables
from database.operations import (
    get_projects,
    get_project_by_id
)

from utils.export_pdf import generate_pdf
from utils.export_docx import generate_docx

load_dotenv()

app = FastAPI(
    title="AI Requirement Engineering System"
)

create_tables()


# ==========================
# Request Models
# ==========================

class GenerateRequest(BaseModel):
    project_name: str
    requirement: str


class AskRequest(BaseModel):
    query: str


# ==========================
# Generate Project
# ==========================

@app.post("/generate")
def generate_project(request: GenerateRequest):

    result = workflow.invoke(
        {
            "project_name": request.project_name,
            "raw_requirement": request.requirement
        }
    )

    pdf_path = generate_pdf(
        result["srs_document"],
        request.project_name
    )

    docx_path = generate_docx(
        result["srs_document"],
        request.project_name
    )

    return {
        "message": "Project generated successfully",

        "analysis":
            result["analyzed_requirement"],

        "user_stories":
            result["user_stories"],

        "use_cases":
            result["use_cases"],

        "srs":
            result["srs_document"],

        "review":
            result["review_report"],

        "pdf":
            pdf_path,

        "docx":
            docx_path
    }


# ==========================
# Ask Questions (RAG)
# ==========================

@app.post("/ask")
def ask_question(request: AskRequest):

    answer = answer_query(
        request.query
    )

    return {
        "query": request.query,
        "answer": answer
    }


# ==========================
# Get All Projects
# ==========================

@app.get("/projects")
def fetch_projects():

    return {
        "projects": get_projects()
    }


# ==========================
# Get Single Project
# ==========================

@app.get("/project/{project_id}")
def fetch_project(project_id: int):

    return get_project_by_id(
        project_id
    )


# ==========================
# Health Check
# ==========================

@app.get("/")
def home():

    return {
        "message":
        "AI Requirement Engineering System Running"
    }
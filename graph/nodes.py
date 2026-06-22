from agents.requirement_agent import RequirementAnalyzer
from agents.ambiguity_agent import AmbiguityDetector
from agents.user_story_agent import UserStoryGenerator
from agents.usecase_agent import UseCaseGenerator
from agents.srs_agent import SRSGenerator
from agents.reviewer_agent import ReviewerAgent


requirement_agent = RequirementAnalyzer()

ambiguity_agent = AmbiguityDetector()

story_agent = UserStoryGenerator()

usecase_agent = UseCaseGenerator()

srs_agent = SRSGenerator()

reviewer_agent = ReviewerAgent()


def requirement_node(state):

    result = requirement_agent.analyze(
        state["raw_requirement"]
    )

    return {
        "analyzed_requirement": result
    }


def ambiguity_node(state):

    result = ambiguity_agent.detect(
        state["analyzed_requirement"]
    )

    return {
        "ambiguities": result
    }


def user_story_node(state):

    result = story_agent.generate(
        state["analyzed_requirement"]
    )

    return {
        "user_stories": result
    }

def usecase_node(state):

    result = usecase_agent.generate(
        state["analyzed_requirement"]
    )

    return {
        "use_cases": result
    }

def srs_node(state):

    result = srs_agent.generate(
        state["analyzed_requirement"],
        state["ambiguities"],
        state["user_stories"],
        state["use_cases"]
    )

    return {
        "srs_document": result
    }


def reviewer_node(state):

    result = reviewer_agent.review(
        state["analyzed_requirement"],
        state["ambiguities"],
        state["user_stories"],
        state["use_cases"],
        state["srs_document"],
        state.get("similar_projects", [])
    )

    return {
        "review_report": result
    }

# faiss node

from database.faiss_store import save_to_faiss, search_faiss


def faiss_node(state):

    combined_text = f"""
    {state['analyzed_requirement']}

    {state['ambiguities']}

    {state['user_stories']}

    {state['use_cases']}

    {state['srs_document']}

    {state['review_report']}
    """

    save_to_faiss(
        state["project_name"],
        combined_text
    )

    similar = search_faiss(state["raw_requirement"])

    state["similar_projects"] = similar 

    return state

# sqlite node
from database.operations import (
    save_project,
    save_document,
    save_review
)

def sqlite_node(state):

    project_id = save_project(
        state["project_name"],
        state["raw_requirement"]
    )

    save_document(
        project_id,
        "analysis",
        state["analyzed_requirement"]
    )

    save_document(
        project_id,
        "ambiguity",
        state["ambiguities"]
    )

    save_document(
        project_id,
        "user_stories",
        state["user_stories"]
    )

    save_document(
        project_id,
        "use_cases",
        state["use_cases"]
    )

    save_document(
        project_id,
        "srs",
        state["srs_document"]
    )

    save_review(
        project_id,
        state["review_report"]
    )

    return state
from langgraph.graph import StateGraph
from langgraph.graph import START, END

from graph.state import RequirementState

from graph.nodes import *

builder = StateGraph(RequirementState)

builder.add_node(
    "requirement",
    requirement_node
)

builder.add_node(
    "ambiguity",
    ambiguity_node
)

builder.add_node(
    "user_story",
    user_story_node
)

builder.add_node(
    "use_case",
    usecase_node
)

builder.add_node(
    "srs",
    srs_node
)

builder.add_node(
    "reviewer",
    reviewer_node
)

builder.add_node(
    "faiss_store",
    faiss_node
)

builder.add_node(
    "sqlite_store",
    sqlite_node
)

builder.add_edge(
    START,
    "requirement"
)

builder.add_edge(
    "requirement",
    "ambiguity"
)

builder.add_edge(
    "ambiguity",
    "user_story"
)

builder.add_edge(
    "user_story",
    "use_case"
)

builder.add_edge(
    "use_case",
    "srs"
)

builder.add_edge(
    "srs",
    "reviewer"
)

builder.add_edge(
    "reviewer",
    "faiss_store"
)

builder.add_edge(
    "faiss_store",
    "sqlite_store"
)

builder.add_edge(
    "sqlite_store",
    END
)

workflow = builder.compile()


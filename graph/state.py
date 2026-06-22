from typing import TypedDict


class RequirementState(TypedDict):

    project_name: str

    raw_requirement: str

    analyzed_requirement: str

    ambiguities: str

    user_stories: str

    use_cases: str

    srs_document: str

    review_report: str

    similar_project: list
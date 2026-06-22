from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.reviewer_prompt import reviewer_prompt


class ReviewerAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

        self.prompt = PromptTemplate(
            template=reviewer_prompt,
            input_variables=[
                "analysis",
                "ambiguity",
                "stories",
                "usecases",
                "srs"
            ]
        )

        self.chain = self.prompt | self.llm

    def review(
    self,
    analyzed_requirement,
    ambiguities,
    user_stories,
    use_cases,
    srs_document,
    similar_projects=None
):

        try:

            response = self.chain.invoke(
                {
                    "analysis": analyzed_requirement,
                    "ambiguity": ambiguities,
                    "stories": user_stories,
                    "usecases": use_cases,
                    "srs": srs_document
                }
            )

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.srs_prompt import srs_prompt


class SRSGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = PromptTemplate(
            template=srs_prompt,
            input_variables=[
                "analysis",
                "ambiguity",
                "stories",
                "usecases"
            ]
        )

        self.chain = self.prompt | self.llm

    def generate(
        self,
        analysis,
        ambiguity,
        stories,
        usecases
    ):

        try:

            response = self.chain.invoke(
                {
                    "analysis": analysis,
                    "ambiguity": ambiguity,
                    "stories": stories,
                    "usecases": usecases
                }
            )

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"
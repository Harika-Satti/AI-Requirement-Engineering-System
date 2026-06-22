from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.requirement_prompt import requirement_prompt
from dotenv import load_dotenv
import os

load_dotenv()


class RequirementAnalyzer:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0

        )

        self.prompt = PromptTemplate(
            template=requirement_prompt,
            input_variables=["requirement"]
        )

        self.chain = self.prompt | self.llm

    def analyze(self, requirement: str):

        try:

            response = self.chain.invoke(
                {
                    "requirement": requirement
                }
            )

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"
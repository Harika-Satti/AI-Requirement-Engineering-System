from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.usecase_prompt import usecase_prompt


class UseCaseGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = PromptTemplate(
            template=usecase_prompt,
            input_variables=["analysis"]
        )

        self.chain = self.prompt | self.llm

    def generate(self, analysis):

        try:

            response = self.chain.invoke(
                {
                    "analysis": analysis
                }
            )

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"
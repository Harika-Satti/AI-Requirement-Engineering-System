from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.ambiguity_prompt import ambiguity_prompt


class AmbiguityDetector:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = PromptTemplate(
            template=ambiguity_prompt,
            input_variables=["analysis"]
        )

        self.chain = self.prompt | self.llm

    def detect(self, analysis):

        try:

            response = self.chain.invoke(
                {
                    "analysis": analysis
                }
            )

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"
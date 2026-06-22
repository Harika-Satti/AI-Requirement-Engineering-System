from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts.user_story_prompt import user_story_prompt


class UserStoryGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = PromptTemplate(
            template=user_story_prompt,
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
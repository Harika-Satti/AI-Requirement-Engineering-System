from dotenv import load_dotenv

from agents.requirement_agent import RequirementAnalyzer
from agents.user_story_agent import UserStoryGenerator

load_dotenv()

requirement_agent = RequirementAnalyzer()
user_story_agent = UserStoryGenerator()

requirement = """
Build an online food delivery platform.

Customers can:
- Register
- Login
- Order food

Restaurant owners can:
- Manage menus
- View orders

Admins can:
- Manage users
"""

analysis = requirement_agent.analyze(requirement)

stories = user_story_agent.generate(analysis)

print("\n===== USER STORIES =====\n")
print(stories)
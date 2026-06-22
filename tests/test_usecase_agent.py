from dotenv import load_dotenv

from agents.requirement_agent import RequirementAnalyzer
from agents.usecase_agent import UseCaseGenerator

load_dotenv()

requirement_agent = RequirementAnalyzer()
usecase_agent = UseCaseGenerator()

requirement = """
Build an online food delivery platform.

Customers can:
- Register
- Login
- Order food
- Track orders

Restaurant owners can:
- Manage menus
- View orders

Admins can:
- Manage users
"""

analysis = requirement_agent.analyze(requirement)

usecases = usecase_agent.generate(analysis)

print("\n===== USE CASES =====\n")
print(usecases)
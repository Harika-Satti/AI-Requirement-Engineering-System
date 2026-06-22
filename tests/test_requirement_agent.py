from dotenv import load_dotenv

from agents.requirement_agent import RequirementAnalyzer

load_dotenv()

agent = RequirementAnalyzer()

sample_requirement = """
Build an online food delivery platform where:

1. Customers can register and login
2. Browse restaurants
3. Order food online
4. Track deliveries

Restaurant owners can:

1. Manage menus
2. Update prices
3. View orders

Admins can:

1. Manage users

2. View reports
"""

result = agent.analyze(sample_requirement)

print(result)
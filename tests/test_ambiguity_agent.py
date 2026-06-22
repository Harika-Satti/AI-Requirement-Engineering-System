from dotenv import load_dotenv

from agents.requirement_agent import RequirementAnalyzer
from agents.ambiguity_agent import AmbiguityDetector

load_dotenv()

requirement_agent = RequirementAnalyzer()
ambiguity_agent = AmbiguityDetector()

requirement = """
Build an online food delivery application.

Customers can order food.
Restaurants can manage menus.
Admins can manage users.
"""

analysis = requirement_agent.analyze(requirement)

ambiguity_report = ambiguity_agent.detect(analysis)

print("\n===== REQUIREMENT ANALYSIS =====\n")
print(analysis)

print("\n===== AMBIGUITY REPORT =====\n")
print(ambiguity_report)
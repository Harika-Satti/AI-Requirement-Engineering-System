from dotenv import load_dotenv

from agents.requirement_agent import RequirementAnalyzer
from agents.ambiguity_agent import AmbiguityDetector
from agents.user_story_agent import UserStoryGenerator
from agents.usecase_agent import UseCaseGenerator
from agents.srs_agent import SRSGenerator
from agents.reviewer_agent import ReviewerAgent

load_dotenv()

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

req_agent = RequirementAnalyzer()
amb_agent = AmbiguityDetector()
story_agent = UserStoryGenerator()
usecase_agent = UseCaseGenerator()
srs_agent = SRSGenerator()
reviewer_agent = ReviewerAgent()

analysis = req_agent.analyze(requirement)

ambiguity = amb_agent.detect(analysis)

stories = story_agent.generate(analysis)

usecases = usecase_agent.generate(analysis)

srs = srs_agent.generate(
    analysis,
    ambiguity,
    stories,
    usecases
)

review = reviewer_agent.review(
    analysis,
    ambiguity,
    stories,
    usecases,
    srs
)

print(review)
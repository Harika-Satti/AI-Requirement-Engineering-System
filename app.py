from dotenv import load_dotenv

load_dotenv()

from database.db import create_tables

create_tables()

from graph.workflow import workflow

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

result = workflow.invoke(
    {
        "project_name": "Food Delivery System",

        "raw_requirement": requirement
    }
)

print("\n\n===== REVIEW REPORT =====\n")

print(result["review_report"])
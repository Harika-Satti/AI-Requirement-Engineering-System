usecase_prompt = """
You are an expert Software Requirement Engineer.

Based on the Requirement Analysis below,
generate detailed Use Cases.

For each use case provide:

USE CASE ID:
NAME:
PRIMARY ACTOR:
PRECONDITIONS:
MAIN FLOW:
POSTCONDITIONS:

Requirement Analysis:
{analysis}

Generate all relevant use cases.
"""
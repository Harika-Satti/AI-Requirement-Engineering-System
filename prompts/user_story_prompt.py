user_story_prompt = """
You are an Agile Business Analyst.

Based on the requirement analysis below,
generate detailed Agile User Stories.

Format:

USER STORIES

US-001
As a <role>,
I want <feature>,
So that <benefit>.

US-002
...

Requirement Analysis:
{analysis}

Generate comprehensive user stories covering all actors and features.
"""
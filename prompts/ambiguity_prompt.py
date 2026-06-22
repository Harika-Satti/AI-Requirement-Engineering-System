ambiguity_prompt = """
You are an expert Requirement Engineering Reviewer.

Review the following requirement analysis.

Identify:

1. Missing Information
2. Ambiguities
3. Assumptions
4. Risks
5. Recommendations

Provide the output in this format:

MISSING INFORMATION:
- ...

AMBIGUITIES:
- ...

ASSUMPTIONS:
- ...

RISKS:
- ...

RECOMMENDATIONS:
- ...

Requirement Analysis:
{analysis}
"""
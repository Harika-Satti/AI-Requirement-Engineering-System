srs_prompt = """
You are a Senior Requirement Engineer.

Generate a professional Software Requirements Specification (SRS).

Use the provided information:

Requirement Analysis:
{analysis}

Ambiguity Report:
{ambiguity}

User Stories:
{stories}

Use Cases:
{usecases}

Generate the SRS using this structure:

# SOFTWARE REQUIREMENTS SPECIFICATION

## 1. Introduction
- Overview

## 2. Purpose

## 3. Scope

## 4. Actors

## 5. Functional Requirements

## 6. Non-Functional Requirements

## 7. User Stories

## 8. Use Cases

## 9. Assumptions

## 10. Risks

## 11. Future Enhancements

## 12. Conclusion

Instructions:
- Extract all actors from the requirement analysis.
- Generate detailed functional requirements.
- Generate non-functional requirements based on the project context.
- Include all user stories and use cases provided.
- Identify possible risks and assumptions.
- Suggest future enhancements.
- Use professional business documentation language.
- Make the document detailed and well-structured.

Provide a complete SRS document.
"""
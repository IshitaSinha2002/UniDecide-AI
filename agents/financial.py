from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def financial_advisor(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the Financial Advisor on a University Student Committee.

        The student is deciding between:
        {universities}

        Student's question:
        {query}

        Analyze the universities from a career perspective.

        Consider:
        - Tuition and overall cost
        - Cost of living
        - Financial aid
        - Scholarships
        - Expected return on investment
        - Career earnings potential
        - Opportunity cost
        - Overall financial value

        Compare all universities fairly.

        Give a clear recommendation and explain which university
        has the strongest financial value.

        Do not make up specific financial figures.
        """
    )

    response = llm.invoke(
        prompt.format(
            univesities=", ".join(state["universities"]),
            query=state["query"]
        )
    )

    return {
        "financial_opinion": response.content
    }
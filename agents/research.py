from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def research_advisor(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the Research Advisor on a University Student Committee.

        The student is deciding between:
        {universities}

        Student's question:
        {query}

        Analyze the universities specifically for AI and research.

        Consider:
        - AI/ML research strength
        - Research opportunities for students
        - Faculty research ecosystem
        - Access to research labs
        - Publications and research culture
        - Opportunites to work with professors
        - Graduate research pathways
        - Strength in emerging AI areas

        Compare all universities fairly.

        Give a clear recommendation and explain which university
        has the strongest research case.

        Do not make up specific facts.
        """
    )

    response = llm.invoke(
        prompt.format(
            universities=", ".join(state["universities"]),
            query=state["query"]
        )
    )

    return {
        "research_opinion": response.content
    }
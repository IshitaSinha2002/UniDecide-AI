from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def alumni_perspective(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the Alumni Perspective Advisor on a University
        Selection Committee.

        The student is deciding between:
        {universities}

        Student's question:
        {query}

        Evaluate the universities from an alumni perspective.

        Consider:
        - Alumni network
        - Long-term professional connections
        - Brand reputation
        - Alumni career mobility
        - Networking opportunities
        - Entrepreneurial ecosystem
        - Long-term value of the university community

        Compare all universities fairly.

        Give a clear recommendation and explain which university
        has the strongest long-term alumni advantage.

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
        "alumni_opinion": response.content
    }
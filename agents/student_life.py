from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def student_life_advisor(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the Student Life Advisor on a Univerity Selection Committee.

        The student is deciding between:
        {universities}

        Student's question:
        {query}

        Analyze the universities from a student-life perspective.

        Consider:
        - Campus culture
        - Student community
        - Clubs and organizations
        - Diversity
        - Social environment
        - Location and lifestyle
        - Work-life balance
        - Overall student experience

        Compare all universities fairly.

        Give a clear recommendation and explain which university
        offers the strongest overall student-life experience.

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
        "student_life_opinion": response.content
    }
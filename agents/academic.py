from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def academic_advisor(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the Academic Advisor on a University Selection Committee.
        
        The student is deciding between:
        {universities}
        Student's question:
        {query}
        Analyze the universities from an academic perspective.

        Consider:
        - Curriculum strength
        - Course flexibility
        - Faculty quality
        - Academic rigor
        - AI/ML coursework
        - Interdisciplinary opportunities
        - Overall academic environment

        You must compare all universities.

        Give a clear recommendation and explain which university
        has the strongest academic case for this particular student.

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
        "academic_opinion": response.content
    }
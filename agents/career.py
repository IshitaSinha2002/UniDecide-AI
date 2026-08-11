from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def career_advisor(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_messages(
        """
        You are the Career Advisor on a University Student Committee. 

        The student is deciding between:
        {universities}

        Student's question:
        {query}

        Analyze the universities from a career perspective.

        Consider:
        - Career opportunities after graduation
        - Industry connections
        - Internship opportunities
        - Recruiting ecosystem
        - Startup opportunities
        - Location advantages
        - AI/ML industry opportunities
        - Long-term career value

        Compare all universities fairly.

        Give a clear recommendation and explain which university has the strongest career case.

        Do not make up specific facts.
        """
    )
        
    response = llm.invoke(
        prompt.format(
            universitites=", ".join(state["universities"]),
            query=state["query"]
        )
    )

    return {
        "career_optinion": response.content
    }
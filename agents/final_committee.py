from langchain_core.prompts import ChatPromptTemplate
from state import UniversityState

def final_committee(state: UniversityState, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are the final committee of a University Selection Committee.
        
        The student asked:
        {query}

        Universities being considered:
        {universities}

        Below are the independent recommendations from the committee:
        ACADEMIC ADVISOR
        {academic_opinion}

        CAREER ADVISOR
        {career_opinion}

        FINANCIAL ADVISOR
        {financial_opinion}

        RESEARCH ADVISOR
        {research_opinion}

        STUDENT LIFE ADVISOR
        {student_life_opinion}

        ALUMNI PERSPECTIVE
        {alumni_opinion}

        You must now act as the final decision-making committee.

        Do the following:
        1. Identify the strongest arguments for each university.
        2. Identify disagreements between the advisors.
        3. Determine which factors matter most for the student's question.
        4. Weigh all advisor perspective.
        5. Select ONE final university.
        6. Explain why it wins.
        7. Mention the strongest alternative and why it lost.
        8. Give a concise final verdict.

        Do not simply count how many advisors selected each university.
        Reason about the quality and relevance of their arguments.

        Your final answer should follow this structure:

        FINAL RECOMMENDATION:
        <university>

        WHY IT WINS:
        <explanation>

        COMMITTEE ANALYST:
        <analysis of the major perspectives>

        STRONGEST ALTERNATIVE:
        <university and explanation>

        FINAL VERDICT:
        <concise conclusion>
        """
    )

    response = llm.invoke(
        prompt.format(
            query=state["query"]
            universities=", ".join(state["universities"]),
            academic_opinion=state["academic_opinion"],
            career_opinion=state["career_opinion"],
            financial_opinion=state["financial_opinion"],
            research_opinion=state["research_opinion"],
            student_life_opinion=state["student_life_opinion"],
            alumni_opinion=state["alumni_opinion"]
        )
    )

    return {
        "final_decision": response.content
    }
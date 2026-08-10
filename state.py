from typing import TypedDict

class UniversityState(TypedDict):
    query: str
    universities: list[str]
    academic_opinion: str
    career_opinion: str
    financial_opinion: str
    research_opinion: str
    student_life_opinion: str
    alumni_opinion: str
    final_decision: str
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

from state import UniversityState

from agents.academic import academic_advisor
from agents.career import career_advisor
from agents.financial import financial_advisor
from agents.research import research_advisor
from agents.student_life import student_life_advisor
from agents.alumni import alumni_perspective
from agents.final_committee import final_committee

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

def run_academic(state):
    return academic_advisor(state, llm)

def run_career(state):
    return career_advisor(state, llm)

def run_financial(state):
    return financial_advisor(state, llm)

def run_research(state):
    return research_advisor(state, llm)

def run_student_life(state):
    return student_life_advisor(state, llm)

def run_alumni(state):
    return alumni_perspective(state, llm)

def run_final_committee(state):
    return final_committee(state, llm)

builder = StateGraph(UniversityState)

builder.add_node("academic_advisor", run_academic)
builder.add_node("career_advisor", run_career)
builder.add_node("financial_advisor", run_financial)
builder.add_node("research_advisor", run_research)
builder.add_node("student_life_advisor", run_student_life)
builder.add_node("alumni_perspective", run_alumni)
builder.add_node("final_committee", run_final_committee)

builder.add_edge(START, "academic_advisor")
builder.add_edge(START, "career_advisor")
builder.add_edge(START, "financial_advisor")
builder.add_edge(START, "research_advisor")
builder.add_edge(START, "student_life_advisor")
builder.add_edge(START, "alumni_perspective")

builder.add_edge("academic_advisor", "final_committee")
builder.add_edge("career_advisor", "final_committee")
builder.add_edge("financial_advisor", "final_committee")
builder.add_edge("research_advisor", "final_committee")
builder.add_edge("student_life_advisor", "final_committee")
builder.add_edge("alumni_perspective", "final_committee")

builder.add_edge("final_committee", END)

university_graph = builder.compile()
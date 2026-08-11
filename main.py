from graph import university_graph


query = input("Enter your university comparison: ")


universities = [
    university.strip()
    for university in query.split(" vs ")
]


initial_state = {
    "query": query,
    "universities": universities,

    "academic_opinion": "",
    "career_opinion": "",
    "financial_opinion": "",
    "research_opinion": "",
    "student_life_opinion": "",
    "alumni_opinion": "",

    "final_decision": ""
}


result = university_graph.invoke(initial_state)


print("\n" + "=" * 70)
print("UNIVERSITY SELECTION COMMITTEE")
print("=" * 70)

print("\nACADEMIC ADVISOR")
print(result["academic_opinion"])

print("\nCAREER ADVISOR")
print(result["career_opinion"])

print("\nFINANCIAL ADVISOR")
print(result["financial_opinion"])

print("\nRESEARCH ADVISOR")
print(result["research_opinion"])

print("\nSTUDENT LIFE ADVISOR")
print(result["student_life_opinion"])

print("\nALUMNI PERSPECTIVE")
print(result["alumni_opinion"])

print("\n" + "=" * 70)
print("FINAL COMMITTEE DECISION")
print("=" * 70)

print(result["final_decision"])
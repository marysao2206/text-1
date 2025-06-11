students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]
maxscore=students[0]["score"]
topstudents=""
for students in students:
    if students["score"] < maxscore:
        maxscore=students["score"]
        topstudents=students['name']
print('top students is :',topstudents)
    
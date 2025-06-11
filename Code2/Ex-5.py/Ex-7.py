students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]
total=0  
for students in students:
    total+=students["score"]
    print(total/len(students))
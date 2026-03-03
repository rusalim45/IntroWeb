numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()

print(numbers)

print(numbers[:3])
print(numbers[-2])
print(numbers[::-1])

student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
student.pop("age")

print(student.keys())
print(student.values())
print(student.items())

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print(union_set)
print(intersection_set)
print(difference_set)

colors = ("red", "blue", "green", "red", "yellow")
print(colors.index("green"))
print(colors.count("red"))

company = {
    "employees": [
        {"name": "Alice", "position": "Developer", "salary": 50000},
        {"name": "Bob", "position": "Designer", "salary": 45000},
    ]
}

company["employees"].append({"name": "Charlie", "position":"Manager","salary":60000})

for employee in company["employees"]:
    print(employee["name"])

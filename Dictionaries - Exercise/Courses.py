courses = {}

while True:
    line = input()
    data = line.split(" : ")
    if line == "end":
        break

    course_name = data[0]
    student_name = data[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for key, val in courses.items():
    print(f"{key}: {len(val)}")
    for i in val:
        print(f"-- {i}")

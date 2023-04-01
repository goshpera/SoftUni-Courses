num = int(input())
my_dict = {}

for i in range(num):
    student_name = input()
    grade = float(input())

    if student_name not in my_dict:
        my_dict[student_name] = []
    my_dict[student_name].append(grade)

for key, val in my_dict.items():
    avrg_grade = sum(val) / len(val)
    if avrg_grade >= 4.50:
        print(f"{key} -> {avrg_grade:.2f}")

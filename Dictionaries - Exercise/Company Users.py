company = {}

while True:
    line = input()
    data = line.split(" -> ")
    if line == "End":
        break

    company_name = data[0]
    employee = data[1]

    if company_name not in company:
        company[company_name] = []
    if employee not in company[company_name]:
        company[company_name].append(employee)

for key, val in company.items():
    print(f"{key}")
    for i in val:
        print(f"-- {i}")

import re

pattern = r"(?P<day>\d{2})([\./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
text = input()

dates = re.finditer(pattern, text)
for date in dates:
    date_data = date.groupdict()
    print(f"Day: {date_data['day']}, Month: {date_data['month']}, Year: {date_data['year']}")


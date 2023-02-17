from datetime import date
first_date = date(2023, 2, 15)
last_date = date(2023, 5, 18)
result = last_date - first_date
print(result.days)
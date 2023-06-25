
# Challenge-Your life in weeks

age = int(input("Enter your age:"))
age_limit = int(input("To what age you think you'll gonna live: "))
years_left = age_limit - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
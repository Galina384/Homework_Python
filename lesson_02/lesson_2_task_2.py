def is_year_leap(year):
    return year % 4 == 0


year = 1993
result = is_year_leap(year)
print(f"год {year}: {result}")

year = 2004
result = is_year_leap(year)
print(f"год {year}: {result}")

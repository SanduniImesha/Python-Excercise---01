seasons = ("winter", "spring", "summer", "autumn")
# index 0 = winter (Dec, Jan, Feb), 1 = spring (Mar, Apr, May),
# 2 = summer (Jun, Jul, Aug), 3 = autumn (Sep, Oct, Nov)

month = int(input("Enter a month number (1-12): "))

season_index = (month % 12) // 3
season = seasons[season_index]

print(f"Month {month} is in {season}.")
kwh = int(input("Enter the number of kWh used: "))

if kwh <= 1000:
    total_cents = kwh * 7.633
else:
    first_tier = 1000 * 7.633
    remaining_kwh = kwh - 1000
    second_tier = remaining_kwh * 9.259
    total_cents = first_tier + second_tier

total_dollars = total_cents / 100

print("Total amount owed: $" + str(round(total_dollars, 2)))
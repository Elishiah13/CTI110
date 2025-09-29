# Elishiah Reed
# 9/28/2025
# HW- P1HW2
# Program that calculates and displays expenses

print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")
print("-----------------------------------")
print(f"Remaining Balance: {remaining_balance}")
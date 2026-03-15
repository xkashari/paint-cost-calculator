# Paint Cost Calculator

square_feet = float(input("Enter square footage: "))
coverage_per_gallon = 350
paint_price = float(input("Enter price per gallon of paint: "))

gallons_needed = square_feet / coverage_per_gallon
total_cost = gallons_needed * paint_price

print("Gallons of paint needed:", round(gallons_needed, 2))
print("Estimated paint cost: $", round(total_cost, 2))

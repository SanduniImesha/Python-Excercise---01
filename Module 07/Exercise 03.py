def gallons_to_liters(gallons):
	
	"""Converts American gallons to liters."""
	return gallons * 3.78541


# main program
gallons = float(input("Enter volume in gallons (negative number to stop): "))

while gallons >= 0:
	liters = gallons_to_liters(gallons)
	print(f"{gallons} gallons = {liters:.2f} liters")
	gallons = float(input("Enter volume in gallons (negative number to stop): "))

print("Done.")

p =int(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
t = int(input("Enter time in years: "))
emi = (p * r * (1 + r) ** t) / ((1 + r) ** t - 1)
i = emi-p
print("The principle amount is:", p)
print( "Intrest to be paid is:", int (i))
print("The EMI is:", int(emi))
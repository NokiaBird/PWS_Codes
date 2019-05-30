print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms) / 1.60934
# round(thing to round, how many decimal points)
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}mi ")

# ask for age
print("How old are you?")
age = input()
if age:
    age = int(age)
    # 18-21 wristband
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")

    # 21+ drink, normal entry
    elif age >= 21:
        print("You are good to enter and can drink!")
    # too young, sorry
    else:
        print("You can't come in, little one :(")
else:
    print("Please enter an age!")

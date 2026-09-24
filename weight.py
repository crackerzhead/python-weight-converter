# Python weight converter

weight_input = input("Enter your weight: ")

# check if the input is a number
if weight_input.isdigit():
    weight = float(weight_input)
    unit = input("Kilogram or Pounds? (K / L): ").upper()

    if unit == "K":
        weight = weight * 2.20462
        print(f"Your weight is: {round(weight, 1)} Lbs.")

    elif unit == "L":
        weight = weight / 2.20462
        print(f"Your weight is: {round(weight, 1)} Kg.")

    else:
        print(f"{unit} was not valid")

else:
    print(f"{weight_input} was not valid")
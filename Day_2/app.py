print("🧮Welcome to the tip calculator ")

totalBill = float(input("What was the total bill?\n$"))
tipPercentage = int(
    input("What percentage tip would you like to give? (10, 12 or 15)\n"))
peopleNumber = int(input("How many people to split the bill?\n"))

totalPerPerson = round((totalBill * (1+tipPercentage/100)) / peopleNumber, 2)
formatedTotalPerPerson = "{:.2f}".format(totalPerPerson)

print(f"Each people should pay: ${formatedTotalPerPerson}")

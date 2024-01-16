# Prints the values to a stream, or to sys.stdout by default
print("🐍 Hello Python World🐍\n")
print("Welcome to the Band Name Generator\n")

# Read a string from standard input
cityName = input("What's name of the city you grew up in? ")
petName = input("What's your pet's name? ")

# Get string length
nameLength = len(cityName)

# Concatenate everything and convert int to string using str(nameLength)
bandName = cityName + petName + str(nameLength)
print("\n\nYour band name could be " + bandName + " 🎶🎶🎶!")

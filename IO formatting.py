
def main():

    outputFile = open("Presidents.txt","w")

    outputFile.write("George Washington")
    for i in range(0,6):
        outputFile.write(f"{i}")
    outputFile.close()
main()

inputFile = open("Presidents.txt","r")
print(inputFile.read(6))
inputFile.close()

#--------------------------------------------------------------------
from random import randint
def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w")
    for i in range(10):
        outputFile.write(str(randint(0, 9)) + " ")
    outputFile.close()  # Close the file

    # Open file for reading data
    inputFile = open("Numbers.txt", "r")
    s = inputFile.read()  # Read all data to s
    numbers = [float(x) for x in s.split()]
    for number in numbers:
        print(number, end=" ")
    inputFile.close()  # Close the file

main()  # Call the main function

#--------------------------------------------------------------------

def main():
    filename = input("Enter a filename: ").strip()
    inputFile = open(filename, "r")  # Open the file

    counts = 26 * [0]  # Create and initialize counts
    for line in inputFile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i])
                  + (" time" if counts[i] == 1 else " times"))

    inputFile.close()  # Close file

# Count each letter in the string
def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():  # Test if ch is a letter
            counts[ord(ch) - ord('a')] += 1

main()  # Call the main function

#--------------------------------------------------------------------------------------------------
#Write a function load_inventory(filename) that:
    #Opens the CSV file
    #Reads it line by line
    #Strips whitespace (strip())
    #Splits each line into product_name, quantity, unit_cost
    #Stores the data in a dictionary:

def load_inventory(filename):
    inventory = {}
    inventaris = open(filename, "r")
    line = inventaris.readline()

    for line in inventaris:
        line = line.strip()  # removes the whitespaces
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 3:
            continue

        product_name = parts[0]
        quantity = int(parts[1])
        cost_per_unit = float(parts[2])

        if product_name not in inventory:
            inventory[product_name] = []

        inventory[product_name] = [quantity, cost_per_unit]
    inventaris.close()


def print_inventory(inventory):
    """
    Prints the inventory in a readable format:

    Product: Widget
      Batch: 50 units at 2.5 €/unit
      Batch: 30 units at 2.2 €/unit
    """
    for product_name, batches in inventory.items():
        print(f"Product: {product_name}")
        for quantity, cost_per_unit in batches:
            print(f"  Batch: {quantity} units at {cost_per_unit} €/unit")
        print()  # blank line between products

def save_inventory(filename, inventory):
    """
    Saves the inventory dictionary back to CSV format:

    product_name,quantity,cost_per_unit
    """
    f = open(filename, "w")

    lines = []
    for product_name, batches in inventory.items():
        for quantity, cost_per_unit in batches:
            lines.append(f"{product_name},{quantity},{cost_per_unit}")

    # join with newline and write once
    content = "\n".join(lines)
    f.write(content)

    f.close()






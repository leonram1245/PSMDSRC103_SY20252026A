# Write a program that repeatedly prompts the user to enter a number.

# If the user enters a line that starts with #, skip that line (don’t process or print it) using continue.

# If the user enters "done", stop using break.

# For every valid numeric entry, keep track of the count, total, minimum, and maximum (do not use min() or max(); use loop patterns/“so far” variables).

# After the loop ends, print:

# Count: <count>
# Total: <total>
# Min: <min>
# Max: <max>
def find_max(numbers):
    if len(numbers) == 0:
        return "NO NUMBERS FOUND"
    elif len(numbers) == 1:
        return numbers[0]
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number

def find_min(numbers):
    if len(numbers) == 0:
        return "NO NUMBERS FOUND"
    elif len(numbers) == 1:
        return numbers[0]
    min_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
    return min_number

def find_total(numbers):
    total = 0
    if len(numbers) == 0:
        return "NO NUMBERS FOUND"
    for num in numbers:
        total+=num
    return total

def find_count(numbers):
    count = 0
    if len(numbers) == 0:
        return "NO NUMBERS FOUND"
    for i in range(len(numbers)+1):
        count = i
    return count


inputs = []
while True:
    line = input("Enter your numbers: ")
    if not line:
        continue
    elif line[0] == "#   ":
        print(line[0])
        continue
    elif line.lower()!="done":
        try:
            inputs.append(float(line))
        except ValueError:
            print("only numbers are allowed!")
    else:
        max_num = find_max(inputs)
        min_num = find_min(inputs)
        total_num = find_total(inputs)
        count_num = find_count(inputs)
        print("Count: ",count_num)
        print("Total: ",total_num)
        print("Min: ", min_num)
        print("Max: ",max_num)
        break

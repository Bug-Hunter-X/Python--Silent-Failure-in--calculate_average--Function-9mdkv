def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle case where list contains no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
data = []
average = calculate_average(data)
print(f"Average: {average}")
data = [10, 20, 30, 0]
average = calculate_average(data)
print(f"Average: {average}")
data = [10, 20, 'a']
average = calculate_average(data)
print(f"Average: {average}") #This will now give 0
data = [10,20,'a',30,40]
average = calculate_average(data)
print(f"Average: {average}") #This will also give 0
data = [10,20,30,40]
average = calculate_average(data)
print(f"Average: {average}") #This will give a valid result
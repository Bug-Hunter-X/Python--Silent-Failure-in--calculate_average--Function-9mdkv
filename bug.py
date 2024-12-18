def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage that could lead to an error
data = []
average = calculate_average(data)
print(f"Average: {average}") #This will give 0, even if it should raise an exception
data = [10, 20, 30, 0]
average = calculate_average(data) #This will give a valid result
print(f"Average: {average}")
data = [10, 20, 'a']
average = calculate_average(data) #This will raise TypeError
print(f"Average: {average}")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

combined_data = zip(names, ages)

# Convert the zip object to a list for demonstration
list_of_tuples = list(combined_data)
print(list_of_tuples)
print(type(list_of_tuples[0][0]))
print((list_of_tuples[1][0]))
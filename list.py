# Create an empty list called my_list.
my_list = []


# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append([10, 20, 30, 40])
print(my_list)



# Insert 15 at the second position (index 1)
my_list = [10,20,30,40]
my_list.insert(1, 15)


# Display the updated list
print(my_list)

# # Extend my_list with another list: [50, 60, 70].
my_list = [10,20,30,40]
# extend with another list
my_list.extend([50,60,70])
print(my_list)


# # Remove the last element from my_list.
my_list = [10,20,30,40]
# Remove the last element
my_list.pop()
print(my_list)


# Sort my_list in ascending order.
my_list = [10,20,30,40]
my_list.sort()
print(my_list)


# Find and print the index of the value 30 in my_list.
my_list = [10, 20, 30, 40]

# Find the index of the value 30
index = my_list.index(30)

# Print the index
print(index)  
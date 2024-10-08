# Loops and lists
#! Loops in Python (Data Science)
import random

# Looping through a range with a for loop
print("For Loop with range:")
for i in range(1, 6):  # range(1, 6) means 1 to 5
    print(f"Iteration {i}")

# List of fruits
fruits = [
    "apple",
    "blueberry",
    "cantaloupe",
    "cherry",
    "grape",
    "kiwi",
    "mango",
    "orange",
    "peach",
    "pear",
    "plum",
    "pineapple",
    "raspberry",
    "strawberry",
    "tangerine",
]

print("\nFor Loop through a list:")
for fruit in fruits:
    if len(fruit) == 5:
        print(f"Found 5-letter fruit: {fruit}")
    else:
        print(f"Fruit: {fruit}")

# Looping through a string (character by character)
word = "Python"
print("\nFor Loop through a string:")
for letter in word:
    print(f"Letter: {letter}")

# Using a while loop
print("\nWhile Loop Example:")
counter = 5
while counter > 0:
    print(f"Counter is at: {counter}")
    counter -= 1  # Decrement the counter

# Using break in a loop
print("\nUsing break in a loop:")
for i in range(10):
    if i == 5:
        print(f"Breaking the loop at {i}")
        break  # Exits the loop when i equals 5
    print(i)

# Using continue in a loop
print("\nUsing continue in a loop:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(f"Odd number: {i}")

# Nested for loops
print("\nNested For Loop Example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Looping through a dictionary
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("\nFor Loop through a dictionary:")
for student, grade in student_grades.items():
    print(f"{student} scored {grade}")

# Looping with else
print("\nLoop with else clause:")
for i in range(1, 6):
    print(i)
else:
    print("Loop completed!")

# Infinite loop with a break condition
print("\nWhile Loop with break:")
i = 1
while True:
    print(f"Iteration {i}")
    i += 1
    if i > 5:  # Break the infinite loop after 5 iterations
        break

# Looping with enumerate to get index and value
print("\nFor Loop using enumerate:")
colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(f"Color at index {index}: {color}")

# Using zip to loop through two lists simultaneously
print("\nLooping through two lists with zip:")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# squaring an iterator in range and doing other operations on num
for num in range(1, 11):
    print(num, num**2, num**3, num**4, num**5)


# condition for modulus for even and odds and math operations on int object in a list
for number in range(1, 11):
    if number % 2 == 0:
        print(number**2)
    else:
        print(number**3)


#! fruits list to be operated on using loops and other methods!
fruits = [
    "apple",
    "blueberry",
    "cantaloupe",
    "cherry",
    "grape",
    "kiwi",
    "mango",
    "orange",
    "peach",
    "pear",
    "plum",
    "pineapple",
    "raspberry",
    "strawberry",
    "tangerine",
]

print("How many items in fruits: ", len(fruits))
#! other methods and operations on list object named 'fruits' with 'string' instances
# 1. Accessing elements
print("First fruit:", fruits[0])  # Access the first item
print("Last fruit:", fruits[-1])  # Access the last item

# 2. Slicing the list
print("First 3 fruits:", fruits[:3])  # Get the first 3 fruits
print("Fruits from index 3 to 6:", fruits[3:7])  # Fruits from index 3 to 6
print("Every second fruit:", fruits[::2])  # Get every second fruit

# 3. Modifying the list
fruits[1] = "blackberry"  # Change 'blueberry' to 'blackberry'
print("After modification:", fruits)

# 4. Appending to the list
fruits.append("watermelon")  # Add an item to the end of the list
print("After appending:", fruits)

# 5. Inserting into the list
fruits.insert(2, "avocado")  # Insert 'avocado' at index 2
print("After inserting:", fruits)

# 6. Removing from the list
fruits.remove("cherry")  # Remove 'cherry' from the list
print("After removing 'cherry':", fruits)

# 7. Popping an element (removes and returns the last element by default)
popped_fruit = fruits.pop()  # Removes the last item ('watermelon')
print("After popping:", fruits)
print("Popped fruit:", popped_fruit)

# Popping from a specific index
popped_fruit_at_index = fruits.pop(2)  # Removes the fruit at index 2 ('avocado')
print("After popping index 2:", fruits)
print("Popped fruit at index 2:", popped_fruit_at_index)

# 8. Checking if an item exists in the list
if "mango" in fruits:
    print("Mango is in the list.")
else:
    print("Mango is not in the list.")

# 9. Finding the index of an item
index_of_pear = fruits.index("pear")
print("Index of 'pear':", index_of_pear)

# 10. Counting occurrences of an item
fruit_count = fruits.count("apple")
print("Count of 'apple':", fruit_count)

# 11. Sorting the list
sorted_fruits = sorted(fruits)  # Temporarily sorted list
print("Temporarily sorted:", sorted_fruits)

fruits.sort()  # Permanently sort the list in place
print("Permanently sorted:", fruits)

# 12. Reversing the list
fruits.reverse()  # Reverses the list in place
print("Reversed list:", fruits)

# 13. List comprehension (create a new list with some transformation)
uppercased_fruits = [
    fruit.upper() for fruit in fruits
]  # Convert all fruits to uppercase
print("Uppercased fruits:", uppercased_fruits)

# 14. Looping through the list
print("Looping through the list:")
for fruit in fruits:
    print(fruit)

# 15. Copying the list
fruits_copy = fruits.copy()  # Shallow copy of the list
print("Copied list:", fruits_copy)

# 16. Clearing the list
fruits.clear()  # Remove all items from the list
print("Cleared list:", fruits)

#! appending to treats an empty list
treats = []

for fruit in fruits:
    if "berry" in fruit:
        treats.append(fruit + " jam")
    elif fruit[0] == "p":
        treats.append(fruit + " popsicle")
    elif len(fruit) <= 5:
        treats.append(fruit + " jelly")
    else:
        treats.append(fruit + " jellybean")

print("The new list of treats are:")
for treat in treats:
    print(treat)

#! import the random for random global module
import random

#! using the zip global method through an array using the function!
students = [
    "Amy",
    "Ben",
    "Cal",
    "Dan",
    "Eli",
    "Fay",
    "Guo",
    "Hal",
    "Ida",
    "Jed",
    "Ken",
    "Les",
    "Moe",
]


def generate_sat_score():
    return random.randint(40, 80) * 10


math_scores = [generate_sat_score() for _ in students]
verbal_scores = [generate_sat_score() for _ in students]

for student, math, verbal in zip(students, math_scores, verbal_scores):
    print(f"{student}: Math: {math}, Verbal: {verbal}")

#! Lottery powerball NYC 1-292 million chance of winning
import random

player = ["Nuraly"]


def generate_full_powerball_ticket():
    main_numbers = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)
    return main_numbers, powerball


ticket = [generate_full_powerball_ticket() for _ in player]

for player, (main_numbers, powerball) in zip(player, ticket):
    print(f"{player}: Main Numbers: {main_numbers}, Powerball: {powerball}")

#! Creating a dictionary and important methods and operations in a dictionary
student_grades = {"Amy": 90, "Ben": 85, "Cal": 92}

# Accessing a value using its key
print(student_grades["Amy"])  # Output: 90

# Adding a new key-value pair
student_grades["Dan"] = 88

# Updating an existing key's value
student_grades["Ben"] = 89
print(student_grades)  # Output: {'Amy': 90, 'Ben': 89, 'Cal': 92, 'Dan': 88}

# Removing an entry using 'del'
del student_grades["Cal"]

# Removing an entry using 'pop()'
removed_value = student_grades.pop("Ben")
print(student_grades)  # Output: {'Amy': 90, 'Dan': 88}
print(removed_value)  # Output: 89

# Checking if a key exists
if "Amy" in student_grades:
    print("Amy's grade is recorded.")  # Output: Amy's grade is recorded

# Iterating through dictionary keys
for student in student_grades:
    print(student)  # Output: Amy, Dan

# Iterating through dictionary values
for grade in student_grades.values():
    print(grade)  # Output: 90, 88

# Iterating through dictionary keys and values
for student, grade in student_grades.items():
    print(f"{student}: {grade}")  # Output: Amy: 90, Dan: 88

# Using 'get()' method to avoid KeyError
print(student_grades.get("Eli", "No grade"))  # Output: No grade

# Display dictionary keys
print(student_grades.keys())  # Output: dict_keys(['Amy', 'Dan'])

# Display dictionary values
print(student_grades.values())  # Output: dict_values([90, 88])

# Display dictionary key-value pairs
print(student_grades.items())  # Output: dict_items([('Amy', 90), ('Dan', 88)])

# Merging another dictionary with 'update()'
new_grades = {"Ben": 82, "Cal": 91}
student_grades.update(new_grades)
print(student_grades)  # Output: {'Amy': 90, 'Dan': 88, 'Ben': 82, 'Cal': 91}

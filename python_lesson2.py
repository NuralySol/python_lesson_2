#! Conditional logic if and else boolean logic

my_int = input("Enter an integer :")

if int(my_int) % 2 == 0:
    print(my_int + " is even")
else:
    print(" is odd")


#! Conditional logic operators

first_name = input("First name: ")
last_name = input("Last name: ")
score = 90

#! f-string is always the answer
print(f"{first_name} {last_name} {score}")


#! Function to validate and process the score
def validate_score(score):
    try:
        # Try converting the input to a float
        user_score = float(score)

        # Check if the score is within the valid range of 1 to 100 (before int conversion)
        if 1 <= user_score <= 100:
            # Convert the float to an integer (intify it)
            user_score = int(user_score)

            # Check if the intified score passes or fails
            if user_score >= 65:
                print(f"Congrats you passed with a score of {user_score}.")
            else:
                print(f"You failed. Your score is {user_score}.")
        else:
            print("Error: Score must be between 1 and 100.")

    except ValueError:
        # Handle the case where the input is not a valid number (float or int)
        print("Error: Invalid input. Please enter a number between 1 and 100.")


# Get user input
user_score = input("Please input a score: ")

# Call the function to validate the input and print the result
validate_score(user_score)


#! veggie method on an immutable (string). lower method (refractor).
def check_veggie(veggie):
    #! Ensures the input contains only alphabetic characters strings only no other data types
    if not veggie.isalpha():
        print("Error: Please enter a valid vegetable name (letters only).")
        return

    # Convert the input to lowercase
    veggie = veggie.lower()

    # Check if the vegetable starts with 'c'
    if veggie[0] == "c":
        print(f"{veggie} starts with the letter 'c'.")
    else:
        print(f"{veggie} starts with the letter '{veggie[0]}' instead.")

    # Check if the vegetable ends with 't'
    if veggie.endswith("t"):
        print(f"{veggie} ends with the letter 't'.")
    else:
        print(f"{veggie} does not end with 't'. It ends with '{veggie[-1]}'.")


# call the function .strip method to remove whitespaces in a 'string' does not change the string
veggie_input = input("Enter a vegetable: ").strip()
check_veggie(veggie_input)


#! more boolean logic 'in' : 'not in' (boolean operators) True and False (case-insensitive)
#! fruits list they are like arrays in JavaScript language

fruits = ["apple", "banana", "mango", "pear"]

# Convert all elements in the list to lowercase for case-insensitive comparison
fruits = [fruit.lower() for fruit in fruits]

# Using 'in' to check if an item exists in the list (case-insensitive)
if "apple".lower() in fruits:
    print("apple is in the list of fruits.")
else:
    print("apple is not in the list of fruits.")

# Using 'not in' to check if an item does not exist in the list (case-insensitive)
if "orange".lower() not in fruits:
    print("orange is not in the list of fruits.")
else:
    print("orange is in the list of fruits.")

# Example with a long string stored in 'sentence' variable with .lower() method
sentence = "The quick brown fox jumps over the lazy dog".lower()

# Using 'in' with a string to check if a word is present (case-insensitive)
if "fox".lower() in sentence:
    print("The word 'fox' is in the sentence.")
else:
    print("The word 'fox' is not in the sentence.")

# Using 'not in' with a string to check if a word is absent (case-insensitive)
if "cat".lower() not in sentence:
    print("The word 'cat' is not in the sentence.")
else:
    print("The word 'cat' is in the sentence.")


#! vowel or consonant checker and validator for user input function.
def check_vowels_and_consonants(word):
    # Define vowels
    vowels = "aeiouAEIOU"

    # Get the length of the word
    word_length = len(word)

    # Loop through each character in the word to see
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                print(f"'{char}' is a vowel.")
            else:
                print(f"'{char}' is a consonant.")
        else:
            print(f"'{char}' is not a letter.")

    # Print the length of the word
    print(f"The word '{word}' has {word_length} characters.")


# Prompt the user for input
user_word = input("Enter a word: ").strip()

# Call the function to check for vowels and consonants
check_vowels_and_consonants(user_word)


#! Garden collector farmer collecting his stock

garden = ["parsley", "cilantro", "beet", "carrot", "cabbage", "cauliflower", "celery", "chard", "chicory",
    "collard greens", "corn", "cucumber", "chickpea", "cassava", "cress", "chives", "broccoli",
    "spinach", "lettuce", "tomato", "eggplant", "bell pepper", "pumpkin", "radish", "peas", "green beans",
    "okra", "onion", "garlic", "leek", "potato", "sweet potato", "yam", "turnip", "rutabaga",
    "parsnip", "beetroot", "zucchini", "kale", "arugula", "endive", "radicchio", "bok choy",
    "brussels sprouts", "fennel", "kohlrabi", "artichoke"]

print("Origiional list in the garden: ",len(garden))

# Basket for veggies
basket = []

# Prompt the user to enter a veggie and use the .strip() .lower() methods on user input
veggie_input = input("Please add a veggie to the basket: ").strip().lower()

# functions are always better in this type of operations 
def veggie_in_garden(veggie):
    # Check if the input is a valid veggie in the garden
    if veggie in garden:
        if veggie not in basket:  # Ensure it is not already in the basket
            basket.append(veggie)
            print(f"{veggie.capitalize()} has been added to your basket!")
        else:
            print(f"{veggie.capitalize()} is already in your basket.")
    else:
        print(f"Invalid input: {veggie.capitalize()} is not in the garden. Please try again.")

# Call the function to check and add the veggie
veggie_in_garden(veggie_input)

# Display the current basket contents that are added to an empty list and also the len of the basket
print(f"Your basket contains:{basket} number of items in a basket list -> {len(basket)}")

#! Prompt user for their test score el if exercise input is a 'string' .strip() the whitespaces
score = input("Enter your test score (0-100): ").strip()

# Check if the input is a valid integer and in the correct range (intify it)
if score.isdigit():
    score = int(score)

    # Determine the grade using if, elif, and else bounded score
    if 90 <= score <= 100:
        print(f"Your score is {score}, and your grade is A.")
    elif 80 <= score < 90:
        print(f"Your score is {score}, and your grade is B.")
    elif 70 <= score < 80:
        print(f"Your score is {score}, and your grade is C.")
    elif 60 <= score < 70:
        print(f"Your score is {score}, and your grade is D.")
    elif 0 <= score < 60:
        print(f"Your score is {score}, and your grade is F.")
    else:
        print("Error: Please enter a score between 0 and 100.")
else:
    print("Invalid input: Please enter a valid integer between 0 and 100.")
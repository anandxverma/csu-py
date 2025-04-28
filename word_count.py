# Default words list and counts
words_list = [ "hello", "world", "hello", "world", "hello", "world" ]
words_count = { "hello": 3, "world": 3 }

# Function to increase the word count
def increment_count(word):
    # Find if the word exists in the word count list,
    # then increment the count
    # else create a new entry with 1
    count = words_count[word] + 1 if word in words_count else 1
    words_count[word] = count

# Function to decrease the word count
def decrease_count(word):
    # Find the word in the list get its count
    count = words_count[word] if word in words_count else 0
    # If the word is found and has only 1 count then
    # Remove the word from the word_count list
    # Else reduce the count by 1
    if count == 1:
        del words_count[word]
    elif count == 0:
        pass
    else:
        words_count[word] = count - 1

# Decorator function to be called
# everytime a word is added or removed from the list
def update_count(func):
    def wrapper(*args):
        if func.__name__ == "add_word":
            increment_count(args[0])
        else:
            decrease_count(args[0])
        return func(*args)
    return wrapper

# Add a new word to the list
@update_count
def add_word(w):
    words_list.append(w)

# Remove a word from the list
@update_count
def remove_word(w):
    if w in words_list:
        words_list.remove(w)
    else:
        pass

# Print the current words list and their counts
print("\nCurrent list:", words_list)
print("Current count:", words_count, "\n")

# Add or remove word fromn the list
word_action = int(input("Enter 1 to add new word, 2 to remove a word, 0 to exit: "))
while word_action != 0:
    if word_action == 1:
        add_word(input("\nEnter a new word to be added: ").lower().strip())
    elif word_action == 2:
        remove_word(input("\nEnter a word to be removed: ").lower().strip())
    else:
        print("Invalid action, pleasse choose a valid option.\n")

    # Print the updated words list
    print("\nUpdated list:", words_list)
    print("Updated count:", words_count, "\n")
    word_action = int(input("Enter 1 to add new word, 2 to remove a word, 0 to exit: "))    

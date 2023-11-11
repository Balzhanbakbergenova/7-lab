#1
def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'text1.txt'


display_file_content(file_path)






#2
import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                print("Random Line:", random_line.strip())
            else:
                print(f"The file '{file_path}' is empty.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'your_file.txt'


read_random_line(file_path)






#3
def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print(f"Number of Uppercase Characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.txt' with the actual path to your text file
file_path = 'your_file.txt'

# Call the function to count uppercase characters in the file
count_uppercase_characters(file_path)








#4
def count_lines_not_starting_with_D(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.strip().startswith('D'))
            print("Output:", count)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'your_file.txt'


count_lines_not_starting_with_D(file_path)






#5
def count_words_ending_with_F(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            count = sum(1 for word in words if word.strip('.,?!').lower().endswith('f'))
            print("Number of Words Ending with 'F':", count)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'your_file.txt'


count_words_ending_with_F(file_path)






#6
def count_all_and_none_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()

            count_all = sum(1 for word in words if word.lower() == 'all')
            count_none = sum(1 for word in words if word.lower() == 'none')

            print(f"Occurrences of 'all': {count_all}")
            print(f"Occurrences of 'none': {count_none}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



file_path = 'your_file.txt'


count_all_and_none_words(file_path)






#7
def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()

            word_frequency = {}
            for word in words:

                cleaned_word = word.strip('.,?!').lower()
                word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1

            print("Word Frequency:")
            for word, frequency in word_frequency.items():
                print(f"{word}: {frequency}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



file_path = 'your_file.txt'


count_word_frequency(file_path)






#8
def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()

            longest_word = max(words, key=len)

            print("Longest Word:", longest_word)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



file_path = 'your_file.txt'


find_longest_word(file_path)





#9
def replace_characters_in_file(file_path, from_char, to_char):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            corrected_content = content.replace(from_char, to_char)
            print("Corrected Version:")
            print(corrected_content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'your_file.txt'
from_character = 'B'
to_character = 'J'


replace_characters_in_file(file_path, from_character, to_character)






#10
def count_occurrences_of_A_and_B(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            count_A = content.lower().count('a')
            count_B = content.lower().count('b')

            print(f"Occurrences of A: {count_A}, B: {count_B}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



file_path = 'your_file.txt'


count_occurrences_of_A_and_B(file_path)


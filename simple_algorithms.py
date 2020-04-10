'''
simple_algorithms.py

This program contains functions for various simple algorithms used as practice.

'''

'''
vowel_counter(s)

Returns the number of vowels in a given string s.

Parameters:
s (string): lowercase string without spaces

Returns:
int: number of vowels
'''


def vowel_counter(s):
    # Count the number of vowels (a, e, i, o, u) in the string, count
    count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in s:
        if char in vowels:
            count += 1

    return count


'''
sometimes_y(s)

Implements the 'sometimes y' rule on given string s.

Parameters:
s (string): The target number to generate primes up to.

Returns:
boolean: True/False depending on whether the string has y
int: number of vowels in the string originally (wihout sometimes y rule)
int: number of vowels in the string after sometimes y rule
'''


def sometimes_y(s):
    # Check if the letter y is present in string s, y_in_string
    y_in_string = False

    if 'y' in s:
        y_in_string = True

    # Use vowel_counter to give the number of vowels without y, original_count
    original_count = vowel_counter(s)

    # If the last letter is y, increase original_count by 1, new_count
    new_count = 0

    if s[-1] == 'y':
        new_count = original_count + 1

    else:
        new_count = original_count

    return y_in_string, original_count, new_count


'''
sentence_counter(sentence)

Returns a list of the number of vowels in each word in a sentence.

Parameters:
sentence (string): A string of a sentence.

Returns:
list: a list of the number of vowels for each word in the sentence.
'''


def sentence_counter(sentence):
    # Remove special characters from the sentence
    sp_char = ['.', ',', '!', '?']

    for i in sp_char:
        sentence = sentence.replace(i, '')

    # Make the words lowercase and split them into a list, word_list
    word_list = sentence.lower().split()

    # Use sometime_y to count the number of vowels in each word, counts
    counts = []

    for word in word_list:
        counts.append(sometimes_y(word)[2])

    return counts


'''
Returns an an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''


def recursive_fib(n):
    # If n is 0 or 1, return the corresponding base case in fib_list, fib_n
    if n <= 1:
        fib_n = n

    # If n is greater than 1, do the calculations and return the nth number
    else:
        fib_n = recursive_fib(n - 2) + recursive_fib(n - 1)

    return fib_n


'''
iterative_fib(n)

Returns an an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''


def iterative_fib(n):
    # Define the base cases, F_0 F_1
    F_0, F_1 = 0, 1

    # Iterate the calculation n times
    for i in range(n):
        F_0, F_1 = F_1, (F_0 + F_1)

    # The nth value is the final F_0 value, fib_n
    fib_n = F_0

    return fib_n


'''
selection_sort(integers)

Returns a sorted list of integers.

Parameters:
integers (int): List of integers you want to sort.

Returns:
list: A list of sorted integers.
'''


def selection_sort(integers):
    # Find the length of the list, length
    length = len(integers)

    # Iterate through the list elements
    for i in range(length):
        # The first element checked becomes the current minimum value, minimum
        minimum = i

        # Check all elements to the right for a smaller value, new_val
        for new_val in range(i + 1, length):
            # If a smaller element is found, it becomes the new minimum
            if integers[minimum] > integers[new_val]:
                minimum = new_val

        # Switch the first element checked with the current minimum
        integers[i], integers[minimum] = integers[minimum], integers[i]

    # The integers list is now sorted, sorted_integers
    sorted_integers = integers

    return sorted_integers


'''
bubble_sort(integers)

Returns a sorted list of integers.

Parameters:
integers (int): List of integers you want to sort.

Returns:
list: A list of sorted integers.
'''


def bubble_sort(integers):
    # Find the length of the list, length
    length = len(integers)

    # Iterate through the list elements
    for i in range(length):
        # Check each element against the following element
        for j in range(0, length - i - 1):
            # Check if an element is larger than the next element
            if integers[j] > integers[j + 1]:
                # If so, switch the elements
                integers[j], integers[j + 1] = integers[j + 1], integers[j]

    # The integers list is now sorted, sorted_integers
    sorted_integers = integers

    return sorted_integers


'''
synonym_checker(synonyms, sentences)

Returns whether two sentences are synonyms or not, given a list of synonyms.

Parameters:
synonyms (list): A list of tuples of the synonyms you should store.
sentences (tuple): A 2-tuple containing two sentences you want to compare.

Returns:
boolean: Whether the sentences are synonyms or not.
'''


def synonym_checker(synonyms, sentences):
    # Create a dictionary from synonyms, syn_dict
    syn_dict = dict(synonyms)

    # Create a list to hold the sentence lists, sentence_list
    sentence_list = []

    # Remove punctuation from the sentences
    sp_char = ['.', ',', '!', '?']

    for sentence in sentences:
        for i in sp_char:
            sentence = sentence.replace(i, '')

        # Make all letters lowercase and split the sentences into lists
        sentence_list.append(sentence.lower().split())

    # Compare each word of the sentences for either the same word or synonyms
    is_synonym = True

    # Check each word of the first sentence, first_word
    for first_word in sentence_list[0]:
        # Keep checking as long as the sentences might be synonyms
        if is_synonym:
            # Find the location of word in the first sentence, word_index
            word_index = sentence_list[0].index(first_word)

            # Find the corresponding word in the second sentence, second_word
            second_word = sentence_list[1][word_index]

            # If the words of the sentences do not match, check syn_dict
            if second_word != first_word:
                # If the first word is in syn_dict and the words are synonyms,
                # then the sentences could be synonyms
                if first_word in syn_dict:
                    if syn_dict[first_word] == second_word:
                        is_synonym = True
                    else:
                        is_synonym = False

                # If the second word is in syn_dict and the words are synonyms,
                # then the sentences could be synonyms
                elif second_word in syn_dict:
                    if syn_dict[second_word] == first_word:
                        is_synonym = True
                    else:
                        is_synonym = False

                # If the words do not match and neither word is in syn_dict,
                # then the sentences are not synonyms
                else:
                    is_synonym = False

    return is_synonym


# TEST CASES
if __name__ == '__main__':
    print("---------------------------------------")
    print("Vowel Counting")
    print("---------------------------------------")
    vowel_tests = [['abcdef', 'abcdefy', 'abc def y'], ['cat', 'catty', 'The big cat.'], ['dog', 'ydog', 'I love dogs!']]
    vowel_answers = [[2, (True, 2, 3), [1, 1, 1]], [1, (True, 1, 2), [1, 1, 1]], [1, (True, 1, 1), [1, 2, 1]]]
    for count, test in enumerate(vowel_tests):
        if(vowel_answers[count][0] == vowel_counter(test[0]) and
        vowel_answers[count][1] == sometimes_y(test[1]) and
        vowel_answers[count][2] == sentence_counter(test[2])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Vowel Count (Correct): ", vowel_answers[count][0])
        print("Vowel Count (Your Answer): ", vowel_counter(test[0]))
        print("Vowel Count with y (Correct): ", vowel_answers[count][1])
        print("Vowel Count with y (Your Answer): ", sometimes_y(test[1]))
        print("Sentence Count (Correct): ", vowel_answers[count][2])
        print("Sentence Count (Your Answer): ", sentence_counter(test[2]))

    print("---------------------------------------")
    print("Fibonacci")
    print("---------------------------------------")
    tests = [[1, 1], [4, 4], [10, 10]]
    answers = [[1, 1], [3, 3], [55, 55]]
    for count, test in enumerate(tests):
        if(answers[count][0] == recursive_fib(test[0]) and
            answers[count][1] == iterative_fib(test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Recursive Fibonacci (Correct): ", answers[count][0])
        print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
        print("Iterative Fibonacci (Correct): ", answers[count][1])
        print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))

    print("---------------------------------------")
    print("Sorting")
    print("---------------------------------------")
    tests = [[-5, 4, 2, 1], [0, 2, -4, 3], [1, 3, 2]]
    answers = [[-5, 1, 2, 4], [-4, 0, 2, 3], [1, 2, 3]]
    for count, test in enumerate(tests):
        if(answers[count] == selection_sort(test) and
            answers[count] == bubble_sort(test)):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Sorted List (Correct): ", answers[count])
        print("Selection Sort (Your Answer): ", selection_sort(test))
        print("Bubble Sort (Your Answer): ", bubble_sort(test))

    print("---------------------------------------")
    print("Synonym Checker")
    print("---------------------------------------")
    tests = [
        [[("movie", "film"), ("reviews", "ratings")], ("I heard that movie got good ratings.", "I heard that film got good reviews.")], 
        [[("movie", "film")], ("I heard that movie got good ratings.", "I heard that film got good reviews.")], 
        [[("movie", "film"), ("reviews", "ratings")], ("I heard that work of cinema got good ratings.", "I heard that film got good reviews.")]
    ]
    answers = [True, False, False]
    for count, test in enumerate(tests):
        if(answers[count] == synonym_checker(test[0], test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Synonyms:", test[0])
        print("Sentences:", test[1])
        print("Synonym? (Correct): ", answers[count])
        print("Synonym? (Your Answer): ", synonym_checker(test[0], test[1]))

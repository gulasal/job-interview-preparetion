# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def isPalindrome():
    x = input("Enter the word: ")
    list_of_words = x.lower().split(" ")
    first_word = list_of_words[0]
    isTrue = first_word == first_word[::-1]
    return isTrue

print(isPalindrome()) 
 




 
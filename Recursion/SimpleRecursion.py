#This is a file that goes through a few simple Recursive examples.

def printArrayElements(array):
    if len(array) == 0:
        return
    print(array[0])
    printArrayElements(array[1:])

def isPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return True and isPalindrome(string[1:-1])
    return False

print(isPalindrome("abcba"))

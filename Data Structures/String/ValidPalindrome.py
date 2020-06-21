#Valid Palindrome
#LC 125
"""
125. Valid Palindrome
Easy

1160

2844

Add to List

Share
Given a string, determine if it is a palindrome,
 considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

#returns alphanumeric, lowercase, version of string
def makeAlnum(s):
    alnum = "".join(c for c in s if c.isalnum())
    return alnum.lower()
def palindrome(s):
    if not s or len(s) == 1 :
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    return False

#RT: #subproblems * size subprolems +work at each call _> O(n)*n == O(n^2)
#SC: O(n) for each recursive call

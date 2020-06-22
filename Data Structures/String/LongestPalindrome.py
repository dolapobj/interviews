#Longest Palindromic Substring
#LC 5
"""
5. Longest Palindromic Substring
Medium

6744

530

Add to List

Share
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
#realize there are 2n-1 possible places for a palindrome to be centered at
#in a string of length n (2n-1) because even and odd!
#at each center, we can try stepping out to the left and right and checking continue
#until its no longer a palindrome!

def longestPalindrome(s):
    longest = ""
    for i in range(len(s)):
        odd = palindrome(s,i,i)
        even = palindrome(s,i,i+1)
        longest = max(longest,even,odd,key = len)
    return longest

def palindrome(s,l,r):
    while l>=0 and r < len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]

#RT: O(n^2) --> check each center (O(n)) and checking if palindrome is O(n) as well!
#SC: O(n) --> we store the longest palindromic string!

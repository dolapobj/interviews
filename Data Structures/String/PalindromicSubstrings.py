#Palindromic Substrings
#LC 647
"""
Given a string, your task is to count how
many palindromic substrings in this string.

The substrings with different start indexes or end indexes are
counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
#similiarly to longestPalindrome, we expand around the center and count the number
#of valid palindromes from among the 2N-1 possible centers.

def countPalindromes(s):
    count = 0
    for i in range(len(s)):
        odd = palindromicSubstrings(s,i,i)
        even = palindromicSubstrings(s,i,i+1)
        count  = count+ odd + even
    return count
def palindromicSubstrings(s,left,right):
    count = 0
    while left >=0 and right < len(s) and s[left] ==s[right]:
        count +=1
        left -=1
        right+=1
    return count

#RT: O(n^2) --> O(n) to traverse all centers, O(n) to check all palindromes for each center
#SC: O(1) --> only use a counter for space!

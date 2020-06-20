#Valid Anagram
#LC 242
"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

from collections import defaultdict

def validAnagram(s,t):
    if len(s) != len(t):
        return False
    sFreq = defaultdict(int)
    tFreq = defaultdict(int)
    for i in range(len(s)):
        sFreq[s[i]] +=1
        tFreq[t[i]] +=1
    return tFreq == sFreq


#RT: O(n) --> Iterate through s once.
#SC: O(n) --> store frequency of each char in each string

#Note --> can also sort! 

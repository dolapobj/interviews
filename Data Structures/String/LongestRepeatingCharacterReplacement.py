#Longest Repeating Character Replacement
#LC 424

"""
Given a string s that consists of only uppercase English
letters, you can perform at most k operations on that string.

In one operation, you can choose any character of
the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing
all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
from collections import defaultdict
#idea: sliding window again, move j until we have no more operations left (hit k non-repeating chars)
#then, move i to index of first non repeating character
def long(s,k):
    charDict = defaultdict(int)
    repeated, start,end = 0,0,0
    maxLength = 0
    while end < len(s):
        charDict[s[end]] +=1
        currentCount = charDict[s[end]]
        #keep track of count of most frequent repeating char in current window
        repeated = max(repeated,currentCount)
        #if my window size - repeated characters is > k --> this means we have used too many ops
        while end-start-repeated + 1 >k:
            charDict[s[start]] -=1
            start+=1
        #check length against size of window!
        maxLength = max(maxLength,end-start+1)
        end+=1

    return maxLength

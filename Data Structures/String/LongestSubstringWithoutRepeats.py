#Longest Substring Without Repeating Characters
#LC 3
"""
Given a string, find the length of the longest substring without
repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring,
             "pwke" is a subsequence and not a substring.
"""
#sliding window approach
def longest(string):
    count,i,j = 0,0,0
    seen = set()
    while i < len(string) and j < len(string):
        if string[j] not in seen:
            seen.add(string[j])
            #add one here because we are moving j forward by 1!
            count = max(count,j-i+1)
            j+=1
        else:
            set.remove(string[i])
            i+=1
    return count

#RT: O(n) --> each element visited at most twice (by both i and j)
#SC: O(n) --> use of a hashset to store elements

# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        convertedList = s.split(" ")
        result = []
        for word in convertedList:
            result.append(word[::-1])
        
        return " ".join( map(str, result) )
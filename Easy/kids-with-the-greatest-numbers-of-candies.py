# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        isGreatestcandies = []
        length = len(candies)
        maxCandy = max(candies)
        for i in range(length):
            if candies[i] + extraCandies >= maxCandy:
                isGreatestcandies.append(True)
            else:
                isGreatestcandies.append(False)
        
        return isGreatestcandies
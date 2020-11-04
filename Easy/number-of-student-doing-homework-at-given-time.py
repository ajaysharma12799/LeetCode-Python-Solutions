# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        length = len(startTime)
        count = 0
        for i in range(length):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
        return count
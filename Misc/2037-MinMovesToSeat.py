class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # sort both lists to align the nearest students to seats
        seats.sort()
        students.sort()
        
        res = 0
        # calculate the total moves by summing up the absolute differences
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        
        return res
        
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # if the total number of flowers is less than required bouquets times flowers per bouquet, return -1
        if len(bloomDay) < m * k:
            return -1

        # helper function to determine if we can make `m` bouquets by `day` days
        def canMake(day):
            bonquets, flowers = 0, 0  # initialize bouquets and flower counter

            # iterate through each bloom day
            for bloom in bloomDay:
                if bloom <= day:  # if the flower blooms by the given day
                    flowers += 1  # increment flower count
                    if flowers == k:  # if we have enough flowers for one bouquet
                        bonquets += 1  # increment bouquet count
                        flowers = 0  # reset flower count for the next bouquet
                else:
                    flowers = 0  # reset flower count if the current flower hasn't bloomed
                if bonquets >= m:  # if we have made enough bouquets
                    return True  # return True as it is possible to make the required bouquets
            return False  # return False if unable to make enough bouquets
        
        # initialize the binary search range
        low, high = min(bloomDay), max(bloomDay)

        # perform binary search
        while low < high:
            mid = (low + high) // 2  # calculate the midpoint of the current range
            if canMake(mid):  # check if it's possible to make `m` bouquets by `mid` days
                high = mid  # if possible, try for fewer days by setting high to mid
            else:
                low = mid + 1  # if not possible, increase the days by setting low to mid + 1
        
        return low  # the minimum number of days required to make `m` bouquets
        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # an empty list to store surviving asteroids
        res = []
        # iterate through each asteroid in the given list
        for a in asteroids:
            # check for potential collision conditions
            while res and a < 0 and res[-1] > 0:
                # calculate the difference in sizes of colliding asteroids
                diff = a + res[-1]
                # if the current asteroid is smaller and will be destroyed
                if diff < 0:
                    res.pop()
                # if the current asteroid is larger and will destroy the previous one
                elif diff > 0:
                    a = 0
                # if both asteroids annihilate each other
                else:
                    a = 0
                    res.pop()
            # if the current asteroid survives the collision conditions
            if a:
                res.append(a)
        # return the list of surviving asteroids after all collisions
        return res

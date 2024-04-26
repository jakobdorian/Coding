class Solution:
    def numTilings(self, n: int) -> int:
        # define a constant MOD for modulo operations
        MOD = 10**9 + 7

        # caching lists for even and odd cases
        hasEvenCache = [False] * (n+1)
        evenCache = [None] * (n + 1)

        hasOddCache = [False] * (n+1)
        oddCache = [None] * (n + 1)

        # function to calculate the number of tilings for even cases
        def even(N):
            if N == 0:
                return 1

            # check if the value is already cached
            if hasEvenCache[N]:
                return evenCache[N]

            # calculate the number of tilings recursively
            count = 0
            count += even(N-1)
            if N - 2 >= 0:
                count += even(N-2)
                count += 2 * odd(N-2)

            # cache the calculated value for future use
            hasEvenCache[N] = True
            evenCache[N] = count % MOD
            return evenCache[N]

        # function to calculate the number of tilings for odd cases
        def odd(N):
            if N == 0:
                return 0

            # check if the value is already cached
            if hasOddCache[N]:
                return oddCache[N]
            
            # calculate the number of tilings recursively
            count = 0
            count += even(N-1)
            count += odd(N-1)

            # cache the calculated value for future use
            hasOddCache[N] = True
            oddCache[N] = count % MOD
            return oddCache[N]

        # return the number of tilings for the given n, modulo MOD
        return even(n) % MOD

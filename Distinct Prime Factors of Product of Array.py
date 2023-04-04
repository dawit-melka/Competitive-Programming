class Solution:
    def primes(self, n):
        if n <= 2: 
            return []
        isPrime = [True] * (n)
        isPrime[0] = isPrime[1] = False
        div = 2

        while div * div < n:
            if isPrime[div]:
                j = div * div
                while j < n:
                    isPrime[j] = False
                    j += div
            
            div += 1
        
        primes = []

        for i in range(n):
            if isPrime[i]:
                primes.append(i)

        return primes

    def distinctPrimeFactors(self, nums: List[int]) -> int:

        primes = self.primes(max(nums)+1)
        count = 0
        for prime in primes:
            for num in nums:
                if num % prime == 0:
                    count += 1
                    break

        return count

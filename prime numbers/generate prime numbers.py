class Solution:
    def primes(self, left, right):
      n = right
      if right < 2:
        return []

      isPrime = [True]*n
      isPrime[0], isPrime[1] = False, False
      div = 2

      while div * div < n:
        if isPrime[div]:
          j = div * div
          while j < n:
            isPrime[j] = False
            j += div
        div += 1
      
      primes = []

      for i in range(left, right):
        if isPrime[i]:
          primes.append(i)

      return primes
      
    def closestPrimes(self, left: int, right: int) -> List[int]:
      primes = self.primes(left, right+1)
      result = [-1,-1]
      currDiff = float("inf")

      for i in range(1, len(primes)):
        if primes[i] - primes[i-1] < currDiff:
          currDiff = primes[i] - primes[i-1]
          result = [primes[i-1], primes[i]]

      return result
      
      

        

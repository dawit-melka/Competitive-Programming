class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfers = [0]*n
        result = 0
        
        def backtrack(index, acceptedRequests):
            nonlocal result
            if index == len(requests):
                if transfers.count(0) == len(transfers):
                    result = max(result, acceptedRequests)
                return
            
            backtrack(index + 1, acceptedRequests)
            
            out_, in_ = requests[index]
            transfers[out_] -= 1
            transfers[in_] += 1

            backtrack(index + 1, acceptedRequests + 1)

            transfers[out_] += 1
            transfers[in_] -= 1
        
        backtrack(0, 0)

        return result

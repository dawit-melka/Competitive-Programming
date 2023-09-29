class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left = 0
        right = len(products)-1
        result = []
        for i in range(len(searchWord)):
            curr = []
            while left <= right and (i >= len(products[left]) or products[left][i] != searchWord[i]):
                left += 1
            
            while right >= left and (i >= len(products[right]) or products[right][i] != searchWord[i]):
                right -= 1
            
            for j in range(left, min(left+3, right+1)):
                curr.append(products[j])
            
            result.append(curr)

        return result

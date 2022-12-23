class Solution:
    def average(self, salary: List[int]) -> float:
        max_val = max(salary[0], salary[1])
        min_val = min(salary[0], salary[1])
        avg = 0
        sum = 0

        for i in range(2,len(salary)):
            if salary[i] > max_val:
                sum += max_val
                max_val = salary[i]
            elif salary[i] < min_val:
                sum += min_val
                min_val = salary[i]
            else:
                sum += salary[i]
            
            avg = sum/(i-1)
        
        return avg
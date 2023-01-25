class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count_boats = 0
        left, right = 0, len(people) - 1
        people.sort()
        while left <= right:
            weight_sum = people[left] + people[right] 
            if weight_sum <= limit:
                left += 1
            right -= 1
            count_boats += 1
        
        return count_boats

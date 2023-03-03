class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort()
        
        for i in range(len(pair)):
            d, s = pair[i]
            pair[i] = (target - d) / s
        
        stack = []
        for time in pair:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        
        return len(stack)

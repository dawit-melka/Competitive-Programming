class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(1,2,1)])
        visited = set([(1,2)])

        while queue:
            p, s, steps = queue.popleft()
            if p == target:
                return steps
            # Accelerate
            p1, s1 = p+s, s*2
            # Reverse
            p2, s2 = p, (-1 if s > 0 else 1)
            if (p1, s1) not in visited and p1 > 0:
                visited.add((p1, s1))
                queue.append((p1, s1, steps+1))
            if (p2, s2) not in visited and p2 > 0:
                visited.add((p2, s2))
                queue.append((p2, s2, steps+1))

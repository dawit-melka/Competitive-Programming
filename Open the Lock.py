class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        map_ = {
                "0":["1","9"],
                "1":["2","0"],
                "2":["3","1"],
                "3":["4","2"],
                "4":["5","3"],
                "5":["6","4"],
                "6":["7","5"],
                "7":["8","6"],
                "8":["9","7"],
                "9":["0","8"]
                                }

        start = ["0", "0", "0", "0"]
        visited = set()
        visited.add("".join(start))
        queue = deque([[start, 0]])

        while queue:
            curr, turns = queue.popleft()
            if "".join(curr) == target:
                return turns
            
            for i in range(4):
                curr_digit = curr[i]
                curr[i] = map_[curr_digit][0]
                if "".join(curr) not in visited and "".join(curr) not in deadends:
                    visited.add("".join(curr))
                    queue.append([curr.copy(), turns+1])
                curr[i] = map_[curr_digit][1]
                if "".join(curr) not in visited and "".join(curr) not in deadends:
                    visited.add("".join(curr))
                    queue.append([curr.copy(), turns+1])
                curr[i] = curr_digit

        return -1 

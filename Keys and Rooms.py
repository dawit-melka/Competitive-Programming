class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = [False] * len(rooms)
        visited_rooms[0] = True
        queue = deque([0])

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                if not visited_rooms[key]:
                    visited_rooms[key] = True
                    queue.append(key) 
        
        return not(False in visited_rooms)

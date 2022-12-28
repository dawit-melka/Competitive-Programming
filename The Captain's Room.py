K = int(input())
room_numbers = list(map(int, input().split()))
family_room = set()
captain_room = set()

for r in room_numbers:
    if r in captain_room:
        captain_room.remove(r)
        family_room.add(r)
    if r not in family_room:
        captain_room.add(r)
    
print(next(iter(captain_room)))

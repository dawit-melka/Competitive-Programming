import sys
input = sys.stdin.readline
            

def main():
    t = int(input())
    
    for _ in range(t):
        planets_num, cost = map(int, input().split())
        planet_orbits = list(map(int,input().split()))
        
        count_same_orbit_planets = {}
        
        for orbit in planet_orbits:
            if orbit in count_same_orbit_planets:
                count_same_orbit_planets[orbit] += 1
            else:
                count_same_orbit_planets[orbit] = 1
                
        min_cost = 0     
        for planets in count_same_orbit_planets.values():
            min_cost += min(planets, cost)
        
        print(min_cost)
        
if __name__ == "__main__":
    main()

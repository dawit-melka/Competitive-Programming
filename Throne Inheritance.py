class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.adj_list = defaultdict(list)
        self.adj_list[kingName] = []
        self.isDead = set()        

    def birth(self, parentName: str, childName: str) -> None:
        self.adj_list[parentName].append(childName)

    def death(self, name: str) -> None:
        self.isDead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(person):
            if not person: 
                return
            if person not in self.isDead:
                result.append(person)
            for child in self.adj_list[person]:
                dfs(child)

        dfs(self.kingName)

        return result
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

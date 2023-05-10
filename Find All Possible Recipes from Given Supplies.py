class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = Counter()
        complete_recipes = []
        recipes_set = set(recipes)
        queue = deque(supplies)


        for i in range(len(recipes)):
            for pre in ingredients[i]:
                graph[pre].append(recipes[i])
            indegree[recipes[i]] = len(ingredients[i])
        

        while queue:
            curr_recipe = queue.popleft()
            if curr_recipe in recipes_set:
                complete_recipes.append(curr_recipe)
            
            for ngh in graph[curr_recipe]:
                indegree[ngh] -= 1
                if indegree[ngh] == 0:
                    queue.append(ngh)
        
        return complete_recipes

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReq = defaultdict(list)
        allPreReq = defaultdict(set)
        indegree = [0] * numCourses
        toDo = deque()
        result = []

        for pre, course in prerequisites:
            preReq[pre].append(course)
            allPreReq[course].add(pre)
            indegree[course] += 1
        
        for i in range(numCourses):
            if not indegree[i]:
                toDo.append(i)
            
        while toDo:
            curr_course = toDo.popleft()
            for course in preReq[curr_course]:
                indegree[course] -= 1
                allPreReq[course].update(allPreReq[curr_course])
                if not indegree[course]:
                    toDo.append(course)
        
        for pre, course in queries:
            result.append(pre in allPreReq[course])
        
        return result

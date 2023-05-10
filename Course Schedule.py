class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        totake = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                totake.append(i)
        
        course_taken = 0
        while totake:
            curr = totake.popleft()
            course_taken += 1
            for course in graph[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    totake.append(course)
        
        return numCourses == course_taken


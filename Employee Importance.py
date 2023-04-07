"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_id = {}
        for employee in employees:
            employees_id[employee.id] = employee

        def dfs(employee):
            if not employee:
                return 0
            curr_count = 0
            for sub_id in employee.subordinates:
                curr_count += dfs(employees_id[sub_id])

            return curr_count + employee.importance

        for employee in employees:
            if employee.id == id:
                return dfs(employee)

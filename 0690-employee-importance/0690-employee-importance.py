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
        d=dict()
        
        for employee in employees:
            d[employee.id]=employee
            
        ans=0
        
        q=[id]
        
        while q:
            now=q.pop()
            ans+=d[now].importance
            
            for next in d[now].subordinates:
                q.append(d[next].id)
        
        return ans
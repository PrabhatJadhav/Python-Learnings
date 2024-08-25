class Employee:
    def __init__(self,full_name,salary,department,on_probation):
        self.full_name=full_name
        self.salary=salary
        self.department=department
        self.on_probation=on_probation
        
    def is_on_probation(self):
        return self.on_probation
        
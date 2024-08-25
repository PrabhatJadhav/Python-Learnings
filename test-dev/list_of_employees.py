import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.employee import Employee

employee1 = Employee('Prabhat','35,000','IT',False)
employee2 = Employee('Prabhat','35,000','IT',True)

# print(employee1.on_probation)

print(employee2.is_on_probation())
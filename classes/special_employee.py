import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.employee import Employee

class SpecialEmployee(Employee):  
    def is_on_probation():
        return False
          
    def is_special_employee():
        return True
        
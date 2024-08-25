import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils.generate_rand_numbers as numbers_generator


# print(numbers_generator.__name__)
print(numbers_generator.a_random_number(100))

# import test_module as test_module

# print(test_module.__name__)


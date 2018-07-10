import Functions_test_Module
area = Functions_test_Module.calcu_sqr_area(5)
print(area)

import Functions_test_Module as f
area = f.calcu_sqr_area(2)
print(area)

#If module you want to import is not in the same dir ,
# use
import sys

sys.path.append("c:\Code") #path
import Functions_test_Module as f
area = f.calcu_triangle_area(5)
print(area)

#installing Module
import matplotlib

import error: module not found

pip install matplotlib

This will install module successfully.
"""
Encapsulate a function call and act as a proxy for methods that are called on the result of that function.
The function is not evaluated until one of the methods on the result is called.
"""
import cProfile
from django.utils.functional import lazy


upper = str.upper
cProfile.run('''for i in range(500000): upper('hello') + ""''', sort='cumtime')

lazy_upper = lazy(upper, str)
cProfile.run('''for i in range(500000): lazy_upper('hello') + ""''', sort='cumtime')
from functools import wraps
from django.db import connection, reset_queries
from timeit import timeit

def only_print_info(repeat_time=1, print_queries=False): # 데코선언, 데코 인자 받고
    def tags_decorator(func): # 위에 함수 받고
        @wraps(func) # 원하는 함수 에다가 wraps
        def func_wrapper(**kw): # 함수 전후로 할거 정하고
            reset_queries()
            result = timeit(func, number=repeat_time)
            q = connection.queries
            print(f"{func.__name__} function refeat time is {repeat_time}")
            print(f"number of queries = {len(q)}")
            if print_queries == True:
                print(f"First Query is = {q[0]} \n ==========================================" )
                print(f"First Query is = {q[-1]} \n ==========================================" )
                print(f"Take Time: {result}")
            return result
        return func_wrapper
    return tags_decorator



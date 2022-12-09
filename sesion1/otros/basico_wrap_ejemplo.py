from functools import lru_cache, wraps

from datetime import datetime, timedelta


def main_func():
    
    def wrapper_cache(func):
        #print(func.__ne__)
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """Documentos de wrapper"""
            print(func)
            return func(*args, **kwargs)
        return wrapped_func
    return wrapper_cache

y=main_func()

z=y(sum([1,2]))

print('>',z,'>>',z.__name__,z.__doc__)
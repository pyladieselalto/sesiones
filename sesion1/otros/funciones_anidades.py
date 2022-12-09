from functools import lru_cache, wraps
from datetime import datetime, timedelta

def mostrar_datos(cadena:str ,maxsize: int =128):
    def mostrar_nombre(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(cadena=cadena)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args,**kwargs):
            if datetime.utcnow()>=func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            
            return func(*args, **kwargs)
        return wrapped_func
    return mostrar_nombre
mostrar_datos()
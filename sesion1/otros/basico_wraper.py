
from functools import wraps
def mi_decorador(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        """Wrapper"""
        original_func(*args,**kwargs)
        print("Usando wrapers !")
    return wrapper

@mi_decorador
def suma_de_dos(num:int):
    """Ingresa un numero y le suma 2"""
    num = num+2
    print(f'Suma, {num}!')

@mi_decorador
def suma_de_tres(num:int):
    """Ingresa un numero y le suma 3"""
    num = num + 3
    print(f'{num}')
print(suma_de_tres(8))
print(suma_de_dos(4))

# conocer sus atributos

print("SUMAS ...")
print(suma_de_tres.__name__,suma_de_tres.__doc__)
print(suma_de_dos.__name__, suma_de_dos.__doc__)

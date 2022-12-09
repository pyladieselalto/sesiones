def steps_to(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2# 2 | 1 1 = dos posibilidades
    elif stair == 3:
        return 4
    else:
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )
print(steps_to(17))

# contando el tiempo
from timeit import repeat
setup_code= "from __main__ import steps_to"
stmt = "steps_to(17)"
times = repeat(stmt=stmt, setup=setup_code, repeat=3 ,number=10)
print(times)
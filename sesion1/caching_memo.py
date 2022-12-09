from functools import lru_cache

@lru_cache
def steps_to_con_cacheo(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return (
            steps_to_con_cacheo(stair - 3)
            + steps_to_con_cacheo(stair - 2)
            + steps_to_con_cacheo(stair - 1)
        )


def steps_to_sin_cacheo(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return (
            steps_to_sin_cacheo(stair - 3)
            + steps_to_sin_cacheo(stair - 2)
            + steps_to_sin_cacheo(stair - 1)
        )
print(steps_to_sin_cacheo(17))

# contando el tiempo
import time

start_time_con_cache= time.time()
print(steps_to_con_cacheo(17))
stop_time_con_cache= time.time()
time_con_cache=stop_time_con_cache - start_time_con_cache

start_time_sin_cache= time.time()
print(steps_to_sin_cacheo(17))
stop_time_sin_cache= time.time()
time_sin_cache=stop_time_sin_cache - start_time_sin_cache

print(f"tiempo con cacheo {time_con_cache} , tiempo sin cache {time_sin_cache}")
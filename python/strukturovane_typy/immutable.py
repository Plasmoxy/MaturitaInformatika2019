from typing import TypeVar, Callable
from copy import deepcopy
T = TypeVar("T")

def produce(s: T, block: Callable[[T], None]) -> T:
    cp: T = deepcopy(s)
    block(cp)
    return cp

j = [1, 2, [3, 4]]
print(produce(j, lambda x: x.append(3)))

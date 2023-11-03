import timeit
import matplotlib.pyplot as plt

def PIterative(Base, Exo):
    R = 1
    for _ in range(Exo):
        R *= Base
    return R

def PowerAndDivideC(Base, Exo):
    if Exo == 0:
        return 1
    if Exo % 2 == 0:
        H = PowerAndDivideC(Base, Exo // 2)
        return H * H
    else:
        H = PowerAndDivideC(Base, (Exo - 1) // 2)
        return Base * H * H

V = list(range(1, 225))
Count = []  
DivideCount = [] 

for n in V:
    base = 2

    IterativeTime = timeit.timeit(lambda: PIterative(base, n), number=150)
    Count.append(IterativeTime)

    DivideConquerTime = timeit.timeit(lambda: PowerAndDivideC(base, n), number=150)
    DivideCount.append(DivideConquerTime)

plt.plot(V, Count, label="Iterative")
plt.plot(V, DivideCount, label="Divide_and_Conquer")
plt.xlabel('N')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()

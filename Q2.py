import timeit
import matplotlib.pyplot as plt
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

def PairsWithSum(S, TARGET):
    merge_sort(S)  
    pairs = binary_search(S, TARGET)  
    return pairs

S = [14, 3, 22, 10, 15, 6, 17, 8, 9]
T = 25 
pairs = PairsWithSum(S, T)
print("Pairs ", T, "are:", pairs)


def MeasureExecution(n):
    S = [random.randint(1, 1000) for _ in range(n)]  
    T = random.randint(1, 2000)  
    time = timeit.Timer(lambda: PairsWithSum(S, T))
    execution_time = time.timeit(number=1)  
    return execution_time

Size = [100, 300, 500, 700, 900, 1200]
ExNum = []

for V in Size:
    time = MeasureExecution(V)
    ExNum.append(time)

plt.plot(Size, ExNum, marker='o')
plt.xlabel('Input Size n')
plt.grid(True)
plt.show()

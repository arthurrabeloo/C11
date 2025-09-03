import numpy as np

arr1 = np.ones(8, dtype = int)
arr2 = np.random.randint(0, 10, size = 8)
arr3 = arr1 + arr2

soma = np.sum(arr3)
print("Soma dos elementos:", soma)

if soma >= 40:
    arr3_reshaped = arr3.reshape(4, 2)
else:
    arr3_reshaped = arr3.reshape(2, 4)

print("Array remodelado:\n", arr3_reshaped)

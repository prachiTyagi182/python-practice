
import copy

original = [1, 2, [3, 4]]

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

shallow_copy[2][0] = 100

print(original)
print(shallow_copy)

deep_copy[2][0] = 500

print(original)
print(deep_copy)
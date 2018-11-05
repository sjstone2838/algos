
"""
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
"""

# Returns index of x in arr if present, else -1 
def binary_search(x, arr, left, right):
	mid = (left + right) // 2 # Floor division
	print mid

	if arr[mid] == x:
		return mid
	elif left == right:
		return -1
	elif x < arr[mid]:
		return binary_search(x, arr, left, mid - 1)	
	else:
		return binary_search(x, arr, mid + 1, right)

assert(binary_search(0, range(0, 10), 0, 9) == 0)
assert(binary_search(5, range(0, 10), 0, 9) == 5)
assert(binary_search(51, range(0, 10), 0, 9) == -1)
assert(binary_search(5, range(0, 10)[::2], 0, 9) == -1)


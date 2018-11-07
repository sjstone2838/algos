"""
range(n) --> range from 0 to n-1
range(n, m, -1) --> reverse ordered range from n to m, where n > m
"""

"""	
Bubble Sort
Check the first 2 items in the array. If they are not sorted, swap them. Move on to the next index. 
Repeat until you've progressed throughout the array without making any swaps.
Once the largest value is part of a pair, it will continually be moved along until the pass is complete
So the total number of required passes is n - 1

Run-time: O(n^2)
Memory: O(1)
"""

def bubble_sort(arr):
	l = len(arr)

	for j in range(len(arr) - 1, 0 , -1):
		for i in range(j):
			if not arr[i] <= arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
			print j, i
			print arr
	return arr


a = [1, 5, 2, 4, 10, 3, 6, 6]
b = range(0, 10)
c = [1, 2, 3]


assert(bubble_sort(a) == [1, 2, 3, 4, 5, 6, 6, 10])
assert(bubble_sort(b) == range(0, 10))
assert(bubble_sort(c) == [1, 2, 3])




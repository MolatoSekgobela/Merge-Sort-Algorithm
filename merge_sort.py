
def merge_sort(list):
	"""

	Implement a merge sort algorithm ( Divide and Conquer Method )

	sort a list a list in ascending order and return a new sorted list

	divide : find midpoint and divide list into sublists
	conquer: recursively sort the sublists
	combine: combine the sublists into 1 list

	"""

	if len(list) <= 1:
		return list


	left_half,right_half = split(list)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left,right)

def split(list):

	"""
	Divide unsorted list at midpoint
	
	return two sublists

	"""

	midpoint =len(list)//2
	left = list[:midpoint]
	right = list[midpoint:]

	return left,right
	
def merge(left,right):
	"""

	this function merges two lists while sorting them
	returns a new merged list

	"""
	list = []
	i = 0 # indexes of right list
	n = 0 # indexes of left list

	while i < len(left) and n < len(right):
		if left[i] < right[n]:
			list.append(left[i])
			i += 1
		else:
			list.append(right[n])
			n += 1
	while i < len(left):
		list.append(left[i])
		i +=1

	while n < len(right):
		list.append(right[n])
		n +=1
	return list

def verify_sorted_list(list):

	"""
	verify sorting 
	"""
	n = len(list)

	if n == 0 or n == 1:
		return True

	return list[0] < list[1] and verify_sorted_list(list[1:])# recursive function call to check if list is sorted, starting in pos 1 to the end

alist = [40,45,78,1,7,26,89,17,4,33]
unsorted_list = [5,6,7,3,7,1,2]



# merge while sorting array

result = merge_sort(alist)

print(verify_sorted_list(unsorted_list))# use verify_sort function to check if list sorted or not (unsorted_list return False)

print(verify_sorted_list(result)) # use verify_sort function to check if list sorted or not (sorted_list returns True)

# print sorted list
print(result)



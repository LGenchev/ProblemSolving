import numpy as np
# help(np.array)


def solution(A):
	left_err_ix=None
	right_err_ix=None
	seen_conflict=False
	temp=0
	for i in range(1,len(A)):
		if (A[i]<A[i-1]):
			if not(seen_conflict):
				seen_conflict=True
				left_err_ix=i-1
			right_err_ix=i
	if left_err_ix!=None:
		temp=A[left_err_ix]
		A[left_err_ix]=A[right_err_ix]
		A[right_err_ix]=temp
		print(A)
		return isSorted(A)
	else:
		print(A)
		return True


def isSorted(A):
	for i in range(0,len(A)-1):
		if A[i+1]<A[i]:
			return False
	return True


if __name__=="__main__":
	S=[1,5,3,3,2,7]
	# print(solution(S))
	# print(isSorted([1,2,3,4,2,5]))
	print(solution([1,2,3,4,3]))





def cntIndexesToMakeBalance(arr, n):
	if (n == 1):
		return 1
	if (n == 2):
		return 0
	sumEven = 0
	sumOdd = 0
	for i in range(n):
		if (i % 2 == 0):
			sumEven += arr[i]
		else:
			sumOdd += arr[i]
	currOdd = 0
	currEven = arr[0]
	res = 0
	newEvenSum = 0
	newOddSum = 0
	for i in range(1, n - 1):
		if (i % 2):
			currOdd += arr[i]
			newEvenSum = (currEven + sumOdd -currOdd)
			newOddSum = (currOdd + sumEven -currEven - arr[i])
		else:
			currEven += arr[i]
			newOddSum = (currOdd + sumEven -
						currEven)
			newEvenSum = (currEven + sumOdd -currOdd - arr[i])
		if (newEvenSum == newOddSum):
			res += 1
	if (sumOdd == sumEven - arr[0]):
		res += 1
	if (n % 2 == 1):
		if (sumOdd == sumEven - arr[n - 1]):
			res += 1
	else:
		if (sumEven == sumOdd - arr[n - 1]):
			res += 1
	return res
arr = [5,5,2,5,8 ]
n = len(arr)	
print(cntIndexesToMakeBalance(arr, n))
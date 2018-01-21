
# Two-Sum problem Solution

'''
The two sum problem is a common interview question, and it is a variation of the subset sum problem.
There is a popular dynamic programming solution for the subset sum problem, but for the two
sum problem we can actually write an algorithm that runs in O(n) time. 

What is the brute force solution?

Naive solution

A naive approach to this problem would be to loop through each number and then loop again through
the array looking for a pair that sums to S. The running time for the below solution would be O(n^2)
because in the worst case we are looping through the array twice to find a pair. 




What is the optimal solution?

Faster solution

We can write a faster algorithm that will find pairs that sum to S in linear time. The algorithm
below makes use of hash tables which have a constant lookup time. As we pass through each element in
the array, we check to see if S minus the current element exists in the hash table. We only need to
loop through the array once, resulting in a running time of O(n) since each lookup and insertion in
a hash table is O(1).
'''

def twoSum(theArr, theSum):

    pairNumsSum = []
    numHashTable = {}

    for num in theArr:

            sumMinusNum = theSum - num

            if (sumMinusNum in numHashTable):
                pairNumsSum.append([num,sumMinusNum])

            numHashTable[num] = num

    return pairNumsSum

def main():
    print(twoSum([3,5,2,-4,8,11], 7))

    
main()

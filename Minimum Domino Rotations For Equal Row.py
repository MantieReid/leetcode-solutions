class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    for x in [A[0], B[0]]: # X becomes the first number in A or in B
      if all(x in d for d in zip(A, B)): # if X is in both lists...then...
       # print("X is " + str(x)), print("\n length of A list is   ", len(A), "\n Number of times x occurs in A is "  + str( A.count(x)))
        #print("\n Number of times X occurs in B is " + str(B.count(x)))
        return len(A) - max(A.count(x), B.count(x))  #Subtract the length of a from  the highest number of times X occurs in A or in B. 
    return -1

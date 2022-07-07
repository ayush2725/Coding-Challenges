import math

class Solution(object):
    
    
    def nCr(self, n,r):
        
        f = math.factorial
        
        return f(n) // f(r) // f(n-r)
    
    def numTrees(self, n):
        
        num = self.nCr(2*n, n)
        
        return num // (n+1)

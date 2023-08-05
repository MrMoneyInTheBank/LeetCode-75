"""
Given two integers a and b, return the sum of the two integers without using 
the operators + and -.
"""

class Solution:
    def add(self, a: int, b: int):
        if not a or not b:
            return a or b 
        return self.add(a^b, (a&b) << 1)

    def getSum(self, a: int, b: int) -> int:

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if self.add(~a, 1) == b:  # -a == b
                return 0
            if self.add(~a, 1) < b:  # -a < b
                return self.add(~self.add(self.add(~a, 1), self.add(~b, 1)), 1) 

        return self.add(a, b)
    
# Time | Space : O(n) | O(n) 


# Python is a really bad choice for this problem. This is because integers are not represented as 32 bits. 
# A language like C++, or Go is much better. However, the logic is the same. Addition of bits can be done with 
# exlcusive OR (1+1 should be 0, 1+0 == 0+1 should be 1, and 0+0 should be 0). We get all the same results with 
# exclusive OR. Now, we can get what we need to carry by using logical AND since we only carry if both bits are one. 
# However, when we carry, we add it to the left of the current bit position therefore we need to AND and then shift left
# We keep doing this until we have nothing left to carry.


"""
Here is the described code in Go

func getSum(a int, b int) int {
    for b != 0 {
        temp := (a & b) << 1
        a = a ^ b
        b = temp 
    }
    return a 
}

Here is the described code in C++

class Solution {
public:
    int getSum(int a, int b){
        while (b != 0){
            int carry = a & b;
            a = a ^ b;
            b = (unsigned)carry << 1;
        }
        return a;
    }
}

Here is the describe code in Java

class Solution{
    public int getSum(int a, int b){
        while (b != 0){
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}
"""
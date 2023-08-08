// Given an integer array nums, return an array answer such that answer[i] 
// is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

#include <vector>

class Solution{
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums){
        int n = nums.size();
        std::vector<int> res(n, 1);

        // calculate the prefix product
        for (int i = 1; i < n; i++){
            res[i] = res[i-1] * nums[i-1];
        }

        // multiply by the suffix product
        int suff = 1;
        for (int i = n - 1; i >= 0; i--){
            res[i] *= suff;
            suff *= nums[i];
        }

        return res;
    };
};

// Create a vector which keeps track of the product of all the numbers before
// the current element. After this is created, we multiply each element in this
// result vector by the suffix product. At first, the suffix product is 1. After
// each element, we multiply the suffix product by the current element. 
//
// Time | Space: O(n) | O(n)

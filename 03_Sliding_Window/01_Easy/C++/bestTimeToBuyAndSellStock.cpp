#include <vector>
#include <algorithm>

class Solution{
    public:
        int maxProfit(std::vector<int>& prices){
            int minSoFar = prices[0];
            int profit = 0;

            for (const int p : prices){
                minSoFar = std::min(minSoFar, p);
                profit = std::max(profit, p - minSoFar);
            }

            return profit;
        };
};

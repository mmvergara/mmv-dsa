#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:

    int minCostClimbingStairs(vector<int>& cost) {	
        // Loop through the array backwards
        // change the current value to the cost of how much from the current position to the top
        for (int i = cost.size()-1; i>=0;i--){
            // the they are the last 2 element then just 1 or 2 step they can reach the top
            // so their values will remain the same because they are always going to be the elements to reach the top
            if ( i+1 == cost.size() || i+2 == cost.size()){
                continue;
            }

            // Current step cost
            int c = cost[i];

            // one step cost
            int ostep = cost[i+1];
            
            // two step cost
            int tstep = cost[i+2];

            // we add cost depends on the step we take
            // if they are equal at cost we take two steps
            if (ostep == tstep){
                c += tstep;
            // one step is less than two step we take one step
            } else if (ostep < tstep) {
                c += ostep;
            // two step is less than two step we take one step
            } else {
                c += tstep;
            }

            // now change the value to the total cost from this i to reach the top
            cost[i] = c;
            
        }

        // now the array is processed we see which first step are we going to take that will take the less cost
        if (cost[0] < cost[1]){
            return cost[0];
        } else {
            return cost[1];
        }
        
    }
};

class Solution {
public:

    int minCostClimbingStairs(vector<int>& cost) {	
        
        
        for (int i = cost.size()-1; i>=0;i--){
            if ( i+1 == cost.size() || i+2 == cost.size()){
                continue;
            }

            

            int c = cost[i];
            int ostep = cost[i+1];
            int tstep = cost[i+2];

            if (ostep == tstep){
                c += tstep;
            } else if (ostep < tstep) {
                c += ostep;
            } else {
                c += tstep;
            }

            cost[i] = c;
            
        }

        if (cost[0] < cost[1]){
            return cost[0];
        } else {
            return cost[1];
        }
        
    }
};

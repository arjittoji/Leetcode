class Solution {
public:
    int maxArea(vector<int>& height) {
        int lower = 0;
        int upper = height.size()-1;
        int maxArea , a = -1;
    while(lower != upper )
    {
        a = min(height[lower],height[upper]) * (upper-lower);
        maxArea = max(maxArea,a);
        if(height[lower] < height[upper])  lower+=1;
           
        else upper-=1;
        
    }
    return maxArea;
        
    }
};
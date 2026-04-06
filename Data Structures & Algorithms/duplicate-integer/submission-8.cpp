class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; // 중복 확인용 set

        for(int i = 0; i < nums.size(); i++) {
            if(seen.find(nums[i]) != seen.end()) {
                return true;
            }
            seen.insert(nums[i]);   // 처음 나온 값은 set에 추가
        }
        return false; 
    }
};

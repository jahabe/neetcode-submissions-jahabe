class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> A; // 숫자가 이미 나왔는지 확인하는 맵 
        for(int i = 0; i < nums.size(); i++) {
            if(A.find(nums[i]) != A.end()) {    // 이미 있는 값이면 중복이라는 말! 
                return true;
            }
            A[nums[i]] = true;  // unordered_map에 처음 나온 숫자를 저장해서 다음에 같은 숫자가 나오면 이미 존재하는지 확인 -> 중복 발견 -> return true; 
        }
        return false; 
    }
};

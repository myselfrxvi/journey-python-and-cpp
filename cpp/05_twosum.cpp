#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(const std::vector<int> nums, int target) {
    std::unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); i++) {
      int compliment = target - nums[i];
      if (seen.count(compliment)) {
        return {seen[compliment], i};
      }
      seen[nums[i]] = i;
    }
  }
};

int main() {
  Solution sol;
  std::vector<int> nums = {2, 7, 11, 15};
  int target = 9;
  std::vector<int> result = sol.twoSum(nums, target);
  std::cout << "Indices: [" << result[0] << ", " << result[1] << "]"
            << std::endl;
  return 0;
}

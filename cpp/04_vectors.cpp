#include <algorithm>
#include <iostream>
#include <vector>

int find_max(const std::vector<int> &num) {
  int max_val = num[0];
  for (auto n : num) {
    max_val = std::max(max_val, n);
  }
  return max_val;
}

int main() {
  std::vector<int> numbers = {14, 55, 3, 99, 42};
  std::cout << "Max No is:" << find_max(numbers) << std::endl;
  return 0;
}
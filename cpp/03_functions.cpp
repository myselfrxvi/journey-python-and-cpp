#include <iostream>

void swap_values(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

int main() {
  int x = 25;
  int y = 40;

  std::cout << "Before swapping: " << x << " " << y << std::endl;
  swap_values(x, y);
  std::cout << "After swapping: " << x << " " << y << std::endl;

  return 0;
}
#include <iostream>

void modifyByValue(int a) { a = 100; }
void modifyByPointer(int *a) { *a = 100; }
void modifyByReference(int &a) { a = 999; }
int main() {
  int score = 100;
  std::cout << "Original score: " << score << std::endl;
  std::cout << "Memory address of score: " << &score << std::endl;
  // Test 1: By Value
  modifyByValue(score);
  std::cout << "After modifyByValue: " << score << std::endl;
  // Test 2: By Reference
  modifyByReference(score);
  std::cout << "After modifyByReference: " << score << std::endl;
  // Test 3: By Pointer
  modifyByPointer(&score);
  std::cout << "After modifyByPointer: " << score << std::endl;
  return 0;
}

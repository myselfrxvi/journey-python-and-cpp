#include <iostream>
#include <memory>

void stackexample() {
  int stack_val = 42;
  std::cout << "Stack address: " << &stack_val << std::endl;
}
void heapexample() {
  int *heap_ptr = new int(888);
  std::cout << "Heap address:  " << heap_ptr << std::endl;
  std::cout << "Heap value:    " << *heap_ptr << std::endl;
  delete heap_ptr;
  heap_ptr = nullptr;
}

void moderncppsmartpointer() {
  std::unique_ptr<int> smart_heap = std::make_unique<int>(555);
  std::cout << "Smart heap address: " << smart_heap.get() << std::endl;
  std::cout << "Smart heap value:   " << *smart_heap << std::endl;
  smart_heap.reset();
}

int main() {
  stackexample();
  heapexample();
  moderncppsmartpointer();
  return 0;
}
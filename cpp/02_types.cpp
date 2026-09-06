#include <iostream>
#include <string>

int main() {
    std::string name;
    int solved;

    std::cout << "Enter Your name: ";
    std::cin >> name;

    std::cout << "Enter solved count: ";
    std::cin >> solved;

    int remaining = 100 - solved;

    std::cout << "Remaining problems = " << remaining << std::endl;
    std::cout << name << " has " << remaining << " problems left to hit 100!" << std::endl;

    return 0;
}
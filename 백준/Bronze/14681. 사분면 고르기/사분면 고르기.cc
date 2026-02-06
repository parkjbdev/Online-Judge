#include <iostream>

int main() {
    int x, y;
    std::cin >> x >> y;
    std::cout << "3241"[(x > 0) << 1 | (y > 0)];
}

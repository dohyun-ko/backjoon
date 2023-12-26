#include <iostream>
#include "vector"
#include "unordered_map"
#include "string"

std::vector<int> froms;
std::vector<int> tos;


void hanoi(int from, int to, int empty, int num) {
    if (num <= 0) {
        return;
    }

    hanoi(from, empty, to, num - 1);

    froms.push_back(from);
    tos.push_back(to);

    hanoi(empty, to, from, num - 1);
}

int count = 0;
std::unordered_map<int, unsigned long long int> memos;

unsigned long long int hanoi_without_out(int from, int to, int empty, int num) {
    if (num <= 0) {
        return 0;
    }

    int key = from * 100000 + to * 10000 + empty * 1000 + num;

//    std::cout << "memo " << key << ": " << memos[key] << std::endl;
    if (memos[key] > 0) {
        return memos[key];
    }

    memos[key] = hanoi_without_out(from, empty, to, num - 1) + 1 + hanoi_without_out(empty, to, from, num - 1);
    return memos[key];
}

std::string hanoi_only_math(int n) {
    if (n < 1) {
        return std::to_string(0);
    }

    return std::to_string(std::stoi(hanoi_only_math(n - 1)) * 2 + 1);
}

int main() {
  int n;

//  std::cin >> n;
//
//  if (n <= 20) {
//      hanoi(1, 3, 2, n);
//      std::cout << froms.size() << std::endl;
//      for (int i = 0; i < froms.size(); i++) {
//          std::cout << froms[i] << " " << tos[i] << std::endl;
//      }
//  } else {
//      std::cout << hanoi_without_out(1, 3, 2, n) << std::endl;
//  }

    for (int i = 0; i <= 100; i++) {
//        std::cout << i << ": " << hanoi_without_out(1, 3, 2, i) << std::endl;
        std::cout << i << ": " << hanoi_only_math(i) << std::endl;
    }
}
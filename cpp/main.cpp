#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct Node {
    struct Node* next;
    int data;
};

struct Node* head = nullptr;

void partOne() {
    std::ifstream input("../inputs/day01.txt");

    if (input.is_open()) {
        std::string line;
        int max = 0;
        int curr = 0;
        while (input.good()) {
            std::getline(input, line);
            if (line.empty()) {
                max = std::max(max, curr);
                curr = 0;
            } else {
                curr += std::stoi(line);
            }
        }

        std::cout << "Max: " << max;
    }
}

void partTwo() {
    std::ifstream input("../inputs/day01.txt");

    if (input.is_open()) {
        std::vector<int> elves;
        std::string line;
        int max = 0;
        int curr = 0;
        while (input.good()) {
            std::getline(input, line);
            if (line.empty()) {
                max = std::max(max, curr);
                curr = 0;
            } else {
                curr += std::stoi(line);
            }
        }

        std::cout << "Max: " << max;
    }
}

int main() {

    head = new Node();
    head->data = 1;
    head->next = new Node();
    head->next->data = 2;
    head->next->next = new Node();
    head->next->next->data = 3;

    Node* curr = head;
    while (curr != nullptr) {
        std::cout << curr->data << '\n';
        curr = curr->next;
    }

    Node* temp = head->next;
    head->next = head->next->next;
    delete temp;

    return 0;
}

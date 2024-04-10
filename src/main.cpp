#include "aa.h"
#include <vector>
#include <string>

int main() {
    aa();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    aa_print_vector(vec);
}

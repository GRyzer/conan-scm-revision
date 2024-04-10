#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define AA_EXPORT __declspec(dllexport)
#else
  #define AA_EXPORT
#endif

AA_EXPORT void aa();
AA_EXPORT void aa_print_vector(const std::vector<std::string> &strings);

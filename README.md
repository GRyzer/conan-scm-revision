# conan-scm-revision

The goal is to have a c++ function that returns the current git commit hash. Our approach is to get this via conan and pass it as a variable in cmake. Cmake generates a .cpp file from a template file with this function.
This approach works as desired for a repo. But if we have many of them, then each has the same conan function. The goal is the reusability of a conan function.

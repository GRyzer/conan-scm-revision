cmake_minimum_required(VERSION 3.15)
project(aa CXX)

configure_file(data/gitRevision.cpp.in gitRevision.cpp)

add_executable(aa src/aa.cpp src/main.cpp ${CMAKE_CURRENT_BINARY_DIR}/gitRevision.cpp)



install(TARGETS aa DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

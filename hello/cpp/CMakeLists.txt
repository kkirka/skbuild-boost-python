cmake_minimum_required(VERSION 3.4.0)

add_library(_cpp_module MODULE _cpp_module.cpp)
link_boost_python(_cpp_module)
python_extension_module(_cpp_module)
install(TARGETS _cpp_module LIBRARY DESTINATION hello/cpp)

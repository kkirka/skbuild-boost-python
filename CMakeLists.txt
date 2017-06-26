cmake_minimum_required(VERSION 3.4.0)

project(hello)

find_package(PythonInterp REQUIRED)
find_package(PythonLibs)
find_package(PythonExtensions REQUIRED)

function(locate_boost_python boost_python_library_target)
    foreach(Boost_PYTHON_VERSION_TAG "-${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}"
                                     "-py${PYTHON_VERSION_MAJOR}${PYTHON_VERSION_MINOR}"
                                     "${PYTHON_VERSION_MAJOR}" "")
        message("Locating python${Boost_PYTHON_VERSION_TAG}")
        find_package(Boost COMPONENTS "python${Boost_PYTHON_VERSION_TAG}")
        if(TARGET Boost::python${Boost_PYTHON_VERSION_TAG})
            set(boost_python_library_target Boost::python${Boost_PYTHON_VERSION_TAG} PARENT_SCOPE)
            break()
        endif()
    endforeach()
endfunction()

find_package(Boost COMPONENTS python)
locate_boost_python(boost_python_library_target)
message("${boost_python_library_target}")

function(link_boost_python target)
    target_include_directories(${target} PUBLIC ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIR})
    target_link_libraries(${target} ${boost_python_library_target})
endfunction()

add_subdirectory(hello/cpp)

#include <boost/python.hpp>

char const* hello()
{
    return "Hello world!";
}

BOOST_PYTHON_MODULE(_cpp_module)
{
    using namespace boost::python;
    def("hello", hello);
}

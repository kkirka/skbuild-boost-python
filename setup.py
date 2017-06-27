from skbuild import setup

setup(
    name="hello-cpp",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="MIT",
    cmake_args=['-DCMAKE_BUILD_TOOL:STRING=make'],
    packages=['hello'],
)

cmake_minimum_required(VERSION 2.8.12)

project(PackageTest)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(SWIG_JNI)
    find_package(Java REQUIRED)
    include(UseJava)

    # Build a testing jar which invokes the jni lib to verify it
    add_jar(
        ConanLibTesterMain
        SOURCES main.java
        INCLUDE_JARS ${CONAN_BIN_DIRS_CLSJ}/clsjJNI.jar
        ENTRY_POINT main
    )
endif()

add_executable(testapp main.cpp)
target_link_libraries(testapp ${CONAN_LIBS})

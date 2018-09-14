cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# add_executable(example example.cpp)
# target_link_libraries(example ${CONAN_LIBS})

find_package(Java REQUIRED)
include(UseJava)

# Build a testing jar which invokes the jni lib to verify it
add_jar(
    LibTesterMain
    SOURCES main.java
    INCLUDE_JARS ${CONAN_LIB_DIRS_CLSJ}/clsjJNI.jar
    ENTRY_POINT main
)

message("${Java_JAVA_EXECUTABLE} -Djava.library.path=${CONAN_LIB_DIRS_CLSJ}
        -classpath ${CONAN_LIB_DIRS_CLSJ} -jar LibTesterMain.jar ...")

add_custom_command(
    TARGET LibTesterMain
    POST_BUILD
    COMMAND ${Java_JAVA_EXECUTABLE} -Djava.library.path=${CONAN_LIB_DIRS_CLSJ}
        -classpath ${CONAN_LIB_DIRS_CLSJ} -jar LibTesterMain.jar "JNI jar call success from conan package"
)

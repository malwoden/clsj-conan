from conans import ConanFile, CMake, tools


class ClsjConan(ConanFile):
    name = "clsj"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/malwoden/clsj-conan"
    description = "clsj is a toy package for testing c++, swig, java and conan togther"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="clsj_src")
        git.clone("https://github.com/malwoden/clsj.git", "master")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="clsj_src")
        cmake.build()

    def package(self):
        self.copy("swig/libclsj_swiggy.so", dst="lib", keep_path=False)
        self.copy("swig/clsjJNI.jar", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["clsjJNI.jar", "clsj_swiggy.so"]


from conans import ConanFile, CMake, tools


class ClsjConan(ConanFile):
    name = "clsj"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Clsj here>"
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


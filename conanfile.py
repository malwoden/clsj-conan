from conans import ConanFile, CMake, tools


class ClsjConan(ConanFile):
    name = "clsj"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/malwoden/clsj-conan"
    description = "clsj is a toy package for testing c++, swig, java and conan togther"
    settings = "os", "compiler", "build_type", "arch"
    options = {"swigJni": [True, False],
               "shared": [True, False]}
    default_options = ("swigJni=True",
                        "shared=False")
    generators = "cmake"

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CLSJ_SWIG_JNI"] = "ON" if self.options.swigJni else "OFF"
        cmake.configure(source_folder="clsj_src")
        return cmake

    def source(self):
        git = tools.Git(folder="clsj_src")
        git.clone("https://github.com/malwoden/clsj.git", "master")

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["clsj"]
        if self.options.swigJni:
            self.cpp_info.libs.extend(["clsj_swiggy"])

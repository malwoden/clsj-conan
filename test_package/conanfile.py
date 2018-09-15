import os

from conans import ConanFile, CMake, tools


class ClsjTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.jar", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("java -Djava.library.path=./bin "
                        "-classpath bin/clsjJNI.jar:ConanLibTesterMain.jar main "
                            "\"JNI jar call success from conan package\"")

import os

from conans import ConanFile, CMake, tools


class ClsjTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["SWIG_JNI"] = "ON" if self.options["clsj"].swigJni else "OFF"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.jar", dst="bin", src="bin")
        self.copy('*.so*', dst='bin', src='bin')

    def test(self):
        if not tools.cross_building(self.settings):
            if self.options["clsj"].swigJni:
                self.run("java -Djava.library.path=./bin "
                            "-classpath bin/clsjJNI.jar:ConanLibTesterMain.jar main "
                                "\"JNI jar call success from conan package\"")
            else:
                os.chdir("bin")
                self.run(".%stestapp" % os.sep)

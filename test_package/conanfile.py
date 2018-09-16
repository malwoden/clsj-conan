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
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            # LD_LIBRARY_PATH is required otherwise the libclsj_swiggy.so will not be able to load libclsj.so
            with tools.environment_append({"LD_LIBRARY_PATH": "./bin" if self.options["clsj"].shared else ""}):
                if self.options["clsj"].swigJni:
                    self.run("java -Djava.library.path=./bin "
                                "-classpath bin/clsjJNI.jar:ConanLibTesterMain.jar main "
                                    "\"JNI jar call success from conan package\"")

            # always run the non swig test app
            os.chdir("bin")
            if self.options["clsj"].shared:
                self.run(".%stestapp" % os.sep)

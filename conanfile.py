from conan import ConanFile
from conan.tools.files import get, copy
from conan.tools.layout import basic_layout
import os

required_conan_version = ">=1.50.0"


class ReaderWriterQueue(ConanFile):
    name = "readerwriterqueue"
    version = "post-1.0.6"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/cameron314/readerwriterqueue"
    description = "A fast single-producer, single-consumer lock-free queue for C++"
    topics = ("cpp11", "cpp14", "cpp17", "queue", "lock-free")
    license = "BSD-2-Clause"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt", "*.h"
    no_copy_source = True
    settings = "os"

    def layout(self):
        basic_layout(self)

    def build(self):
        pass

    def package(self):
        self.copy("*.h")
        
    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        if self.settings.os in ["Linux", "FreeBSD"]:
            self.cpp_info.system_libs = ["pthread"]

    def package_id(self):
        self.info.clear()

from conans import ConanFile, tools


class CppSubprocess(ConanFile):
    name = "cpp-subprocess"
    license = "MIT"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/nextsilicon/cpp-subprocess#readme"
    topics = ("subprocess", "os", "fork")
    description = ("Subprocessing with modern C++, "
                   "The only goal was to develop something that is as close as"
                   "python subprocess module in dealing with processes.")
    # No settings/options are necessary, this is header only
    exports_sources = "subprocess.hpp"
    no_copy_source = True

    _source_subfolder = 'cpp-subprocess'

    def source(self):
        tools.get(**self.conan_data['sources'][self.version],
                  destination=self._source_subfolder, strip_root=True)

    def package(self):
        self.copy("subprocess.hpp", dst="include", src=self._source_subfolder)
        self.copy("LICENSE.MIT", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()

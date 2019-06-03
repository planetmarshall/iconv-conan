from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os.path


class IconvConan(ConanFile):
    name = 'iconv'
    version = '1.16.0'
    license = 'https://www.gnu.org/licenses/lgpl-3.0.en.html'
    url = 'https://www.gnu.org/software/libiconv/'
    description = 'GNU Library for character set conversions.'
    author = 'Andrew Marshall <planetmarshalluk@gmail.com>'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'shared': [True, False]}
    default_options = {'shared': False}
    generators = 'cmake'

    @property
    def _staging_folder(self):
        return os.path.join(self.build_folder, 'stage')

    def source(self):
        url = 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz'
        tools.get(url)

    def build(self):
        with tools.chdir(os.path.join(self.source_folder,'libiconv-1.16')):
            autotools = AutoToolsBuildEnvironment(self)

            args = [
                '--enable-shared' if self.options.shared else '--enable-static',
                '--prefix=' + self._staging_folder
            ]
            autotools.configure(args=args)
            autotools.make()
            autotools.install()

    def package(self):
        self.copy('*', src=self._staging_folder, keep_path=True)

    def package_info(self):
        self.cpp_info.libs = ['iconv']


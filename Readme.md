Libiconv
========

[Conan](https://conan.io/) package for the [GNU Libiconv](https://www.gnu.org/software/libiconv/) project.

The main purpose of this package was to facilitate an Android project that had need
of libiconv. Note that Android API level 28 (9.0, Pie) has iconv available in libc, but this project may be of use 
to anyone needing to build libiconv for versions < 28 or other platforms.
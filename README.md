# cxxfilt
Demangling C++ symbols in python by calling `gc++filt` from homebrew on MacOS.  
Yes it's slower than library access, but it's quick and I want to get this 
implemented.  The existing (cxxfilt)[https://github.com/afg984/python-cxxfilt] 
project is limited to C++ symbol demangling supported by the libc++ libraries 
available on the platform.

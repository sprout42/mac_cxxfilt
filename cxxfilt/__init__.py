"""
Implements the CXXFILT class that opens the `gc++filt` executable.
"""
import subprocess


CXXOBJ = None


class CXXFILT(object):
    """
    class to do C++ name demangling

    TODO: probably better to have the gc++filt subprocess be a class variable
    and guard access to it with a lock.
    """
    def __init__(self, path='/usr/local/bin/gc++filt'):
        self.proc = subprocess.Popen([path], stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def __del__(self):
        self.proc.stdout.close()
        self.proc.stdin.close()

    def demangle(self, symbol):
        """Demangle a C++ symbol

        Keyword arguments:
        symbol -- The string to demangle
        """
        self.proc.stdin.write(symbol + '\n')
        out = self.proc.stdout.readline()
        return out.rstrip('\n')


def demangle(symbol):
    """Function that provides access to the CXXFILT class.

    When calling this function a persistent instance of the CXXFILT class will
    be created.

    Keyword arguments:
    symbol -- The string to demangle
    """
    global CXXOBJ
    if CXXOBJ is None:
        CXXOBJ = CXXFILT()

    return CXXOBJ.demangle(symbol)

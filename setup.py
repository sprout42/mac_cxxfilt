import setuptools

setuptools.setup(
    name='cxxfilt',

    version='0.1',
    packages=setuptools.find_packages(),

    description='Demangling C++ symbols by calling `gc++filt` from homebrew on MacOS',

    url='https://github.com/sprout42/mac-cxxfilt',

    author='sprout42',
    author_email='a.aaron.cornelius@gmail.com',

    license='MIT',
)

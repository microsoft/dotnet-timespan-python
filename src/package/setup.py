from distutils.core import setup
from timespan import __version__

setup(
    name='timespan-python',
    version=__version__,

    url='https://github.com/microsoft/dotnet-timespan-python/src/package',
    author='Mattan Serry',
    author_email='maserry@microsoft.com',

    py_modules=['timespan-python'],
)

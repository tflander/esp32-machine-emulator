# import sys
from distutils.core import setup

#from pathlib import Path

# __dir__ = Path(__file__).absolute().parent
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
# sys.path.pop(0)
# sys.path.append("..")

def read(file_relative):
    file = file_relative
    with open(str(file)) as f:
        return f.read()

setup(
  name = 'esp32-machine-emulator',
  packages = ['esp32-machine-emulator'],
  version = '0.0.9',
  license='MIT',
  description = 'esp32 machine package for test-driving code off-chip',
  long_description = read('README.md'),
  author = 'Todd Flanders',
  author_email = 'toddfbass@gmail.com',
  url = 'https://github.com/tflander/esp32-machine-emulator',
  download_url = 'https://github.com/tflander/esp32-machine-emulator/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['ESP32', "MicroPython", 'TDD'],
  install_requires=[],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Testing :: Mocking',
    'Topic :: Software Development :: Testing :: Unit',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: MicroPython'
  ],
)
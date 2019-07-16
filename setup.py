from distutils.core import setup

def read(file_relative):
    file = file_relative
    with open(str(file)) as f:
        return f.read()

setup(
  name = 'esp32_machine_emulator',
  packages = ['esp32_machine_emulator'],
  version = '0.0.8',
  license='MIT',
  description = 'esp32 machine package for test-driving code off-chip',
  long_description = read('README.rst'),
  author = 'Todd Flanders',
  author_email = 'toddfbass@gmail.com',
  url = 'https://github.com/tflander/esp32-machine-emulator',
  download_url = 'https://github.com/tflander/esp32-machine-emulator/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['ESP32', "MicroPython", 'TDD'],
  install_requires=[],
  classifiers=[
    'Development Status :: 7 - Inactive',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Testing :: Mocking',
    'Topic :: Software Development :: Testing :: Unit',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: MicroPython'
  ],
)
from distutils.core import setup
setup(
  name = 'esp32-machine-emulator',
  packages = ['esp32-machine-emulator'],
  version = '0.0.0',
  license='MIT',
  description = 'esp32 machine package for test-driving code off-chip',
  author = 'Todd Flanders',
  author_email = 'toddfbass@gmail.com',
  url = 'https://github.com/tflander/esp32-machine-emulator',
  download_url = 'https://github.com/tflander/esp32-machine-emulator/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['ESP32', "MicroPython", 'TDD'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Testing Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)
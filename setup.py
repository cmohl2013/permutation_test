from setuptools import setup

setup(name='permutation_test',
      version='0.1',
      description='Implementation of Fishers permutation test',
      #url='http://github.com/storborg/funniest',
      author='Christoph Moehl',
      author_email='christoph.moehl@dzne.de',
      license='MIT',
      packages=['permutation_test'],
      install_requires=['numpy'],
      zip_safe=False)
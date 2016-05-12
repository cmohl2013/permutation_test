from setuptools import setup

setup(name='permutation_test',
      version='0.13',
      description='Implementation of Fishers permutation test',
      url='https://github.com/cmohl2013/permutation_test',
      author='Christoph Moehl',
      author_email='christoph.moehl@dzne.de',
      license='MIT',
      packages=['permutation_test'],
      install_requires=['numpy', 'pandas'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
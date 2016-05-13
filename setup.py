from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='permutation_test',
      version='0.14',
      description='Implementation of Fishers permutation test',
      long_description=readme(),
      url='https://github.com/cmohl2013/permutation_test',
      author='Christoph Moehl',
      author_email='christoph.moehl@dzne.de',
      license='MIT',
      packages=['permutation_test'],
      install_requires=['numpy', 'pandas'],
      entry_points = {
        'console_scripts': [\
              'permtest=permutation_test.permtest:main']
        },
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
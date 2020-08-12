from setuptools import setup

setup(name='wes',
      version='0.17',
      description='Use Wes Anderson Color Palettes in Matplotlib & Seaborn',
      url='https://github.com/ljwolf/wampl',
      author='Levi John Wolf',
      author_email='levi.john.wolf@gmail.com',
      license='CC-BY-SA',
      packages=['wes'],
      install_requires=['matplotlib'],
      include_package_data=True,
      zip_safe=False)

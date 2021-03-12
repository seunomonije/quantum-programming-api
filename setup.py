import setuptools

setuptools.setup(
  name='qapi',
  version='0.0.1',
  author="Seun Omonije, Aidan Evans",
  author_email="seun.omonije@yale.edu",
  description='Harness the power of quantum computing without quantum knowledge.',
  url="https://github.com/seunomonije/quantum-programming-api",
  classifiers=[
    "Programming Language :: Python :: 3",
  ],
  license="Apache 2",
  packages=setuptools.find_packages(),
  py_modules=["qapi"],
  python_requires=">3.6",
  install_requires=[]
)

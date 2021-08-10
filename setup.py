import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="harvest-for-mightyhive",
    version="0.0.1",
    author="Yang Dai",
    author_email="yang.dai2020@gmail.com",
    description="An automation tool to speed up the process of updating entries in harvest",
    long_description=long_description,
    download_url = "https://github.com/superyang713/harvest_automation/archive/refs/tags/v0.0.1.tar.gz", 
    url="https://github.com/superyang713/harvest_automation/blob/main/README.md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
    ],
    install_requires=[
        "selenium",
    ],
)


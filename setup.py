from setuptools import setup, find_packages

with open(file='README.md', mode='r') as f:
    longDescription = f.read()

setup(
    name='SystemCheck',
    version='1.0.0',
    description='',
    author="Enes ARSLAN",
    author_email="enesars716@gmail.com",
    url="https://github.com/Arslanex/System-Check",
    keywords='opencv,cuda, arslanex, computer system',
    install_requires=[
        'numpy',
        'opencv-python',
        'psutil',
        'GPUtil'
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

    ]
)
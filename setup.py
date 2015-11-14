from setuptools import setup, find_packages

setup(
    name='nsperf',
    version='0.0.1',
    description="Utility to generate DNS packages",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "dnspython3==1.12.0",
    ],
    entry_points={
        "console_scripts": ["nsperf = nsperf.shell.run:main"],
    },
)

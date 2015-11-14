from setuptools import setup, find_packages

setup(
    name='nsperf',
    version='0.0.1',
    description="Utility to generate DNS packages",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["nsperf = nsperf.shell.run:main"],
    },
    zip_safe=False,
)

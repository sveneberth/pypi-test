import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="first-package-xyz567",
    version="0.0.2",
    author="Sven Eberth",
    author_email="mail@sveneberth.de",
    description="A small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sveneberth/pypi-test",
    project_urls={
        "Bug Tracker": "https://github.com/sveneberth/pypi-test/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "first_package_xyz567"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

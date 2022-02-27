
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-deepanshi-401903006",
    version="1.0.0",
    author="Deepanshi Srivastava",
    author_email="deepanshi2105@gmail.com",
    description="A package -> Calculates Topsis Score and Rank accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Deepanshi21/topsis_deepanshi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["topsis_deepanshi"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=topsis_deepanshi.topsis:main",
        ]
    },
)

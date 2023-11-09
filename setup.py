import setuptools

setuptools.setup(
    name="streamlit-customized-searchbox",
    version="0.1.0",
    description="Autocomplete Searchbox",
    long_description="Streamlit searchbox that dynamically updates "
    + "and provides a list of suggestions based on a provided function",
    long_description_content_type="text/plain",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7, !=3.9.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
    extras_require={
        "tests": [
            "wikipedia",
            "pytest",
            "pytest-playwright",
        ],
        "dev": [
            "pre-commit",
            "black",
            "isort",
            "ruff",
            "pyright",
        ],
    },
)

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flasktodo",
    version="0.0.1",
    author="Scott Johnson",
    author_email="scottyjohnson002@gmail.com",
    url="https://github.com/ScottJohnson02/flask-todo",
    description="A simple to-do application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'psycopg2'],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

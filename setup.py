from setuptools import find_packages, setup


setup(
    name="musical_instrument_recognition",
    version="0.0.1",
    packages=find_packages("src/"),
    package_dir={"": "src/"},
    install_requires=[
        "django==2.2.24",
		"gunicorn==19.10.0"
    ],
    include_package_data=True,
)

from setuptools import setup

setup(
    name="nxbt",
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python",
        "eventlet==0.31.0",
        "pynput==1.7.1",
        "cryptography==3.4.8",
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)

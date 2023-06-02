import sys

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="with_python-rust",
    version="1.0",
    rust_extensions=[RustExtension("with_python.with_python", binding=Binding.RustCPython)],
    packages=["with_python"],
    # Rust extensions are not zip safe
    zip_safe=False,
    long_description="This is a description for our Rust-Python package.",
    long_description_content_type="text/x-rst"
)
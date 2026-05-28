from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drgpy",
    version="0.0.6",
    description="drgpy is a Python library for assigning a combination of diagnosis and procedure codes to Diagnosis Related Groups (MS-DRG) that is used in Medicare inpatient reimbursement today.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yubin Park",
    author_email="yubin.park@gmail.com",
    url="https://github.com/yubin-park/drgpy",
    license="Apache 2.0",
    install_requires=[],
    include_package_data=True,
    packages=find_packages(),  # This will find the 'drgpy' package in the current directory
    package_data={
        "drgpy": [
            "data/v36/*.txt",
            "data/v37/*.txt",
            "data/v38/*.txt",
            "data/v39/*.txt",
            "data/v40/*.txt",
            "data/v41/*.txt",
            "data/v42/*.txt",
            "data/v43/*.txt"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)

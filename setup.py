import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

requirements = [
    'requests==2.25.1',
    'requests-toolbelt==0.9.1',
    'PySocks==1.7.1',
    'pydantic==1.8.1'
]

setup(
    name='radiojavanapi',
    version='0.2.2',
    author='xHossein',
    license='MIT',
    url='https://github.com/xHossein/radiojavanapi',
    install_requires=requirements,
    keywords=['radiojavan private api','radiojavan-private-api','radiojavan api','radiojavan-api',
              'rj api','rj-api','radiojavan','radio javan','radio-javan'
    ],
    description='Fast and effective RadioJavan API Wrapper',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

requirements = [
    'requests==2.32.5',
    'requests-toolbelt==1.0.0',
    'PySocks==1.7.1',
    'pydantic==2.11.9'
]

setup(
    name='radiojavanapi',
    version='0.6.1',
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
    packages=find_packages(exclude=['*tests*']),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
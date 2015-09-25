from setuptools import setup, find_packages
import ngen


setup(
    author="Anthony",
    name="ngen",
    version=ngen.__version__,
    packages=find_packages(exclude=["tests*", ]),
    url="https://github.com/anthonyalmarza/ngen",
    description="This app handles all communictions on the Reelio Platform.",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords=['singletons', ],
    install_requires=['six', ],
    extras_require={'dev': ['ipdb', 'mock']},
    include_package_data=True
)

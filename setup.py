from setuptools import setup, find_packages

setup(
    name="jabbbar",
    version="0.2.0",
    description="A python 3 wrapper for the Dribbble API",
    url="https://github.com/zabanaa/jabbbar",
    author="Karim Cheurfi (Zabana)",
    author_email="karim.cheurfi@gmail.com",
    license="WTFPL",
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests'],
    keywords=["dribbble", "api", "http", "wrapper", "jabbbar"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)

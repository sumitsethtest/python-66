from setuptools import setup


setup(
    name='flake8-config-4catalyzer',
    version='0.2.1',
    url='https://github.com/4Catalyzer/python/tree/packages/flake8-config-4catalyzer',
    author="Alex Rothberg",
    author_email='arothberg@4catalyzer.com',
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ),
    keywords='flake8',
    install_requires=(
        'flake8',
        'flake8-commas',
        'flake8-debugger',
        'flake8-import-order',
    ),
    extras_require={
        ':python_version>="3.5"': ('flake8-bugbear',),
    },
)

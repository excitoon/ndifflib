import setuptools


setuptools.setup(
    name = 'ndifflib',
    version = '0.1.0',
    description = 'N-way diff library',
    long_description = 'N-way diff library with interface similar to difflib.',
    url = 'https://github.com/excitoon/ndifflib',
    author = 'Vladimir Chebotarev',
    author_email = 'vladimir.chebotarev@gmail.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords = 'diff difflib',
    packages = ['ndifflib'],
    install_requires = [],
    extras_require = { 'dev' : [], 'test' : [] },
    package_data = {},
    data_files = [],
    entry_points = { 'console_scripts' : [] },
    project_urls = {
        'Bug Reports' : 'https://github.com/excitoon/ndifflib/issues',
        'Documentation' : 'https://github.com/excitoon/ndifflib/blob/master/README.md',
        'Source' : 'https://github.com/excitoon/ndifflib'
    }
)

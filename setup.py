try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

requirements = [
	"requests"
]

setup(
    name = "pwned",
    version = "0.0.1",
    url = 'https://github.com/mattpaletta/pwned',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requirements,
    author = "Matthew Paletta",
    author_email = "mattpaletta@gmail.com",
    description = "Check if you have been involed in a breach (password or email).",
    license = "BSD",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ],
    entry_points={
        'console_scripts': [
            'pwned = pwned.__main__:main',
        ]
    },
)

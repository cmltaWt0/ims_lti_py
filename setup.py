from setuptools import setup, find_packages

setup(
    name='ims_lti_py',
    version='0.6',
    description=('A Python library to help implement IMS '
                 'LTI tool consumers and providers'),
    author='Anson MacKeracher',
    author_email='anson@tophatmonocle.com',
    url='https://github.com/tophatmonocle/ims_lti_py',
    packages=find_packages(),
    install_requires=[
        'lxml',
    ],
    dependency_links=[
        'https://github.com/cmltaWt0/python-oauth2/tarball/v1.9.1',
    ],
    license='MIT License',
    keywords='lti',
    zip_safe=True,
    test_suite='tests',
)

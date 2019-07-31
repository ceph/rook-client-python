from setuptools import setup

setup(
    name='rook-ceph-client',
    version='1.0.0',
    packages=['rook_ceph_client'],
    url='',
    license='MIT',
    author='Sebastian Wagner',
    author_email='swagner@suse.com',
    description='Client model classes for the CRDs exposes by Rook',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mypy', 'pytest-mypy']
)

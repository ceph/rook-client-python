import distutils
import subprocess

from setuptools import setup


class MkCodesCommand(distutils.cmd.Command):
  """A custom command to run Pylint on all Python source files."""

  description = 'run mkcodes'
  user_options:list = []

  def initialize_options(self):
      pass

  def finalize_options(self):
      pass

  def run(self):
    """Run command."""
    subprocess.check_call('mkcodes --github --output rook_client/tests/test_{name}.py README.md'.split())


setup(
    name='rook-client',
    version='1.0.0',
    packages=['rook_client'],
    url='',
    license='MIT',
    author='Sebastian Wagner',
    author_email='swagner@suse.com',
    description='Client model classes for the CRDs exposed by Rook',
    install_requires=[
        'pyyaml',
        'docopt',
        'attrs;python_version<"3.7"'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mypy', 'pytest-mypy'],
    cmdclass={
        'mkcodes': MkCodesCommand,
    },
)

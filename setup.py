from setuptools import setup
setup(
    name='build_bot',
    packages=['build_bot'],
    version='1.3',
    description='A fast and easy way to manage CI builds',
    author='davemachado',
    author_email='contact@davemachado.com',
    url='https://github.com/davemachado/build-bot',
    download_url=(
        'https://github.com/davemachado/build-bot/archive/1.0.tar.gz'),
    keywords=['build', 'bot', 'github'],
    classifiers=[],
    scripts=['build_bot/build_bot'],
)

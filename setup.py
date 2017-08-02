from distutils.core import setup
setup(
    name='build_bot',
    packages=['build_bot'],
    version='0.1',
    description='A fast and easy way to manage CI builds',
    author='davemachado',
    url='https://github.com/davemachado/build-bot',
    download_url=(
        'https://github.com/davemachado/build-bot/tarball/0.1'),
    keywords=['build', 'bot', 'github'],
    classifiers=[],
    scripts=['build_bot/build_bot.py'],
)

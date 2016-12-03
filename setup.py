# _*_ coding: utf-8 _*_
from setuptools import setup
setup(
    name='lyricaly',
    packages=["lyricaly"],
    version='1.0.2',
    author='Vignesh M',
    author_email='vigzmv@outlook.com',
    url='https://github.com/vigzmv/Lyricaly',
    download_url='https://github.com/vigzmv/Lyricaly',
    license='MIT License',
    description='Lyricaly Gets Lyrics directly to your Terminal.',
    long_description=open('README.md').read(),
    zip_safe=False,
    install_requires = ['beautifulsoup','requests','bs4'],
    entry_points={
    'console_scripts': [
        'lyricaly=lyricaly.__main__:main',
    ],
},
)

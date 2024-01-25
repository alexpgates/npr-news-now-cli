from setuptools import setup, find_packages

setup(
    name='npr-news-now-cli',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'feedparser',
    ],
    entry_points={
        'console_scripts': [
            'npr-news-now=npr_news_now_cli.listen:main',
        ],
    },
    author="Alex P. Gates",
    author_email="alexpgates@gmail.com",
    description="A command-line tool to listen to the latest NPR news now hourly news update.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/alexpgates/npr-news-now-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

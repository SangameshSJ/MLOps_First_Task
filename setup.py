# setup.py

from setuptools import setup, find_packages

setup(
    name="simplechatbot",
    version="0.1",
    description="A simple chatbot package",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "nltk"
    ],
    entry_points={
        "console_scripts": [
            "chatbot = chatbot.chatbot:chatbot"
        ]
    },
)
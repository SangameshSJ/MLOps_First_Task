from setuptools import setup, find_packages
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="simplechatbot",
    version="0.1",
    packages=find_packages(),
    install_requires=required,  # Automatically installs dependencies
    entry_points={
        "console_scripts": [
            "chatbot = chatbot.chatbot:chatbot",
        ],
    },
)

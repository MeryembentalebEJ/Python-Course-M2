from setuptools import setup, find_packages

setup(
    name="advanced_cli_task_manager",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest"  # pour les tests unitaires
    ],
    entry_points={
        'console_scripts': [
            'task-cli=task_manager.cli:main',
        ],
    },
    author="Meryem Bentaleb",
    description="A CLI-based Task Manager with logging, config, and unit testing",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Environment :: Console"
    ],
    python_requires='>=3.7',
)

from setuptools import setup


setup(
    name='json-log-plots',
    packages=['json_log_plots'],
    install_requires=[
        'json_lines',
        'filelock',
        'matplotlib',
    ],
)

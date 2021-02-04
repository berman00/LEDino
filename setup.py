from setuptools import setup

setup(
    name='LEDino',
    version='0.1',
    py_modules=['LEDino'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ledino=LEDino:ledino
    ''',)
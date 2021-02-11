from setuptools import setup

setup(
    name='LEDino',
    version='1.0',
    py_modules=['LEDino','LEDino-gui', 'LEDino-cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ledino=LEDino:ledino
    ''',)
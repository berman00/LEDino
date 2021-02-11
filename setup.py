from setuptools import setup

setup(
    name='LEDino',
    version='1.0',
    py_modules=['LEDino', 'LEDino_gui', 'LEDino_cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ledino=LEDino_cli:ledino
    ''',)
# PyWinScreenLockPrevent

 PyWinScreenLockPrevent is a Python-based utility designed to prevent screen locks on Windows 10, specifically tailored for use with work laptops. This tool intelligently makes something and ensures that the screen stays active when necessary, improving user experience and productivity in holidays to watch without move mouse every short time.

## Table of Contents

- [PyWinScreenLockPrevent](#pywinscreenlockprevent)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Future work](#future-work)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To use PyWinScreenLockPrevent, you need Python installed on your system. If you haven't already, you can download it from [Python's official website](https://www.python.org/downloads/).

Clone or download this repository to your local machine.

```bash
git clone https://github.com/MohammadYAmmar/PyWinScreenLockPrevent.git
Install the required Python packages listed in the requirements.txt file.
bash
Copy code
pip install -r requirements.txt
Usage
Run the PyWinScreenLockPrevent.py script to launch the GUI.
bash
Copy code
python PyWinScreenLockPrevent.py
```

Creating a Standalone Executable

You have the option to create a standalone executable for PyWinScreenLockPrevent using PyInstaller. This will bundle your script and its dependencies into a single executable file that can be run on Windows systems without needing Python or additional dependencies.

**Note**: Before proceeding, ensure that you have already installed PyInstaller by running `pip install pyinstaller`.

Follow these steps to create the standalone executable:

1. Navigate to the directory where your `PyWinScreenLockPrevent.py` script is located.

2. Open your command prompt or terminal and run the following command:

```bash
pyinstaller --onefile --noconsole PyWinScreenLockPrevent.py

```


In the GUI, click the "Start" button to begin screen lock prevention. The mouse pointer will be moved at regular intervals to simulate user activity.

To stop screen lock prevention, click the "Stop" button.

Configuration
You can customize PyWinScreenLockPrevent by adjusting the following parameters in the PyWinScreenLockPrevent.py script:

interval: Set the interval (in seconds) between mouse cursor movements. Default is 60 seconds (1 minute).

## Future work
The TODO list:
- Verify EXE compatibility on laptop. [✅ Alhumdulillah  work in other laptop with Youtube]
- Enhance "Stop" button functionality. [✅]
- Reduce EXE size (currently 68 MB), by use other lite package.
- Implement operational modes and dynamic button changes, current use for Youtube.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and ensure the code is well-documented.
Test your changes to ensure they work as expected.
Submit a pull request with a clear description of your changes.


## License


This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the terms of the license.

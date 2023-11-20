# HWMon - Hardware Monitor

HWMon is a robust and efficient hardware monitoring tool designed to work on Windows systems. It operates via MQTT to feed Home Assistant with crucial data regarding the health and performance of your hardware.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of Home Assistant.
* You have a Windows machine. HWMon can be run on Windows 7, 8, and 10.

## Installing HWMon

To install HWMon, follow these steps:

1. Download the latest release from the GitHub repository.
2. Extract the contents of the .zip file to your desired location.
3. Open a command prompt with administrative privileges.
4. Navigate to the directory where you extracted HWMon.
5. Run `hwmon.exe install` to install the task.

HWMon uses the Windows Task Scheduler to run with escalated privileges on boot.

## Using HWMon

To use HWMon, simply start your system. The program will run automatically on boot thanks to the Windows Task Scheduler.

If you need to uninstall HWMon, open a command prompt with administrative privileges, navigate to the HWMon directory and run `hwmon.exe uninstall`.

## Contributing to HWMon

To contribute to HWMon, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

# PowerSync ⚡

PowerSync is a sleek, tech-forward application that gives you **command over your smart devices** with a focus on controlling smart lighting. With PowerSync, users can control their Tuya-compatible smart lights. The interface is built with simplicity in mind, allowing users to toggle lights on and off directly from the terminal.

🚀 **Future expansions** include device monitoring, custom commands, and automation to make PowerSync your ultimate smart home controller!

## Features ✨

### Currently Available:
* 🕹️ **Smart Lighting Control**: Turn your smart lights on/off with simple commands.
* 💻 **Command Line Interface (CLI)**: Get a hacker-style interactive experience while controlling your devices.
* 🔐 **Environment-Based Credentials**: Securely load your API keys and credentials from an `.env`file.
* 🖥️ **Device Dashboard**: Monitor and control multiple devices from a centralized dashboard.


### Coming Soon:
* 🛠️ **Custom Commands**: Send specific commands to your devices (e.g., adjust brightness, set timers, switch modes).
* 🌐 **Multi-Device Support**: Manage groups of devices and synchronize actions across them.
* ⏰ **Automation & Scheduling**: Set up schedules to automate actions like turning lights on/off at specific times.
* 🖼️ **Cross-Platform GUIs**: A visual interface option for users who prefer a graphical experience.

## Installation 🛠️

### Prerequisites
* Python 3.6+ 🐍
* A virtual environment (recommended) 🌐
* Tuya-compatible smart lights 💡
* `pip` for installing Python packages 📦

### Steps to Set Up PowerSync

1. **Clone the repository**:
   ```bash
   git clone git@github.com:dendycodes/PowerSync.git
   cd powersync
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   Create a `.env` file in the root folder with your Tuya API details:
   ```
   ENDPOINT=https://openapi.tuyaus.com
   ACCESS_ID=your_access_id
   ACCESS_KEY=your_access_key
   ```

5. **Run PowerSync**:
   ```bash
   python3 tuya_control.py
   ```

## Usage ⚡

Once PowerSync is running, you can control your lights with simple commands:
* **Press [Enter]** to toggle the lights **ON/OFF** 💡.
* **Type** `q` to exit the app 🛑.

## Future Plans 🚀

We're just getting started! PowerSync will evolve into a full-fledged **smart device controller**. Here's what you can expect in future versions:

1. **Device Dashboard**: Display all connected devices and their statuses.
2. **Custom Commands**: Adjust device settings (e.g., brightness, color, modes) from the app.
3. **Multi-Device Management**: Manage and synchronize actions across multiple devices.
4. **Automation & Scheduling**: Automate tasks such as turning lights on/off at certain times.
5. **Cross-Platform Interfaces**: A GUI for users who prefer a visual interface, while retaining the CLI for power users.

## Contributing 🤝

Want to contribute? We'd love your help! Feel free to:
* Open an issue 📝
* Submit a pull request 🚀

## License 📄

This project is licensed under the MIT License.

## Acknowledgments 🙏

Big thanks to the open-source community and the amazing **Tuya IoT** platform for making PowerSync possible!

## Stay Connected 🌐

Follow the project on GitHub for updates!

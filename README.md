# WhatsApp Group Creator - Python Script

This repository contains a Python script that automates the process of creating a new WhatsApp group using WhatsApp Web. The script uses the `Selenium` library to interact with the web interface, allowing users to create a WhatsApp group with specified participants seamlessly.

## Prerequisites

Before using the script, make sure you have the following installed:

1. Python (https://www.python.org/downloads/)
2. Chrome browser (https://www.google.com/chrome/)
3. Chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your-username/whatsapp-group-creator.git
```

2. Navigate to the project directory:

```
cd whatsapp-group-creator
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

1. Start the Chrome browser and open WhatsApp Web (https://web.whatsapp.com/).
2. Scan the QR code using your WhatsApp mobile app to log in.
3. Run the Python script to create a new group:

```
python create_whatsapp_group.py
```

4. Follow the on-screen instructions to enter the group name and the list of participants. Press `Enter` after providing each input.

## Notes

- This script is for educational purposes and should be used responsibly. Automated interactions with WhatsApp Web might go against WhatsApp's Terms of Service, and misuse may lead to account suspension or other actions by WhatsApp.
- Before running the script, ensure that you are authorized to add the participants you are specifying in the group.
- The script uses the `Selenium` library to interact with the web interface. Ensure you have the correct version of the Chrome webdriver corresponding to your Chrome browser version. The webdriver executable should be placed in the same directory as the script or specify its path in the script.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

- The `Selenium` library for providing a robust way to automate browser actions.
- The [Python](https://www.python.org/) community for creating an amazing programming language.

## Disclaimer

This project is not affiliated with WhatsApp or any of its entities. The use of this script is at your own risk. The authors are not responsible for any misuse or consequences arising from the use of this script.

---

Feel free to customize this README to fit your specific project. Ensure that you update the `Prerequisites` and `Usage` sections with any specific details or instructions related to your setup. Also, make sure to provide proper credits and acknowledgments to any libraries or resources used in your project.

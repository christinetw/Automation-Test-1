# Setting Up and Running the Automation Test Script(Mac)
1. **Install Python**:
If Python is not installed on your Mac, download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/)
During installation, ensure to check the option to add Python to your PATH.
2. **Install Selenium**:
Open Terminal on your Mac.
Install Selenium using pip by running the following command:

    ```pip install selenium```

3. **Download ChromeDriver**:
Download the appropriate version of ChromeDriver for your Chrome browser from the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
Extract the downloaded file and move the chromedriver executable to a location in your PATH. For example, you can move it to /usr/local/bin/.
4. **Save HTML File**:
Save the register.html file in the same directory as your Python script or specify the correct file path in the setUp() method where filePath is defined.
5. **Run the Test Script**:
Open Terminal on your Mac.
Navigate to the directory where your Python script is saved using the cd command.
Run the test script using the following command:

    ```python automationTest.py```

6. **View Test Results**:
After running the test script, you should see the Chrome browser open, navigate to the registration page, fill in the form fields, and attempt registration.
If the test is successful, you'll see the Chrome browser close automatically.
If there are any errors, they will be displayed in the Terminal along with relevant information.

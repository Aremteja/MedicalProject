# Setting Up Python Virtual Environment

To ensure a clean and isolated environment for your Python project, it's recommended to use a virtual environment. Follow the instructions below based on your operating system:

## For Windows Users:

### 1. Install Python (if not already installed):
   - Download the latest version of Python from the [official website](https://www.python.org/downloads/).
   - Run the installer and make sure to check the option "Add Python to PATH" during installation.

### 2. Open Command Prompt:
   - Press `Win + R`, type `cmd`, and press Enter to open Command Prompt.

### 3. Install `virtualenv`:
   - Run the following command to install `virtualenv` using `pip`:
     ```
     pip install virtualenv
     ```

### 4. Create a Virtual Environment:
   - Navigate to your project directory using `cd`.
   - Create a virtual environment by running:
     ```
     virtualenv venv
     ```
  - if the above command doesn't work then enter
    ```
    python -m venv venv
    ```

### 5. Activate the Virtual Environment:
   - Activate the virtual environment by running:
     ```
     venv\Scripts\activate
     ```

### 6. Install Django and Pandas:
   - With the virtual environment activated, install Django and Pandas using `pip`:
     ```
     pip install django==4.2

     pip install pandas       
     ```

## For Linux Users:

### 1. Install Python (if not already installed):
   - Most Linux distributions come with Python pre-installed. However, you can install it via package manager if needed. For example, on Ubuntu, you can use:
     ```
     sudo apt-get update
     sudo apt-get install python3
     ```

### 2. Open Terminal:
   - You can open Terminal using your system's application launcher or by pressing `Ctrl + Alt + T`.

### 3. Install `virtualenv`:
   - Run the following command to install `virtualenv` using `pip`:
     ```
     pip install virtualenv
     ```

### 4. Create a Virtual Environment:
   - Navigate to your project directory using `cd`.
   - Create a virtual environment by running:
     ```
     virtualenv venv
     ```

### 5. Activate the Virtual Environment:
   - Activate the virtual environment by running:
     ```
     source venv/bin/activate
     ```

### 6. Install Django and Pandas:
   - With the virtual environment activated, install Django and Pandas using `pip`:
     ```
     pip install django==4.2

     pip install pandas       
     ```


---

Now, you have successfully set up a Python virtual environment! Remember to activate the virtual environment whenever you work on your project.



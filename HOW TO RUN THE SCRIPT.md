### How to Run the Python Program on macOS and Windows (Simple Steps)

On the main github page, go to "Code" then Download ZIP. Then unzip the folder, then you will have a folder called "Image-Matrix-Generator-main".

#### For macOS:
1. **Check if Python is already installed**:
   - Open **Terminal** (press `Cmd + Space`, type "Terminal", and press `Enter`).
   - Type `python3 --version` and press `Enter`.
   - If Python is installed, you'll see a version number. If not, continue to step 2.

2. **Install Python**:
   - Open **Terminal** and type this command to install Python using Homebrew (if you don't have Homebrew, install it first by going to https://brew.sh):
     ```bash
     brew install python
     ```
   - Wait for Python to install.

2. **Install Pillow and PyQt5**:
   - Next, install Pillow and PyQt5 by typing or copy/paste this into the Terminal:
     ```bash
     pip install Pillow PyQt5
     ```
   - Wait for them to install.


4. **Run Your Program**:
   - Navigate to the folder where your script is saved. For example, if it's in your Downloads folder, type:
     ```bash
     cd ~/Downloads/Image-Matrix-Generator-main\
     ```
   - Then, run the program by typing:
     ```bash
     python3 image_matrix_generator_1.0.py
     ```

---

#### For Windows:
1. **Check if Python is installed**:
   - Open **Command Prompt** (press `Win + R`, type "cmd", and press `Enter`).
   - Type `python --version` and press `Enter`.
   - If Python is installed, you'll see a version number. If not, go to step 2.

2. **Install Python**:
   - **Windows 10/11** often comes with Python. If not, type this command in Command Prompt:
     ```cmd
     python
     ```
   - Windows will guide you to install Python if it’s missing.

3. **Install PyQt5 and Pillow**

   For **PyQt5**:
   ```
   pip install PyQt5
   ```

   For **Pillow**:
   ```
   pip install Pillow
   ```

4. **Run Your Program**:
   - Open **Command Prompt** and type:
     ```cmd
     cd Downloads\Image-Matrix-Generator-main\
     ```
   - Then, run your script by typing:
     ```cmd
     python image_matrix_generator_1.0.py
     ```

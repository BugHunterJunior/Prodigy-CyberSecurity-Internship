<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:222222&height=180&section=header&text=Prodigy%20InfoTech%20Internship&fontSize=50&fontColor=00FF00&animation=fadeIn&desc=Cyber%20Security%20Internship&descSize=20&descAlignY=75&descAlign=50" alt="Prodigy Banner" />

<b>🔐 Caesar Cipher Desktop App</b>

<p>
  <img alt="Cyber Security" src="https://img.shields.io/badge/CyberSecurity-0A66C2?style=for-the-badge&logo=hackthebox&logoColor=white" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  <img alt="Platform" src="https://img.shields.io/badge/Prodigy-InfoTech-purple?style=for-the-badge" />
</p>
</div>
<!-- ## Preview
![Caesar Cipher App Preview]() -->

## Overview
This project is a modern, intuitive desktop utility that allows users to encrypt and decrypt text using the classic Caesar Cipher algorithm. It bridges a beautiful frontend UI with a lightweight Python backend using `pywebview`.

## Features
* **Dual Mode Functionality:** Seamlessly switch between Encrypt and Decrypt modes.
* **Native Desktop Experience:** Runs as a standalone application outside the browser.
* **Modern UI/UX:** Responsive, dark-themed interface built with vanilla HTML/CSS/JS.
* **Portable Execution:** Pre-compiled `.exe` file provided for zero-setup execution.

## Architecture
* **Frontend (HTML/CSS/JS):** Handles the user interface layout, styling, and the core Caesar Cipher logic.
* **Python (PyWebview):** Wraps the web-based frontend and renders it as a native, standalone desktop application window.
* **Executable (PyInstaller):** Converts the entire application and its dependencies into a standalone `.exe` file for easy distribution and execution.


## Tech Stack
* **Backend:** Python 3.11, `pywebview`, `pythonnet`
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Packaging:** PyInstaller

## ⚙️ Compatibility Note
* This project relies on `pywebview` and `pythonnet` to function correctly.
* It is confirmed to work stably with **Python 3.11**.
* Newer versions, such as Python 3.14, may experience compatibility issues with these dependencies and are currently not supported for compiling from source.

## 📂 Installation & Usage

### Method 1: Run from Source Code
1. **Install Python:** Ensure **Python 3.11** is installed. (You can use the provided [`python-3.11.9-amd64.exe`]() installer; ensure "Add Python to PATH" is checked during setup).
2. **Install Dependencies:** Open your terminal and install the required libraries:
```bash
pip install pywebview pythonnet
```
3. **Launch the App:** Run the main script:
```bash
py -3.11 app.py
```

### Method 2: Standalone Executable (Recommended)
*No Python installation required.*
1. Download [`Cipher.exe`]() from the repository files.
2. Double-click to launch the application instantly.


### 👨‍💻 Author: 
Shifting strings by 3 keys and sleep schedules by 12 hours. ⏳
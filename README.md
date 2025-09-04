# GedCounter - Automated Audit Tool for GED Digitalization

## Description
This application automates part of the digitalization audit process for the **GED (Electronic Document Management)** at the **Prefeitura Municipal de Angra dos Reis**. It scans selected folders, counts PDF files and pages, and generates an Excel report for verification.

This tool is open-source and free to use, designed to streamline the auditing process with efficiency and accuracy.

🚀 **Developed with dedication by Soarinho (Lucas Soares dos Santos)**, @osoarinho on Instagram.**

## Features
- 📂 **Folder Selection**: Easily choose a directory to process.
- 📄 **PDF Page Counting**: Automatically scans and counts the number of pages in each PDF.
- 📊 **Excel Report Generation**: Outputs a structured report for easy review.
- ✂️ **Automatic Adjustment**: Subtracts one page per file to account for the digital signature seal.
- ✅ **User-Friendly Execution**: Runs in a terminal with status updates for transparency.

## Installation & Usage
### Standalone Version (Windows)
The ready-to-use standalone application is available in the **Windows Standalone Exe** folder. Just run the executable and follow the on-screen instructions.

### Source Code
For those who want to **modify or improve** the application, the source code is available in the **Source Code** folder.

#### Running from Source
1. Install Python (if not already installed) and required dependencies:
   ```bash
   pip install pandas PyPDF2
   ```
2. Run the script:
   ```bash
   python GedCounter.py
   ```

#### Generating a New Executable
To create a new `.exe` from the source code:
1. Install **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. Navigate to the source code folder and run:
   ```bash
   pyinstaller --onefile --console --icon=icon.ico GedCounter.py
   ```
3. The new executable will be created inside the `dist` folder.

## License
This project is **open-source** and free to use. Feel free to contribute, modify, or improve!

---
The End.

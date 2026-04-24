<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:222222&height=180&section=header&text=Prodigy%20InfoTech%20Internship&fontSize=50&fontColor=00FF00&animation=fadeIn&desc=Cyber%20Security%20Internship&descSize=20&descAlignY=75&descAlign=50" />


<b>🔐 Password Complexity Checker</b>

<img src="https://img.shields.io/badge/CyberSecurity-0A66C2?style=for-the-badge&logo=hackthebox&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Platform-Prodigy%20InfoTech-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/CLI-Tool-black?style=for-the-badge&logo=gnubash" />
</div>

---


## Overview

A command-line security utility that evaluates password strength and checks for compromised credentials against the `rockyou.txt` dictionary — all in a clean, colorized terminal interface.

---

## Features

- **Breach Detection** — Cross-references your input against ~14 million known compromised passwords from `rockyou.txt` in real time.

- **Automated Dataset Provisioning** — Automatically downloads and extracts a compressed `rockyou.txt.gz` dataset directly from GitHub Releases on its first run, complete with a dynamic terminal progress bar. 

- **Auto-Cleanup** — Deletes the residual `.gz` archive immediately after extraction to optimize disk space.

- **Complexity Analysis** — Scores passwords across six criteria: length, extended length, uppercase, lowercase, digits, and special characters.

- **Secure Input Handling** — Uses Python's built-in `getpass` module to hide input in the terminal, preventing shoulder surfing.

- **Modern Terminal UI** — Powered by the `rich` library for color-coded output, strength labels, animated progress bars, and dynamic screen clearing.

- **Cross-Platform** — Works seamlessly on Windows, Kali Linux, and standard Linux distributions with built-in SSL bypasses for restrictive environments.
---

## Tech Stack
| Component | Detail |
|---|---|
| Language | Python 3.x 🐍 |
| External Library | `rich` 🎨 |
| Standard Libraries | `re`, `os`, `sys`, `getpass` ⚙️ |
| Dataset | `rockyou.txt` (pre-cleaned, bundled) 📂 |

---

## Installation & Setup ⚙️

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/BugHunterJunior/Prodigy-CyberSecurity-Internship.git
cd Prodigy-CyberSecurity-Internship
```

### 2. 📦 Install Dependencies

**Linux / macOS**
```bash
pip install -r requirements.txt
```

**Windows**
```bash
pip install rich
```

### 3. ▶️ Run the Script

```bash
python pass_checker.py
```

---

## ⚡ How It Works

```
[*] rockyou.txt not found in the current directory.
[+] Downloading rockyou.txt.gz... This may take a moment.
⠋ Downloading rockyou.txt.gz... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 15.0 MB/s
[+] Download complete!
[+] Extracting rockyou.txt.gz...
[+] Extraction complete!
[+] Deleted old rockyou.txt.gz file.

Enter password: ••••••••••••

Password: hunter2
Strength: 🟡 Medium  (Score: 3/6)
Feedback:
- Add uppercase letters
- Add special characters
```

```
Enter password: ••••••••••••

[COMPROMISED] — This password exists in a known data breach (rockyou.txt). DO NOT USE IT!
```

---

## 📈 Strength Scoring
| Score | Label |
|---|---|
| 0 – 2 | 🔴 Weak |
| 3 – 4 | 🟡 Medium |
| 5 – 6 | 🟢 Strong |
| In rockyou.txt | 🚨 Compromised |

---

## 👨‍💻 Author: 
### Your password vs brute force — tested here. 🛡️
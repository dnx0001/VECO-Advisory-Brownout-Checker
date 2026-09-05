<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" />
  <img src="https://img.shields.io/badge/version-v1.0.0-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/python-3.10+-blue" />
  <img src="https://img.shields.io/badge/platform-windows-lightgrey" />
</p>

# VECO Rotational Brownout Checker

A lightweight Python desktop application that helps users quickly identify **rotational brownout schedules** for any barangay/place mentioned in VECO advisories.

The app allows you to:

- Paste the full VECO advisory text  
- Enter any barangay/place (e.g., *Lahug, Apas, Banilad, Talamban, Camputhaw*)  
- Automatically extract:
  - All matching **brownout time windows**
  - The corresponding **tinyurl map links**
  - The **date** of the advisory  
- View results in a clean GUI  
- Optionally build a standalone `.exe` using PyInstaller  

---

## Features

- **User‑input barangay search:** Type any place and get all matching brownout entries.  
- **Unicode‑safe parsing:** Handles stylized VECO text like `𝟐:𝟎𝟎𝐏𝐌` by normalizing to ASCII.  
- **Multiple time windows:** Lists all time windows where the barangay appears.  
- **Map link extraction:** Shows the tinyurl map link for each matching block.  
- **Simple GUI:** Built with Tkinter, no external GUI frameworks.  
- **EXE‑ready:** Works with PyInstaller for easy distribution.

---

## Installation

### 1.📥 Download (windows)
[![Download EXE](https://img.shields.io/badge/Download-EXE-blue?style=for-the-badge)](https://github.com/dnx0001/VECO-Advisory-Brownout-Checker/raw/main/VECO%20Advisory%20Brownout%20Checker.exe)

### 2. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 💘 Proposal Collection

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![NiceGUI](https://img.shields.io/badge/UI-NiceGUI-purple?style=for-the-badge)

A fun, interactive Python application that asks: *"Do You Like Me?"* The catch? **The user physically cannot click "No".** The button evades the cursor, leaving "Yes" as the only option!

This repository contains **two versions** of the app:

| Version | Engine | Best For | Features |
| :--- | :--- | :--- | :--- |
| **Classic** | `Tkinter` | Compatibility | No installation required (Standard Lib). Lightweight, borderless window. |
| **Modern** | `NiceGUI` | Aesthetics | Requires installation. Uses Tailwind CSS, smooth animations, and shadows. |

---

## 📂 Version 1: The Classic (Tkinter)

Built using Python's standard GUI library. It creates a floating, borderless window with a custom "Dark Blue-Grey" theme.

### ✨ Features
* **Zero Dependencies:** Runs on standard Python installations without installing external libraries.
* **Smart Teleportation:** The "No" button calculates safe boundaries to ensure it never jumps off the visible window.
* **Borderless Design:** Uses `overrideredirect(True)` for a clean look.

### 🚀 How to Run

1.  Navigate to the folder.
2.  Run the script:
    ```bash
    python proposal_classic.py
    ```

*(Note: Linux users may need to run `sudo apt-get install python3-tk` if Tkinter isn't installed by default.)*

---

## 📂 Version 2: The Modern (NiceGUI)

Built using **NiceGUI**, a modern web-based UI framework that runs as a native desktop app. It leverages **Tailwind CSS** for styling.

### ✨ Features
* **Smooth Animations:** The "No" button glides to its new position rather than snapping instantly.
* **Modern UI:** Features drop shadows (`shadow-2xl`), rounded corners, and a bouncing heart animation on success.
* **Responsive:** Uses CSS percentages to keep elements centered regardless of window size.

### 🚀 How to Run

1.  **Install NiceGUI:**
    ```bash
    pip install nicegui
    ```
2.  **Run the script:**
    ```bash
    python proposal_modern.py
    ```

---

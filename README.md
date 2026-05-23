# Inventory Control System 📦

A lightweight, console-based Python application designed to audit and manage warehouse stock levels for computer hardware components. This project evaluates current inventory levels against predefined minimum safety stocks to generate an accurate procurement order list.

Developed as part of the **Programming Fundamentals** course at UNAD.

---

## 🚀 Features

* **Matrix-Based Inventory:** Utilizes a structured multidimensional array (matrix) to store core article data: `[Code, Name, Current Stock, Minimum Required Stock]`.
* **Automated Restock Calculation:** Features a dedicated logic function that evaluates shortages and determines the exact number of units to order.
* **Interactive Data Input:** Prompts the user to dynamically update current stock levels via the terminal before running the audit.
* **Clean Terminal Output:** Clears the console screen to present a clean, distraction-free summary of the required purchases.

---

## 🛠️ Requirements & Tech Stack

* **Language:** Python 3.13
* **Core Libraries:** `os` (for native terminal control)

No external dependencies or third-party installations are required.

# BDD-Based Web Automation Framework for Agrichain

## Overview
This is a **BDD-based Web Automation Framework** using **Selenium, Behave, and Python**. The framework follows the **Page Object Model (POM)** and is structured for maintainability and scalability.

---

## 📂 Project Directory Structure
```
/AgrichainBDD
  |-- features
  |   |-- agrichain.feature      # BDD test scenarios
  |   |-- steps
  |   |   |-- test_steps.py      # Step definitions
  |-- pages
  |   |-- base_page.py           # Common browser actions
  |   |-- input_page.py          # Page object for input page
  |   |-- result_page.py         # Page object for result page
  |-- locators
  |   |-- locators.py            # XPaths and CSS locators
  |-- utility
  |   |-- browser_setup.py       # WebDriver initialization
  |   |-- config.py              # Configurations (browser, URL)
  |-- reports
  |-- runner.py                  # Test execution script
  |-- requirements.txt           # Dependencies
```

---

---

## 🚀 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/AgrichainBDD.git
cd AgrichainBDD
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ WebDriver Setup**
Ensure you have the correct WebDriver installed and update `config.py`:
```python
class Config:
    BASE_URL = "https://agrichain.com/qa/input"
    DRIVER_PATH = "/path/to/chromedriver"  # Update this path
```

---

## 🔹 Running the Tests
Execute all tests using:
```bash
python runner.py
```

OR run specific features with:
```bash
behave features/agrichain.feature
```

---

## 🛠️ Framework Components
### **1️⃣ Locators (`locators.py`)**
Contains XPaths and CSS selectors for web elements.

### **2️⃣ Page Objects (`pages/`)**
Defines web page interactions using **Page Object Model (POM)**.

### **3️⃣ Step Definitions (`steps/test_steps.py`)**
Maps Gherkin steps to Python functions.

### **4️⃣ WebDriver Setup (`utility/browser_setup.py`)**
Handles browser initialization and teardown.

### **5️⃣ Configurations (`utility/config.py`)**
Manages base URL and WebDriver path.

### **6️⃣ Test Runner (`runner.py`)**
Executes test cases using Behave.

---

## 📌 Key Features
✅ **BDD with Behave** (Readable Gherkin Syntax)  
✅ **Page Object Model (POM)** (Reusable Components)  
✅ **WebDriver Setup & Configurations** (Easy Scalability)  
✅ **Reporting & Assertions** (Fail-proof Validation)  



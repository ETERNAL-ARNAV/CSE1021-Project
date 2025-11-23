# 📄 Project Report: Console Password Generator

### 1. Project Overview

#### Project Title
**Customizable Console Password Generator**

#### Executive Summary
This project is a command-line interface (CLI) utility built in **Python** designed to generate strong, customizable passwords. It offers two primary modes: generating a completely random password, or generating a password based on a user-provided **base string** which is then secured. Users select from three security levels (**Weak**, **Strong**, **Very Strong**) to control the complexity, character set, and length of the resulting password.

---
### 2. Technical Specifications

#### 💻 Technologies Used
| Component | Technology/Module | Purpose |
| :--- | :--- | :--- |
| **Language** | **Python 3.x** | Core development language. |
| **Randomization** | **random** | Used for character selection and injection point determination to ensure unpredictability. |
| **Aesthetics** | **pyfiglet** | Used for displaying the "PASSWORD GENERATOR" title in ASCII art. |
| **User Input** | **Standard CLI Input** | Handles user interaction for mode, strength, and base string input. |

---
### 3. System Workflow

#### 🔄 Project Workflow
The system follows a sequential, decision-based workflow:

1.  **Initialization:** Program starts and displays the **pyfiglet** welcome screen.
2.  **Mode Selection:** User selects between **Random Generation** or **Custom (Base String) Generation**.
3.  **Security Level Selection:** User chooses the password strength: **Weak**, **Strong**, or **Very Strong**.
4.  **Base String Input (Custom Mode Only):** If Custom mode is selected, the user inputs the base string.
5.  **Password Generation:** **Character sets** are dynamically built based on the security level. The code then either generates a full random sequence or modifies the base string with random characters.
6.  **Output:** The generated password is displayed.
7.  **Replay:** User is prompted to generate another password.



---
### 4. Code Structure and Key Logic

This section focuses on the **main processing blocks** within the script rather than specific function names, reflecting a single-script execution style.

#### 🔑 Core Logic Blocks

| Logic Block | Description | Key Mechanism |
| :--- | :--- | :--- |
| **Character Set Definition** | Defines static strings or lists for **lowercase, uppercase, numbers, and symbols**. | Allows the code to dynamically construct the full character pool based on user choice. |
| **Input Validation** | Handles user prompts for mode and security level, ensuring the input is valid before proceeding. | Uses basic loops and conditional checks to handle non-numeric or out-of-range input. |
| **Password Construction Logic** | The central part of the code that handles the **Random** and **Custom** generation modes. | Uses `random.choice()` or string insertion logic to select and position characters based on the dynamic character pool and required length/salt factor. |
| **Loop & Exit** | Manages the primary execution cycle, allowing the user to generate multiple passwords until they choose to exit. | Controlled by a main `while` loop that can be broken when the user declines to generate another password. |

---
### 5. Security Levels and Character Complexity

| Level | Base Length / Salt Factor | Character Sets Used | Complexity |
| :--- | :--- | :--- | :--- |
| **Weak** | Short | Lowercase, Numbers | Low. |
| **Strong** | Moderate | Lowercase, Uppercase, Numbers | High. Standard for secure accounts. |
| **Very Strong** | Long | Lowercase, Uppercase, Numbers, **Symbols** | Maximum. Highly resistant to brute-force attacks. |
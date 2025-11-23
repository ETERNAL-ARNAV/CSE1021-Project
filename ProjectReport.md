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
| **Data Handling** | **array / Standard List** | Used for managing and manipulating character sets and the base string. |

---
### 3. System Workflow

#### 🔄 Project Workflow
The system follows a sequential, decision-based workflow:

1.  **Initialization:** Program starts and displays the **pyfiglet** welcome screen.
2.  **Mode Selection:** User selects between **Random Generation** or **Custom (Base String) Generation**.
3.  **Security Level Selection:** User chooses the password strength: **Weak**, **Strong**, or **Very Strong**.
4.  **Base String Input (Custom Mode Only):** If Custom mode is selected, the user inputs the base string.
5.  **Password Generation:** The appropriate function is called to build the password based on the selected mode and character pool defined by the security level.
6.  **Output:** The generated password is displayed.
7.  **Replay:** User is prompted to generate another password.



---
### 4. Code Structure and Key Functions

The code is organized into functions managing character sets, user interaction, and the core generation logic.

#### 🔑 Core Logic Functions

| Function Name | Description | Logic Detail |
| :--- | :--- | :--- |
| `get_security_level()` | Handles user input for the strength options (1, 2, or 3). | Includes input validation. |
| `get_character_pool(level)` | **Builds the character set** based on the chosen security level (e.g., adds symbols for 'Very Strong'). |
| `generate_random_password(pool, length)` | **Core for Random Mode.** Randomly selects characters from the `pool` until the target `length` is reached. |
| `generate_custom_password(base_string, pool, strength)` | **Core for Custom Mode.** Takes the `base_string` and **randomly injects** characters from the `pool` into it to increase security. |
| `main_generator_loop()` | Main driver function that handles mode selection, function calls, output, and the replay mechanism. |

---
### 5. Security Levels and Character Complexity

| Level | Base Length / Salt Factor | Character Sets Used | Complexity |
| :--- | :--- | :--- | :--- |
| **Weak** | Short (e.g., 8-10 chars) | Lowercase, Numbers | Low. |
| **Strong** | Moderate (e.g., 12-16 chars) | Lowercase, Uppercase, Numbers | High. Standard for secure accounts. |
| **Very Strong** | Long (e.g., 16-24+ chars) | Lowercase, Uppercase, Numbers, **Symbols** | Maximum. Highly resistant to brute-force attacks. |
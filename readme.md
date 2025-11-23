# 🔑 Password Generator

A simple, yet powerful command-line utility written in Python for generating both completely random passwords and customized passwords based on a user-provided base string.

## ✨ Features

* **Two Generation Modes:**
    * **Random:** Generate a completely random and secure password.
    * **Custom:** Provide a base string (e.g., a memorable phrase) and enhance it with random characters to increase security.
* **Three Security Levels:**
    * **Weak:** Basic characters, suitable for simple use.
    * **Strong:** Includes uppercase, lowercase, and numbers.
    * **Very Strong:** Includes uppercase, lowercase, numbers, and special symbols for maximum security.
* **Single File Execution:** Easy to run as a standalone Python script.
* **Aesthetic Output:** Uses **pyfiglet** for stylish console headings.

---

## 🛠️ Built With

This project is built entirely in **Python** and relies on its standard library and one third-party library:

* **Python 3.x**
* **`random`**: For generating random sequences and characters.
* **`string`**: For capitalizing and conacatenation methods.
* **`array`**: Used for internal data handling (though often the standard Python lists are preferred for general use).

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3.x** installed on your system.

### Installation

1.  **Clone the Repository (or download the script):**
    ```bash
    git clone [https://github.com/YourUsername/your-project-name.git](https://github.com/YourUsername/your-project-name.git)
    cd your-project-name
    ```
---

## 💡 Usage

The program is executed via the command line. When you run the script, it will prompt you to choose a generation mode and a security level.

### Running the Script

Execute the single Python file:

```bash
python password_generator.py
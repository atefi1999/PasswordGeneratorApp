# 🔐 Password Generator CLI App

### A simple and interactive CLI application to generate, save, and view secure passwords with customizable options.

---

## 🛠 Features

- Generate random passwords with:
  - Digits
  - Symbols
  - Uppercase letters
  - Lowercase letters
- Save generated passwords to a file (`passwords.txt`)
- View all saved passwords
- Interactive command-line interface

---

## ⚡ Usage

### 1. Run the application:

```bash
python password_generator_cli_app.py
```

### 2. Follow the menu:

```bash
🔐 Password Generator CLI
1️⃣ Generate a new password
2️⃣ View saved passwords
3️⃣ Exit
```

### 3. If generating a password, provide:

```bash
Password length
Use digits? (y/n)
Use symbols? (y/n)
Use uppercase letters? (y/n)
Use lowercase letters? (y/n)
```

### 4. Optionally save the password to (`passwords.txt`)

#### 📌 Example Output

```bash
🔐 Password Generator CLI
1️⃣ Generate a new password
2️⃣ View saved passwords
3️⃣ Exit
👉 Choose an option: 1
📏 Password length: 12
Use digits? (y/n): y
Use symbols? (y/n): y
Use uppercase letters? (y/n): y
Use lowercase letters? (y/n): y
✅ Password generated: G7!k2$hQ9@Lw
Do you want to save it? (y/n): y
💾 Password saved to passwords.txt.

📂 Saved passwords:
1. G7!k2$hQ9@Lw
```
---
## 🎥 Demo

<img  alt="screenshot"  src="https://github.com/user-attachments/assets/f83daecd-336c-400d-b976-8cd55b82f23c"  width="50%" />

---

## 📝 Notes

- This is a command-line application; no GUI.
- Make sure to keep passwords.txt secure.
- Python 3.6+ recommended

---

## 📂 Project Structure
```markdown
.
├── password_generator_cli_app.py # Main CLI application
├── passwords.txt # File to store generated passwords
└── README.md # Project documentation
```

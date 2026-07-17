# 🚀 AEVRION Programming Language v0.4

> A lightweight, beginner-friendly programming language built in Python.

---

## ✨ Features

- ⚡ Fast and lightweight
- 🖥️ Interactive REPL (Shell)
- 📄 Execute `.avr` source files
- 🔤 Variables
- ➕ Arithmetic operations
- 📢 Built-in `print()`
- ⌨️ Built-in `input()`
- 🎨 Colored terminal output
- 📦 Easy to install

---

# 📂 Project Structure

```
AEVRION_v0.4/
│
├── examples/
│   ├── hello.avr
│   ├── variables.avr
│   └── math.avr
│
├── src/
│   ├── lexer.py
│   ├── parser.py
│   ├── interpreter.py
│   ├── shell.py
│   ├── builtins.py
│   ├── banner.py
│   ├── colors.py
│   └── ...
│
├── main.py
├── aevrion
├── version.py
├── requirements.txt
└── README.md
```

---

# 📥 Installation (Termux)

## 1. Update packages

```bash
pkg update -y
pkg upgrade -y
```

## 2. Install Python & Git

```bash
pkg install python git -y
```

## 3. Clone the repository

```bash
git clone https://github.com/LEGENDDATABASEOFFICIAL/AEVRION.git
```

## 4. Open the project

```bash
cd AEVRION_v0.4
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, skip this step.

## 6. Run AEVRION

```bash
python main.py
```

or

```bash
./aevrion
```

---

# 🚀 Usage

Start the interactive shell:

```bash
python main.py
```

Example:

```avr
print("Hello World")
```

Output

```text
Hello World
```

---

# 📄 Run an AEVRION Program

```bash
python main.py examples/hello.avr
```

---

# 📝 Examples

## Hello World

```avr
print("Hello, World!")
```

---

## Variables

```avr
let name = "AEVRION"

print(name)
```

---

## Math

```avr
let a = 10
let b = 20

print(a + b)
print(a * b)
```

---

## User Input

```avr
let name = input("Enter your name: ")

print("Hello")
print(name)
```

---

# 📚 Commands

Run shell

```bash
python main.py
```

Run file

```bash
python main.py program.avr
```

Make launcher executable

```bash
chmod +x aevrion
```

Run launcher

```bash
./aevrion
```

---

# 🛠 Troubleshooting

### ModuleNotFoundError

```bash
pip install -r requirements.txt
```

---

### Permission denied

```bash
chmod +x aevrion
```

---

### Python not found

```bash
pkg install python -y
```

---

### Git not found

```bash
pkg install git -y
```

---

### Command not working

```bash
pkg update
pkg upgrade
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ashraful Ahmed**

Creator of **AEVRION Programming Language**

Built with ❤️ using Python.

---

⭐ If you like **AEVRION**, don't forget to star the repository!

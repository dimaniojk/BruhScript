# BruhScript

👊 **BruhScript** is a meme-based programming language that combines humor with real power. It’s designed to be simple, fun, and practical for automating tasks, working with files, and interacting with APIs.

---

## Features
- **Meme syntax:** Easy to read and use.
- **Extensibility:** Add new commands through plugins.
- **Practicality:** Ideal for file management, API interactions, and basic scripting.
- **Learning-friendly:** Perfect for beginners in programming.

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/BruhScript.git
cd BruhScript
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Example Usage

### **Hello World**
```txt
bruh start
yeet "Hello, world!"
bruh end
```

### **Arithmetic**
```txt
bruh start
set x 10
set y 20
add x y result
yeet "The sum of {x} and {y} is {result}"
bruh end
```

### **Working with Plugins**
```txt
bruh start
load_plugin "src/plugins/math_plugin.py"
math_add 15 25 sum
yeet "Sum from plugin: {sum}"
math_multiply 5 6 product
yeet "Product from plugin: {product}"
bruh end
```

### **File Operations**
```txt
bruh start
write_file "test.txt" "Hello, BruhScript!"
read_file "test.txt" content
yeet "File content: {content}"
bruh end
```

---

## How Plugins Work
1. Create a Python file (e.g., `custom_plugin.py`).
2. Add functions inside it:
   ```python
   def custom_command(arg, variables):
       variables["result"] = f"Processed {arg}"
       return variables
   ```
3. Load the plugin in your script:
   ```txt
   load_plugin "custom_plugin.py"
   custom_command "Test input"
   yeet "Result: {result}"
   ```

---

## Supported Commands

### **Core Commands**
| Command            | Description                                   | Example                                     |
|--------------------|-----------------------------------------------|--------------------------------------------|
| `bruh start`       | Start of the program                         | `bruh start`                               |
| `bruh end`         | End of the program                           | `bruh end`                                 |
| `yeet`             | Print text                                   | `yeet "Hello, world!"`                     |
| `set`              | Set a variable                               | `set x 10`                                 |
| `add`              | Add two variables                            | `add x y result`                           |

### **Plugins**
| Command            | Description                                   | Example                                     |
|--------------------|-----------------------------------------------|--------------------------------------------|
| `load_plugin`      | Load a plugin                                | `load_plugin "math_plugin.py"`             |
| `math_add`         | Addition (from `math_plugin`)                | `math_add 10 20 result`                    |
| `math_multiply`    | Multiplication (from `math_plugin`)          | `math_multiply 5 6 result`                 |

### **File Operations**
| Command            | Description                                   | Example                                     |
|--------------------|-----------------------------------------------|--------------------------------------------|
| `write_file`       | Write data to a file                         | `write_file "example.txt" "Hello!"`        |
| `read_file`        | Read data from a file                        | `read_file "example.txt" content`          |

---

## Plugins
Available plugins:
1. **math_plugin.py:** Arithmetic operations.
2. **file_plugin.py:** File management.

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make changes and commit them:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push your branch and create a Pull Request!

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Enjoy coding with BruhScript! 🚀

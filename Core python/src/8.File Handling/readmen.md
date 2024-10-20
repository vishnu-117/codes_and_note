with open('filename', 'a') as f: # able to append data to file
	f.write(var1) # Were var1 is some variable you have set previously
	f.write('data') 
	f.close() 

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, returns an error if the file does not exist
"w+" - Write - Opens a file for writing, creates one if the file does not exist.
"x" - Create - Creates the specified file, returns an error if the file exists


Here’s a comprehensive list of functions and methods used for **file handling** in Python, including a brief description of when to use each function:

### **1. File Handling Functions**

1. **`open()`**
   - Opens a file and returns a file object.
   - **When to use**: Whenever you need to read, write, or append to a file.
   - **Example**:
     ```python
     file = open('file.txt', 'r')
     ```

2. **`close()`**
   - Closes the file.
   - **When to use**: After performing file operations to release system resources.
   - **Example**:
     ```python
     file.close()
     ```

---

### **2. File Read Methods**

1. **`read()`**
   - Reads the entire content of the file as a string.
   - **When to use**: When you want to read the entire file content at once.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         content = file.read()
     ```

2. **`readline()`**
   - Reads a single line from the file.
   - **When to use**: When you want to read the file line by line but don't want all lines at once.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         line = file.readline()
     ```

3. **`readlines()`**
   - Reads all the lines of the file and returns a list of lines.
   - **When to use**: When you want to read all lines at once, but in a list format.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         lines = file.readlines()
     ```

4. **File Iteration**
   - Iterating over a file object reads the file line by line.
   - **When to use**: For large files, where reading line by line is more memory efficient.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         for line in file:
             print(line)
     ```

---

### **3. File Write Methods**

1. **`write()`**
   - Writes a string to the file.
   - **When to use**: When you want to write or overwrite content in a file.
   - **Example**:
     ```python
     with open('file.txt', 'w') as file:
         file.write("This is some text.")
     ```

2. **`writelines()`**
   - Writes a list of strings to the file.
   - **When to use**: When you want to write multiple lines at once from a list.
   - **Example**:
     ```python
     lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
     with open('file.txt', 'w') as file:
         file.writelines(lines)
     ```

---

### **4. File Modes**

These modes are used with the `open()` function to specify how the file should be accessed:
1. **`'r'`**: Read mode (default mode, file must exist).
2. **`'w'`**: Write mode (creates a new file or truncates an existing file).
3. **`'a'`**: Append mode (adds to the file without truncating).
4. **`'b'`**: Binary mode (used for binary files, like images or videos).
5. **`'t'`**: Text mode (default mode for reading and writing files).
6. **`'x'`**: Exclusive creation (fails if the file exists).

---

### **5. File Pointer Methods**

1. **`tell()`**
   - Returns the current file position (in bytes).
   - **When to use**: To find out where the current position of the file pointer is.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         print(file.tell())  # Output: current position in file
     ```

2. **`seek(offset, whence)`**
   - Moves the file pointer to a specified position.
   - **When to use**: To move the file pointer to a specific location for reading or writing.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         file.seek(5)  # Moves to the 5th byte
         print(file.read())  # Reads from the 5th byte onwards
     ```

---

### **6. File Information Methods**

1. **`flush()`**
   - Flushes the write buffer of the file, forcing any buffered output to be written to disk.
   - **When to use**: When writing to a file and you want to ensure the data is written to disk immediately.
   - **Example**:
     ```python
     with open('file.txt', 'w') as file:
         file.write("Some data")
         file.flush()  # Ensures the data is written immediately
     ```

2. **`fileno()`**
   - Returns the file descriptor, which is a number representing the file opened by the OS.
   - **When to use**: To get the file descriptor number if needed for low-level I/O operations.
   - **Example**:
     ```python
     with open('file.txt', 'r') as file:
         print(file.fileno())  # Outputs file descriptor number
     ```

---

### **7. Handling Binary Files**

1. **Reading Binary Files (`'rb'`)**:
   - Reads a file in binary mode.
   - **When to use**: When reading non-text files like images or videos.
   - **Example**:
     ```python
     with open('image.png', 'rb') as file:
         binary_data = file.read()
     ```

2. **Writing Binary Files (`'wb'`)**:
   - Writes data in binary mode.
   - **When to use**: When writing to non-text files.
   - **Example**:
     ```python
     with open('output_image.png', 'wb') as file:
         file.write(binary_data)
     ```

---

### **8. File Operations with Pathlib**

For modern file handling, Python's `pathlib` module is more intuitive:

1. **`Path().write_text()`**: Writes text to a file using `pathlib`.
   ```python
   from pathlib import Path
   Path('example.txt').write_text("Hello, World!")
   ```

2. **`Path().read_text()`**: Reads text from a file using `pathlib`.
   ```python
   content = Path('example.txt').read_text()
   print(content)
   ```

---

### **Summary**

Here’s a quick summary of the most common file handling methods:

- **Open/Close File**: `open()`, `close()`
- **Reading Files**: `read()`, `readline()`, `readlines()`
- **Writing Files**: `write()`, `writelines()`
- **Pointer Control**: `tell()`, `seek()`
- **Other**: `flush()`, `fileno()`

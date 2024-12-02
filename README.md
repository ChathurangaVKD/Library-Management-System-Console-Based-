# Library Management System (Console-based)

## Project Overview  
This Library Management System is a console-based application developed using Python. It emphasizes foundational programming concepts learned throughout the course, including problem-solving, code organization, and efficient use of control structures, data types, functions, and data structures. The project demonstrates the principles of **Object-Oriented Programming (OOP)** and follows the **SOLID design principles** to ensure modularity, maintainability, and scalability.

The application allows users to manage a library system, including adding, searching, borrowing, and returning books. By utilizing different control structures, the code ensures smooth interaction with the user while adhering to OOP concepts to keep the code organized and efficient.

---

## Project Structure  
The code consists of three main components, each following principles of Object-Oriented Programming (OOP) to keep the code modular, maintainable, and scalable:

1. **`book.py`:**  
   Defines the `Book` class that holds the attributes and methods for each book.

2. **`library.py`:**  
   Defines the `Library` class that manages the collection of books and the core functionality of borrowing, returning, adding, and searching for books.

3. **`library_ui.py`:**  
   Handles the user interface by displaying the menu and interacting with the user to carry out library operations.

Each class is designed to follow the SOLID principles and ensure that changes and extensions can be made easily without affecting the core system.

---

## Key Features  

1. **Add Book:**  
   Users can add new books to the library by providing the title and author.  

2. **Display Books:**  
   View the entire collection of books, including their availability status.  

3. **Search Book:**  
   Search for books by title or author. Partial matches are supported.  

4. **Borrow Book:**  
   Borrow a book by specifying its title. The system checks availability and updates the status accordingly.  

5. **Return Book:**  
   Return a borrowed book, updating its availability status.  

6. **Exit:**  
   Safely exits the program.  

---

## Technologies Used  
- **Programming Language**: Python  
- **Design Patterns**: Singleton Pattern for the `Library` class  
- **Principles**:  
  - **OOP**: Classes (`Book`, `Library`, `LibraryUI`) encapsulate data and behavior.  
  - **SOLID Principles**: Ensures each class has a single responsibility and follows dependency inversion.  

---

## Installation and Setup  
1. **Prerequisites:**  
   Ensure Python 3.x is installed on your system.  


2. **Clone the Repository:**  
   ```bash  
   git clone https://github.com/your-repository/library-management-system.git  
   cd library-management-system

3. **Run the Program:**
   Open a terminal and run:
   ```bash
   python library_ui.py

## Usage Instructions

1. **Start the Program:**
   After running the program, the main menu will be displayed, providing you with several options:
   - Add a new book to the library.
   - Display all books in the library.
   - Search for books by title or author.
   - Borrow or return books.
   - Exit the program.

2. **Follow Prompts:**
   - Enter the corresponding number for the action you wish to perform.
   - If prompted, provide details such as the book title or author. The program will guide you through each action.

3. **Exit Gracefully:**
   - When you’re finished, select option `6` from the menu to exit the application.
# Quick-Calc — Software Testing Assignment

## Project Description

Quick-Calc is a simple calculator application developed for the Advanced Software Engineering course.  
The application performs basic arithmetic operations including addition, subtraction, multiplication, and division.

The calculator also includes:
- handling of division by zero
- support for negative numbers and decimal numbers
- a clear function to reset the calculator

The main goal of this project is to demonstrate clean code structure, automated testing, and proper use of Git and GitHub version control.

---

## Setup Instructions

1. Clone the repository

git clone https://github.com/Shivam-0128/swe-testing-assignment.git

2. Navigate to the project folder

cd swe-testing-assignment

3. Install dependencies

pip install -r requirements.txt

---

## Running the Application

You can run the calculator using:

python app.py

---

## How to Run Tests

All tests are written using the Pytest framework.

To execute the test suite run:

python -m pytest

This will run all unit tests and integration tests located in the **tests/** directory.

---

## Testing Framework Comparison: Pytest vs Unittest

Python provides multiple testing frameworks for automated testing. Two of the most commonly used frameworks are **Unittest** and **Pytest**.

**Unittest** is the built-in testing framework included with Python. It is inspired by Java's JUnit framework and uses a class-based structure for writing tests. While it is powerful and reliable, it often requires more boilerplate code and can make simple tests harder to read.

**Pytest**, on the other hand, is a modern testing framework designed to simplify test writing. It allows developers to write tests using simple functions instead of classes, automatically discovers test files, and provides detailed error messages when tests fail. Pytest also supports advanced features such as fixtures, parameterized tests, and plugins.

For this project **Pytest was chosen** because it allows cleaner test syntax, easier test discovery, and faster development of the testing suite.

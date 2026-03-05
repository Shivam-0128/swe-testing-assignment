&nbsp;Testing Strategy — Quick-Calc



This document explains the testing strategy used for the Quick-Calc calculator application.  

The goal of testing was to verify that all calculator operations work correctly and that the system handles edge cases such as division by zero.



The tests were written using the \*\*Pytest\*\* framework and are located in the `tests/` directory.



All tests can be executed with the command:



python -m pytest





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;1. Overview



Quick-Calc is a simple calculator application written in Python.  

The testing approach focuses on verifying the correctness of the core calculation logic and ensuring that the calculator behaves correctly during normal operations and edge cases.



Two types of tests were implemented:



\- \*\*Unit Tests\*\* – testing individual calculator functions

\- \*\*Integration Tests\*\* – testing how different parts of the application work together





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;2. What Was Tested



The following features were tested:



\- Addition of two numbers

\- Subtraction of two numbers

\- Multiplication of two numbers

\- Division of two numbers

\- Division by zero handling

\- Operations with negative numbers

\- Operations with decimal numbers

\- Operations with very large numbers

\- Clear function resetting the result to zero

\- A full calculation flow simulating user interaction



These tests ensure that the calculator behaves correctly for both normal inputs and edge cases.





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;3. What Was NOT Tested



Some areas were intentionally not tested because they are outside the scope of this assignment:



--Performance testing--  

The calculator is a very small application and does not process large workloads, so performance testing was unnecessary.



--Security testing--  

The application does not handle sensitive data or network communication.



--User interface testing--  

The assignment specifically states that the focus should be on code and testing quality rather than the UI.



--Cross-platform testing--  

The application was tested only in the development environment.





-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;4. Testing Concepts from Lecture



&nbsp;4.1 Testing Pyramid



The testing pyramid suggests that most tests should be unit tests, with fewer integration tests and even fewer end-to-end tests.



This project follows that structure:



| Test Layer | Number of Tests |

|------------|----------------|

| Unit Tests | 8 |

| Integration Tests | 2 |



Unit tests form the majority because they are fast, simple, and test the core logic directly.





-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;4.2 Black-Box vs White-Box Testing



--White-box testing-- means the tester understands the internal code and tests specific functions directly.



--Black-box testing-- focuses only on inputs and outputs without considering the internal implementation.



In this project:



\- Unit tests follow a --white-box approach-- because they directly test methods of the `Calculator` class.

\- Integration tests follow a --black-box approach-- because they simulate user actions and verify the final result.





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





&nbsp;4.3 Functional vs Non-Functional Testing



The tests in this project focus on \*\*functional testing\*\*.



Functional testing verifies that the system performs the correct calculations based on the input.



Examples include:



\- verifying that `5 + 3 = 8`

\- verifying that division by zero raises an error

\- verifying that the clear function resets the result



Non-functional aspects such as performance, security, or usability were not tested because they are not critical for this small application.





---------------------------------------------------------------------------------------------------------------------------------------------------------------------------





&nbsp;4.4 Regression Testing



The test suite can also be used for --regression testing--.



Whenever changes are made to the calculator code, running the test suite will ensure that existing functionality still works correctly.



If a previously working feature stops working, the failing test will immediately reveal the issue.





--------------------------------------------------------------------------------------------------------------------------------------------------------------------------



&nbsp;5. Test Results Summary



All tests were executed using --Pytest-- and passed successfully.



| Test Name | Type | Result |

|----------|------|--------|

| test\_add | Unit | Passed |

| test\_subtract | Unit | Passed |

| test\_multiply | Unit | Passed |

| test\_divide | Unit | Passed |

| test\_divide\_by\_zero | Unit | Passed |

| test\_negative\_numbers | Unit | Passed |

| test\_decimal\_numbers | Unit | Passed |

| test\_large\_numbers | Unit | Passed |

| test\_full\_addition\_flow | Integration | Passed |

| test\_clear\_after\_operation | Integration | Passed |


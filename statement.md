Project Statement

Lottery Eligibility Checker

Problem Statement

Develop a web-based Python application that accepts a lottery number from the user and determines the user's eligibility and lottery category based on predefined numerical conditions.

The application should initially display a welcome message such as "Hello User" and provide an input field where the user can enter their lottery number.

After receiving the lottery number, the application must calculate the sum of its digits.

Functional Requirements

The system should follow these conditions:

1. Accept a lottery number from the user.

2. Calculate the sum of all digits in the lottery number.

3. If the sum of the digits is odd, display:
   
   "Better Luck Next Time!"

4. If the sum of the digits is even, the user becomes eligible.

5. For an eligible number, check whether the lottery number is a multiple of 5.

6. If it is a multiple of 5, display:
   
   "Gifts Only"

7. If it is not a multiple of 5, check whether the lottery number contains any prime digit.

8. The prime digits considered are:
   
   2, 3, 5, 7

9. If the number contains at least one prime digit, display:
   
   "Higher Wins"

10. If the number does not contain any prime digit, display:

"Lower Wins"

Expected Processing Logic

Input Lottery Number
        ↓
Calculate Digit Sum
        ↓
Check Even/Odd
        ↓
Odd → Not Eligible
        ↓
Even → Eligible
        ↓
Check Multiple of 5
   ↓              ↓
 Yes              No
 ↓                 ↓
Gifts Only    Check Prime Digit
                    ↓
             ┌──────┴──────┐
            Yes            No
             ↓              ↓
       Higher Wins     Lower Wins

Example Cases

Lottery Number| Digit Sum| Result
1246| 13| Not Eligible
1234| 10| Higher Wins
2468| 20| Higher Wins
1111| 4| Lower Wins
1250| 8| Gifts Only

Technical Requirements

The application should be developed using:

- Python
- Flask framework
- HTML
- CSS

The project should be organized into separate files for Python logic, HTML templates, and CSS styling.

Expected Outcome

The final application should provide a simple and user-friendly interface where the user enters a lottery number and immediately receives an eligibility result and, when applicable, a corresponding winning category.

The project is intended to demonstrate basic Python programming, logical decision-making, web development, and GitHub project organization.

Project Purpose

This project is developed for educational purposes to demonstrate how programming logic can be integrated into a simple web application.
Lottery Eligibility Checker

📌 Project Overview

The Lottery Eligibility Checker is a simple Python-based web application developed using Flask. It allows a user to enter a lottery number and determines their eligibility and winning category according to predefined rules.

The project demonstrates the use of Python functions, conditional statements, loops, HTML forms, Flask routing, and basic CSS styling.

🎯 Objective

The main objective of this project is to create a simple web-based lottery eligibility system where:

- The user enters a lottery number.
- The sum of the digits is calculated.
- The digit sum determines the basic eligibility.
- Prime digits determine the winning category.
- Numbers that are multiples of 5 are eligible for gifts only.

🧠 Eligibility Rules

The application follows these rules:

1. The sum of all digits of the lottery number is calculated.
2. If the digit sum is odd, the user is not eligible.
3. If the digit sum is even, the user is eligible.
4. If an eligible number is a multiple of 5, the user is eligible for Gifts Only.
5. If an eligible number contains a prime digit ("2, 3, 5, or 7"), the user is eligible for Higher Wins.
6. If an eligible number does not contain a prime digit, the user is eligible for Lower Wins.

🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Git
- GitHub
- Visual Studio Code

📂 Project Structure

lottery-website/
│
├── app.py
├── README.md
├── STATEMENT.md
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

⚙️ How to Run the Project

Step 1: Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open the project

Open the project folder in Visual Studio Code.

Step 3: Create a virtual environment

python -m venv venv

Step 4: Activate the virtual environment

For Windows:

venv\Scripts\activate

Step 5: Install the required package

pip install -r requirements.txt

Step 6: Run the application

python app.py

Step 7: Open the website

Open the local Flask address shown in the terminal, usually:

http://127.0.0.1:5000

🔄 Working Flow

Start
  ↓
Display "Hello User"
  ↓
Enter Lottery Number
  ↓
Calculate Sum of Digits
  ↓
Is the Sum Even?
  ├── No → Better Luck Next Time
  │
  └── Yes
       ↓
    Is Number a Multiple of 5?
       ├── Yes → Gifts Only
       │
       └── No
            ↓
       Contains Prime Digit?
       ├── Yes → Higher Wins
       │
       └── No → Lower Wins

🧪 Example

For the lottery number:

1234

Digit sum:

1 + 2 + 3 + 4 = 10

Since 10 is even, the number is eligible.

The number contains the prime digits "2" and "3", so the result is:

Higher Wins

📚 Learning Outcomes

Through this project, the following concepts are practiced:

- Python variables and data types
- Functions
- "if-else" conditions
- Loops
- Lists
- User input handling
- Number and digit operations
- Flask routing
- HTML forms
- CSS styling
- Basic web application development
- Git and GitHub project management

⚠️ Disclaimer

This project is created for educational and programming practice purposes only. It is a simulated lottery eligibility system and does not represent a real-money lottery or gambling service.

👩‍💻 Author

[Your Name]

B.Tech CSE (AI & ML)
VIT Bhopal University

📄 License

This project is intended for educational purposes.
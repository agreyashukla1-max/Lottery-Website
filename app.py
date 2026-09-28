from flask import Flask, render_template, request

app = Flask(__name__)


# Check whether a digit is prime
def is_prime_digit(digit):
    return digit in [2, 3, 5, 7]


# Calculate the sum of digits
def digit_sum(number):
    return sum(int(digit) for digit in str(number))


# Decide lottery eligibility
def check_lottery(number):
    total = digit_sum(number)

    # Rule 1: Odd digit sum = not eligible
    if total % 2 != 0:
        return {
            "eligible": False,
            "message": "Better luck next time!",
            "type": None
        }

    # Rule 2: Multiple of 5 = gifts only
    if number % 5 == 0:
        return {
            "eligible": True,
            "message": "Congratulations!",
            "type": "Gifts Only"
        }

    # Rule 3: Contains a prime digit = higher wins
    digits = [int(digit) for digit in str(number)]

    if any(is_prime_digit(digit) for digit in digits):
        return {
            "eligible": True,
            "message": "Congratulations!",
            "type": "Higher Wins"
        }

    # Rule 4: No prime digit = lower wins
    return {
        "eligible": True,
        "message": "Congratulations!",
        "type": "Lower Wins"
    }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        lottery_number = request.form.get("lottery_number")

        try:
            number = int(lottery_number)

            if number < 0:
                result = {
                    "eligible": False,
                    "message": "Please enter a valid positive lottery number.",
                    "type": None
                }
            else:
                result = check_lottery(number)

        except ValueError:
            result = {
                "eligible": False,
                "message": "Please enter a valid number.",
                "type": None
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)


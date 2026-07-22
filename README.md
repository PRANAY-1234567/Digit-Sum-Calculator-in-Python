# Digit Sum Calculator in Python

## 📌 Overview


This project is a simple Python program that calculates the **sum of the digits** of a given positive integer.

The program repeatedly extracts the last digit of the number using the modulus (`%`) operator, adds it to a running total, and removes the last digit using integer division (`//`) until the number becomes zero.

This project is ideal for beginners learning loops, arithmetic operators, and number manipulation in Python.

---

## 🚀 Features

* Accepts a positive integer from the user
* Extracts each digit individually
* Calculates the sum of all digits
* Uses a `while` loop for digit processing
* Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
├── digit_sum.py
└── README.md
```

---

## 💻 Source Code

```python
num = int(input("Enter any number : "))

digit_sum = 0

while num > 0:
    digit = num % 10
    num //= 10
    digit_sum += digit

print("The digit sum is", digit_sum)
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-digit-sum.git
cd python-digit-sum
```

### Run the Program

```bash
python digit_sum.py
```

---

## 📋 Sample Output

### Example 1

```text
Enter any number : 5873
The digit sum is 23
```

### Example 2

```text
Enter any number : 12345
The digit sum is 15
```

### Example 3

```text
Enter any number : 999
The digit sum is 27
```

---

## 🧠 Concepts Covered

* User Input
* `while` Loop
* Modulus (`%`) Operator
* Integer Division (`//`)
* Number Manipulation
* Arithmetic Operations

---

## 🔍 How It Works

1. Read an integer from the user.
2. Initialize `digit_sum` to **0**.
3. Repeat while the number is greater than **0**:

   * Extract the last digit using `% 10`.
   * Add the digit to `digit_sum`.
   * Remove the last digit using `// 10`.
4. Display the final sum of all digits.

---

## 📖 Algorithm

1. Start the program.
2. Input a positive integer.
3. Set `digit_sum = 0`.
4. While the number is greater than 0:

   * Find the last digit.
   * Add it to `digit_sum`.
   * Remove the last digit.
5. Print the sum of the digits.
6. End the program.

---

## ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(d)**   |
| Space Complexity | **O(1)**   |

Where **d** is the number of digits in the input number.

---

## 🔮 Future Improvements

* Support negative numbers
* Calculate the product of digits
* Reverse the entered number
* Check whether the number is a palindrome
* Find the largest and smallest digit
* Build a menu-driven number utility application

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How to extract digits from an integer
* How modulus and integer division work
* How to use loops for number processing
* Basic arithmetic operations in Python
* Writing clean and efficient Python programs

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software Engineer | Python | Java | SQL | Data Analytics

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="508" height="480" alt="image" src="https://github.com/user-attachments/assets/c5aa7561-63c1-4e27-bee1-b4db8ecebb7b" />

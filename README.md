# Python-Bootcamp
# Python Fundamentals & Mini-Projects

Welcome to this repository! This collection features a series of Python script mini-projects designed to solve practical problems, implement classic games, and work with APIs. Each project focuses on core software engineering concepts, logic design, and robust error handling.

---

## 🚀 Projects Overview & Core Concepts Covered

### 1. 🃏 Blackjack (Casino Card Game)
A fully-featured, object-oriented terminal implementation of the classic casino game.
* **Concepts:** 
  * **Object-Oriented Programming (OOP):** Leverages multiple interacting classes (`Card`, `Deck`, `Hand`, `Chips`).
  * **State & Inventory Management:** Tracking complex elements like game chips, user placing bets, drawing from a shrinking pool of cards, and mutating state dynamically.
  * **Dynamic Logic Evaluation:** Automatic calculation of values with flexible runtime rules (such as adjusting Aces from 11 down to 1 if the hand goes bust).

### 2. ❌ Tic-Tac-Toe
A 2-player competitive board game played entirely via user input terminal prompts.
* **Concepts:** 
  * **Matrix/Grid Representation:** Using a 1D list structure to represent and display a 2D interactive matrix board.
  * **Permutation Matching / Win-Condition Checkers:** Algorithmic verification checking for row, column, and diagonal matches after every turn.
  * **Data Validation:** Checking that terminal strings are numeric digits and ensuring the target coordinate hasn't already been taken.

### 3. 🌦️ Weather API Integrator
A real-time weather checking terminal utility utilizing a live external REST API.
* **Concepts:** 
  * **HTTP Client Requesting:** Utilizing the `requests` library to fetch third-party JSON payloads.
  * **Secure Secrets Management:** Loading sensitive credential data out of runtime files using local variables via `.env` files.
  * **JSON Deserialization:** Navigating nested dictionary structures to pluck out location names and temperature properties.

### 4. 🔑 Caesar Cipher Encoder
A mathematical cryptography utility that applies traditional character offsets to protect plaintext.
* **Concepts:** 
  * **ASCII manipulation:** Converting alphabetic characters directly to code decimals via `ord()` and reversing them back with `chr()`.
  * **Modular Arithmetic:** Using the modulo `% 26` operator to handle character overflow wrapped gracefully within bounds.

### 5. 🔁 Palindrome Checking Engine
A low-overhead script evaluating structural character sequences forward and backward.
* **Concepts:** 
  * **Advanced String Slicing:** Harnessing step parameters (`[::-1]`) to cleanly reverse strings in single expressions.
  * **Case Insensitivity Optimization:** Standardizing character evaluations uniformly via `.lower()` strings.

### 6. 💵 Sales Tax Calculator
A practical terminal utility that applies currency multipliers on base values.
* **Concepts:** 
  * **Data Type Inter-conversion:** Transforming terminal string user entries into integers.
  * **Float Formatting Expression:** Injecting dynamically formatted floating-point output sequences inside a string literal.

---

## 🛠️ General Python Mastery Exhibited

Across all files, several critical, fundamental coding patterns are consistently applied:

* **Defensive Input Validation:** Utilizing continuous looping (`while(True)`) patterns paired with active exception wrapping (`try/except`) to prevent terminal application crashes due to bad user input.
* **Control Flow Operations:** Complex routing flows involving relational constraints and Boolean switches to smoothly manage looping logic.

---

## 📦 How to Run the Projects

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name

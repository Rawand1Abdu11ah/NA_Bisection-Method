# NA_Bisection Method
 Python program to solve every Bisection Method equations
 
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Installation

To use this project, you need to clone the repository and install any dependencies (if required).

1. Clone the repository:
   ```bash
   git clone https://github.com/Rawand1Abdu11ah/Python-Bisection-Method.git

 ##  Usage
 * Run the program:
   python bisection_method.py

 * Enter the required inputs:
   * Lower bound (a)
   * Upper bound (b)
   * Tolerance (epsilon)
   * Maximum number of iterations (max_iter)
   * Function to be solved (f(x))
  

   ## Example
# Define the function to be solved
def f(x):
    return x**2 - 2

# Set the initial parameters
a = 0
b = 2
epsilon = 1e-6
max_iter = 100

# Call the bisection method function
root = bisection_method(f, a, b, epsilon, max_iter)

print("The root of the equation is:", root)

## License
This project is licensed under the MIT License.

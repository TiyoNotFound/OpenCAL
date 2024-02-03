# OpenCAL

OpenCAL is an open-source calculator application with multiple engine types, offering a variety of mathematical operations.

## Features

- **Four Engine Types:**
  - **engine-1:** Basic arithmetic operations (add, subtract, multiply, divide)
  - **engine-2:** Faster arithmetic operations (faster_add, faster_subtract, faster_multiply, faster_divide)
  - **engine-3:** Advanced math operations (cube, square, cubic_root, square_root)
  - **engine-4:** Custom functions and advanced operations (power, log_base_10, absolute_value, exponential, sin, cos, tan, arcsin, arccos, arctan, cube, square)

- **User-friendly Interface:**
  - Select the desired engine type.
  - View detailed features, including descriptions and functions.
  - Support for mathematical expressions with error handling.

## Engine Overview

### engine-1: Basic Arithmetic

The engine-1 is designed for fundamental arithmetic operations, providing a solid foundation for everyday calculations.

- **Operations:**
  - Addition (add)
  - Subtraction (subtract)
  - Multiplication (multiply)
  - Division (divide)

### engine-2: Faster Arithmetic

Engine-2 enhances arithmetic operations, prioritizing speed and efficiency for quicker calculations.

- **Operations:**
  - Faster Addition (faster_add)
  - Faster Subtraction (faster_subtract)
  - Faster Multiplication (faster_multiply)
  - Faster Division (faster_divide)

### engine-3: Advanced Math

Engine-3 introduces advanced mathematical operations, extending the calculator's capabilities beyond basic arithmetic.

- **Operations:**
  - Cube (cube)
  - Square (square)
  - Cubic Root (cubic_root)
  - Square Root (square_root)

### engine-4: Custom Functions and Advanced Operations

Engine-4 is a versatile engine that supports custom functions and a wide range of advanced mathematical operations.

- **Operations:**
  - Power (power)
  - Logarithm (Base 10) (log_base_10)
  - Absolute Value (absolute_value)
  - Exponential (exponential)
  - Trigonometric Functions (sin, cos, tan, arcsin, arccos, arctan)
  - Cube (cube)
  - Square (square)


## Example Implementation

```python
from calculator_engine import create_calculator_engine

# Create a calculator engine of type "engine-3"
calculator_engine = create_calculator_engine(engine_type="engine-3")

# Use the calculator engine
result = calculator_engine.tcalculator_engine("cube(3) + square_root(16)")
print(result)  # Output: 27.0
```

## Usage

- Select an engine type (1-4) to leverage specific features.
- Enter mathematical expressions to get results.
- Type 'back' to change the engine type and 'exit' to quit the calculator.

## Open Source Information

This project is open-source under the MIT License, providing flexibility for usage, modification, and distribution.

- **License:** [MIT License](LICENSE)
- **Contribution Guidelines:** [Contribution Guidelines](CONTRIBUTING.md)
- **Issue Tracker:** [Report Issues](https://github.com/TiyoNotFound/OpenCAL/issues)
- **Pull Requests:** [Submit Pull Requests](https://github.com/TiyoNotFound/OpenCAL/pulls)

Feel free to contribute, report issues, or use the code in your projects!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README now includes an example implementation showcasing how to use the OpenCAL library. Adjust it based on your specific repository details and preferences.

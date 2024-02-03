# my_calculator/calculator_engine.py
import math
from fractions import Fraction

class tcalcalculator_engine:
    def __init__(self, engine_type="engine-1"):
        self.engine_type = engine_type
        self.memory, self.depth, self.custom_functions = self.parse_engine_type(engine_type)

    def parse_engine_type(self, engine_type):
        engine_types = {
            "engine-1": (1, 5, {"add": lambda x, y: x + y, "subtract": lambda x, y: x - y, 
                               "multiply": lambda x, y: x * y, "divide": lambda x, y: x / y}),
            "engine-2": (2, 10, {"faster_add": lambda x, y: x + y, "faster_subtract": lambda x, y: x - y,
                                 "faster_multiply": lambda x, y: x * y, "faster_divide": lambda x, y: x / y}),
            "engine-3": (3, 15, {"cube": lambda x: x**3, "square": lambda x: x**2,
                                 "cubic_root": lambda x: x**(1/3), "square_root": lambda x: math.sqrt(x)}),
            "engine-4": (4, 20, {"power": lambda x, y: x**y, "log_base_10": lambda x: math.log10(x),
                                 "absolute_value": lambda x: abs(x), "exponential": lambda x: math.exp(x),
                                 "sin": lambda x: math.sin(x), "cos": lambda x: math.cos(x),
                                 "tan": lambda x: math.tan(x), "arcsin": lambda x: math.asin(x),
                                 "arccos": lambda x: math.acos(x), "arctan": lambda x: math.atan(x),
                                 "cube": lambda x: x**3, "square": lambda x: x**2})
        }

        return engine_types.get(engine_type, (1, 5, {}))

    def tcalculator_engine(self, expression):
        try:
            namespace = {"__builtins__": None, "math": math, "abs": abs, "factorial": math.factorial, "log": math.log,
                         "Fraction": Fraction}
            namespace.update(self.custom_functions)

            result = eval(expression, namespace)

            # Check if the result is a fraction and format it
            if isinstance(result, Fraction):
                return f"Fraction: {result.numerator}/{result.denominator}"
            elif result is not None:
                return result
            else:
                return f"Error: Evaluation of '{expression}' resulted in None"
        except KeyError as e:
            return f"Error: Engine doesn't support the operation {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

def create_calculator_engine(engine_type="engine-1"):
    return tcalcalculator_engine(engine_type)

from calculator_engine import create_calculator_engine


from tabulate import tabulate

def print_operations():
    print("Available Operations:")
    print("1. Basic Arithmetic (engine-1)")
    print("2. Faster Arithmetic (engine-2)")
    print("3. Advanced Math (engine-3)")
    print("4. Custom Functions (engine-4)")

def select_operation():
    while True:
        operation_choice = input("Select an operation (1-4): ")
        if operation_choice.isdigit() and 1 <= int(operation_choice) <= 4:
            return f"engine-{operation_choice}"
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def engine_features(engine_type):
    calculator_engine = create_calculator_engine(engine_type)
    features = []
    
    # Extract features from the custom_functions dictionary
    for operation, func in calculator_engine.custom_functions.items():
        features.append((operation, func.__doc__))

    return features

def display_features_table(engine_type):
    features = engine_features(engine_type)
    print(f"\nFeatures for {engine_type} Engine:")
    print(tabulate(features, headers=["Operation", "Description"], tablefmt="grid"))

def main():
    print("Welcome to the Simple Calculator!")

    while True:
        print_operations()
        engine_type = select_operation()

        # Create the selected calculator engine
        calculator_engine = create_calculator_engine(engine_type)

        # Display features table for the selected engine
        display_features_table(engine_type)

        while True:
            # Get user input
            user_input = input("Enter a mathematical expression (or 'back' to change operation, 'exit' to quit): ")

            # Check if the user wants to exit
            if user_input.lower() == "exit":
                print("Goodbye!")
                return
            elif user_input.lower() == "back":
                break

            try:
                # Use the calculator engine to evaluate the expression
                result = calculator_engine.tcalculator_engine(user_input)
                print("Result:", result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

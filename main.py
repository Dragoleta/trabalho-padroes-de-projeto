from complex_password_strategy import ComplexPasswordStrategy
from simple_password_strategy import SimplePasswordStrategy

# Usage example
if __name__ == "__main__":
    simple_strategy = SimplePasswordStrategy()
    simple_strategy.generate_password()

    complex_strategy = ComplexPasswordStrategy()
    complex_strategy.generate_password()

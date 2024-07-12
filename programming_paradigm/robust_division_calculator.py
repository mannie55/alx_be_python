def safe_divide(numerator, denominator):
        
        try:
            num1 = float(numerator)
            num2 = float(denominator)
            return f"The result of the division is {num1 / num2}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."   
        except ValueError:
            return "Error: Please enter numeric values only."
            
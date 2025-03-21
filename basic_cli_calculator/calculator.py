import argparse
import sys

def calculate(num1, operation, num2):
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'sub':
            return num1 - num2
        elif operation == 'mul':
            return num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        else:
            return "Error: Invalid operation."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Basic CLI Calculator using argparse")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operation", type=str, help="Operation: add, sub, mul, div")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    result = calculate(args.num1, args.operation.lower(), args.num2)
    
    print(f"Result: {result}" if isinstance(result, (int, float)) else result)

if __name__ == "__main__":
    main()

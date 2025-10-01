"""
My Python Application
A simple Python project example
"""

def greet(name="World"):
    """Greet someone by name."""
    return f"Hello, {name}!"

def main():
    """Main function."""
    print(greet())
    print(greet("Marcus"))
    print("Welcome to my Python app!")

if __name__ == "__main__":
    main()

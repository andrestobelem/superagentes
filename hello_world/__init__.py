"""
Hello World Module

A simple module that provides basic hello world functionality.
"""

from .hello import say_hello, get_greeting

__version__ = "1.0.0"
__all__ = ["say_hello", "get_greeting"]


def main():
    """Main function to demonstrate the hello_world module functionality."""
    print("=== Hello World Module Demo ===\n")

    # Basic hello world examples
    print("1. Basic usage:")
    print(f"   {say_hello()}")
    print(f"   {say_hello('Alice')}\n")

    # Multi-language greetings
    print("2. Multi-language greetings:")
    print(f"   English: {get_greeting('Bob', 'en')}")
    print(f"   Spanish: {get_greeting('Carlos', 'es')}")
    print(f"   French:  {get_greeting('Marie', 'fr')}")
    print(f"   German:  {get_greeting('Hans', 'de')}")
    print(f"   Italian: {get_greeting('Marco', 'it')}\n")

    # Default language fallback
    print("3. Default language fallback:")
    print(f"   Unknown language: {get_greeting('Unknown', 'xx')}\n")

    print("=== Demo completed ===")


if __name__ == "__main__":
    main()

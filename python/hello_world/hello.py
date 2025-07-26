"""
Hello World Functions

This module contains the main functions for greeting users.

Examples:
    Basic usage:
        >>> from hello_world import say_hello, get_greeting
        >>> say_hello()
        'Hello, World!'
        >>> say_hello("Alice")
        'Hello, Alice!'

    Multi-language greetings:
        >>> get_greeting("Bob", "en")
        'Hello, Bob!'
        >>> get_greeting("Carlos", "es")
        '¡Hola, Carlos!'
        >>> get_greeting("Marie", "fr")
        'Bonjour, Marie!'
        >>> get_greeting("Hans", "de")
        'Hallo, Hans!'
        >>> get_greeting("Marco", "it")
        'Ciao, Marco!'

    Default language fallback:
        >>> get_greeting("Unknown", "xx")
        'Hello, Unknown!'
"""


def say_hello(name: str = "World") -> str:
    """
    Say hello to a person.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def get_greeting(name: str = "World", language: str = "en") -> str:
    """
    Get a greeting in different languages.

    Args:
        name (str): The name to greet. Defaults to "World".
        language (str): The language for the greeting. Defaults to "en".

    Returns:
        str: A greeting message in the specified language.
    """
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!",
        "de": f"Hallo, {name}!",
        "it": f"Ciao, {name}!",
    }

    return greetings.get(language, greetings["en"])

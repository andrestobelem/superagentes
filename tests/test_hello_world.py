"""
Tests for the hello_world module.

This module contains unit tests for the hello_world functionality.
"""

from hello_world import say_hello, get_greeting


class TestSayHello:
    """Test cases for the say_hello function."""

    def test_say_hello_default(self):
        """Test say_hello with default parameter."""
        result = say_hello()
        assert result == "Hello, World!"

    def test_say_hello_with_name(self):
        """Test say_hello with a specific name."""
        result = say_hello("Alice")
        assert result == "Hello, Alice!"


class TestGetGreeting:
    """Test cases for the get_greeting function."""

    def test_get_greeting_default(self):
        """Test get_greeting with default parameters."""
        result = get_greeting()
        assert result == "Hello, World!"

    def test_get_greeting_english(self):
        """Test get_greeting in English."""
        result = get_greeting("Bob", "en")
        assert result == "Hello, Bob!"

    def test_get_greeting_spanish(self):
        """Test get_greeting in Spanish."""
        result = get_greeting("Carlos", "es")
        assert result == "¡Hola, Carlos!"

    def test_get_greeting_french(self):
        """Test get_greeting in French."""
        result = get_greeting("Marie", "fr")
        assert result == "Bonjour, Marie!"

    def test_get_greeting_german(self):
        """Test get_greeting in German."""
        result = get_greeting("Hans", "de")
        assert result == "Hallo, Hans!"

    def test_get_greeting_italian(self):
        """Test get_greeting in Italian."""
        result = get_greeting("Marco", "it")
        assert result == "Ciao, Marco!"

    def test_get_greeting_unknown_language(self):
        """Test get_greeting with unknown language (should fallback to English)."""
        result = get_greeting("Unknown", "xx")
        assert result == "Hello, Unknown!"

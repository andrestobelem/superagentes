# Súper Agentes

Super Agents

## Development Environment Setup

### Prerequisites

Before starting, make sure you have installed:

1. **pyenv** - For managing multiple Python versions
2. **pipenv** - For managing dependencies and virtual environments

### Installing pyenv (macOS)

```bash
# Install pyenv using Homebrew
brew install pyenv

# Add pyenv to PATH (add to ~/.zshrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc
```

### Installing pipenv

```bash
# Install pipenv globally
pip install pipenv
```

### Project Setup

1. **Clone the repository** (if you haven't already):

```bash
git clone https://github.com/andrestobelem/superagentes
cd superagentes
```

2.**Install the correct Python version**:

```bash
# Install Python 3.13.5 using pyenv
pyenv install 3.13.5

# Set the local version for this project
pyenv local 3.13.5
```

3.**Create and activate the virtual environment**:

```bash
# Create the virtual environment with pipenv and install all dependencies
pipenv install --dev

# Activate the virtual environment
pipenv shell
```

### Installation Verification

To verify that everything is configured correctly:

```bash
# Check Python version
python --version  # Should show Python 3.13.5

# Verify pipenv is working
pipenv --version

# Verify black is available
black --version
```

### Useful Commands

```bash
# Activate the virtual environment
pipenv shell

# Install a new dependency
pipenv install package-name

# Install a development dependency
pipenv install --dev package-name

# Format code with black
pipenv run format

# Run tests
pipenv run test

# Run tests with coverage report
pipenv run test-cov

# Run tests and generate HTML coverage report
pipenv run test-cov-html

# View installed dependencies
pipenv graph

# Exit the virtual environment
exit
```

### Project Structure

```text
superagentes/
├── Pipfile              # Dependency configuration
├── Pipfile.lock         # Exact dependency versions
├── .venv/               # Virtual environment (created automatically)
├── hello_world/         # Hello World module
│   ├── __init__.py
│   ├── __main__.py
│   └── hello.py
├── tests/               # Test files
│   └── test_hello_world.py
├── example.py           # Example usage
└── README.md           # This file
```

### Hello World Module

The `hello_world` module provides simple greeting functionality with support for multiple languages.

#### Features

- **Basic greetings**: Simple hello world functionality
- **Multi-language support**: Greetings in English, Spanish, French, German, and Italian
- **Default fallback**: Falls back to English for unsupported languages
- **Easy to use**: Simple function calls with optional parameters

#### Usage

##### Basic Usage

```python
from hello_world import say_hello, get_greeting

# Basic hello world
print(say_hello())  # Output: Hello, World!

# Greet a specific person
print(say_hello("Alice"))  # Output: Hello, Alice!
```

##### Multi-language Greetings

```python
from hello_world import get_greeting

# English (default)
print(get_greeting("Bob", "en"))  # Output: Hello, Bob!

# Spanish
print(get_greeting("Carlos", "es"))  # Output: ¡Hola, Carlos!

# French
print(get_greeting("Marie", "fr"))  # Output: Bonjour, Marie!

# German
print(get_greeting("Hans", "de"))  # Output: Hallo, Hans!

# Italian
print(get_greeting("Marco", "it"))  # Output: Ciao, Marco!
```

##### Default Language Fallback

```python
# Unknown language falls back to English
print(get_greeting("Unknown", "xx"))  # Output: Hello, Unknown!
```

#### Running the Module Demo

You can run a demonstration of all features:

```bash
# Run as a module
python -m hello_world

# Or from within the virtual environment
pipenv run python -m hello_world
```

This will output:

```text
=== Hello World Module Demo ===

1. Basic usage:
   Hello, World!
   Hello, Alice!

2. Multi-language greetings:
   English: Hello, Bob!
   Spanish: ¡Hola, Carlos!
   French:  Bonjour, Marie!
   German:  Hallo, Hans!
   Italian: Ciao, Marco!

3. Default language fallback:
   Unknown language: Hello, Unknown!

=== Demo completed ===
```

#### API Reference

##### `say_hello(name: str = "World") -> str`

Returns a simple greeting message.

- **Parameters:**
  - `name` (str): The name to greet. Defaults to "World".
- **Returns:**
  - `str`: A greeting message in English.

##### `get_greeting(name: str = "World", language: str = "en") -> str`

Returns a greeting in the specified language.

- **Parameters:**
  - `name` (str): The name to greet. Defaults to "World".
  - `language` (str): The language code. Supported: "en", "es", "fr", "de", "it". Defaults to "en".
- **Returns:**
  - `str`: A greeting message in the specified language, or English if language is not supported.

### Testing

The project includes automated testing with pytest and coverage reporting:

#### Running Tests

```bash
# Run all tests with verbose output
pipenv run test

# Run tests with coverage report in terminal
pipenv run test-cov

# Run tests and generate HTML coverage report
pipenv run test-cov-html
```

#### Coverage Reports

- **Terminal Coverage**: Shows coverage percentage and missing lines in the terminal
- **HTML Coverage**: Generates a detailed HTML report in `htmlcov/` directory
  - Open `htmlcov/index.html` in your browser to view the full report
  - Shows line-by-line coverage with highlighted missing lines

#### Test Structure

- Tests are located in the `tests/` directory
- Test files follow the naming convention: `test_*.py`
- Each test function should start with `test_`

### Important Notes

- **Python 3.13.5**: The project requires this specific version
- **Virtual Environment**: Always work within the virtual environment activated with `pipenv shell`
- **Code Formatting**: The project uses Black for automatic code formatting
- **Dependencies**: All dependencies are managed through Pipfile

### Troubleshooting

If you encounter issues:

1. **Python not found**: Make sure pyenv is in your PATH
2. **Wrong version**: Run `pyenv local 3.13.5` in the project directory
3. **Missing dependencies**: Run `pipenv install --dev` to reinstall everything
4. **Corrupted environment**: Delete `.venv/` and run `pipenv install --dev` again

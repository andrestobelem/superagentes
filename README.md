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

2. **Install the correct Python version**:
```bash
# Install Python 3.13.5 using pyenv
pyenv install 3.13.5

# Set the local version for this project
pyenv local 3.13.5
```

3. **Create and activate the virtual environment**:
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
black .

# View installed dependencies
pipenv graph

# Exit the virtual environment
exit
```

### Project Structure

```
superagentes/
├── Pipfile              # Dependency configuration
├── Pipfile.lock         # Exact dependency versions
├── .venv/               # Virtual environment (created automatically)
└── README.md           # This file
```

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

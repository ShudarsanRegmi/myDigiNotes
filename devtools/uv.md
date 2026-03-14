# UV Essentials

## 1. What is `uv`

`uv` is a modern Python package manager developed by Astral. It is written in Rust and designed to be extremely fast. It replaces several traditional Python tools such as:

* pip
* pip-tools
* virtualenv
* parts of pyenv workflows

The tool manages dependencies, virtual environments, lock files, and project execution in a unified and efficient manner.

Key advantages:

* Very fast dependency resolution
* Automatic environment management
* Reproducible builds through lock files
* Cleaner project workflow

---

# 2. Creating a New UV Project

Initialize a new project:

```bash
uv init myproject
cd myproject
```

This generates a basic project structure.

Typical structure:

```
myproject/
├── pyproject.toml
├── README.md
└── src/
```

The file `pyproject.toml` is the central configuration file where dependencies and project metadata are stored.

---

# 3. Creating a Virtual Environment

Create a virtual environment inside the project:

```bash
uv venv
```

This creates a folder:

```
.venv/
```

inside the project directory.

Specify a Python version if needed:

```bash
uv venv --python 3.11
```

---

# 4. Activating the Virtual Environment

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

After activation your terminal prompt usually shows:

```
(.venv)
```

This indicates Python commands will run inside the virtual environment.

---

# 5. Installing Dependencies

## Installing packages (recommended method)

```bash
uv add fastapi
```

Install multiple packages:

```bash
uv add numpy pandas
```

This command performs three operations:

1. Installs the package
2. Updates `pyproject.toml`
3. Updates `uv.lock`

---

# 6. Installing Existing Project Dependencies

If the project already contains dependencies defined in `pyproject.toml`, run:

```bash
uv sync
```

This installs all dependencies into the virtual environment.

The `uv.lock` file ensures deterministic dependency versions.

---

# 7. Running Programs with UV

Instead of activating the virtual environment, you can directly run commands:

```bash
uv run python script.py
```

Run tests:

```bash
uv run pytest
```

Run modules:

```bash
uv run python -m app.main
```

`uv` automatically uses the correct virtual environment.

---

# 8. Using UV as a pip Replacement

You can still install packages in pip style:

```bash
uv pip install requests
```

However this approach does not update `pyproject.toml`. The recommended method is:

```
uv add <package>
```

because it keeps dependency metadata consistent.

---

# 9. Removing Dependencies

Remove a package:

```bash
uv remove numpy
```

This updates both:

* `pyproject.toml`
* `uv.lock`

---

# 10. Updating Dependencies

Update all dependencies:

```bash
uv lock --upgrade
```

Or reinstall everything:

```bash
uv sync
```

---

# 11. Dependency Locking

`uv` creates a file called:

```
uv.lock
```

This lock file records exact dependency versions so that every developer installs identical packages.

This is essential for:

* reproducible builds
* CI pipelines
* collaborative development

---

# 12. Running One-Off Tools

Run Python tools without installing them permanently:

```bash
uvx black .
```

Example:

```bash
uvx ruff check .
```

`uvx` temporarily installs and runs the tool.

This is useful for:

* linters
* formatters
* CLI utilities

---

# 13. Installing Development Dependencies

Example:

```bash
uv add pytest --dev
```

Development dependencies are used for:

* testing
* linting
* formatting
* debugging

They are not required for production environments.

---

# 14. Typical UV Workflow

A standard workflow looks like:

Initialize project:

```bash
uv init project
cd project
```

Create environment:

```bash
uv venv
```

Activate environment:

```bash
source .venv/bin/activate
```

Add dependencies:

```bash
uv add fastapi
uv add numpy
```

Install project dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run python main.py
```

---

# 15. Traditional Python Workflow vs UV

Traditional workflow:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

UV workflow:

```
uv venv
uv add <package>
uv sync
uv run <command>
```

UV simplifies dependency management and significantly accelerates installation.

---

# 16. When UV is Particularly Useful

UV becomes especially valuable in the following scenarios:

Large Python projects with many dependencies.

Machine learning environments where installation speed matters.

Collaborative teams needing deterministic environments.

CI/CD pipelines where reproducible dependency resolution is essential.

---

# 17. Key Commands Quick Reference

Create project:

```
uv init project
```

Create environment:

```
uv venv
```

Activate environment:

```
source .venv/bin/activate
```

Add dependency:

```
uv add <package>
```

Install dependencies:

```
uv sync
```

Run script:

```
uv run python script.py
```

Remove dependency:

```
uv remove <package>
```

Run temporary tool:

```
uvx <tool>
```

---

# 18. Conceptual Summary

`uv` attempts to modernize Python development by combining multiple tools into a single cohesive system. It focuses on:

* speed
* deterministic environments
* simpler developer experience
* better dependency tracking

For modern Python projects, `uv` is increasingly replacing traditional `pip + venv` workflows.

"""
Open Source Project Markdown Helper

This script is a simple, single-file utility designed to help maintainers 
and first-time contributors quickly generate standard project files in Markdown
format (README, CONTRIBUTING guide, etc.).

It is highly useful for beginners as it shows the expected structure of a
well-maintained open-source repository.

Usage:
    python oss_project_helper.py
    (The script will prompt the user for input and generate the files.)
"""

import sys
import os
from typing import Optional

def generate_readme(project_name: str, description: str) -> str:
    """
    Generates a basic README.md template.
    """
    return f"""# {project_name.strip()}

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🌟 About

{description.strip()}

This project aims to solve [briefly state the problem or goal].

## 🚀 Installation

This project uses only standard Python libraries and can be run directly.

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YourUsername/](https://github.com/YourUsername/){project_name.lower().replace(' ', '-')}.git
    cd {project_name.lower().replace(' ', '-')}
    ```

2.  Run the script:
    ```bash
    python main_script_name.py
    ```

## ✨ Usage

[Provide a simple, quick example of how to use the main functionality.]

## 🤝 Contributing

We welcome contributions! Please see the **[CONTRIBUTING.md](CONTRIBUTING.md)** file for guidelines on how to submit issues, features, and pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""

def generate_contributing_guide(project_name: str) -> str:
    """
    Generates a CONTRIBUTING.md template tailored for new contributors.
    """
    return f"""# Contributing to {project_name}

We love community contributions! Thank you for taking the time to help us improve.

## 📝 Guidelines

### Reporting Bugs

* Ensure the bug hasn't already been reported by searching the [Issues page].
* Open a new issue and include the following:
    * A clear and concise **title**.
    * **Steps to reproduce** the behavior.
    * Your **environment** (OS, Python version, etc.).

### Suggesting Enhancements

* Open an issue and describe the enhancement clearly.
* Explain **why** this feature would be useful.

### 💻 Pull Requests (PRs)

1.  **Fork** the repository and create your feature branch (`git checkout -b feature/AmazingFeature`).
2.  **Commit** your changes following conventional commit style (e.g., `feat: add new feature`).
3.  Ensure your code passes any existing **tests** (if applicable).
4.  **Push** to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request** and briefly describe your changes.

**First-time contributor?** Look for issues tagged `good first issue`!

## 🔗 Code of Conduct

Please note that this project is governed by a Code of Conduct. By participating, you are expected to uphold this code.
"""

def save_file(filename: str, content: str):
    """
    Saves the generated content to a file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully generated and saved: {filename}")
    except IOError as e:
        print(f"❌ Error saving file {filename}: {e}")

def main():
    """
    Main function to run the CLI utility and generate files.
    """
    print("\n--- Open Source Project File Generator ---")
    
    # 1. Get project information
    project_name = input("Enter the name of your project (e.g., SimpleSummarizer): ")
    if not project_name:
        project_name = "New Python Utility"
    
    description = input("Enter a short, one-sentence description of the project: ")
    if not description:
        description = "A simple, single-file utility for demonstration purposes."

    print("\nWhat files would you like to generate?")
    print("1: README.md")
    print("2: CONTRIBUTING.md")
    print("3: Both README.md and CONTRIBUTING.md (Recommended for OSS!)")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    # 2. Generate and Save Files
    
    if choice in ['1', '3']:
        readme_content = generate_readme(project_name, description)
        save_file("README.md", readme_content)

    if choice in ['2', '3']:
        contributing_content = generate_contributing_guide(project_name)
        save_file("CONTRIBUTING.md", contributing_content)
    
    if choice not in ['1', '2', '3']:
        print("Invalid choice. No files were generated.")
        
    print("\nGeneration Complete.")
    print("These Markdown files are ready to be added to your GitHub repository.")


if __name__ == "__main__":
    main()

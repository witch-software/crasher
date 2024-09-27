# Contributing to Crasher

We welcome contributions from the community, whether it's fixing bugs, improving documentation, adding new features, or reporting issues. This document outlines the process to contribute effectively to Crasher.

## How to Contribute

There are several ways to contribute to the Crasher project:
1. **Reporting Bugs**: Help us improve the project by reporting any bugs you encounter.
2. **Suggesting Enhancements**: Propose new features or improvements to existing functionality.
3. **Contributing Code**: Submit fixes, enhancements, or new features via pull requests.
4. **Improving Documentation**: Fix typos, clarify usage examples, or add new guides.

### Reporting Bugs

If you find a bug, please help us by submitting an issue to the [GitHub Issue Tracker](https://github.com/witch-software/crasher/issues). Make sure to include:
- A descriptive title for the issue.
- Steps to reproduce the issue.
- Steps to reproduce the issue.
- Screenshots or code snippets if relevant.
- Information about your environment (OS, Python version, etc.).

### Suggesting Enhancements

To suggest a new feature or enhancement:
1. Open a new [GitHub issue](https://github.com/witch-software/crasher/issues/new) with the "enhancement" label.
2. Provide a detailed explanation of the feature, its purpose, and how it would improve the project.
3. If possible, propose an implementation or share examples of similar features in other projects.

### Submitting Code (Pull Requests)

We appreciate all contributions to the Crasher codebase! Before starting, make sure you:
- Review open issues to see if the feature or bug has already been addressed.
- Follow the guidelines below for submitting code contributions.

#### 1. Fork the Repository
1. Navigate to the [Crasher GitHub repository](https://github.com/witch-software/crasher).
2. Click the "Fork" button in the top-right corner to create a copy of the repository in your GitHub account.

#### 2. Create a Branch
1. Clone your forked repository:
```
git clone https://github.com/your-username/crasher.git 
```
2. Create a new branch for your feature or bug fix:
```
git checkout -b feature-or-bug-description
```

#### 3. Make Your Changes
- Follow the existing code style and structure.
- Include clear and concise comments in your code where necessary.
- Write or update tests to cover your changes.
- Test your changes to ensure they work as expected.

#### 4. Commit and Push
1. Add and commit your changes:
```
git add .
git commit -m "Brief description of changes"
```
2. Push your changes to your fork:
```
git push origin feature-or-bug-description
```

#### 5. Open a Pull Request
1. Navigate to your forked repository on GitHub.
2. Click the "Compare & pull request" button.
3. In the pull request description, clearly explain:
    - What changes were made.
    - Why these changes are necessary.
    - Any relevant issue numbers or links.
4. Submit your pull request for review.

#### 6. Respond to Review Feedback
A project maintainer will review your pull request and may request changes. Be sure to:
- Address any feedback promptly.
- Update your branch with the latest changes from the `main` branch if needed:
```
git fetch upstream
git checkout main
git merge upstream/main
```
Once your pull request is approved, it will be merged into the project.

## Code Guidelines
When contributing code, please adhere to the following guidelines:

- **Python Version**: Crasher supports Python 3.10, 3.11, and 3.12. Ensure your code is compatible with these versions.
- **Code Style**: Follow the PEP 8 style guide for Python. Use tools like flake8 or black to check your code.
- **Testing**: Ensure all code is covered by unit tests. You can run the tests using:
    ```
    pytest
    ```
- **Documentation**: If your changes affect the functionality, update the corresponding documentation in the repository or Wiki.

## Community Guidelines
We follow a code of conduct based on respect, inclusivity, and a welcoming environment for all contributors. Please be mindful of how you communicate with other contributors and maintainers.

## Need Help?
If you have any questions about the contribution process or specific issues, feel free to reach out by creating a GitHub issue or contacting the maintainers via email.

Thank you for your interest in contributing to Crasher!

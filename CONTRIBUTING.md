# Contributing to Foo et al. Parameterization

Thank you for your interest in contributing to this project! Here is how to contribute:

1. **Fork the repository:** Click the "Fork" button on GitHub to create your own copy of the repository.

2. **Clone your fork locally:** Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/foo_param.git

3. **Create a new branch:** Create a seperate branch using:
   ```bash
   git checkout -b feature/your-feature-name

4. **Test your changes:** The software package contains a unit tests 'tests' directory. Run the existing unit tests to make sure that they pass. If applicable, write new tests to cover your changes.
    ```bash
    python -m unittest tests.test_foo

5. **Push Changes:** 
    a) Push your branch to your fork on Github:
    ```bash
    git push origin feature/your-feature-name

    b) Create a pull request (PR): Visit the main repository on GitHub and click "New pull request" button. Choose your branch as the compare branch and provide a descriptive title and summary for your PR.

    c) Once the administrators of the main repository approve your changes, it will be merged to the main branch
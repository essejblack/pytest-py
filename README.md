# Pytest Functions in a Class

This project demonstrates the use of `pytest` to test various functionalities within a Python class. Below is an overview of the test functions included in the `TestMain` class.

## Test Class: `TestMain`

### Setup and Teardown
- `setup_class(cls)`: Runs once before all tests in the class. Used for class-level setup.
- `setup_method(self, method)`: Runs before each test method. Used for method-level setup.
- `teardown_method(self, method)`: Runs after each test method. Used for method-level cleanup.

### Test Functions
1. **`test_main`**: A simple test that prints "test main".
2. **`test_InAssert`**: Tests integer equality using `assert`.
3. **`test_StrAssert`**: Tests string equality using `assert`.
4. **`test_arrayAssert`**: Tests list equality using `assert`.
5. **`test_dictAssert`**: Tests dictionary equality using `assert`.
6. **`test_float`**: Tests floating-point arithmetic using `pytest.approx` for precision.
7. **`test_exception`**: Verifies that a `ValueError` is raised using `pytest.raises`.

### Additional Notes
- The `pytest.approx` function is used to handle floating-point precision issues.
- The `pytest.raises` context manager is used to test exceptions.

To run the tests, execute the following command in the terminal:
```bash
pytest test_file.py
```

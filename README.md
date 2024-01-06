# Calculator Project

This simple calculator project is built using Streamlit. It provides basic arithmetic operations: addition, subtraction, multiplication, and division.

## File Structure
- `backend.py`: Contains the mathematical functions for the calculator operations.
- `ui.py`: Implements the Streamlit user interface for the calculator.

## How to Use
1. Clone the repository.
2. Install the necessary dependencies (Streamlit).
3. Run `ui.py` using Streamlit.

```bash
streamlit run ui.py
```

Access the calculator through the provided Streamlit interface in your browser.

## Operations Supported
- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts one number from another.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides one number by another.

## Usage
- Input the first and second numbers.
- Select the desired operation.
- View the output displayed in the Streamlit interface.

## Example
Here's an example of how the calculator works:

```python
# Code snippet
from backend import add, subs, multiply, divide
# ... (Streamlit UI code)

# The selected operation
operation = 'Addition'
# Numbers provided by the user
x = 5
y = 3
# Output
result = add(x, y)
print(f"The result of {operation} is: {result}")
```

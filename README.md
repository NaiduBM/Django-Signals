# Python Rectangle Class Demo

This project demonstrates a simple Python implementation of a Rectangle class with iterator functionality.

## Features

- Rectangle class with length and width properties
- Iterable interface that yields dimensions as dictionaries
- Type hints for better code clarity

## Usage

### Rectangle Class

The `Rectangle` class is defined in `rectangle.py`. Here's how to use it:

```python
from rectangle import Rectangle

# Create a rectangle with length 5 and width 3
rect = Rectangle(5, 3)

# Iterate over the rectangle's dimensions
for dimension in rect:
    print(dimension)
```

Output:
```
{'length': 5}
{'width': 3}
```

### Running the Code

To run the example:

```bash
python rectangle.py
```

## Project Structure

- `rectangle.py` - Contains the Rectangle class implementation
- `index.js` - A simple Node.js starter file
- `package.json` - Project configuration and dependencies

## Requirements

- Python 3.x
- Node.js (for running index.js)

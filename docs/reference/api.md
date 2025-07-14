# API Reference

This document provides complete reference information for the `diataxis-docs` Python module.

## Module: main

The main module provides example functionality demonstrating documentation patterns.

### Classes

#### DocumentationExample

A sample class to demonstrate documentation patterns.

```python
class DocumentationExample(name: str)
```

**Parameters:**
- `name` (str): The name for this example instance

**Methods:**

##### add_item(item: str) -> None

Add an item to the collection.

**Parameters:**
- `item` (str): The item to add

**Example:**
```python
example = DocumentationExample("demo")
example.add_item("tutorial")
```

##### get_items() -> List[str]

Get all items in the collection.

**Returns:**
- List[str]: A copy of all items in the collection

**Example:**
```python
items = example.get_items()
print(items)  # ['tutorial', 'how-to guide']
```

##### find_item(search_term: str) -> Optional[str]

Find an item containing the search term.

**Parameters:**
- `search_term` (str): The term to search for

**Returns:**
- Optional[str]: The first matching item, or None if not found

**Example:**
```python
found = example.find_item("guide")
if found:
    print(f"Found: {found}")
```

### Functions

#### process_data(data: List[str]) -> dict

Process a list of data items.

**Parameters:**
- `data` (List[str]): List of string data to process

**Returns:**
- dict: A dictionary with the following keys:
  - `count` (int): Number of items
  - `items` (List[str]): The original items
  - `first` (Optional[str]): First item or None
  - `last` (Optional[str]): Last item or None

**Example:**
```python
result = process_data(["a", "b", "c"])
print(result)
# {'count': 3, 'items': ['a', 'b', 'c'], 'first': 'a', 'last': 'c'}
```

#### main() -> None

Main entry point for the application. Demonstrates usage of the DocumentationExample class and process_data function.

**Example:**
```python
if __name__ == "__main__":
    main()
```

## Type Annotations

This module uses the following type annotations from the `typing` module:

- `List`: For typed lists
- `Optional`: For values that might be None

## Module Attributes

The module defines `__all__` to specify its public API:

```python
__all__ = ['DocumentationExample', 'process_data', 'main']
```
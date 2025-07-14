"""
Diátaxis Documentation Example Project

This module demonstrates a simple Python application with comprehensive
documentation following the Diátaxis framework.
"""

from typing import List, Optional


class DocumentationExample:
    """A sample class to demonstrate documentation patterns."""
    
    def __init__(self, name: str) -> None:
        """Initialize the DocumentationExample.
        
        Args:
            name: The name for this example instance.
        """
        self.name = name
        self._items: List[str] = []
    
    def add_item(self, item: str) -> None:
        """Add an item to the collection.
        
        Args:
            item: The item to add.
        """
        self._items.append(item)
    
    def get_items(self) -> List[str]:
        """Get all items in the collection.
        
        Returns:
            A list of all items.
        """
        return self._items.copy()
    
    def find_item(self, search_term: str) -> Optional[str]:
        """Find an item containing the search term.
        
        Args:
            search_term: The term to search for.
            
        Returns:
            The first matching item, or None if not found.
        """
        for item in self._items:
            if search_term in item:
                return item
        return None


def process_data(data: List[str]) -> dict:
    """Process a list of data items.
    
    Args:
        data: List of string data to process.
        
    Returns:
        A dictionary with processing results.
    """
    return {
        "count": len(data),
        "items": data,
        "first": data[0] if data else None,
        "last": data[-1] if data else None,
    }


def main() -> None:
    """Main entry point for the application."""
    print("Diátaxis Documentation Example")
    print("=" * 30)
    
    # Create an example instance
    example = DocumentationExample("demo")
    
    # Add some items
    items = ["tutorial", "how-to guide", "reference", "explanation"]
    for item in items:
        example.add_item(item)
    
    # Process and display results
    results = process_data(example.get_items())
    
    print(f"Documentation types: {results['count']}")
    print(f"Items: {', '.join(results['items'])}")
    
    # Search for a specific item
    search = "guide"
    found = example.find_item(search)
    if found:
        print(f"Found item containing '{search}': {found}")


if __name__ == "__main__":
    main()

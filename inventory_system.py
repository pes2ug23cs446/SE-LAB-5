"""
Inventory Management System Module.

This module provides functions to manage inventory stock data including
adding, removing, loading, saving, and reporting on inventory items.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add.
        logs (list, optional): List to store log messages.

    Returns:
        None
    """
    if logs is None:
        logs = []

    if not item or not isinstance(item, str):
        logging.warning("Invalid item name provided")
        return

    if not isinstance(qty, int) or qty < 0:
        logging.warning("Invalid quantity provided")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item (str): The name of the item to remove.
        qty (int): The quantity to remove.

    Returns:
        None
    """
    try:
        if item not in stock_data:
            logging.warning("Item '%s' not found in inventory", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info(
                "Item '%s' removed from inventory (quantity depleted)",
                item
            )
    except KeyError as e:
        logging.error("Error removing item: %s", e)
    except TypeError as e:
        logging.error("Invalid quantity type: %s", e)


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item (str): The name of the item.

    Returns:
        int: The quantity of the item, or 0 if not found.
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): The path to the JSON file.

    Returns:
        dict: The loaded stock data.
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Data loaded from %s", file)
    except FileNotFoundError:
        logging.warning(
            "File '%s' not found. Starting with empty inventory.",
            file
        )
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        stock_data = {}
    return stock_data


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): The path to the JSON file.

    Returns:
        None
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
        logging.info("Data saved to %s", file)
    except IOError as e:
        logging.error("Error saving data: %s", e)


def print_data():
    """
    Print the current inventory report.

    Returns:
        None
    """
    print("Items Report")
    print("-" * 30)
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("-" * 30)


def check_low_items(threshold=5):
    """
    Check for items with quantity below a threshold.

    Args:
        threshold (int): The minimum quantity threshold.

    Returns:
        list: List of items below the threshold.
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory system functionality.

    Returns:
        None
    """
    logging.info("Starting inventory system")

    add_item("apple", 10)
    add_item("banana", 5)
    add_item(123, "ten")  # This will be caught by validation
    remove_item("apple", 3)
    remove_item("orange", 1)  # This will log a warning

    apple_qty = get_qty("apple")
    print(f"Apple stock: {apple_qty}")

    low_items = check_low_items()
    print(f"Low items: {low_items}")

    save_data()
    load_data()
    print_data()

    # Removed dangerous eval() usage
    print("Inventory system operations completed")
    logging.info("Inventory system operations completed")


if __name__ == "__main__":
    main()

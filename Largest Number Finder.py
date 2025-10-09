"""
Largest Number Finder
Finds the largest number from a sequence of user inputs.
"""


def get_number_input(prompt):
    """
    Get valid number input from user with error handling.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        float: Valid number input, or None if user wants to quit
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Allow user to quit with 'q' or 'quit'
            if user_input.lower() in ['q', 'quit']:
                return None
            
            # Support both integers and floats
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def find_largest_number(sentinel=-1):
    """
    Find the largest number from user input.
    
    Args:
        sentinel: The value that stops input (default: -1)
        
    Returns:
        tuple: (largest_number, smallest_number, all_numbers)
    """
    numbers = []
    
    print("=" * 60)
    print("Largest Number Finder")
    print(f"Enter numbers to find the largest ({sentinel} to stop, 'q' to quit)")
    print("=" * 60)
    
    while True:
        number = get_number_input("\nEnter a number: ")
        
        # User quit the program
        if number is None:
            print("\nExiting program...")
            return None, None, None
        
        # Sentinel value stops input
        if number == sentinel:
            break
        
        numbers.append(number)
        print(f"✓ Added: {number} (Total: {len(numbers)} numbers)")
    
    # Check if any numbers were entered
    if not numbers:
        print(f"\nNo numbers entered (only sentinel value {sentinel}).")
        return None, None, None
    
    # Find largest and smallest
    largest = max(numbers)
    smallest = min(numbers)
    
    return largest, smallest, numbers


def display_results(largest, smallest, numbers):
    """
    Display comprehensive statistics about the numbers.
    
    Args:
        largest: The largest number
        smallest: The smallest number
        numbers (list): All entered numbers
    """
    if largest is None:
        return
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Largest number:  {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Range:           {largest - smallest}")
    print(f"Count:           {len(numbers)}")
    print(f"Sum:             {sum(numbers)}")
    print(f"Average:         {sum(numbers) / len(numbers):.2f}")
    
    print(f"\nAll numbers: {numbers}")
    
    # Show position of largest and smallest
    largest_positions = [i + 1 for i, n in enumerate(numbers) if n == largest]
    smallest_positions = [i + 1 for i, n in enumerate(numbers) if n == smallest]
    
    print(f"\nLargest appears at position(s): {largest_positions}")
    print(f"Smallest appears at position(s): {smallest_positions}")


def main():
    """Main entry point for the program."""
    while True:
        largest, smallest, numbers = find_largest_number(sentinel=-1)
        
        if largest is None and numbers is None:
            break
        
        display_results(largest, smallest, numbers)
        
        # Ask if user wants to run again
        print("\n" + "=" * 60)
        run_again = input("Find more numbers? (yes/no): ").lower()
        
        if run_again not in ['yes', 'y']:
            print("\nThank you for using the Largest Number Finder!")
            break


if __name__ == "__main__":
    main()
"""
Even and Odd Number Counter
Counts even and odd numbers from user input until 0 is entered.
"""


def get_number_input(prompt):
    """
    Get valid integer input from user with error handling.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        int: Valid integer input, or None if user wants to quit
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Allow user to quit with 'q' or 'quit'
            if user_input.lower() in ['q', 'quit']:
                return None
            
            return int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def count_even_odd_numbers():
    """
    Main function to count even and odd numbers.
    
    Returns:
        tuple: (odd_count, even_count, all_numbers)
    """
    odd_numbers = 0
    even_numbers = 0
    all_numbers = []
    
    print("=" * 50)
    print("Even/Odd Number Counter")
    print("Enter numbers to count (0 to stop, 'q' to quit)")
    print("=" * 50)
    
    while True:
        number = get_number_input("\nEnter a number: ")
        
        # User quit the program
        if number is None:
            print("\nExiting program...")
            return None, None, None
        
        # 0 terminates counting
        if number == 0:
            break
        
        # Store the number for display
        all_numbers.append(number)
        
        # Check if the number is odd or even
        # Using modulo 2: odd numbers have remainder 1 or -1
        if number % 2 != 0:
            odd_numbers += 1
        else:
            even_numbers += 1
    
    return odd_numbers, even_numbers, all_numbers


def display_results(odd_count, even_count, numbers):
    """
    Display the counting results with statistics.
    
    Args:
        odd_count (int): Count of odd numbers
        even_count (int): Count of even numbers
        numbers (list): List of all entered numbers
    """
    if odd_count is None:
        return
    
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Odd numbers count:  {odd_count}")
    print(f"Even numbers count: {even_count}")
    print(f"Total numbers:      {odd_count + even_count}")
    
    if numbers:
        print(f"\nNumbers entered: {numbers}")
        
        # Additional statistics
        print(f"\nPercentage odd:  {odd_count / len(numbers) * 100:.1f}%")
        print(f"Percentage even: {even_count / len(numbers) * 100:.1f}%")


def main():
    """Main entry point for the program."""
    while True:
        odd_count, even_count, numbers = count_even_odd_numbers()
        
        if odd_count is None:
            break
        
        display_results(odd_count, even_count, numbers)
        
        # Ask if user wants to run again
        print("\n" + "=" * 50)
        run_again = input("Count more numbers? (yes/no): ").lower()
        
        if run_again not in ['yes', 'y']:
            print("\nThank you for using the Even/Odd Counter!")
            break


if __name__ == "__main__":
    main()
"""
Counter Loop Examples and Improvements
Demonstrates proper countdown loops with best practices.
"""


def basic_countdown_improved():
    """
    Improved version of the basic countdown loop.
    More explicit condition makes intent clearer.
    """
    print("=" * 50)
    print("Basic Countdown (Improved)")
    print("=" * 50)
    
    counter = 5
    
    # More explicit: counter > 0 instead of just counter
    while counter > 0:
        print(f"Inside the loop. Counter: {counter}")
        counter -= 1
    
    print(f"Outside the loop. Counter: {counter}")
    print()


def countdown_with_range():
    """
    More Pythonic approach using range() - recommended style.
    """
    print("=" * 50)
    print("Countdown with range() - Most Pythonic")
    print("=" * 50)
    
    # Cleaner and more readable
    for counter in range(5, 0, -1):
        print(f"Inside the loop. Counter: {counter}")
    
    print(f"Outside the loop. Counter: 0")
    print()


def countdown_with_features():
    """
    Enhanced countdown with additional features.
    """
    print("=" * 50)
    print("Enhanced Countdown")
    print("=" * 50)
    
    start = 10
    counter = start
    iterations = 0
    
    print(f"Starting countdown from {start}...\n")
    
    while counter > 0:
        iterations += 1
        
        # Add visual feedback
        if counter <= 3:
            print(f"⚠️  Inside the loop. Counter: {counter} (Almost done!)")
        else:
            print(f"✓  Inside the loop. Counter: {counter}")
        
        counter -= 1
    
    print(f"\n🎉 Outside the loop. Counter: {counter}")
    print(f"Total iterations: {iterations}")
    print()


def countdown_with_validation(start_value):
    """
    Countdown with input validation and error handling.
    
    Args:
        start_value (int): Starting counter value
    """
    print("=" * 50)
    print(f"Validated Countdown from {start_value}")
    print("=" * 50)
    
    # Validate input
    if not isinstance(start_value, int):
        print("Error: Counter must be an integer")
        return
    
    if start_value <= 0:
        print("Error: Counter must be positive")
        return
    
    counter = start_value
    
    while counter > 0:
        print(f"Counter: {counter}")
        counter -= 1
    
    print(f"Countdown complete! Final value: {counter}")
    print()


def flexible_countdown(start, end=0, step=1):
    """
    Flexible countdown/countup function.
    
    Args:
        start (int): Starting value
        end (int): Ending value (exclusive)
        step (int): Step size
    """
    print("=" * 50)
    print(f"Flexible Counter: {start} → {end} (step: {step})")
    print("=" * 50)
    
    counter = start
    
    # Handle both countdown and countup
    if start > end:
        while counter > end:
            print(f"Counter: {counter}")
            counter -= step
    else:
        while counter < end:
            print(f"Counter: {counter}")
            counter += step
    
    print(f"Final value: {counter}")
    print()


def countdown_with_break():
    """
    Countdown with early exit capability.
    """
    print("=" * 50)
    print("Countdown with Early Exit")
    print("=" * 50)
    
    counter = 10
    abort_at = 3
    
    print(f"Counting down from {counter}, aborting at {abort_at}...\n")
    
    while counter > 0:
        print(f"Counter: {counter}")
        
        # Early exit condition
        if counter == abort_at:
            print(f"\n⚠️  Emergency stop at {counter}!")
            break
        
        counter -= 1
    else:
        # This runs only if break was NOT called
        print("\n✓ Countdown completed normally")
    
    print(f"Final counter value: {counter}")
    print()


def main():
    """Demonstrate all countdown variations."""
    
    print("\n" + "=" * 50)
    print("ORIGINAL CODE ANALYSIS")
    print("=" * 50)
    print("""
Original Code:
    counter = 5
    while counter:  # ⚠️  Implicit boolean check (works but unclear)
        print("Inside the loop.", counter)
        counter -= 1
    print("Outside the loop.", counter)

Issues:
- 'while counter:' is less explicit than 'while counter > 0'
- Works because 0 is falsy, but intent isn't clear
- Good practice: use explicit comparisons
""")
    
    # Run all examples
    basic_countdown_improved()
    countdown_with_range()
    countdown_with_features()
    countdown_with_validation(5)
    countdown_with_validation(0)  # Error case
    flexible_countdown(10, 0, 2)  # Count down by 2
    flexible_countdown(0, 10, 2)  # Count up by 2
    countdown_with_break()
    
    print("\n" + "=" * 50)
    print("BEST PRACTICES SUMMARY")
    print("=" * 50)
    print("""
1. Use explicit conditions: 'while counter > 0' not 'while counter'
2. Prefer 'for' loops with range() when possible (more Pythonic)
3. Add input validation for robustness
4. Use descriptive variable names (iterations_remaining vs counter)
5. Consider using 'break' for early exits
6. Remember: 'else' clause runs if loop completes without 'break'
    """)


if __name__ == "__main__":
    main()
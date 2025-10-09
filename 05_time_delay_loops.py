"""
Time Delay Loop Examples
Various scenarios using time.sleep() with countdown timers.
"""

import time
import sys


def hide_and_seek_countdown():
    """
    Original: Hide and seek countdown timer.
    """
    print("=" * 50)
    print("🙈 HIDE AND SEEK COUNTDOWN")
    print("=" * 50)
    
    for i in range(1, 6):
        print(f"{i}HIDE AND SEEK")
        time.sleep(1)
    
    print("Ready or not, here I come!")
    print()


def rocket_launch_countdown():
    """
    Scenario 1: Rocket Launch Countdown
    """
    print("=" * 50)
    print("🚀 ROCKET LAUNCH SEQUENCE")
    print("=" * 50)
    print("Initiating countdown...\n")
    
    for i in range(10, 0, -1):
        if i <= 3:
            print(f"🔥 T-minus {i}... ENGINES FIRING!")
        else:
            print(f"⏱️  T-minus {i}...")
        time.sleep(1)
    
    print("🚀 LIFTOFF! We have liftoff!")
    print()


def microwave_timer():
    """
    Scenario 2: Microwave heating countdown.
    """
    print("=" * 50)
    print("🍕 MICROWAVE TIMER")
    print("=" * 50)
    
    heating_time = 5
    print(f"Heating your food for {heating_time} seconds...\n")
    
    for i in range(heating_time, 0, -1):
        # Visual progress bar
        bars = "█" * i + "░" * (heating_time - i)
        print(f"⏲️  {i} seconds remaining [{bars}]")
        time.sleep(1)
    
    print("🔔 BEEP BEEP BEEP! Your food is ready!")
    print()


def fitness_workout_timer():
    """
    Scenario 3: Workout exercise timer.
    """
    print("=" * 50)
    print("💪 WORKOUT TIMER - PLANK HOLD")
    print("=" * 50)
    print("Get into position!\n")
    
    time.sleep(2)  # Preparation time
    print("Starting in...")
    
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("GO! Hold that plank!\n")
    
    exercise_duration = 10
    for i in range(1, exercise_duration + 1):
        remaining = exercise_duration - i + 1
        
        if remaining <= 3:
            print(f"💥 {i} seconds - ALMOST THERE! Just {remaining} more!")
        elif i % 5 == 0:
            print(f"✓ {i} seconds - Keep going! You got this!")
        else:
            print(f"💪 {i} seconds...")
        
        time.sleep(1)
    
    print("\n🎉 Great job! Rest and recover!")
    print()


def traffic_light_simulator():
    """
    Scenario 4: Traffic light sequence.
    """
    print("=" * 50)
    print("🚦 TRAFFIC LIGHT SIMULATOR")
    print("=" * 50)
    
    lights = [
        ("🔴 RED", 3, "STOP!"),
        ("🟡 YELLOW", 2, "Get ready..."),
        ("🟢 GREEN", 3, "GO!")
    ]
    
    for color, duration, message in lights:
        print(f"\n{color} - {message}")
        for i in range(duration, 0, -1):
            print(f"  {i}...", end="\r")  # Overwrite same line
            sys.stdout.flush()
            time.sleep(1)
    
    print("\n\nTraffic cycle complete!")
    print()


def study_pomodoro_timer():
    """
    Scenario 5: Pomodoro study timer (shortened version).
    """
    print("=" * 50)
    print("📚 POMODORO STUDY TIMER")
    print("=" * 50)
    
    focus_time = 8  # Normally 25 minutes
    break_time = 3  # Normally 5 minutes
    
    print(f"Focus time: {focus_time} seconds\n")
    print("📖 Start studying NOW!\n")
    
    for i in range(1, focus_time + 1):
        remaining = focus_time - i
        if remaining == 0:
            print(f"⏰ {i}/{focus_time} - Time for a break!")
        elif remaining <= 2:
            print(f"📚 {i}/{focus_time} - Almost break time!")
        else:
            print(f"📖 {i}/{focus_time} - Stay focused...")
        time.sleep(1)
    
    print("\n☕ Break time! Relax...\n")
    
    for i in range(break_time, 0, -1):
        print(f"🧘 Break: {i} seconds remaining")
        time.sleep(1)
    
    print("\n✅ Break over! Back to work!")
    print()


def new_year_countdown():
    """
    Scenario 6: New Year's Eve countdown.
    """
    print("=" * 50)
    print("🎉 NEW YEAR'S EVE COUNTDOWN")
    print("=" * 50)
    print("Get ready to celebrate!\n")
    
    for i in range(10, 0, -1):
        if i == 1:
            print(f"🎆 {i}... ")
        else:
            print(f"🎊 {i}...")
        time.sleep(1)
    
    print("\n🎉🎊 HAPPY NEW YEAR! 🎊🎉")
    print("🎆" * 10)
    print()


def cooking_timer():
    """
    Scenario 7: Pasta cooking timer.
    """
    print("=" * 50)
    print("🍝 PASTA COOKING TIMER")
    print("=" * 50)
    
    cook_time = 7  # Normally would be 8-12 minutes
    print(f"Cooking pasta for {cook_time} seconds...\n")
    print("🔥 Water is boiling! Pasta added!\n")
    
    for i in range(1, cook_time + 1):
        remaining = cook_time - i
        percentage = int((i / cook_time) * 100)
        
        if remaining == 0:
            print(f"✓ {i}/{cook_time} seconds [{percentage}%] - Perfect al dente!")
        elif remaining <= 2:
            print(f"🍝 {i}/{cook_time} seconds [{percentage}%] - Almost ready, check texture!")
        else:
            print(f"⏲️  {i}/{cook_time} seconds [{percentage}%] - Still cooking...")
        
        time.sleep(1)
    
    print("\n🍽️  Pasta is ready! Drain and serve!")
    print()


def presentation_timer():
    """
    Scenario 8: Presentation/speech timer with warnings.
    """
    print("=" * 50)
    print("🎤 PRESENTATION TIMER")
    print("=" * 50)
    
    time_limit = 8  # 8 second presentation
    print(f"You have {time_limit} seconds for your speech.\n")
    print("🎤 Begin speaking NOW!\n")
    
    for elapsed in range(1, time_limit + 1):
        remaining = time_limit - elapsed
        
        if remaining == 0:
            print(f"⏰ {elapsed}s - TIME'S UP! Please wrap up.")
        elif remaining <= 2:
            print(f"⚠️  {elapsed}s - {remaining}s remaining - Start concluding!")
        elif remaining == time_limit // 2:
            print(f"⏱️  {elapsed}s - Halfway point!")
        else:
            print(f"✓ {elapsed}s - {remaining}s remaining")
        
        time.sleep(1)
    
    print("\n👏 Thank you for your presentation!")
    print()


def breathing_exercise():
    """
    Scenario 9: Guided breathing meditation.
    """
    print("=" * 50)
    print("🧘 BREATHING EXERCISE")
    print("=" * 50)
    print("Let's practice calm breathing.\n")
    
    cycles = 3
    
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}/{cycles}")
        
        # Breathe in
        print("\n🌬️  Breathe IN slowly...")
        for i in range(4):
            print("  ↑ " + "·" * (i + 1))
            time.sleep(1)
        
        # Hold
        print("\n⏸️  Hold your breath...")
        for i in range(2):
            print("  ─ Hold")
            time.sleep(1)
        
        # Breathe out
        print("\n🌊 Breathe OUT slowly...")
        for i in range(4):
            print("  ↓ " + "·" * (4 - i))
            time.sleep(1)
        
        print()
    
    print("✨ Exercise complete. You should feel more relaxed!")
    print()


def main():
    """
    Run all timer scenarios.
    """
    scenarios = [
        ("HIDE AND SEEKi", hide_and_seek_countdown),
        ("Rocket Launch", rocket_launch_countdown),
        ("Microwave Timer", microwave_timer),
        ("Workout Timer", fitness_workout_timer),
        ("Traffic Light", traffic_light_simulator),
        ("Study Timer", study_pomodoro_timer),
        ("New Year Countdown", new_year_countdown),
        ("Cooking Timer", cooking_timer),
        ("Presentation Timer", presentation_timer),
        ("Breathing Exercise", breathing_exercise)
    ]
    
    print("\n" + "=" * 50)
    print("⏰ TIME DELAY LOOP EXAMPLES")
    print("=" * 50)
    print("\nChoose a scenario:\n")
    
    for idx, (name, _) in enumerate(scenarios, 1):
        print(f"{idx}. {name}")
    print(f"{len(scenarios) + 1}. Run ALL scenarios")
    print("0. Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
        
        if choice == 0:
            print("Goodbye!")
            return
        elif choice == len(scenarios) + 1:
            print("\n🎬 Running all scenarios...\n")
            for name, func in scenarios:
                func()
                time.sleep(2)  # Pause between scenarios
        elif 1 <= choice <= len(scenarios):
            print()
            scenarios[choice - 1][1]()
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    main()
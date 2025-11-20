"""
Grade Calculator
A command-line tool that computes weighted averages for course grades.
Features input validation, modular design, and support for multiple assignments.
"""


def get_float_input(prompt, min_value=0.0, max_value=100.0):
    """
    Gets and validates a float input from the user.
    Args:
        prompt: The prompt message to display
        min_value: Minimum allowed value (default: 0.0)
        max_value: Maximum allowed value (default: 100.0)
    Returns:
        float: Valid user input
    """
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_assignment_data():
    """
    Collects assignment data from the user.
    Returns:
        list: List of tuples (assignment_name, score, weight)
    """
    assignments = []
    
    print("\n" + "="*60)
    print("Enter Assignment Information")
    print("="*60)
    print("(Enter assignment name as 'done' when finished)\n")
    
    total_weight = 0.0
    
    while True:
        name = input("Assignment name (or 'done' to finish): ").strip()
        
        if name.lower() == 'done':
            if len(assignments) == 0:
                print("Please enter at least one assignment!")
                continue
            break
        
        if not name:
            print("Assignment name cannot be empty!")
            continue
        
        score = get_float_input(f"Score for '{name}' (0-100): ", 0.0, 100.0)
        weight = get_float_input(f"Weight for '{name}' (0-100): ", 0.0, 100.0)
        
        assignments.append((name, score, weight))
        total_weight += weight
        
        print(f"✓ Added: {name} - Score: {score}%, Weight: {weight}%")
        print(f"Total weight so far: {total_weight:.2f}%\n")
    
    return assignments, total_weight


def calculate_weighted_average(assignments, total_weight):
    """
    Calculates the weighted average grade.
    Args:
        assignments: List of tuples (name, score, weight)
        total_weight: Total weight of all assignments
    Returns:
        tuple: (weighted_average, weighted_sum, total_weight)
    """
    if total_weight == 0:
        return 0.0, 0.0, 0.0
    
    weighted_sum = sum(score * weight for _, score, weight in assignments)
    weighted_average = weighted_sum / total_weight
    
    return weighted_average, weighted_sum, total_weight


def get_letter_grade(percentage):
    """
    Converts percentage to letter grade.
    Args:
        percentage: Grade percentage (0-100)
    Returns:
        str: Letter grade
    """
    if percentage >= 97:
        return "A+"
    elif percentage >= 93:
        return "A"
    elif percentage >= 90:
        return "A-"
    elif percentage >= 87:
        return "B+"
    elif percentage >= 83:
        return "B"
    elif percentage >= 80:
        return "B-"
    elif percentage >= 77:
        return "C+"
    elif percentage >= 73:
        return "C"
    elif percentage >= 70:
        return "C-"
    elif percentage >= 67:
        return "D+"
    elif percentage >= 63:
        return "D"
    elif percentage >= 60:
        return "D-"
    else:
        return "F"


def get_gpa(percentage):
    """
    Converts percentage to GPA (4.0 scale).
    Args:
        percentage: Grade percentage (0-100)
    Returns:
        float: GPA value
    """
    if percentage >= 97:
        return 4.0
    elif percentage >= 93:
        return 4.0
    elif percentage >= 90:
        return 3.7
    elif percentage >= 87:
        return 3.3
    elif percentage >= 83:
        return 3.0
    elif percentage >= 80:
        return 2.7
    elif percentage >= 77:
        return 2.3
    elif percentage >= 73:
        return 2.0
    elif percentage >= 70:
        return 1.7
    elif percentage >= 67:
        return 1.3
    elif percentage >= 63:
        return 1.0
    elif percentage >= 60:
        return 0.7
    else:
        return 0.0


def display_results(assignments, weighted_average, total_weight):
    """
    Displays the calculation results in a formatted way.
    Args:
        assignments: List of tuples (name, score, weight)
        weighted_average: Calculated weighted average
        total_weight: Total weight of all assignments
    """
    print("\n" + "="*60)
    print("Grade Calculation Results")
    print("="*60)
    
    print(f"\n{'Assignment':<30} {'Score':<10} {'Weight':<10} {'Contribution':<15}")
    print("-" * 60)
    
    for name, score, weight in assignments:
        contribution = (score * weight) / total_weight if total_weight > 0 else 0
        print(f"{name:<30} {score:<10.2f} {weight:<10.2f} {contribution:<15.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL':<30} {'':<10} {total_weight:<10.2f}")
    
    print("\n" + "="*60)
    print(f"Weighted Average: {weighted_average:.2f}%")
    print(f"Letter Grade: {get_letter_grade(weighted_average)}")
    print(f"GPA: {get_gpa(weighted_average):.2f}")
    print("="*60)
    
    # Warning if total weight doesn't equal 100%
    if abs(total_weight - 100.0) > 0.01:
        print(f"\n⚠️  Warning: Total weight is {total_weight:.2f}%, not 100%.")
        print("   The calculation assumes this is the total weight.")


def main():
    """Main function to run the grade calculator."""
    print("\n" + "="*60)
    print("Grade Calculator - Weighted Average Tool")
    print("="*60)
    print("This tool calculates your course grade using weighted averages.")
    print("Enter your assignments with their scores and weights.")
    
    while True:
        # Get assignment data
        assignments, total_weight = get_assignment_data()
        
        # Calculate weighted average
        weighted_average, weighted_sum, total_weight = calculate_weighted_average(
            assignments, total_weight
        )
        
        # Display results
        display_results(assignments, weighted_average, total_weight)
        
        # Ask if user wants to calculate another course
        print("\n" + "="*60)
        another = input("Calculate another course? (yes/no): ").strip().lower()
        
        if another not in ['yes', 'y']:
            print("\nThank you for using the Grade Calculator! 👋")
            break


if __name__ == "__main__":
    main()


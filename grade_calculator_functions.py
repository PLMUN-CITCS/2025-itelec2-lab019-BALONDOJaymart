def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    
    Returns:
        float: The valid numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: ").strip())  # Exact prompt required
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    
    Parameters:
        score (float): The numerical score to evaluate.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main program flow to obtain user input, calculate grade, and display results.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")  # Matches exact output format

if __name__ == "__main__":
    main()

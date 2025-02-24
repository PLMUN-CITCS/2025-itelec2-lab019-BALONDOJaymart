def get_student_score() -> float:
    """
    Prompts the user to enter their score and returns it as a float.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score: float = float(input("Enter your score: "))  # Type hint for score
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

def main() -> None:
    """
    Main program flow to calculate and display the student's grade.
    
    Returns:
        None
    """
    score: float = get_student_score()  # Type hint for score
    grade: str = calculate_grade(score)  # Type hint for grade
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()

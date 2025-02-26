# 2025-ITELEC2-LAB019
Week 05 - Working with Functions

Laboratory # 19 - Group Activity # 01 - Problem 01: Enhanced Grade Calculator with Function Decomposition

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 19 - Group Activity # 01 - Problem 01: Enhanced Grade Calculator with Function Decomposition**

   **Objective:**
   This challenge aims to reinforce your understanding of functions and their practical application in program design. You will practice:
   - Defining functions with specific purposes.
   - Using the return statement to pass values between functions.
   - Decomposing a problem into smaller, more manageable functions.
   - Applying conditional logic (if, elif, else) for decision-making.
   - Handling user input and ensuring valid data types.

   **Desired Output:**
   ```bash
   Enter your score: 85
   Your Grade is: B
   ```
   
   **Notable Observations:**
   - Function Decomposition: The problem is divided into two distinct functions (get_student_score and calculate_grade), promoting modularity and code reusability.
   - Data Flow: The get_student_score function handles user input and returns a numerical score, which is then passed as an argument to the calculate_grade function. The calculated grade is returned and used for the final output.
   - Conditional Logic: The calculate_grade function uses if, elif, and else statements to determine the correct grade based on the provided score and the grading scale.

   **Python Best Practices**
   - Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables (e.g., get_student_score, calculate_grade, score).
   - Docstrings: Include docstrings for each function to explain its purpose, parameters, and return value.
   - Type Hints (Optional but Recommended): Use type hints to indicate the expected data types for function parameters and return values. This improves code readability and helps with error checking.
   - Input Validation (Challenge Extension): Consider adding input validation to the get_student_score function to ensure the user enters a valid numerical score.
   - Test Thoroughly: Test your program with various inputs (including edge cases and invalid input) to ensure it functions correctly.

   **Challenge Requirements:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `grade_calculator_functions.py`
      
   2. get_student_score() Function:
      - Purpose: Handles user input to obtain the student's score.
      - No parameters.
      - Prompts the user to enter their score.
      - Reads and converts the input to a numerical type (integer or float).
      - Returns the numerical score.
      
   3. calculate_grade(score) Function:
      - Purpose: Determines the letter grade based on the given score and grading scale.
      - Takes one parameter: score (numeric).
      - Uses conditional statements (if, elif, else) to check the score against the grading scale.
      - Returns the corresponding letter grade ('A', 'B', 'C', 'D', or 'F') as a string.

   4. Main Program Flow
      - Calls get_student_score() to obtain the student's score.
      - Calls calculate_grade(), passing the returned score as an argument.
      - Displays the calculated grade to the user.
     
   **Conclusion**
   This challenge encourages you to apply your knowledge of functions to create a practical program that solves a real-world problem. By decomposing the problem into separate functions, you can write more organized, reusable, and maintainable code. This modular approach is essential for building larger and more complex programs.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 05 - Laboratory # 19"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```

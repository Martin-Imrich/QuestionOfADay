import random
import datetime
import sys

def get_daily_question():
    # Read questions from file
    with open('questions.txt', 'r') as file:
        questions = file.readlines()
    
    # Get today's date
    today = datetime.date.today()
    
    # Use the day of the year to select a question
    random.seed(today.year)  # Ensure the same question is selected for the whole day
    question_index = today.timetuple().tm_yday % len(questions)
    
    return questions[question_index]

def main():
    question = get_daily_question()
    print("Today's question:")
    print(question)
    sys.stdout.write(question)
    sys.stdout.flush()
    print("Press Enter to exit...")
    val = input()

if __name__ == "__main__":
    main()

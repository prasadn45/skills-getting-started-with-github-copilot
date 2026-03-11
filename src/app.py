def signup_for_activity(student, activity):
    participants = []
    
    # Validate student is not already registered
    if student in participants:
        raise ValueError("Student is already signed up!")
        
    participants.append(student)
    # Code logic for signing up the student to the activity
    print(f"{student} has been signed up for {activity}.")

# Original function code needed for context

# Code logic for handling activity signups, participant management, etc.
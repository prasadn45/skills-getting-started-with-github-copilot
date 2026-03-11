from fastapi import HTTPException

# Assuming participants is a list that stores email addresses of registered participants
participants = []

async def signup_for_activity(email: str):
    # Duplicate registration check
    if email in participants:
        raise HTTPException(status_code=400, detail="Student is already registered")
    participants.append(email)
    return {"message": "Registration successful"}
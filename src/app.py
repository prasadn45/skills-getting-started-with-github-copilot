from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class Activity(BaseModel):
    name: str
    description: str
    schedule: str
    max_participants: int
    participants: List[str]
    category: str

activities: Dict[str, Activity] = {
    "Soccer": Activity(
        name="Soccer",
        description="A team game played with a round ball that may not be touched with the hands or arms during play.",
        schedule="Wednesdays at 4 PM",
        max_participants=20,
        participants=[],
        category="Sport"
    ),
    "Tennis": Activity(
        name="Tennis",
        description="A racket sport that can be played individually against a single opponent or between two teams of two players each.",
        schedule="Fridays at 6 PM",
        max_participants=20,
        participants=[],
        category="Sport"
    ),
    "Basketball": Activity(
        name="Basketball",
        description="A team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court.",
        schedule="Thursdays at 5 PM",
        max_participants=15,
        participants=[],
        category="Sport"
    ),
    "Theater Club": Activity(
        name="Theater Club",
        description="A club for students interested in acting and theater production.",
        schedule="Mondays at 3 PM",
        max_participants=30,
        participants=[],
        category="Art"
    ),
    "Music Band": Activity(
        name="Music Band",
        description="A group of musicians who perform together.",
        schedule="Tuesdays at 4 PM",
        max_participants=10,
        participants=[],
        category="Art"
    ),
    "Robotics Club": Activity(
        name="Robotics Club",
        description="A club focused on building and programming robots.",
        schedule="Thursdays at 4 PM",
        max_participants=12,
        participants=[],
        category="Intellectual"
    ),
    "Debate Team": Activity(
        name="Debate Team",
        description="A team that participates in organized debates on various topics.",
        schedule="Wednesdays at 6 PM",
        max_participants=15,
        participants=[],
        category="Intellectual"
    )
}

@app.post("/register/{activity_name}")
async def register(activity_name: str, participant_name: str):
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    if len(activity.participants) >= activity.max_participants:
        raise HTTPException(status_code=400, detail="Activity is full")
    if participant_name in activity.participants:
        raise HTTPException(status_code=400, detail="Participant is already registered")
    activity.participants.append(participant_name)
    return {"message": "Registration successful", "activity": activity.name}

@app.get("/activities")
async def get_activities():
    return activities

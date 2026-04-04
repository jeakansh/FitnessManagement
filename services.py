import random

class FitnessService:
    def __init__(self):
        # Programs for AI-style generation derived from Aceestver-3.2.4.py
        self.program_templates = {
            "Fat Loss": ["Full Body HIIT", "Circuit Training", "Cardio + Weights"],
            "Muscle Gain": ["Push/Pull/Legs", "Upper/Lower Split", "Full Body Strength"],
            "Beginner": ["Full Body 3x/week", "Light Strength + Mobility"]
        }

    def generate_ai_program(self, program_type="Fat Loss"):
        """Mock AI behavior to pick a random routine for the program type."""
        if program_type not in self.program_templates:
            program_type = "Beginner"
        return random.choice(self.program_templates[program_type])

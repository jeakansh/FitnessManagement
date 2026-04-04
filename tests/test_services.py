import pytest
from services import FitnessService

def test_generate_ai_program_fat_loss():
    service = FitnessService()
    result = service.generate_ai_program("Fat Loss")
    assert result in ["Full Body HIIT", "Circuit Training", "Cardio + Weights"]

def test_generate_ai_program_muscle_gain():
    service = FitnessService()
    result = service.generate_ai_program("Muscle Gain")
    assert result in ["Push/Pull/Legs", "Upper/Lower Split", "Full Body Strength"]

def test_generate_ai_program_beginner():
    service = FitnessService()
    result = service.generate_ai_program("Beginner")
    assert result in ["Full Body 3x/week", "Light Strength + Mobility"]

def test_generate_ai_program_invalid_fallback():
    service = FitnessService()
    result = service.generate_ai_program("Unknown Program")
    # Should fallback to Beginner
    assert result in ["Full Body 3x/week", "Light Strength + Mobility"]

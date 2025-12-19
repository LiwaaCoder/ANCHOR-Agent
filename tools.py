from google.genai import types

def emergency_alert(reason: str, location: str):
    """
    Triggers an emergency alert to caregivers/services.
    
    Args:
        reason: The reason for the emergency (e.g., "Fall detected", "User shouted help").
        location: The current location description or coordinates.
    """
    print(f"!!! EMERGENCY ALERT TRIGGERED !!!")
    print(f"Reason: {reason}")
    print(f"Location: {location}")
    print(f"!!! ALERT SENT !!!")
    return {"status": "alert_sent", "reason": reason, "location": location}

# Tool definition for Gemini
emergency_alert_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="emergency_alert",
            description="Triggers an emergency alert to caregivers when a danger is detected.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "reason": types.Schema(type=types.Type.STRING, description="The specific reason for the emergency."),
                    "location": types.Schema(type=types.Type.STRING, description="Current location of the user."),
                },
                required=["reason", "location"],
            ),
        )
    ]
)

all_tools = [emergency_alert_tool]

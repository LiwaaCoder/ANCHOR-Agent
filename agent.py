import os
import datetime
from google import genai
from config import SYSTEM_INSTRUCTION, GOOGLE_API_KEY
from tools import all_tools

class AnchorAgent:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        # We use a chat session to maintain the "Cognitive Threading"
        self.chat = self.client.chats.create(
            model="gemini-2.5-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                tools=all_tools,
                temperature=0.7, # Slightly creative but grounded
            )
        )
        print("ANCHOR Agent initialized and ready.")

    def redact_pii(self, text):
        """
        Simple regex-based PII redaction for numerical sequences.
        """
        import re
        # Redact potential credit card numbers (13-19 digits)
        text = re.sub(r'\b(?:\d[ -]*?){13,16}\b', '[REDACTED_NUMERIC_ID]', text)
        return text

    def process_input(self, text_input=None, image_path=None, audio_path=None, context=None):
        """
        Processes multimodal input and returns the agent's textual response.
        """
        message_parts = []

        # Add Context Metadata first
        if context:
            context_str = f"[CONTEXT]: {context}"
            message_parts.append(context_str)
        else:
             # Default context if none provided
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_parts.append(f"[CONTEXT]: Time: {now}")

        # Add Text (could be audio transcription)
        if text_input:
            safe_text = self.redact_pii(text_input)
            message_parts.append(f"[AUDIO_TRANSCRIPT]: {safe_text}")

        # Add Image
        if image_path:
            try:
                # We need to read the image file. 
                 with open(image_path, "rb") as f:
                    image_data = f.read()
                    message_parts.append(genai.types.Part.from_bytes(data=image_data, mime_type="image/jpeg")) 
            except Exception as e:
                print(f"Error loading image: {e}")
                return "Error processing image input."

        # Add Audio Codec
        if audio_path:
             # Similar handling for audio files
             pass 

        # Send to Gemini
        try:
            response = self.chat.send_message(message_parts)
            
            # Smart extraction to avoid 'thought' warnings
            final_text = ""
            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if part.text:
                        final_text += part.text
            
            if not final_text:
                final_text = response.text # Fallback
                
            return final_text
        except Exception as e:
            print(f"Error communicating with Gemini: {e}")
            return "I am having trouble connecting to my service."

    def generate_daily_reflection(self):
        """
        Triggers the 8:00 PM reflection.
        """
        prompt = "It is now 8:00 PM. Please generate the 'Daily Reflection' based on today's events."
        return self.chat.send_message(prompt).text

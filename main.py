import os
import sys
# Add current directory to path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent import AnchorAgent

def main():
    print("Initializing ANCHOR System...")
    try:
        agent = AnchorAgent()
    except Exception as e:
        print(f"Failed to initialize: {e}")
        return

    print("\n--- ANCHOR IS LISTENING ---")
    print("Enter mock inputs. Format examples:")
    print("  'text: Who is that?'")
    print("  'image: /path/to/image.jpg'")
    print("  'context: GPS at park'")
    print("  'quit' to exit.")

    while True:
        try:
            user_input = input("\n[INPUT]> ").strip()
            # Clean input (remove terminal pasted quotes)
            user_input = user_input.strip("'\"").strip()

            if user_input.lower() in ["quit", "exit"]:
                break
            
            text_val = None
            image_val = None
            context_val = None

            # Smart parser
            if user_input.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) and os.path.exists(user_input):
                 print(f"[System]: Detected image file: {user_input}")
                 image_val = user_input
            elif user_input.startswith("image:"):
                image_val = user_input.split("image:", 1)[1].strip()
            elif user_input.startswith("context:"):
                context_val = user_input.split("context:", 1)[1].strip()
            elif user_input == "trigger_reflection":
                 print(f"\n[ANCHOR]: {agent.generate_daily_reflection()}")
                 continue
            else:
                text_val = user_input

            response = agent.process_input(text_input=text_val, image_path=image_val, context=context_val)
            print(f"\n[ANCHOR]: {response}")

        except KeyboardInterrupt:
            print("\nShutting down.")
            break
        except EOFError:
            print("\nEnd of input. Exiting.")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")

if __name__ == "__main__":
    main()

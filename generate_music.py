import json
import os

def load_story():
    with open('story.json', 'r') as f:
        return json.load(f)

def generate_music():
    story = load_story()
    print(f"Generating music for style: {story['music_style']}")
    
    os.makedirs('output/audio', exist_ok=True)
    # Placeholder for Audiocraft or other music gen API
    # music_file = call_music_gen(story['music_style'])
    print("Background music generated.")

if __name__ == "__main__":
    generate_music()

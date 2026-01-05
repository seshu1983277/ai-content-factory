import json
import os

def generate_subtitles():
    with open('story.json', 'r') as f:
        story = json.load(f)
    
    print("Generating SRT files and on-screen text overlays...")
    os.makedirs('output/subtitles', exist_ok=True)

if __name__ == "__main__":
    generate_subtitles()

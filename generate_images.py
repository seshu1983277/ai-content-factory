import json
import os

def load_story():
    with open('story.json', 'r') as f:
        return json.load(f)

def generate_images():
    story = load_story()
    print(f"Generating images for theme: {story['theme']}")
    
    os.makedirs('output/images', exist_ok=True)
    
    for scene in story['scenes']:
        prompt = scene['video_prompt']
        scene_num = scene['scene_number']
        print(f"Generating image for Scene {scene_num}: {prompt}")
        # Placeholder for SD API call
        # with open(f'output/images/scene_{scene_num}.jpg', 'wb') as f:
        #     f.write(api_call(prompt))

if __name__ == "__main__":
    generate_images()

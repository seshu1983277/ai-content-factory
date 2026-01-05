import json

def publish():
    with open('story.json', 'r') as f:
        story = json.load(f)
    
    meta = story['instagram']
    print(f"Publishing to Instagram: {meta['caption']}")
    # API calls to Instagram Graph API

if __name__ == "__main__":
    publish()

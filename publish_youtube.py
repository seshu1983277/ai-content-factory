import json

def publish():
    with open('story.json', 'r') as f:
        story = json.load(f)
    
    meta = story['youtube']
    print(f"Publishing to YouTube: {meta['title']}")
    # API calls to YouTube Data API v3

if __name__ == "__main__":
    publish()

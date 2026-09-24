import json
import requests
import datetime

top_stories = requests.get(
    url="https://hacker-news.firebaseio.com/v0/topstories.json",
    headers = {"User-Agent": "TrendPulse/1.0"}

)

# print(top_stories.status_code)
# print(top_stories.json())
stories = top_stories.json()
# print(type(stories))
technology_counter = worldnews_counter = sports_counter = science_counter = entertainment_counter = 0

json_stories = []

technology_keywords = ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"]
worldnews_keywords = ["war", "government", "country", "president", "election", "climate", "attack", "global"]
sports_keywords = ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"]
science_keywords = ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"]
entertainment_keywords = ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

def lower(l):
    lowercase_keywords = []
    for word in l:
       lowercase_keywords.append(word.lower())
    return lowercase_keywords

technology_keywords = lower(technology_keywords)
worldnews_keywords = lower(worldnews_keywords)
sports_keywords = lower(sports_keywords)
science_keywords = lower(science_keywords)
entertainment_keywords = lower(entertainment_keywords)

keywords_list = [technology_keywords, worldnews_keywords, sports_keywords, science_keywords, entertainment_keywords]

print(keywords_list)
count = 25

itr = 0


for story in stories:
    story_detail = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story}.json',headers = {"User-Agent": "TrendPulse/1.0"}
)

    # print(f"-------------------{stories.index(story)}--------------------")
    # print(story_detail.status_code)
    story_detail = story_detail.json()

    if "descendants" not in story_detail:
        story_detail["descendants"] = None

    detail = {
        "post_id" : story_detail["id"],
        "title" : story_detail["title"],
        "score" : story_detail["score"],
        "num_comments" : story_detail["descendants"],
        "author" : story_detail["by"],
        "collected_at" : str(datetime.datetime.now())
    }


    if any(word in detail["title"].lower() for word in technology_keywords) and technology_counter<count+5:
        detail["category"] = "Technology"
        technology_counter += 1
        json_stories.append(detail)

    elif any(word in detail["title"].lower() for word in worldnews_keywords) and worldnews_counter<count:
        detail["category"] = "World News"
        worldnews_counter += 1
        json_stories.append(detail)

    elif any(word in detail["title"].lower() for word in sports_keywords) and sports_counter<count:
        detail["category"] = "Sports"
        sports_counter += 1
        json_stories.append(detail)


    elif any(word in detail["title"].lower() for word in science_keywords) and science_counter<count:
        detail["category"] = "Science"
        science_counter += 1
        json_stories.append(detail)

    elif any(word in detail["title"].lower() for word in entertainment_keywords) and entertainment_counter<count+5:
        detail["category"] = "Entertainment"
        entertainment_counter += 1
        json_stories.append(detail)

    if "category" not in detail:
        continue
    itr += 1

print("Stories collected in Total:", itr)

with open("data/output.json", "w") as file:
    json.dump(json_stories, file, indent=4)



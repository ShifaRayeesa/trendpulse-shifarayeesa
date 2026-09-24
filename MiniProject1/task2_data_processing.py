import pandas as pd

json_file = "data/output.json"
csv_file = "data/output.csv"
df = pd.read_json(json_file)
print(f"Loaded {len(df)} stories from {json_file}")

df.drop_duplicates(["post_id"])
print(f"After removing duplicates : {len(df)}")

df.dropna(subset=["post_id","title","score"], how="any")
print(f"After removing nulls : {len(df)}")

df["score"] = df["score"].astype(int)
df["num_comments"] = pd.to_numeric(df["num_comments"]).astype('Int64')

df = df[df["score"] >= 5]
print(f"After removing low score : {len(df)}")

df["title"] = df["title"].str.strip()
# print(df.columns.tolist())
# print(f"----------------\n{df}\n------------------")
print("\n")
print(f"Saved {len(df)} stories to file")
technology_stories = df[df["category"] == "Technology"]
worldnews_stories = df[df["category"] == "World News"]
sports_stories = df[df["category"] == "Sports"]
science_stories = df[df["category"] == "Science"]
entertainment_stories = df[df["category"] == "Entertainment"]
print("\n")
print(f"Tecnology stories : {len(technology_stories)}")
print(f"World News stories : {len(worldnews_stories)}")
print(f"Sports stories : {len(sports_stories)}")
print(f"Science stories : {len(science_stories)}")
print(f"Entertainment stories : {len(entertainment_stories)}")

df.to_csv(csv_file, index=False)

import pandas as pd

read_csv = "data/output.csv"
trend_csv = "data/trends.csv"

df = pd.read_csv(read_csv)
print(f"Loaded data : {df.shape}")
print(f"First 5 rows: \n{df.head()}")
# print(f"Rows = {df.shape[0]}, Columns = {df.shape[1]}")

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print(f"Average Score    : {avg_score}")
print(f"Average comments : {avg_comments}")

# Mean, Median and Standard Deviation of score
median_score = df["score"].median().astype(int)
sd_score = df["score"].std()
min_score = df["score"].min()
max_score = df["score"].max()

print("--- NumPy Stats ---")
print(f"Mean score    : {avg_score}")
print(f"Median score  : {median_score}")
print(f"Std Deviation : {sd_score}")
print(f"Max score     : {max_score}")
print(f"Min score     : {min_score}")

# Top Category
top_category = df['category'].value_counts().idxmax()
topcategory_count = len(df[df["category"] == top_category])
print(f"Most stories in: {top_category} ({topcategory_count} stories)")

# Max commented story
top_commented = df["num_comments"].idxmax()
top_story = df.loc[top_commented, ["post_id","title", "num_comments"]]
print(f"Most commented story is '{top_story['title']}' (id:{top_story['post_id']}) -"
      f" {top_story['num_comments']} comments")

#Adding new columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Saving the updated dataframe to csv
df.to_csv(trend_csv, index=False)

print(f"Saved to {trend_csv}")
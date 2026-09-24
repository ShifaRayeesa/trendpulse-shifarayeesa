import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

read_csv = "trends.csv"

df = pd.read_csv(read_csv)

fig = plt.figure(figsize=(14, 8), layout="constrained")

ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

top10 = df.nlargest(10, "score").copy()
top10["short_title"] = top10["title"].apply(lambda x: x[:47]+"..." if len(x)>50 else x)
top10 = top10.iloc[::-1]

ax1.barh(top10["short_title"], top10["score"], color="skyblue", edgecolor="black")
ax1.set_title("Top 10 Stories by Score", fontsize=14, fontweight="bold")
ax1.set_xlabel ("Score", fontsize=12)
ax1.set_ylabel("Story Title", fontsize=12)
ax1.tick_params(axis="y", labelsize=8.0)

category_count = df["category"].value_counts()
color_palatte = ["red", "blue", "green", "yellow", "pink"]

ax2.bar(category_count.index, category_count.values, color=color_palatte, edgecolor="black")
ax2.set_title("Stories per Category", fontsize=14, fontweight="bold")
ax2.set_xlabel("Category", fontsize=12)
ax2.set_ylabel("No. of stories", fontsize=12)
ax2.tick_params(axis='x', rotation=20, labelsize=8.0)

sb.scatterplot(x=df["score"], y=df["num_comments"], hue=df["is_popular"], palette="viridis",edgecolor="black", ax=ax3)
ax3.set_title("Score vs Comments", fontsize=14, fontweight="bold")
ax3.set_xlabel("Score", fontsize=12)
ax3.set_ylabel("Comments", fontsize=12)
ax3.tick_params(axis='both', labelsize=10)


plt.suptitle("Trend Pulse Dashboard", fontsize=16, fontweight="bold")
plt.savefig("outputs/dashboard.png")
plt.show()
plt.close()
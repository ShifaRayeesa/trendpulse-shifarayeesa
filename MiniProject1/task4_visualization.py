import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

read_csv = "data/trends.csv"

df = pd.read_csv(read_csv)

def draw():
    plt.tight_layout()
    plt.savefig("outputs/chart3_scatter.png")
    plt.show()
    plt.close()

def get_topstories():
    top10 = df.nlargest(10, "score").copy()
    top10["short_title"] = top10["title"].apply(lambda x: x[:47]+"..." if len(x)>50 else x)
    top10 = top10.iloc[::-1]
    plt.figure(figsize=(10,6))
    plt.barh(top10["short_title"], top10["score"], color="skyblue", edgecolor="black")
    plt.title("Top 10 Stories by Score", fontsize=14, fontweight="bold")
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Story Title", fontsize=12)
    draw()

def get_categories():
    category_count = df["category"].value_counts()
    color_palatte = ["red", "blue", "green", "yellow", "pink"]
    plt.figure(figsize=(8,6))
    plt.bar(category_count.index, category_count.values, color=color_palatte, edgecolor="black")
    plt.title("Stories per Category", fontsize=14, fontweight="bold")
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("No. of stories", fontsize=12)
    draw()

def get_scatterplot():
    plt.figure(figsize=(7,7))
    sb.scatterplot(x=df["score"], y=df["num_comments"], hue=df["is_popular"], palette="viridis",edgecolor="black")
    plt.title("Score vs Comments", fontsize=14, fontweight="bold")
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Comments", fontsize=12)
    draw()

print("Charts: \n1.Top 10 Stories by Score \n2.Stories per Category \n3.Score vs Comments")
choice = int(input("Enter your choice:"))

match choice:
    case 1:
        get_topstories()

    case 2:
        get_categories()

    case 3:
        get_scatterplot()



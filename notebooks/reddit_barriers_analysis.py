import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/mens_skincare_reddit_starter_dataset.csv")

# ---------------------------
# PRE-ADOPTION BARRIERS
# ---------------------------
pre_df = df[df["stage"] == "pre_adoption"]

pre_counts = pre_df["barrier"].value_counts()

print("Pre-adoption barrier counts:")
print(pre_counts)

pre_counts.plot(kind="bar")
plt.title("Pre-Adoption Barriers to Male Skincare")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.savefig("../pre_adoption_barriers.png", bbox_inches="tight")
plt.show()


# ---------------------------
# POST-ADOPTION PATTERNS
# ---------------------------
post_df = df[df["stage"] == "post_adoption"]

post_counts = post_df["barrier"].value_counts()

print("\nPost-adoption patterns:")
print(post_counts)

post_counts.plot(kind="bar")
plt.title("Post-Adoption Preferences (Advice Patterns)")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.savefig("../post_adoption_patterns.png", bbox_inches="tight")
plt.show()
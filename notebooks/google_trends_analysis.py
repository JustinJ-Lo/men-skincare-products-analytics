import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# LOAD (CORRECT)
# ---------------------------
df = pd.read_csv("../data/google_trends.csv")

# Rename Time → Date
df.rename(columns={"Time": "Date"}, inplace=True)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Convert numeric columns
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Set index
df.set_index("Date", inplace=True)

# ---------------------------
# PLOT
# ---------------------------
plt.figure(figsize=(12,6))

for col in df.columns:
    plt.plot(df.index, df[col], label=col)

plt.title("Google Trends: Men's Skincare Search Interest")
plt.ylabel("Search Interest")
plt.xlabel("Time")

plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.savefig("../trends_chart.png", bbox_inches="tight")
plt.show()

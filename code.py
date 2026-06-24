import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import string

# Read text file
with open("sample_text.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Define stop words
stop_words = {
    "the", "is", "and", "a", "to", "in", "of", "for", "on", "with", "as", "by",
    "an", "at", "be", "this", "that", "are", "it", "from"
}

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Tokenize words
words = text.split()

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Count frequencies
word_counts = Counter(filtered_words)

# Get top 20 words
top_words = word_counts.most_common(20)

print("Top 20 words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar([w for w, _ in top_words], [f for _, f in top_words])
plt.xticks(rotation=45)
plt.title("Top 20 Word Frequencies")
plt.tight_layout()
plt.savefig("bar_chart_example.png")
plt.show()

# Word cloud
wc = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(" ".join(filtered_words))

wc.to_file("word_cloud_example.png")

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
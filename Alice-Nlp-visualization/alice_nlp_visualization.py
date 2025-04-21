import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from sklearn.decomposition import PCA
import gensim.downloader as api
import seaborn as sns

# Load and clean text
with open("C:/Users/mrvul/PycharmProjects/TranPhuongNam_2202085/Alice-Nlp-visualization/11-0.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Remove Project Gutenberg headers and footers
text = re.split(r"\*\*\* START OF.*?\*\*\*", text, maxsplit=1)[-1]
text = re.split(r"\*\*\* END OF.*?\*\*\*", text, maxsplit=1)[0]

# Remove punctuation and make lowercase
clean_text = re.sub(r"[^a-zA-Z\s]", "", text).lower()
words = clean_text.split()

# Count word frequencies
word_counts = Counter(words)

# Word Cloud
wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
plt.figure(figsize=(15, 7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Alice in Wonderland")
plt.show()

# Bar Chart of Top 20 Words
most_common = word_counts.most_common(20)
labels, values = zip(*most_common)

plt.figure(figsize=(12, 6))
plt.bar(labels, values, color='skyblue')
plt.xticks(rotation=45)
plt.title("Top 20 Most Common Words")
plt.ylabel("Frequency")
plt.show()

# Load GloVe embeddings
glove = api.load("glove-wiki-gigaword-100")

# Filter for top words in GloVe
filtered_words = [word for word, _ in most_common if word in glove]
vectors = np.array([glove[word] for word in filtered_words])

# Reduce dimensions with PCA
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

# Plot semantic relationships
plt.figure(figsize=(10, 8))
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1])
for i, word in enumerate(filtered_words):
    plt.text(reduced_vectors[i, 0] + 0.1, reduced_vectors[i, 1], word)
plt.title("Semantic Word Relationships via GloVe + PCA")
plt.grid(True)
plt.show()

# Word similarity heatmap
similarities = np.array([[glove.similarity(w1, w2) for w2 in filtered_words] for w1 in filtered_words])

plt.figure(figsize=(12, 10))
sns.heatmap(similarities, xticklabels=filtered_words, yticklabels=filtered_words, cmap='coolwarm', annot=False)
plt.title("Word Similarity Heatmap (GloVe)")
plt.show()

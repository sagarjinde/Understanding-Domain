from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import pyplot
import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# define training data

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()

file_names = os.listdir('./asdf')

file_count = len(file_names)
div_file_size = file_count/5

default_stopwords = set(nltk.corpus.stopwords.words('english'))
custom_stopwords = set(["'s","n't","'re","'ll","'d","'ve","''","``","--"])
all_stopwords = default_stopwords | custom_stopwords

#calculating frequency distrabution
sent_words = []
all_doc_words = []
print('Extracting words and performing lemmatization.')

for file_name in file_names:
	doc_words = []
	with open('./asdf/' + file_name) as f:
		sentences = nltk.sent_tokenize(f.read())
		for sentence in sentences:	

			words = nltk.word_tokenize(sentence)

			# Remove single-character tokens (mostly punctuation)
			words = [word for word in words if len(word) > 1]

			# Remove numbers
			words = [word for word in words if not word.isdigit()]

			# Lowercase all words (default_stopwords are lowercase too)
			words = [word.lower() for word in words]

			# Remove stopwords
			words = [word for word in words if word not in all_stopwords]

			# perform lemmatization of words
			words = [wordnet_lemmatizer.lemmatize(word) for word in words]

			sent_words.append(words)
			doc_words.extend(words)

		f.close()
	all_doc_words.append(doc_words)

print('Training Word2Vec Model')
# train model
model_50 = Word2Vec(sent_words, min_count=500, size = 50)
model_50.save("word2vec50.model")

model_100 = Word2Vec(sent_words, min_count=500, size = 100)
model_100.save("word2vec100.model")


# fit a 2d PCA model to the vectors
X = model_50[model_50.wv.vocab]

# Applying K-Means
kmeans = KMeans(n_clusters=4, random_state=0)
pred_y = kmeans.fit_predict(X)

# dimentionality reduction
tsne = TSNE()
result = tsne.fit_transform(X)


print('Creating a plot of words whose frequency is more than 500')
# create a scatter plot of the projection

# size = 50
words = list(model_50.wv.vocab)
for i, word in enumerate(words):
  	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]), zorder=1)
pyplot.scatter(result[:, 0], result[:, 1], c=pred_y, cmap='rainbow', zorder=2)
pyplot.suptitle("Word2Vec with size = 50")
pyplot.show()

# size = 100
words = list(model_100.wv.vocab)
kmeans = KMeans(n_clusters=4, random_state=0)
pred_y = kmeans.fit_predict(result)
for i, word in enumerate(words):
  	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]), zorder=1)
pyplot.scatter(result[:, 0], result[:, 1], c=pred_y, cmap='rainbow', zorder=2)
pyplot.suptitle("Word2Vec with size = 100")
pyplot.show()

# Doc2Vec
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(all_doc_words)]
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)

print('Training Doc2Vec')
for epoch in range(10):
	print('iteration {0}/10'.format(epoch+1))
	model.train(documents,
		total_examples=model.corpus_count,
		epochs=20)
	# decrease the learning rate
	model.alpha -= 0.0002
	# fix the learning rate, no decay
	model.min_alpha = model.alpha


docvec = []
for i in range(file_count):
	docvec.append(model.docvecs[i])

# applying K-Means
kmeans = KMeans(n_clusters=4, random_state=0)
pred_y = kmeans.fit_predict(docvec)

# dimentionality reduction
result = tsne.fit_transform(docvec)

# find file index
"""game_wanted = ['gameURL_318.txt', 'gameURL_600.txt', 'gameURL_601.txt']
game_index = []
for i in range(file_count):
	if file_names[i] in game_wanted:
		game_index.append(i)"""

# plot scatter-plot
for i in range(file_count):
  	pyplot.annotate(file_names[i], xy=(result[i, 0], result[i, 1]), zorder=1)
pyplot.scatter(result[:, 0], result[:, 1], c=pred_y, cmap='rainbow', zorder=2)

# hilight games wanted
"""for game_i in game_index:
	pyplot.scatter(result[game_i,0], result[game_i,1], color='lawngreen', zorder=3)"""

pyplot.suptitle("Doc2Vec")
pyplot.show()



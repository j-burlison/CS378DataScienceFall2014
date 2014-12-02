from gensim import corpora, models, similarities
from itertools import chain

""" DEMO """
f = open('input.txt', 'r')
documents = [line for line in f]
  

# remove common words and tokenize
stoplist = set('for a of the and to in foundation inc organization fund association & de la '.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# Create Dictionary.
id2word = corpora.Dictionary(texts)
# Creates the Bag of Word corpus.
mm = [id2word.doc2bow(text) for text in texts]

# Trains the LDA models.
lda = models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=10, \
                               update_every=1, chunksize=10000, passes=10)

# Prints the topics.
f = open('topics.txt', 'w')
for top in lda.print_topics():
  print top
  add = top + "\n"
  f.write(add)
print
f.write('\n')
f.write('\n')
print
for top in lda.print_topics():
    f.write("Topic: ")
    result = ''.join([i for i in top if not i.isdigit()])  
    exclude = set('+' '*' '.')
    result = ''.join(ch for ch in result if ch not in exclude)
    f.write(result + '\n')
print
# Assigns the topics to the documents in corpus
lda_corpus = lda[mm]

# Find the threshold, let's set the threshold to be 1/#clusters,
# To prove that the threshold is sane, we average the sum of all probabilities:
scores = list(chain(*[[score for topic,score in topic] \
                      for topic in [doc for doc in lda_corpus]]))
threshold = sum(scores)/len(scores)
print threshold

cluster1  = [j for i,j in zip(lda_corpus,documents) if i[0][1] > threshold]
cluster2  = [j for i,j in zip(lda_corpus,documents) if i[1][1] > threshold]
cluster3  = [j for i,j in zip(lda_corpus,documents) if i[2][1] > threshold]
cluster4  = [j for i,j in zip(lda_corpus,documents) if i[3][1] > threshold]
cluster5  = [j for i,j in zip(lda_corpus,documents) if i[4][1] > threshold]
cluster6  = [j for i,j in zip(lda_corpus,documents) if i[5][1] > threshold]
cluster7  = [j for i,j in zip(lda_corpus,documents) if i[6][1] > threshold]
cluster8  = [j for i,j in zip(lda_corpus,documents) if i[7][1] > threshold]
cluster9  = [j for i,j in zip(lda_corpus,documents) if i[8][1] > threshold]
cluster10 = [j for i,j in zip(lda_corpus,documents) if i[9][1] > threshold]
clusters = [cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8, cluster9, cluster10]
for i in range(1,10):
    String = 'cluster_' + str(i) + '.txt'
    f = open(String, 'w')
    for item in clusters[i-1]:
      f.write("%s\n" % item)
import pandas as pd
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
import pyLDAvis.gensim_models

# Загрузка данных
df = pd.read_csv("processed_articles.csv")
texts = [text.split() for text in df['processed_summary']]

# Построение словаря и корпуса
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Модель LDA
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=10)

# Визуализация
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(vis, "lda_visualization.html")
print("Визуализация сохранена как lda_visualization.html")

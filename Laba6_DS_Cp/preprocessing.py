import pandas as pd
import spacy

# Загрузка данных
df = pd.read_csv("articles.csv")
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

df['processed_summary'] = df['summary'].apply(preprocess_text)
df.to_csv("processed_articles.csv", index=False)
print("Предобработка завершена, файл сохранен как processed_articles.csv")

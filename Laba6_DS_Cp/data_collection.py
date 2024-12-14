import arxiv
import pandas as pd

query = "Data Science OR Machine Learning"
search = arxiv.Search(
    query=query,
    max_results=100,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)
articles = []
for result in search.results():
    articles.append({
        "title": result.title,
        "summary": result.summary,
        "published": result.published,
        "authors": [author.name for author in result.authors],
    })

df = pd.DataFrame(articles)
df.to_csv("articles.csv", index=False)  # Сохраняем в файл
print("Данные успешно сохранены в файл articles.csv")

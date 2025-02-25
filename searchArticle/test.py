import arxiv

def search_arxiv(author, affiliation, year):
    query = f'author:"{author}" AND submittedDate:[{year}-01-01 TO *]'
    search = arxiv.Search(
        query=query,
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = []
    client = arxiv.Client()
    for result in client.results(search):
        results.append({
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'published': result.published,
            'summary': result.summary,
            'pdf_url': result.pdf_url
        })

    return results

# 示例调用
author = "Chen Hong"
affiliation = "beihang"
year = 2020

articles = search_arxiv(author, affiliation, year)
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Authors: {', '.join(article['authors'])}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}")
    print(f"PDF URL: {article['pdf_url']}")
    print("\n")
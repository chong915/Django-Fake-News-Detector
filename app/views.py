from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from newsapi import NewsApiClient
from newspaper import Article
import pickle
import nltk
nltk.download('punkt')

# Create your views here.

def about(request):
	return render(request, 'app/about.html', {'title': 'About'})

def home(request):
	newsapi = NewsApiClient(api_key='f8c00901885e40e9ab6c9223d5e4b9eb')
	all_articles = newsapi.get_top_headlines(q="covid", country="my",
                                     language='en',
                                     page=1, page_size=6)
	return render(request, 'app/home.html', {'articles': all_articles['articles']})

def article(request):
	if request.method == "POST":
		try:
			article_url = request.POST["article-url"]
			print(f"URL : {article_url}")
			article = Article(article_url)
			article.download()
			print("Article Downloaded")
			article.parse()
			article.nlp()
		except:
			return HttpResponse(status=404)

		title = article.title
		authors = article.authors
		if article.publish_date is None:
			publish_date = ""
		else:
			publish_date = article.publish_date.strftime("%Y-%m-%d")
		text = article.text
		
		summary = article.summary
		keywords = article.keywords

		top_image = article.top_image

		tfidf_vectorizer = pickle.load(open('app/tfidf_vectorizer.pkl', 'rb'))
		random_forest = pickle.load(open('app/random_forest.pkl', 'rb'))

		x = tfidf_vectorizer.transform([text])
		y_pred = random_forest.predict_proba(x)[0]
		real_prob = round(y_pred[0] * 100, 2)
		fake_prob = round(y_pred[1] * 100, 2)
		if fake_prob > 50.0:
			color = "#d9534f"
		else:
			color = hsl(142, 90%, 61%)
		article_data = {'title': title, 'authors': authors, 'url': article_url, 'publish_date': publish_date,
						'text': text, 'summary': summary, 'keywords': keywords,'top_image': top_image,
						'real_prob': real_prob, 'fake_prob': fake_prob, 'color': color}
		return render(request, 'app/article.html', {'article_data': article_data})
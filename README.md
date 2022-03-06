# Django-Fake-News-Detector
An Django Fake News Detector Website (Final Semester Project - 3 credit hours)

*This project was also documented in the form of journal paper*
Link: https://github.com/chong915/Django-Fake-News-Detector/blob/ca6803c104b3bc2f8d74560ebf389ac06076837a/data_science_journal_paper.pdf

# Data Science Project Documentation
## Introduction

Link : [https://fake-news-app-project.herokuapp.com/](https://fake-news-app-project.herokuapp.com/)

This website is targeted at the general public in Malaysia. It acts as a third party fact-checking website for Malaysians to check the credibility and trustworthiness of online news. This website an open-source Python library called NewsAPIClient to get the latest and current Covid-19 news in Malaysia and all these news fetched will get displayed in the dashboard of my homepage. Not only that, the other main function of my website is to help people to detect fake news. So, there’s a text field box in the homepage that lets users to enter the news article URL to analyze that particular news article.

![image](https://user-images.githubusercontent.com/63859992/156906996-3dc59a89-fd3c-4cab-9eb2-0b6a5b29fe1c.png)

## Dashboard of the Latest Covid-19 news in Malaysia

The picture above shows the dashboard on the homepage of my website, where people can see the latest news related to Covid-19. This feature will keep the website visitors updated on the latest Covid-19 news. The News displayed in the dashboard will gets updated every few hours, as the backend of the website will fetch latest Covid-19 news and display them on the dashboard. Hence, it’s considered a real-time dashboard.

## Analyze Covid-19 News Articles
![image](https://user-images.githubusercontent.com/63859992/156907070-4b530ae8-f77f-4aca-ab0e-0461538a5f9d.png)

The picture above shows the homepage of my website. There’s a TextField for visitors to enter any news article URL. The backend of the website will then analyze the news articles content and output the keywords within that particular article, as well as the probability of the Covid-19 news being Fake or Real. The picture below shows an example of the summary of the news article analyzed by the backend of the website. The information retrieved are:

1) Title 
2) Date
3) Authors
4) Keywords
5) Probability of Fake/Real
![image](https://user-images.githubusercontent.com/63859992/156907073-1afe8397-deb4-4edf-8e38-b96652a2d186.png)

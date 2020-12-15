# -*- coding: utf-8 -*-
import scrapy
#import os
#import nltk
#from nltk.corpus import stopwords

class GameReviewSpider(scrapy.Spider):
    name = 'game_review'
    #Glinks = []
    page_number = 2
    count = 1
    #allowed_domains = ['https://www.gamespot.com/reviews/']
    start_urls = ['https://www.gamespot.com/reviews/']
    #nltk.download('stopwords')
    #nltk.download('punkt')

    #custom_settings={ 'FEED_URI': "./asdf/gameURL_%(time)s.json",'FEED_FORMAT': 'json'}
    custom_settings={ 'FEED_URI': "gameCSV_%(time)s.csv",'FEED_FORMAT': 'csv'}

    def parse(self, response):
	#title = response.css('title::text').extract()
	games = response.css('article.media.media-game.media-game')
	links = games.css('a::attr(href)').getall()       

	#print("*************************************")

	for link in links:
		#GameReviewSpider.Glinks.append(link)
		temp_link = 'https://www.gamespot.com' + link.encode('ascii','ignore')
		#print(temp_link)
		yield response.follow(temp_link,callback = self.crawl_data)	

	#print("*************************************")
	
	# crawl the page and store the data	


	next_page = 'https://www.gamespot.com/reviews/?page=' + str(GameReviewSpider.page_number)

	#print(len(GameReviewSpider.Glinks))

	if GameReviewSpider.page_number <= 30:
		GameReviewSpider.page_number = GameReviewSpider.page_number + 1
		yield response.follow(next_page,callback = self.parse)


    def crawl_data(self, response):

	#custom_settings={ 'FEED_URI': "./asdf/gameURL_"+str(count)+".json",'FEED_FORMAT': 'json'}
	"""url = response.request.url
	metadata = response.request.meta
	title = response.css('h1.kubrick-info__title::text').extract_first().strip()"""  
	content = response.css('div.js-content-entity-body')
	data_raw = content.css('p::text').extract()
	data = ' '.join(data_raw).encode('ascii','ignore')

	with open('./asdf/gameURL_'+str(GameReviewSpider.count)+'.txt', 'w') as f:
		f.write(data)
		f.close()

		"""f.write('url : ' + url + "\n" + 
			'title : ' + title + "\n" +
			'metadata : ' + str(metadata) + "\n" + 
			'doc_id : ' + 'gameURL_'+str(GameReviewSpider.count)+'.txt' + "\n\n" + 
			'content : \n' + data)"""

	scraped_info = {
		
		'url' : response.request.url,
		'title' : response.css('h1.kubrick-info__title::text').extract_first().strip(), 
		'metadata' : response.request.meta,
		'doc_id' : 'gameURL_'+str(GameReviewSpider.count)+'.txt'
	}

	GameReviewSpider.count = GameReviewSpider.count + 1

	yield scraped_info
	

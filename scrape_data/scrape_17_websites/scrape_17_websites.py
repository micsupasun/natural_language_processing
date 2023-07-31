from bs4 import BeautifulSoup
import requests
import http.client
import mimetypes
# from services.rabbitmq_service import rabbitmq_service
# rabbit_send = rabbitmq_service()


class crawler_scrape: 
    def method_one():
        conn = http.client.HTTPSConnection("www.prachachat.net")
        payload = ''
        headers = {}
        all_path = ["/feed", "/finance/feed", "/marketing/feed", "/economy/feed", "/politics/feed", "/world-news/feed"]
        dict_item = {"title":"","date":"","url":"","source":""} 
        for i in range(len(all_path)):
            conn.request("GET", all_path[i], payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
            items = soup.find_all('item')
            for item in items:
                dict_item["title"] = item.title.text
                dict_item["date"] = " ".join(item.pubdate.text.split(' ')[1:4])
                dict_item["source"] = "prachachat"
                dict_item["url"] = item.select_one('comments').text.split('#')[0]
                # rabbit_send.send(dict_item,'ocsb_1_r')
        print(dict_item)
    def method_three():
        conn = http.client.HTTPSConnection("www.posttoday.com")
        payload = ''
        headers = {}
        all_path = ["/rss/src/politics.xml", "/rss/src/world.xml", "/rss/src/economy.xml", "/rss/src/money.xml"]
        dict_item = {"title": "","date":"","url":"","source":""}  
        for i in range(len(all_path)):
            conn.request("GET", all_path[i], payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
            items = soup.find_all('item')
            for item in items:
                try:
                    dict_item["title"] = item.get_text('split').split('split')[0]
                    dict_item["date"] = " ".join(item.get_text('split').split('split')[3].split(' ')[1:4])
                    dict_item["url"] = item.get_text('split').split('split')[1]
                    dict_item["source"] = "posttoday"
                except:
                    dict_item["title"] = item.get_text('split').split('split')[0]
                    dict_item["date"] = " ".join(item.get_text('split').split('split')[2].split(' ')[1:4])
                    dict_item["url"] = item.get_text('split').split('split')[1]
                    dict_item["source"] = "posttoday"
                # rabbit_send.send(dict_item,'ocsb_1_r')
        print(dict_item)
    def method_four():
        conn = http.client.HTTPSConnection("news.mthai.com")
        payload = ''
        headers = {}
        all_path = ["/politics-news/feed", "/world-news/feed"]
        dict_item = {"title":"","date":"","url":"","source":""}
        for i in range(len(all_path)):
            conn.request("GET", all_path[i], payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
            items = soup.find_all('item')
            for item in items:
                dict_item["date"] = " ".join(item.pubdate.text.split(' ')[1:4])
                dict_item["title"] = item.description.text.split('\n]]>')[0].strip().split('\n')[0]
                dict_item["url"] = item.find_all('a')[0].get('href')
                dict_item["source"] = "news.mthai.com"
                # rabbit_send.send(dict_item,'ocsb_1_r')
        print('test',dict_item)
    def method_five():
        conn = http.client.HTTPSConnection("news.ch3thailand.com")
        payload = ''
        headers = {}
        all_path = ["/rss/EconomicNews.rss","/rss/PoliticsNews.rss"]
        dict_item = {"date":"","url":"","source":""}
        for i in range(len(all_path)):
            conn.request("GET", all_path[1], payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
            items = soup.find_all('item')
            for item in items:
                dict_item['date'] = item.pubdate.text.split(' ')[0]
                dict_item['url'] = item.get_text('sss').split('sss')[10].split('\r\n')[0]
                dict_item['source'] = 'news.ch3thailand'
                dict_item['title'] = ''
                # rabbit_send.send(dict_item,'ocsb_1_r')
        print(dict_item)

    def method_six():
        conn = http.client.HTTPConnection("www.biotechthailand.com")
        payload = ''
        headers = {
        'Cookie': 'dnetsid=zryhv2mkjh2oizuzzjoe3jl5; afrvt=5a481d8ecc124b5f9c5a48518e7ae0be; HomeAdOverlay=i=zryhv2mkjh2oizuzzjoe3jl5&t=637371501831250000&f=True; TS013d6f05=016da9c3ffbe8201105a5a98d0f08ff441cc221ca49fb917d725dbfdaf2c05c64057cac8cec16e31c3a17438cda57e7c209cdcfefa4a7de40b6462bb7907bb67241f4734e9fed8e2e22447c78d450750b3ffad1dad'
        }
        conn.request("GET", "/news/list/2020", payload, headers)
        res = conn.getresponse()
        data = res.read()
        soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
        title = soup.select('h3.post_title_newslist')
        date = soup.select('div.post_info_newslist')
        link = soup.select('a.newstitle')
        dict_item = {"title":"","date":"","url":"","source":""} 
        for i in range(len(title)):
            dict_item['title'] = title[i].text.strip()
            date_list = date[i].text.strip().split(' ')[:3]
            dict_item['date'] = ' '.join(date_list)
            dict_item['url'] = 'www.biotechthailand.com' + link[i].get('href')
            dict_item['source'] = 'biotechthailand'
            # rabbit_send.send(dict_item,'ocsb_1_r')
        print(dict_item)
    # method_six()

class TestScrape():
    def main_two():
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=international&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=topics-society&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=topics-health-care&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=security&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=energy&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        # https://www.dailysignal.com/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat=topics-economy&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229
        list_web = ["international", "topics-society", "topics-health-care", "security", "energy", "topics-economy"]
        dict_item = {"title":"","date":"","url":"","source":""} 
        for web in range(len(list_web)):
            conn = http.client.HTTPSConnection("www.dailysignal.com")
            payload = ''
            headers = {
            'Cookie': '__cfduid=d8ea0f0c7b3085d308c8a100d5c532f1e1601867885'
            }
            conn.request("GET", f"/wp-content/plugins/daily-signal-ajax/daily-signal-ajax.php?action=cat_posts&page=1&cat={list_web[web]}&excludes%5B%5D=477157&excludes%5B%5D=483337&excludes%5B%5D=487677&excludes%5B%5D=488119&excludes%5B%5D=493287&excludes%5B%5D=493381&excludes%5B%5D=493557&excludes%5B%5D=493857&excludes%5B%5D=506229", payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
            date_time = soup.select('time')
            title = soup.select('h2')
            url = soup.select('a.call-to-action')
            for i in range(len(title)):
                dict_item['title'] = title[i].text.strip()
                dict_item['date'] = date_time[i].text
                dict_item['url'] = url[i].get('href')
                dict_item['source'] = 'Dialy Signal'
        print('dict_2 = ',dict_item)
    def main_one():
        # https://www.pewresearch.org/publications/?programs=global-migration-and-demography
        # https://www.pewresearch.org/publications/?programs=internet-tech
        # https://www.pewresearch.org/publications/?programs=politics

        # https://www.pewresearch.org/publications/?programs=social-trends
        # https://www.pewresearch.org/publications/?programs=science
        list_web = ["global-migration-and-demography", "internet-tech", "politics", "social-trends", "science"]
        dict_item = {"title":"","date":"","url":"","source":""} 
        for web in range(len(list_web)):
            conn = http.client.HTTPSConnection("www.pewresearch.org")
            payload = ''
            headers = {}
            conn.request("GET", f"/publications/?programs={list_web[web]}", payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
            title = soup.select('div.title')
            date_time = soup.select('div.react-story-item')
            url = soup.select('article')
            
            for i in range(len(title)):
                dict_item['title'] = title[i].text
                dict_item['date'] = date_time[i].get('data-date')
                dict_item['url'] = url[i].get('href')
                dict_item['source'] = 'Pew Research Center'
        print('dict_1 = ',dict_item)
# https://techcrunch.com/wp-json/tc/v1/magazine?page=5&_embed=true&cachePrevention=0
    def main_three():
        dict_item = {"title":"","date":"","url":"","source":""} 
        url = f"https://techcrunch.com/wp-json/tc/v1/magazine?page=5&_embed=true&cachePrevention=0"
        request_json = requests.get(url).json()
        for i in range(len(request_json)):
            dict_item['title'] = request_json[i]['title']['rendered']
            dict_item['date'] = request_json[i]['modified_gmt'].split('T')[0]
            dict_item['url'] = request_json[i]['guid']['rendered']
            dict_item['source'] = 'Tech Crunch'
        print('dict_3 = ',dict_item)

# https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&searchSelected=world&contentTypes=%7B%22interactive%22:true,%22slideshow%22:true,%22video%22:true,%22article%22:true%7D&size=10&offset=3
# https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&searchSelected=science&contentTypes=%7B%22interactive%22:true,%22slideshow%22:true,%22video%22:true,%22article%22:true%7D&size=10&offset=2
# https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&searchSelected=tech&contentTypes=%7B%22interactive%22:true,%22slideshow%22:true,%22video%22:true,%22article%22:true%7D&size=10&offset=1
# https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&searchSelected=politics&contentTypes=%7B%22interactive%22:true,%22slideshow%22:true,%22video%22:true,%22article%22:true%7D&size=10&offset=20
    def main_four():
        list_web = ['world','science','tech','politics']
        dict_item = {"title":"","date":"","url":"","source":""} 
        for k in range(len(list_web)):
            if list_web[k] == 'world':
                length_web = 4
            elif list_web[k] == 'science':
                length_web = 3
            elif list_web[k] == 'tech':
                length_web = 2
            elif list_web[k] == 'politics':
                length_web = 21
            for i in range(1,length_web):
                url = f"https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&searchSelected={list_web[k]}&contentTypes=%7B%22interactive%22:true,%22slideshow%22:true,%22video%22:true,%22article%22:true%7D&size=10&offset={i}"
                request_json = requests.get(url).json()
                
                for j in range(len(request_json)):
                    dict_item['title'] = request_json[j]['title']
                    dict_item['date'] = request_json[j]['lastPublishedDate'].split('T')[0]
                
                    dict_item['url'] =  f'{request_json[j]["url"]}'
                    dict_item['source'] = 'Fox News'
        print('dict_4 = ',dict_item)


# https://www.engineering.com/DesignerEdge/DesignerEdgeArticles/CategoryID/38/CurrentPage/1.aspx
# https://www.engineering.com/Hardware/CategoryID/45/CurrentPage/1.aspx
# https://www.engineering.com/Education/EducationArticles/CategoryID/39/CurrentPage/1.aspx
# https://www.engineering.com/AdvancedManufacturing/CategoryID/41/CurrentPage/1.aspx
# https://www.engineering.com/ARVR/CategoryID/47/CurrentPage/1.aspx

# https://www.engineering.com/ElectronicsDesign/ElectronicsDesignArticles/CategoryID/31/CurrentPage/1.aspx
# https://www.engineering.com/3DPrinting/3DPrintingArticles/CategoryID/20/CurrentPage/1.aspx
# https://www.engineering.com/IOT/CategoryID/44/CurrentPage/1.aspx
    def main_five():
        listweb = [
            '/DesignerEdge/DesignerEdgeArticles/CategoryID/38/CurrentPage/1.aspx', 
            '/Hardware/CategoryID/45/CurrentPage/1.aspx',
            '/Education/EducationArticles/CategoryID/39/CurrentPage/1.aspx',
            '/AdvancedManufacturing/CategoryID/41/CurrentPage/1.aspx',
            '/ARVR/CategoryID/47/CurrentPage/1.aspx',

            '/ElectronicsDesign/ElectronicsDesignArticles/CategoryID/31/CurrentPage/1.aspx',
            '/3DPrinting/3DPrintingArticles/CategoryID/20/CurrentPage/1.aspx',
            '/IOT/CategoryID/44/CurrentPage/1.aspx',
        ]
        conn = http.client.HTTPSConnection("www.engineering.com")
        payload = ''
        headers = {
        'Cookie': 'um_IsMobile=False; .ASPXANONYMOUS=oEA0snXR1gEkAAAAMTA0ZTk3YzAtZDAyYi00ZmNhLTk3NTctZjc2MWNhMmNmZjZm0; ASP.NET_SessionId=zqxh322gcz3d3nwec0v3a4js; language=en-US'
        }
        for i in range(len(listweb)):
            conn.request("GET", listweb[i], payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
            date_time = soup.select('div.articleAuthor span')
            title_and_url = soup.select('a.articleLinkTitle')
            dict_item = {"title":"","date":"","url":"","source":""} 
            date_time_clean = [date_time[i].text.strip() for i in range(len(date_time)) if ' ' in date_time[i].text.strip()]
            for j in range(len(title_and_url)):
                dict_item['title'] = title_and_url[j].text
                dict_item['date'] = date_time_clean[j]
                dict_item['url'] =  title_and_url[j].get('href')
                dict_item['source'] = 'engineering.com'
        print('dict_5 = ',dict_item)
# https://www.reuters.com/news/archive/businessnews?view=page&page=10&pageSize=10
# https://www.reuters.com/news/archive/marketsNews?view=page&page=15&pageSize=10
# https://www.reuters.com/news/archive/personalfinance?view=page&page=1&pageSize=10
# https://www.reuters.com/news/archive/technologynews?view=page&page=5&pageSize=10
    def main_six():
        conn = http.client.HTTPSConnection("www.reuters.com")
        payload = ''
        headers = {}
        list_web = ['businessnews', 'marketsNews', 'personalfinance', 'technologynews']
        dict_item = {"title":"","date":"","url":"","source":""} 
        for i in range(len(list_web)):
            if list_web[i] == 'businessnews':
                length_web = 11
            elif list_web[i] == 'marketsNews':
                length_web = 16
            elif list_web[i] == 'personalfinance':
                length_web = 2
            elif list_web[i] == 'technologynews':
                length_web = 6
            print(length_web)
            for j in range(1,length_web):
                conn.request("GET", f"/news/archive/{list_web[i]}?view=page&page={j}&pageSize=10", payload, headers)
                res = conn.getresponse()
                data = res.read()
                soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
                date_time = soup.select('span.timestamp')
                title = soup.select('h3.story-title')
                url = soup.select('div.story-content a')
                for k in range(len(date_time)):
                    dict_item['title'] = title[k].text.strip()
                    dict_item['date'] = date_time[k].text
                    dict_item['url'] = 'https://www.reuters.com' + url[k].get('href')
                    dict_item['source'] = 'Reuters'
        print('dict_6 = ',dict_item)


# https://www.enterpriseai.news/category/sectors/financial-services-sectors/
# https://www.enterpriseai.news/category/sectors/government-sectors/
# https://www.enterpriseai.news/category/sectors/retail-sectors/
# https://www.enterpriseai.news/category/sectors/healthcare-sectors/

# https://www.enterpriseai.news/category/sectors/manufacturing-sectors/
# https://www.enterpriseai.news/category/sectors/energy-sectors/
    def main_seven():
        conn = http.client.HTTPSConnection("www.enterpriseai.news")
        payload = ''
        headers = {
        'Cookie': '__cfduid=dfa335f9e7b8d24704ac07b9842810b6c1601886595; cookielawinfo-checkbox-necessary=yes'
        }
        dict_item = {"title":"","date":"","url":"","source":""} 
        list_web = ['financial-services-sectors', 'government-sectors','retail-sectors', 'manufacturing-sectors', 'energy-sectors']
        for i in range(len(list_web)):
            conn.request("GET", f"/category/sectors/{list_web[i]}/", payload, headers)
            res = conn.getresponse()
            data = res.read()
            soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
            soup_page = soup.select("h2.entry-title a")

            for j in range(len(soup_page)):
                dict_item['title'] = soup_page[j].text
                dict_item['url'] = soup_page[j].get('href')
                dict_item['source'] = 'Enterprise AI'
        print('dict_7 = ',dict_item)




# https://www.entrepreneur.com/topic/women-entrepreneurs/1
    def main_eight():
        conn = http.client.HTTPSConnection("www.entrepreneur.com")
        payload = ''
        headers = {
        'Cookie': 'language=en; edition=ap; geo={\'latitude\':\'13.700\',\'longitude\':\'100.600\',\'city\':\'bangkok\',\'continent_code\':\'AS\',\'country_code\':\'TH\',\'country_code3\':\'THA\',\'country_name\':\'thailand\',\'postal_code\':\'10110\',\'region\':\'10\',\'area_code\':\'0\',\'metro_code\':\'-1\'}; entrepreneur_permutive=c2_i_DLiwa; entrepreneur_permutive_cs=c2_i_DLiwa'
        }
        conn.request("GET", "/topic/women-entrepreneurs/1", payload, headers)
        res = conn.getresponse()
        data = res.read()
        soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
        text = soup.select('h3')
        url = soup.select('h3 a')
        dict_item = {"title":"","date":"","url":"","source":""} 
        for i in range(len(text)):
            dict_item['title'] = text[i].text
            dict_item['url'] = 'www.entrepreneur.com' + url[i].get('href')
            dict_item['source'] = 'Entrepreneur'
        print('dict_8 = ',dict_item)

    def main_nine():
        # https://www.popsci.com/arcio/rss/
        conn = http.client.HTTPSConnection("www.popsci.com")
        payload = ''
        headers = {}
        conn.request("GET", "/arcio/rss/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        dict_item = {"title":"","date":"","url":"","source":""} 
        soup = BeautifulSoup(data.decode("utf-8"), 'xml')
        title = soup.select('title')[1:]
        url = soup.select('link')[2:]
        date_time = soup.select('pubDate')
        print(len(title),len(url),len(date_time))
        for i in range(len(title)):
            dict_item['title'] = title[i].text
            dict_item['date'] = " ".join(date_time[i].text.split(' ')[1:4])
            dict_item['url'] = url[i].text
            dict_item['source'] = 'Popular Science'
        print('dict_9 = ',dict_item)
            

# https://businessfacilities.com/industry-news/
    def main_ten():
        conn = http.client.HTTPSConnection("businessfacilities.com")
        payload = ''
        headers = {
        'Cookie': '__cfduid=d8468e4869aa422db5e435827c627a1351601958064'
        }
        dict_item = {"title":"","date":"","url":"","source":""} 
        conn.request("GET", "", payload, headers)
        res = conn.getresponse()
        data = res.read()
        soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
        soup_page = soup.select('div.td-block-span6')
        # link_page = soup.select('div.td-block-span6 div.td-module-meta-info a')
        date_time = soup.select('div.td-block-span6 time')
        text = soup.select('div.td-block-span6 div.td-excerpt')
        url = soup.select('div.td-block-span6 h3.entry-title.td-module-title a')
        for i in range(len(date_time)):
            dict_item['title'] = text[i].text.strip()
            dict_item['date'] = date_time[i].text
            dict_item['url'] = url[i].get('href')
            dict_item['source'] = 'Business Facilities'
        print('dict_10 = ',dict_item)
# https://www.strategy-business.com/tech-and-innovation/tech-and-innovation-archive
    def main_eleven():
        conn = http.client.HTTPSConnection("www.strategy-business.com")
        payload = ''
        headers = {
        'Cookie': 'sid=740ab3ab4c98f2517661718d73cd444e; visid_incap_1339430=pGYUVnTuRXGpKOkh5JFwA2kOfF8AAAAAQUIPAAAAAABO+JK85g+W7XDF/az44hH/; incap_ses_1264_1339430=wyJtWDEgLGzroDDrVqGKEW0OfF8AAAAA8sLgPgJQy0wDjS0qhSR6hw=='
        }
        conn.request("GET", "/tech-and-innovation/tech-and-innovation-archive", payload, headers)
        res = conn.getresponse()
        data = res.read()
        dict_item = {"title":"","date":"","url":"","source":""} 
        soup = BeautifulSoup(data.decode("utf-8"), 'html.parser')
        date = soup.select('div.date')
        text_and_link = soup.select('h3.title a')
        for i in range(len(date)):
            dict_item['title'] = text_and_link[i].text.strip()
            dict_item['date'] = date[i].text
            dict_item['url'] = text_and_link[i].get('href')
            dict_item['source'] = 'Strategy+Business'
        print('dict_11 = ',dict_item)

    def main_twelve():
        # https://www.bbc.com/future/data/search/article-by-premium/future/future-now?page=1&itemsPerPage=8
        dict_item = {"title":"","date":"","url":"","source":""} 
        url = f"https://www.bbc.com/future/data/search/article-by-premium/future/future-now?page=1&itemsPerPage=8"
        request_json = requests.get(url).json()
        for i in range(len(request_json)):
            dict_item['title'] = request_json['results'][i]['Content']['BodyIntro']
            dict_item['date'] = request_json['results'][i]['Content']['DisplayDate'].split('T')[0]
            dict_item['url'] = "https://www.bbc.com/" + request_json['results'][i]['Metadata']['Id']
            dict_item['source'] = "BBC Future"
        print('dict_12 = ',dict_item)
print(crawler_scrape.method_one())
print(crawler_scrape.method_three())
print(crawler_scrape.method_four())
print(crawler_scrape.method_five())
print(crawler_scrape.method_six())


print('----------------------------------')
print(TestScrape.main_one())
print(TestScrape.main_two())
print(TestScrape.main_three())
# print(TestScrape.main_four())
print(TestScrape.main_five())
print(TestScrape.main_six())
print(TestScrape.main_seven())
# print(TestScrape.main_eight())
# print(TestScrape.main_nine())
print(TestScrape.main_ten())
print(TestScrape.main_eleven())
# print(TestScrape.main_twelve())
print('----------------------------------')

# เช็คprintด้วยตอนจบ
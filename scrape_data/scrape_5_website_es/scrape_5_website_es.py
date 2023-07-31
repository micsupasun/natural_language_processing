import http.client
import mimetypes
from bs4 import BeautifulSoup
from functions.connect_url import connect_url
import re
import datetime
from prettyprinter import pprint
import requests
con_url = connect_url()
list_web = ['prachachat', 'posttoday', 'mthai', 'ch3thailand','biotechthailand']

def date_time_from_eco(date,format_date):
    dateQ3 = datetime.datetime.strptime(date,format_date).strftime('%Y-%m-%d') + "T00:00:00"
    date = datetime.datetime.strptime(date,format_date).strftime('%d %B %Y')
    return dateQ3, date

def web_prachachat(url,date):
    date_time = " ".join(date.split(' ')[1:4])
    date_time_stamp,date_string= date_time_from_eco(date_time,"%d %b %Y")
    domain = url.split('/')[0]
    sub_domain = url[len(domain):]
    dict_data = {"date":[],"dateQ3":[],"text":[]}
    data = con_url.get_data_from_http(domain,sub_domain)
    soup = BeautifulSoup(data.decode("utf-8"),'html.parser')
    soup_text = soup.select("div.td-post-content p")
    text = ""
    for element in soup_text:
        text += element.text+ "\n"
    text = text.rstrip() 
    return date_time_stamp,date_string,text

def web_posttoday(url, date):
    date_time = " ".join(date.split(' ')[1:4])
    date_time_stamp,date_string= date_time_from_eco(date_time,"%d %b %Y")
    domain = url.split('/')[0]
    sub_domain = url[len(domain):]
    text = ""
    data = con_url.get_data_from_http(domain,sub_domain)
    soup = BeautifulSoup(data.decode("utf-8"),'html.parser')
    soup_page = soup.select("div.article-content p")
    soup_intro = soup.select("div.article-intro")[0]
    text += soup_intro.text.lstrip().rstrip() + "\n"
    for element in soup_page:
        text += element.text+ "\n"
    text = text.rstrip()
    print(text)
    return date_time_stamp,date_string,text

## news mthai
def web_mthai(url, date):
    date_time = " ".join(date.split(' ')[1:4])
    date_time_stamp,date_string= date_time_from_eco(date_time,"%d %b %Y")
    domain = url.split('/')[2]
    sub_domain = url.split(domain)[1]
    select_number = sub_domain.rsplit('/', 1)[1].replace(".html","")
    text = ""
    data = con_url.get_data_from_http(domain,sub_domain)
    soup = BeautifulSoup(data.decode("utf-8"),'html.parser')
    # print(soup)
    soup_page = soup.select("div#content-inner-"+select_number+" p" + " ,div#content-inner-"+select_number+" ul")
    print(select_number)
    for element in soup_page:
        text += element.text
    return date_time_stamp,date_string,text


## news ch3thailand
def web_ch3thailand(url, date):
    date_time = date.split(' ')[0].split('-')[2] + ' ' + date.split(' ')[0].split('-')[1] + ' ' + date.split(' ')[0].split('-')[0]
    date_time_stamp,date_string= date_time_from_eco(date_time,"%d %m %Y")
    text = ""
    domain = url.split('/')[2]
    sub_domain = url.split('news.ch3thailand.com')[1]
    data = con_url.get_data_from_http(domain,sub_domain)
    soup = BeautifulSoup(data.decode("utf-8"),'html.parser')
    soup_page = soup.select("div.content-news p")
    for element in soup_page:
        text += element.text + "\n"
    return date_time_stamp,date_string,text

def web_biotechthailand(url, date):
    date_time = '30 September 20'
    domain = url.split('/')[2]
    date_time_stamp,date_string = date_time_from_eco(date_time,"%d %B %y")
    conn = http.client.HTTPConnection(domain)
    payload = ''
    headers = {
    'Cookie': 'dnetsid=krrrkio4py0wxw0ktox0wgzi; afrvt=da81f9496ca0461f9568ed53b8889b97; HomeAdOverlay=i=krrrkio4py0wxw0ktox0wgzi&t=637374220527571250&f=True; TS013d6f05=016da9c3ffff76a1fe2f219e57f4b6a3871af3d1088bfa5e31f0e43633f76d0f8e7811a2033a27d88d7a92dc7fdf962404076b41c20f0332a6956d45ab6d382bf714e6de9af02190b821c38ac4a0a22a07b7c7c52a'
    }
    conn.request("GET", url.split(domain)[1], payload, headers)
    res = conn.getresponse()
    data = res.read()
    soup = BeautifulSoup(data.decode("utf-8"), 'lxml')
    soup_page = soup.select_one("div.post_body_newslist").text.split('ที่มา :')[0].strip()
    return date_time_stamp, date_string, soup_page
def main():
    # data = {'source':'prachachat',
    #         'url': "www.prachachat.net/finance/news-530347",
    #         'date':"Fri, 02 Oct 2020 08:41:57 +0000"}
    # data = {'source':'posttoday',
    #         'url': "www.posttoday.com/politic/news/634358",
    #         'date':"Fri, 02 Oct 2020 16:00:00"}
    data = {'source':'mthai',
        'url': "https://news.mthai.com/politics-news/797560.html",
        'date':"Fri, 24 Apr 2020 08:22:05 +0000"}
    # data = {'source':"ch3thailand",
    #     'url': "http://news.ch3thailand.com/%e0%b8%82%e0%b9%88%e0%b8%b2%e0%b8%a7%e0%b9%80%e0%b8%a8%e0%b8%a3%e0%b8%a9%e0%b8%90%e0%b8%81%e0%b8%b4%e0%b8%88/100304/%e0%b8%a1%e0%b8%b5%e0%b8%95%e0%b8%b1%e0%b9%8b%e0%b8%a7%e0%b8%81%e0%b8%b1%e0%b8%99%e0%b8%ab%e0%b8%a3%e0%b8%b7%e0%b8%ad%e0%b8%a2%e0%b8%b1%e0%b8%87---%e0%b9%80%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%a2%e0%b8%a7%e0%b8%9b%e0%b8%b5%e0%b9%83%e0%b8%ab%e0%b8%a1%e0%b9%88-%e0%b8%9a%e0%b8%82%e0%b8%aa-%e0%b9%80%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b9%88%e0%b8%a2%e0%b8%a7%e0%b8%9b%e0%b8%81%e0%b8%95%e0%b8%b4%e0%b9%80%e0%b8%95%e0%b9%87%e0%b8%a1%e0%b8%ab%e0%b8%a1%e0%b8%94%e0%b8%97%e0%b8%b8%e0%b8%81%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%99%e0%b8%b1%e0%b9%88%e0%b8%87%e0%b9%81%e0%b8%a5%e0%b9%89%e0%b8%a7---%e0%b9%80%e0%b8%9b%e0%b8%b4%e0%b8%94%e0%b8%a3%e0%b8%96%e0%b9%80%e0%b8%aa%e0%b8%a3%e0%b8%b4%e0%b8%a1%e0%b9%83%e0%b8%ab%e0%b9%89%e0%b8%88%e0%b8%ad%e0%b8%87%e0%b9%80%e0%b8%9e%e0%b8%b4%e0%b9%88%e0%b8%a1.html",
    #     'date':"2019-12-20 14:04:08"}
    # data = {'source':"biotechthailand",
    #     'url': "http://www.biotechthailand.com/news/1293034/6",
    #     'date':"30 September 20"}
    if data['source'] in list_web:
        send_date_q3, send_date_string, send_title = globals()["web_" + data['source']](data['url'], data['date'])
        print('---------------------')
        print(send_date_q3)
        print('---------------------')
        print(send_date_string)
        print('---------------------')
        print(send_title)
        data['title'] = send_title
        data['date'] = send_date_q3
        data['dateQ3'] = send_title
# print(main())

# print(TestScrape.main_one())
es_database = {
        "date": "",
        "date_attr": "",
        "src": "Pew Research Center",
        "text_remove": "",
        "text_select": "div.post-content > p",
        "date_format": "MMMM d, yyyy",
        "type_url":""
}
data_scrape = [
    {'title': 'Public Views About Science in Sweden', 'date': '2020-09-29', 'url': 'https://www.pewresearch.org/science/fact-sheet/public-views-about-science-in-sweden/', 'source': 'Pew Research Center'},
    {'title': 'Defining ‘Contractor’ Status Would Provide Some Relief for Struggling Workers and Small Businesses', 'date': 'September 23, 2020', 'url': 'https://www.dailysignal.com/2020/09/23/defining-contractor-status-would-provide-some-relief-for-struggling-workers-and-small-businesses/', 'source': 'Dialy Signal'},
    {'title': 'Twitter is building &#8216;Birdwatch,&#8217; a system to fight misinformation by adding more context to tweets', 'date': '2020-10-03', 'url': 'https://techcrunch.com/2020/10/02/twitter-is-building-birdwatch-a-system-to-fight-misinformation-by-adding-more-context-to-tweets/', 'source': 'Tech Crunch'},
    {'title': 'Temperature Sensors Employ IoT Connectivity to Speed COVID-19 Screening ', 'date': 'April 14, 2020', 'url': 'https://www.engineering.com/IOT/ArticleID/20173/Temperature-Sensors-Employ-IoT-Connectivity-to-Speed-COVID-19-Screening.aspx', 'source': 'engineering.com'},
    {'title': 'Uber Freight raises $500 mln, valuation rises to $3.3 billion', 'date': 'Oct 02 2020', 'url': 'https://www.reuters.com/article/us-uber-funding/uber-freight-raises-500-mln-valuation-rises-to-3-3-billion-idUSKBN26N1OY', 'source': 'Reuters'},
    {'title': 'AWS Plows Snow Family to the Edge', 'date': '', 'url': 'https://www.enterpriseai.news/2020/06/17/aws-plows-snow-family-to-the-edge/', 'source': 'Enterprise AI'},
    {'title': 'The Saxe Gotha Industrial Park, home to Nephron Pharmaceuticals, Kennedy Innovation Complex and two Amazon facilities, makes this Park ideal for life sciences, advanced manufacturing and other related industries. This 714-acre Park is bordered by an East to West interstate and accessed by a North to South Interstate, boasts rail accessibility and all utilities are located within the Park.', 'date': 'October 1, 2020', 'url': 'https://businessfacilities.com/2020/10/business-facilities-county-of-lexington-south-carolina/', 'source': 'Business Facilities'},
    {'title': 'The fourth industrial revolution in agriculture', 'date': 'October 10, 2019 ', 'url': 'https://www.strategy-business.com/article/The-fourth-industrial-revolution-in-agriculture', 'source': 'Strategy+Business'},
]

es_database = [
# 0 = https://www.pewresearch.org/hispanic/2020/08/11/about-one-in-four-u-s-hispanics-have-heard-of-latinx-but-just-3-use-it/
{'date': '', 'date_attr': '', 'src': 'Pew Research Center', 'text_remove': '', 'text_select': 'div.post-content > p', 'date_format': '%Y-%m-%d', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': '__cfduid=d8ea0f0c7b3085d308c8a100d5c532f1e1601867885'},
# 1 =  https://www.dailysignal.com/2020/09/23/defining-contractor-status-would-provide-some-relief-for-struggling-workers-and-small-businesses/
{'date': 'div.header-wrapper time', 'date_attr': '', 'src': 'Dialy Signal', 'text_remove': '', 'text_select': 'div.tds-content p', 'date_format': '%B %d, %Y', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': '__cfduid=d8ea0f0c7b3085d308c8a100d5c532f1e1601867885'},
# 2 =  https://techcrunch.com/?p=2053808
{'date': '', 'date_attr': '', 'src': 'Tech Crunch', 'text_remove': '', 'text_select': 'div.article-content > p,div.article-content > h2,div.article-content > ul', 'date_format': '%Y-%m-%d', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': 'A3=d=AQABBKGnel8CEM3jgazaLHWcn2Zzl6OK5-EFEgEBAQH5e1-EXwAAAAAA_SMAAA&S=AQAAAty-h_ZnkosDtiIPr6HYdBY; GUC=AQEBAQFfe_lfhEIiWwTK; BX=e3psakdfnl9t1&b=3&s=a2; A1=d=AQABBKGnel8CEM3jgazaLHWcn2Zzl6OK5-EFEgEBAQH5e1-EXwAAAAAA_SMAAAcIoad6X6OK5-E&S=AQAAAm1tuhwlicL-RaLa2p_cxH0; A1S=d=AQABBKGnel8CEM3jgazaLHWcn2Zzl6OK5-EFEgEBAQH5e1-EXwAAAAAA_SMAAAcIoad6X6OK5-E&S=AQAAAm1tuhwlicL-RaLa2p_cxH0'},
# 3 =  https://www.engineering.com/IOT/ArticleID/20173/Temperature-Sensors-Employ-IoT-Connectivity-to-Speed-COVID-19-Screening.aspx
{'date': '', 'date_attr': '', 'src': 'engineering.com', 'text_remove': '', 'text_select': 'div#articleBodyArea', 'date_format': '%B %d, %Y', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': '.ASPXANONYMOUS=oEA0snXR1gEkAAAAMTA0ZTk3YzAtZDAyYi00ZmNhLTk3NTctZjc2MWNhMmNmZjZm0; um_IsMobile=False; ASP.NET_SessionId=ppiatvsbicw05mqkdnvsixm2; language=en-US; Article20173=1'},
# 4 =  https://www.reuters.com/article/us-uber-funding/uber-freight-raises-500-mln-valuation-rises-to-3-3-billion-idUSKBN26N1OY
{'date': 'div.ArticleHeader_date', 'date_attr': '', 'src': 'Reuters', 'text_remove': '', 'text_select': 'p.Paragraph-paragraph-2Bgue.ArticleBody-para-TD_9x', 'date_format': '%b %d %Y', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': ''},
# 5 =  https://www.enterpriseai.news/2020/06/17/aws-plows-snow-family-to-the-edge/
{'date': 'div.entry-meta > a > span', 'date_attr': '', 'src': 'Enterprise AI', 'text_remove': 'div.entry-content p.caption, div.entry-content p.comment-input-wrap.pad, div.entry-content p.comment-textarea-wrap', 'text_select': 'div.entry-content p', 'date_format': '%B %d, %Y', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': '__cfduid=dfa335f9e7b8d24704ac07b9842810b6c1601886595; cookielawinfo-checkbox-necessary=yes'},
# 6 =  https://businessfacilities.com/2020/10/business-facilities-county-of-lexington-south-carolina/
{'date': '', 'date_attr': '', 'src': 'Business Facilities', 'text_remove': '', 'text_select': 'p', 'date_format': '%B %d, %Y', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': '__cfduid=d8468e4869aa422db5e435827c627a1351601958064'},
# 7 =  https://www.strategy-business.com/article/The-fourth-industrial-revolution-in-agriculture
{'date': 'time.date', 'date_attr': '', 'src': 'Strategy+Business', 'text_remove': '', 'text_select': 'div.content > p, div.content > h3', 'date_format': '%B %d, %Y ', 'type_url': 'http', 'type_soup': 'html.parser', 'type_http': 'https', 'cookie': 'visid_incap_1339430=pGYUVnTuRXGpKOkh5JFwA2kOfF8AAAAAQUIPAAAAAABO+JK85g+W7XDF/az44hH/; sid=af9701294d44787d068d656d7198c3d0; incap_ses_1264_1339430=TJE4H9F321av+bbrVqGKEeBKfV8AAAAAH/I00yRV1dpUN+OzXPATYw=='},
]

# print(es_database)
def center_data(data_scrape):
    data_scrape = data_scrape[2]
    # print(data_scrape)
    url = data_scrape['url']
    title = data_scrape['title']
    date = data_scrape['date']
    source =data_scrape['source']

    es_database = es_database[2]

    # print(data_scrape['url'])
    if es_database['type_url'] == 'http':
        domain = data_scrape['url'].split('/')[2]
        sub_domain = data_scrape['url'].split(domain)[1]
        # print(domain)
        # print(sub_domain)
    else:
        domain = data_scrape['url'].split('/')[0]
        sub_domain = data_scrape['url'][len(domain):]
    if es_database["type_http"] == "https":
        data = con_url.get_data_from_https(domain, sub_domain, es_database["cookie"])
    elif es_database["type_http"] == "http":
        data = con_url.get_data_from_http(domain, sub_domain, es_database["cookie"])
    soup = BeautifulSoup(data.decode("utf-8"),es_database['type_soup'])
    # print(soup)
    list_soup_remove = []
    soup_text = soup.select(es_database['text_select'])
    if es_database['text_remove'] != "":
        soup_remove = soup.select(es_database['text_remove'])
        for i in range(len(soup_remove)):
            list_soup_remove.append(soup_remove[i].text.strip())
    text = ""
    for i in range(len(soup_text)):
        if soup_text[i].text.strip() not in list_soup_remove:
            text += soup_text[i].text.strip() + "\n"

    if data_scrape['date'] != "":
        date_time = data_scrape['date']
    elif es_database["date"] != "":
        date_time = soup.select_one(es_database["date"]).text
    else:
        print('test')
    dateQ3,date_string= date_time_from_eco(date_time,es_database['date_format'])
    data_scrape['text'] = text.strip()
    data_scrape['dateQ3'] = dateQ3
    data_scrape['date'] = date_string
    pprint(data_scrape)

# center_data(data_scrape)















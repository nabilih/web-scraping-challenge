from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd

# global dictionary to store all results
mars_scrape_dict = {}

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph
def scrape_Mars_news():

    url = 'https://mars.nasa.gov/news'
    browser = init_browser()
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    try:
        title = soup.find_all('div', class_='content_title')[1].text
        paragraph= soup.find_all('div', class_='article_teaser_body')[0].text
        
        mars_scrape_dict['news_title'] = title
        mars_scrape_dict['news_body'] = paragraph

    except AttributeError as e:
        return(e)
             
    finally:
        browser.quit()
        
# navigate the Jet Propulsion Lab site and find the image url for the current Featured Mars Image
def scrape_featured_image():
             
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser = init_browser()
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    try:
        url = soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href')
        featured_image_url = "https://www.jpl.nasa.gov" + url
        
        mars_scrape_dict['featured_image'] = featured_image_url
    
    except AttributeError as e:
        print(e)
    
    finally:
        browser.quit()

# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page      
def scrape_Mars_Weather():
             
    url= 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    try:
        mars_weather = soup.find_all('div', class_='js-tweet-text-container')[0].p.text       
        mars_scrape_dict['mars_weather'] = mars_weather
    
    except AttributeError as e:
        print(e)

# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the plane
def scrape_Mars_Facts():
    
    url = 'https://space-facts.com/mars/'
    
    try:
        facts = pd.read_html(url)[0]
        facts = facts.rename(columns={0:'Property', 1: 'value'})
        facts = facts.set_index('Property')
        facts_html = facts.to_html()
        mars_scrape_dict['mars_facts'] = facts_html
        
    except AttributeError as e:
        print(e)
        
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres        
def scrape_Mars_hemispheres():
   

    base_url = 'https://astrogeology.usgs.gov'
    url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    browser = init_browser()
    
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    full_image_list=[]

    i=1

    try:
        Hemispheres = soup.find_all('a', class_='itemLink product-item')
    
        for i in range(4):

            # Store title of image
            title = Hemispheres[i].text.strip('Enhanced ')
            # get the image url on the main page and append to the base url for a complete url reference
            image_url = base_url + Hemispheres[i]['href']

            # Open the full resolution image page
            browser.visit(image_url)
            html = browser.html
            soup = bs( html, 'html.parser')

            # find the full resolution image
            full_resolution_url = soup.find('img', class_='wide-image')['src']

            # Append the information in a list of dictionaries 
            full_image_list.append({'title' : title, 'img_url' : base_url + full_resolution_url})  
         
        mars_scrape_dict['hemispheres'] = full_image_list         
    except AttributeError as e:
        print(e)

def scrape():                                     
    
    scrape_Mars_news()
    scrape_featured_image()
    scrape_Mars_Weather()
    scrape_Mars_Facts()
    scrape_Mars_hemispheres()
    return mars_scrape_dict


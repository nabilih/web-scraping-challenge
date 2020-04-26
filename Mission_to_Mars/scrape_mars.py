{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "from splinter import Browser\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# store all of Mars scrape results in one dictionary\n",
    "mars_scrape_dict={}\n",
    "\n",
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "def scrape_Mars_news():\n",
    "    url = 'https://mars.nasa.gov/news' \n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    try:\n",
    "        title = soup.find_all('div', class_='content_title')[1].text\n",
    "        paragraph= soup.find_all('div', class_='article_teaser_body')[0].text\n",
    "\n",
    "    except AttributeError as e:\n",
    "        return(e)\n",
    "\n",
    "#         finally:\n",
    "#     browser.quit()\n",
    "        \n",
    "    mars_scrape_dict['news_title'] = title\n",
    "    mars_scrape_dict['news_body'] = paragraph\n",
    "       \n",
    "def scrape_Featured_image():\n",
    "    \n",
    "    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "\n",
    "    try:\n",
    "        article_style = soup.find('article', class_='carousel_item')['style']\n",
    "        url_start = article_style.find(\"url('\")\n",
    "        url_end = article_style.find(\"'_;\")\n",
    "        url = article_style[url_start+len(\"url('\"):url_end]\n",
    "    \n",
    "    except AttributeError as e:\n",
    "        print(e)\n",
    "    \n",
    "    finally:\n",
    "        browser.quit()\n",
    "        \n",
    "    featured_image_url = \"https://www.jpl.nasa.gov\" + url\n",
    "\n",
    "    mars_scrape_dict.update({'featured_image_url': featured_image_url})\n",
    "      \n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    scrape_Mars_news()\n",
    "    scrape_Featured_image()\n",
    "    return mars_scrape_dict\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

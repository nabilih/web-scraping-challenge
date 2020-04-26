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
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"/usr/local/bin/chromedriver\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "\n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    listings = {}\n",
    "\n",
    "    url = \"https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "    listings[\"headline\"] = soup.find(\"a\", class_=\"result-title\").get_text()\n",
    "    listings[\"price\"] = soup.find(\"span\", class_=\"result-price\").get_text()\n",
    "    listings[\"hood\"] = soup.find(\"span\", class_=\"result-hood\").get_text()\n",
    "\n",
    "    return listings\n"
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

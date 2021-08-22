{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "18c64cfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd\n",
    "def scrape_all():\n",
    "    # Initiate headless driver for deployment\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5d3cf42e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-56-bd1e48fd63b7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Visit the mars nasa news site\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'https://redplanetscience.com/'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# Optional delay for loading the page\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "\n",
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('div.list_text')\n",
    "slide_elem.find('div', class_='content_title')\n",
    "\n",
    "# Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title\n",
    "\n",
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "c775f10b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news(browser):\n",
    "\n",
    "    # Scrape Mars News\n",
    "    # Visit the mars nasa news site\n",
    "    url = 'https://redplanetscience.com/'\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Optional delay for loading the page\n",
    "    browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "\n",
    "    # Convert the browser html to a soup object and then quit the browser\n",
    "    html = browser.html\n",
    "    news_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        slide_elem = news_soup.select_one('div.list_text')\n",
    "        # Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "        news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "        # Use the parent element to find the paragraph text\n",
    "        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "\n",
    "    except AttributeError:\n",
    "        return None, None\n",
    "\n",
    "    return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "da0e28c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    # Visit URL\n",
    "    url = 'https://spaceimages-mars.com'\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Find and click the full image button\n",
    "    full_image_elem = browser.find_by_tag('button')[1]\n",
    "    full_image_elem.click()\n",
    "\n",
    "    # Parse the resulting html with soup\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Find the relative image url\n",
    "        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "\n",
    "    except AttributeError:\n",
    "        return None\n",
    "\n",
    "    # Use the base url to create an absolute url\n",
    "    img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "\n",
    "    return img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "dd2a0657",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_facts():\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Use 'read_html' to scrape the facts table into a dataframe\n",
    "        df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "\n",
    "    except BaseException:\n",
    "        return None\n",
    "\n",
    "    # Assign columns and set index of dataframe\n",
    "    df.columns=['Description', 'Mars', 'Earth']\n",
    "    df.set_index('Description', inplace=True)\n",
    "\n",
    "    # Convert dataframe into HTML format, add bootstrap\n",
    "    return df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "fd6f80f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 92.0.4515\n",
      "Get LATEST driver version for 92.0.4515\n",
      "Driver [C:\\Users\\reske\\.wdm\\drivers\\chromedriver\\win32\\92.0.4515.107\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "\n",
    "    # If running as script, print scraped data\n",
    "    print(scrape_all())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ec9363c",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

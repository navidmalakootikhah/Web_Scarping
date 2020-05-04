#!/usr/bin/env python
# coding: utf-8

# In[337]:


from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
import re


# In[338]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html



# In[339]:


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# ## Scraping Nasa Page -'https://mars.nasa.gov/news/'###

# In[342]:


def scrape():

    browser = init_browser()
    url1 = 'https://mars.nasa.gov/news/'

    #scraping the first url 
    browser.visit(url1)


    # In[343]:


    # pulling data from the first url 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quote = soup.find_all('li', class_='slide')
    title= quote[0].find('div',class_='content_title').text
    paragraph= quote[0].find('div',class_='rollover_description_inner').text


    # ## Scraping MARS image Page -'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # In[344]:


    # scraping thes second url 
    url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)


    # In[345]:


    # pulling data from the secon url 
    html2=browser.html
    soup2=BeautifulSoup(html2,"lxml")

    image=str(soup2.find('article',class_='carousel_item')['style'])



    # In[346]:


    image=image.split("background-image: url('/spaceimages/images/wallpaper/")
    image_name=image[1].split("');")


    # In[347]:


    featured_image_url="https://www.jpl.nasa.gov/spaceimages/images/wallpaper/"+image_name[0]


    # In[348]:


    featured_image_url



    # ## Scraping Mars Facts Page -https://space-facts.com/mars/)

    # In[352]:


    url4='https://space-facts.com/mars/'
    tables = pd.read_html(url4)


    # In[353]:


    df=tables[0]


    # In[354]:


    df.columns = ['Title', 'Value']
    df.set_index('Title', inplace=True)


    # In[355]:


    html_table = df.to_html()


    # In[356]:


    html_table=html_table.replace('\n', '')


    # In[358]:


    df.to_html('table.html')


    # ## Scraping Mars Hemispheres  https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

    # In[359]:


    def init_browser():
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)


    url_full_img = "https://astrogeology.usgs.gov"
    url_usgs = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_usgs)

    time.sleep(4)
    html4= browser.html
    soup4= BeautifulSoup(html4, "html.parser")
    url_list= []
    for i in range (8):
        if (i % 2) == 0:
            url_image = soup4.find('div', class_="collapsible results").find_all('a')[i]['href']
            full_url = url_full_img + url_image
            url_list.append(full_url)
            
            
            


    final_hemispheres_info=[]
    for url in url_list:
        
        browser = init_browser()
        browser.visit(url)

        time.sleep (4)

        
        html5= browser.html
        soup5= BeautifulSoup(html5, "html.parser")

        
        src_image = soup5.find('img', class_="wide-image")['src']
        url_final_image = url_full_img + src_image

            
        image_title = soup5.find('h2', class_="title").get_text()

            
        dic = {"Title": image_title ,"Image_URL": url_final_image}
        final_hemispheres_info.append(dic)


    mars_data = {"title": title, "paragraph": paragraph,"featured_image_url":featured_image_url,"fact_table":html_table, "title_1": final_hemispheres_info[0]["Title"],"img_url_1": final_hemispheres_info[0]["Image_URL"],"title_2": final_hemispheres_info[1]["Title"],"img_url_2": final_hemispheres_info[1]["Image_URL"],"title_3": final_hemispheres_info[2]["Title"],"img_url_3": final_hemispheres_info[2]["Image_URL"],"title_4": final_hemispheres_info[3]["Title"],"img_url_4": final_hemispheres_info[3]["Image_URL"]}


    # In[360]:


    return(mars_data)


# In[ ]:






# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse HTML to Bsoup
html = browser.html
main_page_soup = soup(html, 'html.parser')
# count pictures
picture_count = len(main_page_soup.select('div.item'))

for i in range(picture_count):
 
    results = {}
    link = main_page_soup.select('div.description a')[i].get('href')
    # Use the base URL to create an absolute URL
    url = f'https://marshemispheres.com/{link}'
    browser.visit(url)
    html = browser.html
    image_page_soup = soup(html, 'html.parser')
    img_url = image_page_soup.select_one('div.downloads ul li a').get('href')
    title = image_page_soup.select_one('h2.title').get_text()
    #results to dic
    url = f'https://marshemispheres.com/{img_url}'
    results = {'img_url':url, 'title':title}
    hemisphere_image_urls.append(results)
    
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls
browser.quit()


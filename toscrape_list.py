import requests
import bs4
import lxml
base_url='https://books.toscrape.com/catalogue/page-{}.html'
book1=[]
book2=[]
book3=[]
book4=[]
book5=[]

for x in range(1,51):
    page = requests.get(base_url.format(x))
    con= bs4.BeautifulSoup(page.text,'lxml')
    for y in range(20):
        parts=con.select('.product_pod')[y]
        if []!=parts.select('.star-rating.One'):
            book1.append(parts.select('a')[1]['title'])
        elif []!=parts.select('.star-rating.Two'):
            book2.append(parts.select('a')[1]['title'])
        elif []!=parts.select('.star-rating.Three'):
            book3.append(parts.select('a')[1]['title'])
        elif []!=parts.select('.star-rating.Four'):
            book4.append(parts.select('a')[1]['title'])
        elif []!=parts.select('.star-rating.Five'):
            book5.append(parts.select('a')[1]['title'])
        
print(f'\n\nList of  {len(book1)} books with One star are : '+'-'*50)
for x in range(len(book1)):
    print(book1[x])

print(f'\n\nList of  {len(book2)} books with Two star are : '+'-'*50)
for x in range(len(book2)):
    print(book2[x])

print(f'\n\nList of  {len(book3)} books with Three star are : '+'-'*50)
for x in range(len(book3)):
    print(book3[x])

print(f'\n\nList of  {len(book4)} books with Four star are : '+'-'*50)
for x in range(len(book4)):
    print(book4[x])

print(f'\n\nList of  {len(book5)} books with Five star are : '+'-'*50)
for x in range(len(book5)):
    print(book5[x])                         


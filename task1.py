from bs4 import BeautifulSoup
import requests
import pprint

url=("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
page=requests.get(url)
# print(page)

soup=BeautifulSoup(page.content,"html.parser")
res=soup.tittle
# print(soup.prettify())

def scrap_top_list():
    main_div=soup.find('div',class_='lister')
    # return main_div
# print(scrap_top_list())
    tbody=main_div.find('tbody',class_='lister-list')
    # return tbody
# print(scrap_top_list())
    trs=tbody.find_all('tr')
    # return trs
# print(scrap_top_list())

    movies_ranks=[]
    movies_name=[]
    year_of_realease=[]
    movies_urls=[]
    movies_rating=[]


    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        # return position
# print(scrap_top_list())

        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movies_ranks.append(rank)
    # return movies_ranks
# print(scrap_top_list())

        title=tr.find('td',class_="titleColumn").a.get_text()
        # return title
# print(scrap_top_list())
        movies_name.append(title)

        year=tr.find('td', class_="titleColumn").span.get_text()
        # return year
# print(scrap_top_list())
        year_of_realease.append(year)
    # return year_of_realease
# print(scrap_top_list())

        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        # return imdb_rating
# print(scrap_top_list())
    
        movies_rating.append(imdb_rating)

        link=tr.find('td',class_="titleColumn").a['href']
        # return link
# print(scrap_top_list())
        movies_link="https://www.imdb.com"+link
        # return movies_link
# print(scrap_top_list())
        movies_urls.append(movies_link)

    Top_movies=[]
    details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movies_ranks)):
        details['position']=int(movies_ranks[i])
        details['name']= str(movies_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details['year']=int(year_of_realease[i])
        details['rating']= float(movies_rating[i])
        details['urls']=movies_urls[i]
        Top_movies.append(details.copy())
        details={'position':'','name':'','year':'','rating':'','url':''}

    return(Top_movies)
# pprint.pprint(scrap_top_list())


# TASK 2 ##################................

scrapped=scrap_top_list()

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
        year=i['year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    return movie_dict
# print(group_by_year(scrapped))
group_by_year(scrapped)
dec_arg=group_by_year(scrapped)

#   TASK 3 ####################.......................

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    # print(list1)
    list1.sort()
    # print(list1)

    for i in list1:
        moviedec[i]=[]
    # print(movies)
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x <= dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)

    return(moviedec)
pprint.pprint(group_by_decade(dec_arg))

# TASK 4 ##########................


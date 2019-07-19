#https://swapi.co/api

#GET/https://swapi.co/api/

#http https://swapi.co/api/people/:id/

import requests

search = input("Star Wars Character Finder///EnterName///---->")

r = requests.get('https://swapi.co/api/people/')
response = r.json()
str(response)
x = 1 

while response != search:
    r = requests.get('https://swapi.co/api/people/' + str(x) + '/')
    response = r.json()
    response = str(response)
    print(response.find(search))
    if search in response:
        print(response)
        break
    else:
        x += 1

        
#response will never be the same as the search cause response is a bunch of stuff 
        















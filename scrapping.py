from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
# Let's get some data from TechCrunch.com
from IPython.display import HTML
HTML('<iframe src=https://techcrunch.com/ width=700 height=500></iframe>')

#Requests function along with get() function calls the webpage and gives a response of html format as a readable text style 
page = requests.get("https://techcrunch.com/").text
soup = BeautifulSoup(page, 'html5lib') #'html5lib is a format used for HTML pages, and 'lxml' is used for XML  
title_results=[]
tags_results=[]
author_results=[]
time_results=[]
#Using find_all to find all the titles
for title in soup.find_all('h2', class_="post-title"):
    title_results.append(title.text)
#Using find_all to find all the tags under 'title' tag
for tags in soup.find_all('a', class_="tag"):
    tags_results.append(tags.text)
#Using find_all to find all the authors       
for x in soup.find_all('div',class_='byline'):
    for author in x.find_all('a'):
        author_results.append(author.get_text())
#Using find_all to find all the dates and time under 'datatime' tag
    for date in x.find_all('time',class_='timestamp'):
        time_results.append(date.get('datetime'))
#Making all the lengths of columns equal         
length =len(title_results)-len(tags_results)
length1= len(author_results)-len(title_results)

#pop function is used to find all the missing data on site
for i in range(length1):
    author_results.pop()
for i in range(length):
    tags_results.append('No Tag')
    
#Data is displayed in table format
final_result = pd.DataFrame({'Tags': tags_results,'Date': time_results,'Author': author_results,'Title': title_results})

#Print data
final_result

Scraping https://www.data.gov link to identify the number of data sets available.

#Question 2
from bs4 import BeautifulSoup
from IPython.display import HTML
import requests
HTML('<iframe src=https://www.data.gov/ width=700 height=500></iframe>')
page = requests.get("https://www.data.gov/").text
soup = BeautifulSoup(page, 'html5lib')
#Using variable data to store all values that fall under 'small' tag
data = soup.find('small')
#Using variable number to store the number of datasets that fall under 'a' tag 
number = data.find('a')
#Print the number of datasets
print("The number of data sets available are:",number.text)

#Exercise 3
from bs4 import BeautifulSoup
import requests
from IPython.display import HTML
import numpy as np
#Contains all the 'Yes'
A=[]
#Contains all the 'Nays'
B=[]
#contains subtracted values
all_list=[]
#Status_rejected = []
R =[]
vote_count=[]

page = requests.get("https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_115_1.xml").text
soup = BeautifulSoup(page,'xml')
#Looping, in order to extract all the result status
for status in soup.find_all('result'):
    R.append(status.text)
# Get the count of votes 
for count in soup.find_all('vote_number'):
    vote_count.append(count.text)
for final in soup.find_all('vote_tally'):
#Getting the count of all 'yeas' and 'nays'
            a = final.find('yeas')
            A.append(a.text)
            b = final.find('nays')
            B.append(b.text)
#As A and B are arrays, we need to convert them into integer format in order to subtract the values
Yes_count = [int(i) for i in A]
No_count  = [int(j) for j in B]
#all_list will contain the subtracted values
all_list = np.array(Yes_count) - np.array(No_count)
S=[]
#Looping results to find Rejected status
for z in range(len(R)):
#Check whether the subtracted value is in between -5 to +5 range and also whether its status is rejected or not
      if(R[z]=='Rejected' and vote_count[z] and -5<all_list[z]<5 ):
            S.append([R[z],vote_count[z], all_list[z]])
print("\nList of votes which match Rejected criteria:\nStatus of the vote\tVote Tally\tMargin less than 5\n\n",S)
print("\nThe number of U.S. Senate votes that were rejected by a margin of less than 5 votes:",len(S))

Give the number of alerts and warnings for international travel given by the US government.

#Exercise 4
from bs4 import BeautifulSoup
import requests
from IPython.display import HTML
count_warning=[]
count_alert=[]
#Requesting page to get all the data using requests.get 
page = requests.get("https://travel.state.gov/content/passports/en/alertswarnings.html").text
soup = BeautifulSoup(page,'html')
# find all the warning tags
for warning in soup.find_all('td', class_="warning"):
    #append the count of warnings
    count_warning.append(warning.text)
# find all the alert tags
for alert in soup.find_all('td', class_="alert"):
    ##append the cunt of alerts
    count_alert.append(alert.text)
#get the total number of warnings
print("Total number of warnings are:",len(count_warning)) 
#get the total number of alerts
print("Total number of alerts are:",len(count_alert))

Report the total number of female babies whose names start with 'K' so far this decade.

#Exercise 5
from bs4 import BeautifulSoup
import requests
from IPython.display import HTML
import numpy as np
all_Text=[]
girls=[]
page = requests.get("https://www.ssa.gov/OACT/babynames/decades/names2010s.html").text
soup = BeautifulSoup(page,'html')
for i in soup.find_all('table', class_="border table"):
    for count in i.find_all('tr', align="right"):
        # extracts all the data including boys and girls names with their count
        all_Text.append(count.text)
for line in all_Text:
    #adding commas in order to access via indexing
    y = [value for value in line.split()]
    #using step and stop loop to access only girls names and their count
    for j in range(3, len(y), 1):
        #girls will contain only girls and their count
        girls.append(y[j])
numbers=[]
Darray=np.array(girls)        
for i in range(len(Darray)):
    #check girls names starting with K
    if (Darray[i][0]=='K'):
        #total number of female babies whose names start with 'K'
        numbers.append(Darray[i+1].replace(',', ''))
#converting list to int type
m=[int(i) for i in numbers] 
final=sum(m)
#gets the total number of female babies whose names start with 'K'
print("Total number of female babies whose names start with 'k':", final)

Question 6:
Scrap the data and plot of a graph of features of all songs

#Exercise 6
import spotipy
import sys
import spotipy.util as util
import matplotlib.pyplot as plt
import csv

D =[]
A=[]

# file path is given in order to read songs stored in .csv file
with open('C:/Users/Madhura Snehal/Downloads/song-list.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        #D array contains all the data related to artists, albums etc
        D.append(row)
#list1 contains all appended songs
list1 = [item[0] for item in D]

#scope of the profile's user rights are defined
scope = 'user-library-read'
#credentials are set
username = 'Madhura Buchake'
# User Authorisation
# user's client id, client secret and redirect uri is set. variable 'token' will contain the resopnse of the request
token = util.prompt_for_user_token(username,scope,client_id='f5201862176f42888178de4597b9756a',client_secret='fbf0385a13854c3fb69acc5d7266fe92',redirect_uri='https://www.google.com/')

#spotify function is called
spotify = spotipy.Spotify(token)

new_results=[]        
for i in range (len(list1)):
    #songs from 'list1' are searched on the site
    results = spotify.search(q='track:' + list1[i], type='track')
    #new_results array contain all the songs searched on site
    new_results.append(results)

for i in new_results:
    # As new_results is a dictionary with nested list, a loop is tested on new_results array
    for j in i['tracks']['items']:
        #to check if href is present in j loop
        if 'href' in j:
            #only if href is present with 't' as a starting letter at the 27th position, then print the id's of the songs
            if(j['href'][27]=='t'):
                print(j['id'])
                #print('\n')
                
new_array =[]
for x in range(len(new_results)):
    for y in (new_results[x]['tracks']['items']):
            if(y['href'][27]=='t'):
                new_array.append(y['id'])

#function is defined in order to extract audio features of all the songs 
def energy(A): 
    audio_features = spotify.audio_features(A)
    adf=[]
    for t in audio_features:
        if (t is None):
            adf.append((0,0))
        else:
            # energy and valence are extracted from the entire features 
            adf.append((t['energy'], t['valence']))
    return adf

new_values=[]
for h in range(0,5874):
    #after every 50th value, next 50 values are considered 
    new_values.append(energy(new_array[h:h+49]))
    
list2=[]
for x in new_values:
    for y in x:
        list2.append(y)
        
#Plot graph for energy and valence
x,y = zip(*list2)
plt.figure(figsize=(12,9))#default figure size of plot
ax = plt.subplot(111)
#Frames of the plot are removed
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.get_xaxis().tick_bottom();
ax.get_yaxis().tick_left();

#Plot the graph
plt.scatter(x,y, c="g", alpha=0.8, marker=r'$\clubsuit$',
            label="Luck")
#Title of the plot
plt.title("Energy vs Valence Graph", fontsize=15)
#X-axis label 
plt.xlabel("Energy", fontsize=15)
#y-axis label
plt.ylabel("Valence", fontsize=15)
plt.show()

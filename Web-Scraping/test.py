import requests
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
result = requests.get("https://www.premierleague.com/tables")

# To make sure that the website is accessible, we can
# ensure that we obtain a 200 OK response to indicate
# that the page is indeed present:
print(result.status_code)

# For other potential status codes you may encounter,
# consult the following Wikipedia page:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# We can also check the HTTP header of the website to
# verify that we have indeed accessed the correct page:
#print(result.headers)

# For more information on HTTP headers and the information
# one can obtain from them, you may consult:
# https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

# Now, let us store the page content of the website accessed
# from requests to a variable:
src = result.content

# Now that we have the page source stored, we will use the
# BeautifulSoup module to parse and process the source.
# To do so, we create a BeautifulSoup object based on the
# source variable we created above:
soup = BeautifulSoup(src, 'lxml')

# Now that the page source has been processed via Beautifulsoup
# we can access specific information directly from it. For instance,
# say we want to see a list of all of the links on the page:

links = soup.find("tbody", {"class":"tableBodyContainer isPL"})
#finds team position
teamPosition = []
link = links.findAll("td", {"class": "pos button-tooltip"})
for name in link:
    namee = name.findAll("span", {"class":"value"})
    for nameee in namee:
        teamPosition.append(nameee.string)
        #print(nameee.string)

#finds team name
teamName = []
link = links.findAll("td", {"class": "team"})
for name in link:
    namee = name.findAll("span", {"class":"long"})
    for nameee in namee:
        teamName.append(nameee.string)
        #print(nameee.string)

#finds team games played
teamPlayed = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[3]
    for nameee in namee:
        teamPlayed.append(nameee.string)
        #print(nameee.string)

#finds team games won
teamWon = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[4]
    for nameee in namee:
        teamWon.append(nameee.string)
        #print(nameee.string)

#finds team games drawn
teamDrawn = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[5]
    for nameee in namee:
        teamDrawn.append(nameee.string)
        #print(nameee.string)

#finds team games lost
teamLost = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[6]
    for nameee in namee:
        teamLost.append(nameee.string)
        #print(nameee.string)

#finds team GF
teamGF = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[7]
    for nameee in namee:
        teamGF.append(nameee.string)
        #print(nameee.string)

#finds team GA
teamGA = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[8]
    for nameee in namee:
        teamGA.append(nameee.string)
        #print(nameee.string)

#finds team GD
teamGD = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[9]
    for nameee in namee:
        teamGD.append(nameee.string.strip())
        #print(nameee.string)

#finds team points
teamPoints = []
link = links.findAll("tr", {"data-compseason":"274"})
for name in link:
    namee = name.findAll("td")[10]
    for nameee in namee:
        teamPoints.append(nameee.string)
        #print(nameee.string)
    
    


with open('index.handlebars', 'w') as f:
    f.write("<table>\n")
    f.write("<tr><th>Position</th><th>Club</th><th>Played</th><th>Won</th><th>Drawn</th><th>Lost</th><th>GF</th><th>GA</th><th>GD</th><th>Points</th></tr>\n")
    for x in range(20):
        f.write("<tr name='Pos_"+teamPosition[x]+"'>")
        f.write("<td class='place'>"+teamPosition[x]+"</td>")
        f.write("<td class ='teamName' name='"+teamName[x]+"'>"+teamName[x]+"</td>")
        f.write("<td class ='teamPlayed'>"+teamPlayed[x]+"</td>")
        f.write("<td class ='teamWon'>"+teamWon[x]+"</td>")
        f.write("<td class ='teamDrawn'>"+teamDrawn[x]+"</td>")
        f.write("<td class ='teamLost'>"+teamLost[x]+"</td>")
        f.write("<td class ='teamGF'>"+teamGF[x]+"</td>")
        f.write("<td class ='teamGA'>"+teamGA[x]+"</td>")
        f.write("<td class ='teamGD'>"+teamGD[x]+"</td>")
        f.write("<td class ='teamPoints'>"+teamPoints[x]+"</td>")
        f.write("</tr>\n")
    f.write("</table>")

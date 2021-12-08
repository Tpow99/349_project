import requests         # grab web-page
from bs4 import BeautifulSoup as bsopa  # parse web-page
import json
import os.path

scrpDataL = []
for j in range(0, 15, 10):  # calling 15 entries

    position, location = 'data scientist', 'seattle'

    url_page = requests.get('https://www.indeed.com/jobs?q={}&l={}&sort=date='.format(position, location) + str(j))

    soup = bsopa(url_page.text, 'html.parser')
    #     print(soup) use this if you want to check if working properly, response code 200

    for jobCard in soup.find_all('div', {"class": "job_seen_beacon"}):
        j = jobCard.find('tbody')  # calling the table body to go inside of
        a = j.find('tr')  # going inside the table


        for n in a.find_all('h2', {'class': 'jobTitle jobTitle-color-purple jobTitle-newJob'}):
            jobCard_data = {}

            jobTitle = n.find_all('span')[1].get_text()  # if you don't use the 1, you get the 'new' posting text
            jobCard_data['Position'] = jobTitle
            #print(jobTitle)

            # Company Name is in new nesting:
            companyDiv = a.find('div', {'class': 'heading6 company_location tapItem-gutter'})
            companySpan = companyDiv.find('span')
            company = (companySpan.get_text())
            #print(company)
            jobCard_data['Company'] = company
            #             print(a.find('span',{'class':'companyName'}).get_text()) # alt version

            # Location:
            locationPreTag = companyDiv.find('pre')
            # print(locationPreTag.find('div', {'class': 'companyLocation'}).get_text() + '\n')
            location = locationPreTag.find('div', {'class': 'companyLocation'}).get_text()
            jobCard_data['Location'] = location

            # Salary if available:
            if a.find('div', {'class': 'heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly'}):
                try:
                    #print(a.find('div', {'class': 'metadata salary-snippet-container'}).get_text())
                    salary = a.find('div', {'class': 'metadata salary-snippet-container'}).get_text()
                    jobCard_data['Salary'] = salary
                except AttributeError:
                    #print("No salary posted...")
                    jobCard_data['Salary'] = "No salary posted"
            else:
                #print('No salary posted...')
                jobCard_data['Salary'] = "No salary posted"

            scrpDataL.append(jobCard_data)

# print the scraped data for checking
print(f'{len(scrpDataL)} results\n')
for jobEntry in scrpDataL:
    for data in jobEntry.items():
        print(data, end='\n')
    print()

# add data from list of dictionaries to JSON file
if os.path.exists('scraped_jobs.json'): # updates JSON file if it exists already with newly-scraped data
    with open('scraped_jobs.json', 'r+') as file:
        fileData = json.load(file)
    for jobDict in scrpDataL:
        fileData.append(jobDict)
    with open('scraped_jobs.json', 'w', encoding='UTF8') as file:
        json.dump(fileData, file, indent=2)
else:   # if JSON file doesn't exist yet
    with open('scraped_jobs.json', 'w', encoding='UTF8') as file:
        json.dump(scrpDataL, file, indent=2)

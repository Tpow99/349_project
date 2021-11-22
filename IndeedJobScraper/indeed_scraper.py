import pandas as pd
import requests         # grab web-page
from bs4 import BeautifulSoup as bsopa  # parse web-page
import datetime         # format date/time
import csv

scrpDataL = []
for j in range(0, 15, 10):  # calling 15 entries

    position, location = 'data scientist', 'california'

    url_page = requests.get('https://www.indeed.com/jobs?q={}&l={}&sort=date='.format(position, location) + str(j))

    soup = bsopa(url_page.text, 'html.parser')
    #     print(soup) use this if you want to check if working properly, response code 200

    for jobCard in soup.find_all('div', {"class": "job_seen_beacon"}):
        j = jobCard.find('tbody')  # calling the table body to go inside of
        a = j.find('tr')  # going inside the table


        for n in a.find_all('h2', {'class': 'jobTitle jobTitle-color-purple jobTitle-newJob'}):
            jobCard_data = []

            jobTitle = n.find_all('span')[1].get_text()  # if you don't use the 1, you get the 'new' posting text
            jobCard_data.append(jobTitle)
            #print(jobTitle)

            # Company Name is in new nesting:
            companyDiv = a.find('div', {'class': 'heading6 company_location tapItem-gutter'})
            companySpan = companyDiv.find('span')
            company = (companySpan.get_text())
            #print(company)
            jobCard_data.append(company)
            #             print(a.find('span',{'class':'companyName'}).get_text()) # alt version

            # Location:
            locationPreTag = companyDiv.find('pre')
            # print(locationPreTag.find('div', {'class': 'companyLocation'}).get_text() + '\n')
            location = locationPreTag.find('div', {'class': 'companyLocation'}).get_text()
            jobCard_data.append(location)

            # Salary if available:
            if a.find('div', {'class': 'heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly'}):
                try:
                    #print(a.find('div', {'class': 'metadata salary-snippet-container'}).get_text())
                    salary = a.find('div', {'class': 'metadata salary-snippet-container'}).get_text()
                    jobCard_data.append(salary)
                except AttributeError:
                    #print("No salary posted...")
                    jobCard_data.append("No salary posted")
            else:
                #print('No salary posted...')
                jobCard_data.append("No salary posted")

            scrpDataL.append(jobCard_data)

# print the scraped data for checking
print(f'{len(scrpDataL)} results\n')
for jobEntry in scrpDataL:
    for data in jobEntry:
        print(data, end='\n')
    print()

# add list of scraped data to CSV file
cols = ['Position', 'Company', 'Location', 'Salary']
with open('scraped_jobs.csv', 'w', encoding='UTF8', newline='') as file:
    write = csv.writer(file)
    write.writerow(cols)
    write.writerows(scrpDataL)

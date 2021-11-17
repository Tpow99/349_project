from random import randint, sample
#### read jobs and positions and organize in list ####

with open('companies.txt') as f:
    lines = f.readlines()

employers = []
for x in lines:
    x = x.replace('\n','')
    y = (x.split(','))
    y[1] = float(y[1])
    employers.append(y)

with open('positions.txt') as f:
    lines = f.readlines()

positions = []
for x in lines:
    x = x.replace('\n','')
    y = (x.split(','))
    y[1] = float(y[1])
    positions.append(y)

with open('locations.txt') as f:
    lines = f.readlines()

locations = []
for x in lines:
    x = x.replace('\n', '')
    locations.append(x)

#######----#######

    
baseSal = 50000 #base salary constant, all pay is calculated beginning with this


def genJob(quantity): # returns a list of dictionaries containing 'title', 'company', 'salary', and 'location'
    output = []
    for x in range(quantity):
        seedEmp = randint(0,len(employers)-1)
        seedPos = randint(0,len(positions)-1)
        seedSal = randint(-100,100)*100 #random salary offset, +/- up to $10k
        employer = employers[seedEmp][0]
        job = positions[seedPos][0]
        location = locations[randint(0,len(locations)-1)]

        #salary is (base salary * position bias * company bias) +/- random offset
        salary = round(((baseSal * positions[seedPos][1] * employers[seedEmp][1]) + (seedSal)),2)
        if positions[seedPos][1] == 0: #edge case for interns to prevent negative salaries
            salary = 0
        
        output.append({'position':job, 'company':employer, 'location':location, 'salary':salary})
    return output

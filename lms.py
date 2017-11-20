from bs4 import BeautifulSoup as pretty
import requests,os
import warnings
from datetime import datetime


#current date
date=datetime.now()


#to retrieve month date and year from a given input(it is used later when we extract the date of submission from the table) 
def month(i):
        return (((i.split(','))[1]).split(' '))[2]
def year(i):
        return (((i.split(','))[1]).split(' '))[3]
def day(i):
        return (((i.split(','))[1]).split(' '))[1]
def smtoint(mon):
    return int((datetime.strptime(mon,"%B")).month)


#to remove the warnings shown while making connection
warnings.filterwarnings("ignore")


#verification of the txt file for storing data and deleting it for writing fresh data
if os.path.exists("updates.txt"):
    os.system("rm updates.txt")


#establishing connection
with requests.Session() as c:
    url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
    USERNAME = '********'
    PASSWORD = '********'
    
    #logging into LMS
    c.get(url, verify= False)
    info = dict(username=USERNAME, password=PASSWORD, next='/')
    c.post(url, data=info)

    #subject id of all the courses which i found out by inspecting the HTML
    subjects = [920,929,894,918,921,922]
    
    #looping through all the subjects
    for no in subjects:
        page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=' + str(no))
        html = page.text
        code = pretty(html, "html.parser")  
        topic= code.h1.string  

        #l1 is for list of assignments and l2 for their submission dates
        l1=[]
        l2=[]
        a = code.findAll("td", {"class" : "cell c1"})
        for i in a:
            l1.append(i.string)
        if l1==[]:
            l1 = ["no updates"]
        b = code.findAll("td", {"class" : "cell c2"})
        for i in b:
            l2.append(i.string)
        if l2==[]:
            l2 = [""]
        l=[]
        for i in range(len(l1)):
            l.append(l1[i]+ "   " + l2[i])

        s=[]
        #check wether the submisiion date is greater than or less than current date. If yes it appends it to the list
        for i in range(len(l)):
            #for handling error due to empty row or coloumn in the table at taret site
            try:
                submon=smtoint(month(l[i]))
                subday=int(day(l[i]))
                subyear=int(year(l[i]))
                if ([subyear,submon,subday]>=[date.year,date.month,date.day]):     
                    data = str(l1[i]) +" submission on " + str(l2[i])
                    s.append(data)
            except IndexError:
                pass
        
        #condition for no updates
        if s == []:
            s= ["No updates"]      

        #writing the result in the txt file  
        f = open("updates.txt", 'a')
        f.write("\n --------------------------------------------------------------------- \n" + topic  )
        for i in s:
            f.write("\n" + i + "\n")
        f.write("\n")
        f.close()
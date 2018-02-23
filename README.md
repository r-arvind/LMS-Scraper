# A Simple Scraper (with login facility)

For those of you wondering what LMS is, my college has a portal called Learning Management System where you can find all the assignments that you have to submit, study materials, lecture presentations of your Courses.

You can check out the LMS here: [IIIT B-LMS](https://lms.iiitb.ac.in)

What this Scraper does is it logs into your account, scrapes all info about the assignments that has to be Submitted.


## Requirements
* Requests Module ( [Installation](http://docs.python-requests.org/en/master/user/install/) )
* Beautiful Soup ( [Installation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) )

## Requirements Part -2 (which you won't be having unless you are from my college i.e IIIT Bangalore)
* Username (IMT/MT*******)
* Password
* Your Course ID's

Enter these info in their respective places. Username and Login should be entered at the place marked '*******'. Enter the Course ID's inside the list 'Subject'(around line 45).

After you run the script, a text file called updates.txt will be created where you can find all the updates. Whenever the script is run, the existing updates.txt is deleted and a new one is created for the new data.
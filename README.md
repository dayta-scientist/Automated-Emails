# Automated-Emails
This project of pure programming in **Python** language consists of sending automatic E-mails every day at a time defined by the programmer, to certain people from a list that is in an excel file, who have interests in a particular topic (example: Bitcoin, NASA).

The data of interest of the different people is extracted by the program every day at the specified time from the News API page (https://newsapi.org/), for which you need to obtain an API key. In the program to mask the display of the key, as well as the E-mail password, environment variables were used.


## The architecture is as follows: 

  - requirements.txt: 
      All the programs necessary to run the main.py file correctly are listed. It is always advisable to create a virtual environment to assert the versions of each program, ensuring its correct operation. 

  - news.py: 
      The news of the different topics of interest of the people listed in the excel file (people.xlsx) are obtained 

  - api_key.py: 
      The environment variable is obtained with the API key generated on the page - https://newsapi.org/ -, which will then be imported by news.py 

  - email_password.py: 
      The environment variable is obtained with the password of the E-mail in charge of sending to the different addresses of the people listed in the excel file (people.xlsx), which will then be imported by main.py

   - main.py: 
      It is the program that brings together all of the above and is finally in charge of sending the E-mails with the news of interest to each person that appears in the list of the excel file (people.xlsx), using the Pandas package (https: //pandas.pydata.org/) to read this information inside the program

   - E-mail_result.jpg: 
      The result of the E-mail sent to each person can be observed
      
### Install the dependencies:

```sh
pip install -r requirements.txt

```
  

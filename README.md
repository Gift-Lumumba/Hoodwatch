# Hoodwatch

 This is a web application that allows one to be in the loop about everything happening in his/her neighborhood from contact information of different meeting announcements or even alerts.This application was created on 22th October 2018

# Author
Gift Lumumba

## Link to Deployed Site on Heroku
https://gift-hood.herokuapp.com/

## Setup and installation

- Clone the Repo uding the following command:
  `git clone https://github.com/Gift-Lumumba/Hoodwatch.git`
- Activate virtual environment using python3.6 as default handler by running 
    `python3.6 -m venv virtual` then enter the virtual environment using `source virtual/bin/activate`
- Download the latest version of pip in the virtual environment: `$ curl https://bootstrap.pypa.io/get-pip.py | python`

- Install all application dependancies 
`pip install -r requirements.txt`

- Create the Database
    -On the terminal,run `psql`
    - Create a database by typing 
      `CREATE DATABASE hood;` for example.

- Create a .env file and add the following:

    - SECRET_KEY = `<Secret_key>`
    - DB_NAME = `awards`
    - DB_USER = `<Username>`
    - DB_PASSWORD = `your db password`
    - DEBUG = `True`

- Run Initial Migration
    `python3.6 manage.py makemigrations <name of the app>`
    `python3.6 manage.py migrate`

- Run the app
    `python3.6 manage.py runserver`
    `Open terminal on localhost:8000`

## User Stories
The application user is able to:
- Create an account and confirm through email verification.
- Sign in to the application to start using.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Search for Neighbourhoods
- Only view details of a single neighborhood.
- View my profile page.
 

## Technologies Used
- Python 3.6.6(Django Framework)
- HTML5
- CSS3
- Bootstrap4
- Postgresql
- Heroku(Deployment)
- Visual Studio Code text editor

## Known Bugs
No known bugs so far.Contact me if you come across any.

## Support and Contact Details
For any comments,suggestions,feedback or inquiries about my application,Contact me via email:giftlumumba2@gmail.com


## License
*MIT License*
Copyright <2018> <GIFT LUMUMBA>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2018 **Gift Lumumba**

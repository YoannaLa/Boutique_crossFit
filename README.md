
![](images/responsive.jpg)



Simple and practical website for CrossFit fanatics!

CrossFit Gear is a full stack e-commerce web application with a small, unique selections of products and gifts that someone interested in the world of CrossFit will enjoy. Or a friend who wants to surprise a love one with a funky gift 

This website is for educational purposes only. So on this website please use only the details below in the card sections 
Card number: 4242 4242 4242 4242
Use any expiration date (month/year) in the future, any 3 digit CVC code and 5 digit post code.

This website is my five and fianal  ‘Milestone Project’ as part of the Full Stack Development journey of Code Institute. The focus is  on using the Django framework,  an authorisation and authentication system and using, learning about  Stripe for payments and AWS cloud base storage services. 

A live website can be view on https://crossfit-gear.herokuapp.com/

#   User Experience (UX)
##  User stories
##  Scope level
### Requirements
##  Interaction Design and Information Design
## The pages
##  Wireframes
##  Colors
## Font Family
#   Features
## Existing Features
## Features left to implement
# Technologies Used
## Languages
## Frameworks and libraries
### Tools and Programmes
# Testing
# Deployment
## Deployment to Heroku
## Forking this GitHub Repository
## Cloning this GitHub Repository
## Setup local deployment
# Media
# Credits

#   User Experience (UX)
## See user stories 
![](images/user.stories.png)

From the users stories I've created the following:

### Requirements
1. A home page with nav bar
2. A design which is responsive on different screen sizes
3. A product page
4. A option to register and login to a personal account
5. A page with all the products
6. A all products page
7. Banner reagding new deals
8. Adding products to a shopping baskets, chosing size and units
9. An option to search
10. An option to fillter products
11. An indiation of search and numbers of results
12. A page to checkout with the products and costs
13. Possiblity to ajdust the shopping basket
14. Secure checkout with the payment details using Stripe
15. Email confirming the purchase details
16. Secure admin site for the website owner to Add, Edit, Delete a product

### Additional requriments 
1. Recover your password

# Structure of the website
The overall look is kept the same on each page as much as possible, to enhance single-use-learning:
* The header and footer are the same on each page.
* Buttons are styled in the same way.
* The layout is consistent

The navigation is simple and consistent:
* home page show nav bar
* The logo at the top of the page is also the link to the home page.
* Buttons can be used to navigate products sorting, products cateories and special offers
* Search button, account and shopping basket buttons 
* "Have a look" button which takes user to all products page
* banner with a wrapping deal if the purchase spends more that £25

The information provided should be easily visible:
* The user see on which page they are, e.g. by using headers.
* The user gets a visual feedback during certain actions (e.g. focussing on, clicking on, hovering over buttons and links).
* Messages(toasts) are used to confirm or inform about current actions.


## Wireframes (home page, shop page, basket, lognin, signin profile)


## Colors and  font
 * Roboto for font
 * Color - #555 and  rgb(64, 121, 187)

# Features
## Features 
* Responsive on all devices
* A nav bar alows user to navigate the website easlie, on small devices in collapes into hamuburger manu to make it readable
* Function to regiser for an account, by filling a form
* Fucntion to log in an log out of the account, by filling a form 
* A search bar, to easly find a product 
* A search button to search by price, rating and category
* Categories under the gear tap, to make it quicker to find a product
* A Special offers button to see what deal the site can offer
* Payment function using Stripe
* Toats messages to inform user after completing a function 
* A confirmation modal after purchasing 

## Forms
* A resister form to sign up for a account
* A sign in form
* A checkout form for the purchasing, with the payment details
* A form that allows to add, review and delete products - admin access only

## CRUD (Create, Read, Update, Delete) function

* Create 
1. Admin to create a new product 

* Read 
1. Users can search and view products in deatil

* Delete
1. Admin can delete any products from the site

## Features still to be implement
1. Delete a user/profile by the user 

# Technologies used
## Languages
* HTML5 for markup.
* CSS for styling.
* Javascript for interactivity.
* Python3 for backend programming.

## Frameworks & libraries used
* Bootstrap - code snippets to assist wtih the responsiveness of the site
* jQuery, a javascript library 
* Google fonts .
* Font Awesome for the icons used
* Django is a high-level Python web framework for .

## Tools & Programmes used
* microsoft word to making the wireframes.
* Chrome Developer Tools to sort out any bugs, size issue
* GitHub for storing the files and version control of the website.
* PostgreSQL .
* Amazon AWS used to store static files after deployment.
* Heroku a cloud platform for deploying my site
* W3C Markup Validation
* W3C CSS Validation Service for CSS
* JSHint to check the Javascript code.
* PEP8 checker to clean up the code

# Deployment
The site was building using Git and pushed to GitHub:
    git add .
    git commit -m "commit message"
    git push

Heroku was used for deployment

## Heroku :

1. Create a heroku app
* Log in to my Heroku account
* Create a new app and follow instuctions 

ScreenSHOT

* Using "resource" tab and add a postgres to the app
* Submit the form

2. Postgress Database:
* Install dj_database and psycopg2.
    pip3 install dj_database_url
    pip3 install psycopg2-binary
* Create requirement.txt file and freeze and add the databases to the file 
* Add the databases in sittings files 
* Scroll down to DATABASES, comment out the default configuration and add the database url from Heroku
DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
}
You can the database url from Heroku's Config Vars in the Settings tab.

* Run migration - python3 manage.py runmigrations
* Using tlocatl database loaddata db.json and import the categories 

3. Create a superuser form my admin panel
* Type: python3 manage.py createsuperuser
* Add a username and password

4. Local and remote database:
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

5. Installing gunicon - pip3 install gunicorn
6. Create Procfile and web: gunicorn boutique_crossfit.wsgi:application in the filer
7. Connect to heroku in the profile - I had to use the Heroku login -i with my credetials 
    * Temporarily disable the collection of static files
    * add the host mame in settings.py - ALLOWED_HOSTS = ['<heroku appname>.herokuapp.com', 'localhost']
    * commit to GitHub
    * commit to Heroku - heroku git:remote -a <Heroku appname>
    * push to Heroku - git push heroku





# Credits

## Code
1. The project is heavily based on the Code Institute walkthrough project 5 - 'Boutique Ado". 
The Code has been copied and adopted form the vidos provided

## Content
1. Product description have been taken from - https://www.amazon.co.uk/


## Media 
1. All the product images and descirptions - https://www.amazon.co.uk/
2. Main image - https://www.bing.com/images/


## Acknowledgements
* A big thank you to some of the very dedicated tutors who clearly love their job
* A thank you for all the advise I was able to search in Slack 

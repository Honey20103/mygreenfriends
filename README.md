<p align="center">
  <img src="https://github.com/Honey20103/mygreenfriends/blob/master/static/img/jpg.png" style="margin: 0;" >
</p>



[![Build Status](https://travis-ci.com/Honey20103/mygreenfriends.svg?branch=master)](https://travis-ci.com/Honey20103/mygreenfriends)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)


This is a place for every and all that want to be closer to the world of green. On this myGreenfriends e-commerce website I share plants, plantastic stories, info and tell one or two jokes. 
The e-commerce website is developed for the actual plants I have in my private home. The main goal of the website will provide users the ability to browse through different plants found in my home and have the ability to purchase them. This might scale into an actual plant store in the future.

The website will consist of a login page, a signup page and a main page displaying the plants available to buy. Once a product is added to the users cart, they will be able to purchase by entering delivery and payment details. User profile will allow the user to view a history of their purchases. Creating an account will allow customer to change their passwords and registered addresses, and also login with existing Google accounts. 

This website is built with Django Python Web Framework and Stripe (a payment processing platform) to provide a fully functional e-commerce website.

If you would like to test the payment functionality of this project, please use the following payment details:

Card number: 4242 4242 4242 4242
CVC: any 3 digit number
Expiration Date: Any future date



***

### Website

A live demo can be found [here](https://my-green-friends.herokuapp.com/)

***

## Table of Contents
  * [UX](#ux)
  * [User stories](#user-stories)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
    + [Database Schema](#database-schema)
    + [Surface](#surface)
  * [Technologies](#technologies)
    + [JavaScript Libraries](#javascript-libraries)
    + [Python & Django Plugins](#python---django-plugins)
  * [Features](#features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Admin login gave a 500 error](#admin-login-gave-a-500-error)
  * [Deployment](#deployment)
    + [Deploy requirements](#deploy-requirements)
    + [Local deployment](#local-deployment)
    + [Heroku deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)
    
## UX

### User stories
| User Story ID                  | As a     | I want to be able to…                                             | In order to …                                                                |
|--------------------------------|-------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Registration and User Accounts         |             |                                                                   |                                                                               |
| 1                              | Shopper & Site Guest    | Register for an account                                          | Have an account to view my current & past orders                                                       |
| 2                              | Shopper & Site Guest    | Login with Gmail Acc                                          | I'd like the flexibility to login with any account i.e Google                            |
| 3                              | Shopper & Site Guest      | Login and Logout                                              | Quickly and easily retrieve personal information image                                        |
| 4                              | Shopper & Site Guest      | Recover my password                                           | If I forget my password, Recover access to my account,                                                       |
| 5                              | Shopper & Site Guest      | Receive an email conformation  | Verify my registration was successful and receive info                                                          |
| 6                              | Shopper & Site Guest   | Have a personalized user profile                                  | To view my personal information such as payment information and order history |
| Site Navigation         |             |                                                                   |                                                                               |
| 7                              | Shopper     | View a list of plants                                           | Figure out what i want                                                         |
| 8                              | Shopper     | View plant details                                              | To view plant description and care info                                       |
| 9                              | Shopper     | View the cart details                                          | To manage my purchase                                                         |
| 10                              | Shopper     | Adjust the quantity of items in my cart or remove them | To manage my purchase                                                         |

| 11                              | Shopper     | View more pictures                                         | To see more pictures and realistic view                                                         |
| Purchasing and Checkout        |             |                                                                   |                                                                               |
| 12                             | Customer    | View plants in my cart to be purchased                              | Identify the plants and total cost before I checkout                        |
| 13                             | Customer    | Adjust the quantity or remove items in my cart                     | Easily make changes before checkout                                           |
| 14                             | Customer    | Enter my payment information                                      | Check out easily with no problems                                             |
| 15                             | Customer    | View an order confirmation after checkout                         | Verify there are no mistakes with my info                                   |

| Sorting and Filtering          |             |                                                                   |                                                                               |
| 16                             | Shopper     | Sort the list of plants                                         | I'd like the ability to sort by plant price, by name and by size                             |
| 17                             | Shopper     | Search for a plant by name or description                       | Quickly find the plant I am interested in by inserting it's name                                  |
| Plant Care          |             |                                                                   |                                                                               |
| 18                             | Shopper /Site Guest    | Get Plant tips & ideas                                         | By having a possible blog option p                             |
| 19                             | Shopper/ Site Guest     | Know more about the vision                       | By reading through blog posts                                  |





### Strategy
The overall strategy is for site guests or potential customers to be able to purchase my house plants and to set up a profile in order to view past orders, to save delivery and payment information with the possibility of returning to the website to purchase again. My goal in the design was to make it as easy as possible for users to view all the plants available and checkout as fast as possible, to have a clean look with no clutter or information overload by having a user-friendly and minimalistic design. The Homepage tells a story of what the site is about, and the logo which I had designed by a third party vendor on Fiverr makes it eyecatching, and helps visitors navigate to the plants by clicking the logo in the Nav bar. My backgroung overlays are specifically chosen to set the tone of the webiste mellow and planty, all downloaded from pexel, and plant uploads taken by myself and presets done in Lightroom Adobe. The Quicksand font sets the tone too, and so do the color themes mainly Green and white pallets.

### Scope
For customers, I want to provide them with an easy to understand and use tool. The idea is to have customers return ASAP and thus making things easier such like logging in with Google API, helping for a faster, quicker shopping experience. 

* The ability to reset passwords.
* Edit Cart by removing and updating chose plants in the checkout menu.
* Store personal shopping information and previous orders
* Ability to Create an account and store account in database
* Functionality to login and log out of user profile


### Skeleton

Initial wireframes were done on paper and pen, I'll probably at a later stage add a design made in Balsamic, it was a bit challenging to figure out how I wanted the UX to be, although my idea was to maintain a clean and minimalistic look, and easy to use. The look and feel are intentionally planned for mobile and desktop.

### Wireframes

[Home Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/homepage.png)

[Login Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/loginpage.png)

[Brew Log Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/logpage.png)

### Database Schema

In my development environment in Gitpod the SQLite3 DB was used, however in deploying to Heroku it uses Postgresql, the transition was smooth in terms of fieldsets and keys.
The structure of the products, cart and checkout apps were derived from Code institue study material.


Profiles app:
To store customer data such like delivery info.

| Name             | Database Key            | Field Type   | Validation                                       |
|------------------|-------------------------|--------------|--------------------------------------------------|
| Phone Number     | default_phone_number    | CharField    | max_length=20, null= True, blank =True           |
| Street Address  | default_street_address | CharField    | max_length=80, null= True, blank =True           |
| Town or City     | default_town_or_city    | CharField    | max_length=40, null= True, blank =True           |
| Postcode         | default_postcode        | CharField    | max_length=20, null= True, blank =True           |
| Country          | default_country         | CountryField | blank_label ='Country', null = True,  blank=True |
| user             | user                    | OneToOneField |                                                 |

Categories:
Purpose to segment plants into types or groups.

| Name          | Database Key  | Field Type | Validation/Requirements               |
|---------------|---------------|------------|---------------------------------------|
| Name          | name          | CharField  | max_length=200                        |
| Friendly Name | friendly_name | CharField  | max_length=200, null=True, blank=True |


Products app:
Displays all the plants in the store
| Name             | Database Key            | Field Type   | Validation                                       |
|------------------|-------------------------|--------------|--------------------------------------------------|
| Category         | default_category        | ForeignKey   | max_length=20, null= True, blank =True           |
| SKU              | default_sku             | CharField    | max_length=80, null= True, blank =True           |
| Name             | default_name            | CharField    | max_length=40, null= True, blank =True           |
| Description      | default_description     | TextField    | max_length=20, null= True, blank =True           |
| Care             | default_care            | CountryField | max_length=254, null=True, blank=True.           |
| Size             | default_size            | TextField    | max_digits=6, decimal_places=2                   |
| Price            | default_price           | DecimalField | max_digits=6, decimal_places=2                   |
| Image_url        | default_image_url       | URLField     | max_length=1024, null=True, blank=True           |
| Image            | default_care            | ImageField   | null=True, blank=True                            |

Extra to products app:
Displays all the plants in the store
| Name             | Database Key            | Field Type   | Validation                                       |
|------------------|-------------------------|--------------|--------------------------------------------------|
| product          | default_product         | ForeignKey   | 'Product', default=None, on_delete=models.CASCADE|
| images           | default_images          | ImageField   | upload_to = 'images/'                            |


Blog: 
Read up on what we are about and what sparks my interest

| Name           | Database Key   | Field Type     | Validation/Requirements                                                                      |
|----------------|----------------|----------------|----------------------------------------------------------------------------------------------|
| author         | User           | ForeignKey     | User, on_delete=models.CASCADE, null=False, blank=True                                       |
| title          | title          | CharField      | max_length=120, null=True, blank=False                                                       |
| subtitle       | subtitle       | CharField      | max_length=120, null=True, blank=False                                                       |
| body           | body           | SlugField      |                                                                                              |
| created_at     | created        | DateTimeField  | auto_now=True, null=False                                                                    |
| updated_at     |  updated       | DateTimeField  | auto_now=True, null=False                                                                    |
| status         | choices        | IntegerField   | blank=True, null=True, default=""                                                            |
| slug           | slug           | SlugField      | unique=True, max_length=250, default=None                                                    |


After creating the apps and their models, `` python manage.py makemigrations `` was run in the terminal to create the initial model package and `` python manage.py migrate `` was then used to apply the model to the database and create the table.

Throughout the development, I had adjusted fields were necessary.

### Surface
My idea for the design is to have colour relating to beer such as brown, gold, orange or essentially brown theme colour palette, this will help users associate with the act of beer brewing.

<img src="https://github.com/Honey20103/BrewMaster/blob/master/wireframes/themecolor1.png" style="margin: 0;" width="600" height="250" >




***

## Features

### Existing Features

* **User Accounts** - Signup for an account, log-in and log-out.
* **Log/Recipe page** - When a recipe or brew log is selected the user will be presented with the page for that recipe. 
* **Add Log/Recipe** - The user can go to the menu and open the add log brew day page, providing the user with a diary or digital like a notebook to log their brew day content and add them to the database.
* **Add Ingredient** - Ingredient options will be available however if an option is not found, the user can add a new ingredient to the database.
* **Edit & Delete ingredients** - Ability for the user to edit and delete ingredients.
* **Multiple users login** - Ability to have more profiles for multiple beer brewers to log their recipes.
* **View ther brewers logs** - Ability for brewers to unhide or unlock certain logs to be publicly visible to other brewers on the app.

### Future Features

- **Social sharing buttons**: Users will be able to share beer recipes to their social media channels via the social sharing buttons provided. 
- **Brew Images** Ability to add/update a log by adding an image or images of the final brew result.
- **Log order arrangement**List logs in dashboard according to date of brew and not when entered.
- **Rating system** - The ability to star rate favourite brew day recipe
- **Database per user login** -  Have separate DB for each user, prevent other users deleting or viewing logs

***

## Technologies Used

### Frontend

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Bootstrap](https://getbootstrap.com/)
* [Materialize](https://materializecss.com/)
* [Bulma](https://bulma.io/)


### Backend

* [Python](https://www.python.org/)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [MongoDB](https://www.mongodb.com/)
* [SQLite3](https://sqlite.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

### Deployed

* [Heroku](https://www.heroku.com/)

***

## Testing

#### Code Validation

#### Devices used to Test

The BrewMaster App was test with the following devices:

MacBook Pro Laptop
HP Pavilion Laptop
Samsung Galaxy S9 Mobile
iPhone XS Max

Google Chrome
Microsoft Edge
Mozilla Firefox

Experience for mobile devices when it pertains to the homepage was not responsive to section/column of the image.(FIXED)

#### User Story Testing

The full user story testing can be found [here](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/BrewMaster%20User%20Story%20Testing.pdf).

* Feedback from Users;
  - The add log form seemed to have been allowing creation of log with empty fields. (FIXED)
  - The datepicker doesn't require an entry to submit form. (Attempted to fix this with a js script however submit button becomes unfunctional, thus was unable to fix this issu, however Date field shows red if empty)

#### [Web Accessibility](https://www.webaccessibility.com/)

<img src="https://github.com/Honey20103/BrewMaster/blob/master/wireframes/webaccessibility.png" style="margin: 0;" >


#### Chrome Developer Tools and Gitpod vscode
Constantly used to ensure the app is mobile-first, and works well with all kinds of devices and provide real-time ability to identify errors in my HTML code, and helped me troubleshoot my HTML/CSS.

Gitpod terminal providing lint issues and problems when it comes to the different scripts/languages.

Further more for css testing I used this [site](http://csslint.net/) no errors found except warnings that informed that for IE6,IE7,IE8 I require fallback colors color: rgba(65, 48, 13, 0.959); I have made relevant changes to ommit this warning.

Used the DOM to detect how to properly fix issue with Fade in Overlay CSS hover effect not functioning well for mobile devices, and inserted necesarry media queries in CSS to fix the issue, the text now no longer overlaps the image background when size decreases.

[W3C CSS Validator](https://jigsaw.w3.org/) reported 14 errors.

HTML valid according to [site](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbrewmaster-app.herokuapp.com%2F)

#### Random User Testing
Sent the app to boyfriend and colleagues to use, collecting their feedback for bug fixes and adjustments.

#### Python Testing
I used [PEP8online](http://pep8online.com/) together with gitpod Problem tab to observe errors and warnings. At the moment errors have been fixed, only warnings exist naming the warning "line too long"

#### JS Testing
Test any javascript errors with jslint [site](http://www.jslint.com/) no error apart from lint warning and too long empty spaces, i've removed those.

#### MongoDB Testing

Test mongoDB connection with the command 'mongod'

```brew
gitpod /workspace/BrewMaster/homebrew_app $ mongod
2020-10-02T00:26:15.526+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] MongoDB starting : pid=58337 port=27017 dbpath=/data/db 64-bit host=ws-0567368c-beaf-4649-ab50-f1f1a84e5304
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] db version v4.0.20
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] git version: e2416422da84a0b63cde2397d60b521758b56d1b
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.1.1d  10 Sep 2019
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] modules: none
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] build environment:
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten]     distmod: ubuntu1804
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten]     distarch: x86_64
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2020-10-02T00:26:15.543+0000 I CONTROL  [initandlisten] 11444 MB of memory available to the process out of 60395 MB total system memory
```
mongod is the primary daemon process for the MongoDB system. It handles data requests, manages data access, and performs background management operations.

#### SQLite Testing
Two ways to test that when a user signed up they were stored in the database or it worked;
  - Used a sqlite database viewer to look at the row that was added to the table
  - I also tried signing up with the same email address again, and when I got an error, I knew the first email was saved properly, also it redirected me ssuccessfuly to the login page.

#### Known Bugs


#### Expected Behavior
* Burger menu in mobile view immediately displays nav menu without clicking the burger.(FIXED)

* Logo Image and favicon image will not load. (FIXED)

* JS for datepicker functionality will not initiate from static/js/script.js file, it only successfuly initiates js code is directly in base.html file.

* Fade in Overlay CSS hover effect not functioning well for mobile devices. (FIXED).

* ENV VARIABLES - Went above and beyond to create environmental variables for my secret keys and URI's, however all my attempted where rendered unsuccessful. Kept receiving *ValueError: You must specify a URI or set the MONGO_URI Flask config variable* despite all attempts to use correct methods of setting up with env.py and also via gitpod. Reached out for help on the CodeInstitute slack channel and Tutor assistance, tutor could not help figure it out, neither the channel could help. I've exhausted all attempts to try not to submit my project with visible private info.


***

## Deployment / Project Setup 

Download
```bash
git clone https://github.com/Honey20103/BrewMaster.git
cd homebrew_app
```

Install python3
```bash
#use brew
brew install python3
```

Install pip3
```bash
#use apt-get
sudo apt install python3-pip
```

Deploy virtual environment.
```bash
#use pip3
pip3 install virtualenv
virtualenv venv
source ./venv/bin/activiate
```

Install requirements
```bash 
# install python requirements
pip3 install -r requirements.txt
```
Deploy SQLite database
```python
# python3
from app import db, create_app
db.create_all(app=create_app())
```
Deploy Mongo database
```bash 
#Setup Mongo DB account [here](https://www.mongodb.com/)
Create a mongoDB database.
Create a collection in it: logs
```
In a terminal, you can set the FLASK_APP and FLASK_DEBUG values:
```bash
# these gives instrcution to flask on how to load the app, it should point to the folder that holds the __init__.py.
# or create .flaskenv file and add the below without 'export'cmd
export FLASK_APP=project
export FLASK_DEBUG=1
```
Run app locally
```bash
flask run
```

Deploy to Heroku

* Create a free account in [Heroku](https://signup.heroku.com/)
* Once logged in Click on "Create new app", provide an app name of your choice and preffered region where the server your app will be deployed on.
* Follow instruction [here](https://devcenter.heroku.com/articles/heroku-cli) on how to install the heroku cli on your device

* Back to your CLI and project directory:

Login (provide email address and password when prompted)
```bash
heroku login -i
```

Initialize a git repository in a new or existing directory
```bash
$ cd my-project/
$ git init
$ heroku git:remote -a your-app-name-goes-here
```

Deploy your app by committing your code to the repository and deploy it to Heroku using Git.
```bash
$ git add .
$ git commit -am "write a valuable commit message here"
$ git push heroku master
```
Observe the build process in your CLI python app is set, requirements.txt and procffle are found.

### App Link
When your build is successful your app would be deployed at similar [link:https://your-app-name.herokuapp.com/](https://brewmaster-app.herokuapp.com/) to this one.


***

## Credits

### Content
The content on the site is derived from my boyfriend's self-made beer brewing log manuscript book. 

### Code
[Hover CSS effect on homepage: ](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_overlay_fade) This package of CSS was used to render the behaviour of the homepage front image when hovering the image, to show the about of the app.

[Blueprints and configurations in application:](https://www.youtube.com/watch?v=Wfx4YBzg16s) This tutorial helped me use Application Factory, which allows to easily create multiple instances of the app with different configurations. The Blueprints restructuring split up my app into more manageable sections i.e Auth.py, main.py and _init_.py. 

[Authentication to App:](https://www.digitalocean.com/community/tutorials) Tutorial helped with setting up authentication to webapp.

### Media 

- The logo for the project was taken from the [pngtree](https://pngtree.com/) site. 

### Acknowledgements
- I was inspired to create this website from observing the struggles I watched my boyfriends encounter by trying to keep and maintain a manual notebook to store his brew day info or records, especially thankful for the help with testing functionality of the app. Thank you Robert Flink.

- I'd like to thank tutor Tim Nelson at CodeInstitute who helped unblock me when i was completely stuck and providing extra helpful resources.


<p align="center">
  <img src="https://github.com/Honey20103/BrewMaster/blob/master/homebrew_app/project/static/images/brewmaster2.png" style="margin: 0;" width="150" height="100">
</p>

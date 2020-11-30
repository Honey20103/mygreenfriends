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
  * [Features](#features)
    + [Existing Features](#exitsing-features)
    + [Future Features](#future-features)
  * [Technologies](#technologies)
  * [Testing](#testing)
  * [Bugs](#bugs)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Admin login gave a 500 error](#admin-login-gave-a-500-error)
  * [Deployment](#deployment)
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
| 10                              | Shopper     | Adjust the quantity of items in my cart or remove them | To manage my purchase                       |
| 11                              | Shopper     | View more pictures                                         | To see more pictures and realistic view    |
| Purchasing and Checkout        |             |                                                                   |                                                                               |
| 12                             | Customer    | View plants in my cart to be purchased                              | Identify the plants and total cost before checkout  |
| 13                             | Customer    | Adjust the quantity or remove items in my cart                     | Easily make changes before checkout   |
| 14                             | Customer    | Enter my payment information                                      | Check out easily with no problems        |
| 15                             | Customer    | View an order confirmation after checkout                         | Verify there are no mistakes with my info  |
| Sorting and Filtering          |             |                                                                   |                                              |
| 16                             | Shopper     | Sort the list of plants                                         | I'd like the ability to sort by plant price, by name and by size      |
| 17                             | Shopper     | Search for a plant by name or description                       | Quickly find the plant I am interested in by inserting it's name    |
| Plant Care          |             |                                                                   |                                                  |
| 18                             | Shopper /Site Guest    | Get Plant tips & ideas                                         | By having a possible blog option |
| 19                             | Shopper/ Site Guest     | Know more about the vision                       | By reading through blog posts              |





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

[Home Page](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/homepage.jpg)

[Login/Signup Page](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/login.jpg)

[Products Page ](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/productpage.jpg)

[Products Detail Page ](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/productdetail.jpg)

[Shopping Cart ](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/cart.jpg)

[Checkout Page ](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/checkout.jpg)

[Order confirmation Page ](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/orderconfirm.jpg)


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

My idea for the design is to have colour relating to plants and greenhouse kind of look. Chosen colours where  gold, orange or essentially brown theme colour palette, this will help users associate with the act of beer brewing.

<img src="https://github.com/Honey20103/mygreenfriends/blob/master/static/img/palletes.png" style="margin: 0;" width="600" height="250" >


***

## Features

### Existing Features

* **Profile page** - Allow the user to insert their billing/shipping information. If the user is logged in during checkout or when trying to fill out the contact form, their personal information will already be populated. On the profile page, the user will be able to view their past orders and click on them to once again view the order summary. The profile link in the navbar is only available to users who are logged in.
* **Login/Register page** - Created with Django- Allauth, the login and register has all of the standard features to create a new user. Styling was customized to make it unique. There are pages included to handle:
Sign up - requires username, email, password twice and an email will be sent with a verification link
Login - requires either username or email and password with a toast message confirming successfully signed in, includes Google login ability
Logout - Once completed logout, a toast message confirming successfully logged out
Forgot password - requires email and email will be sent to link to update password
* **Login with Google** OAuth login capabilities.
* **Products** - Shoppers can view all plants, or view by category, or view by sorting either price or naming. Ability to search for words found in plant names or descriptions.
* **Plant view** - The user/shopper has the ability to view more pictures if the product contains more pictures, and view care details
* **Cart** - Users can add or delete services to their cart which will be saved in the backend right away.
As a user logs out the cart will be remembered in the system to be finished later. 
When the customer checkout, a secured payment can be made with credit card is complete.
The main goal of the profile page is to allow the user to insert their billing/shipping information. If the user is logged in during checkout or when trying to fill out the contact form, their personal information will already be populated. On the profile page, the user will be able to view their past orders and click on them to once again view the order summary. The profile link in the navbar is only available to users who are logged in.
* **Blog** - Ability to view and readup on latest blogs organised in first created order.
* **Order confirmation page** - The Order Confirmation page has a heading at the top to thank the user for shopping on the site. Below the heading the user will get a message to let them know the order has been confirmed and that they will recieve an e-mail confirmation. The confitmaion has an unique order number and the date and time of the sale. Below this is all the order details which has the details of the product, delivery and the billing information.
The page has a button on the botton of the page which is keep shopping and that will bring the user back to the products page.
* **Checkout Page** - Forms containing user details and address, followed by payment information. If the user enters an incorrect card number they will be shown that they have entered an incorrect card number. But if the card number is correct they will be able to enter the details without any error notification.
Overview of order summary displaying the image, name, quantity, sub total, order total, delivery and grand total.

### Future Features

- **Add bidding functionality**: Users will now bid on plants that are on auction, bid end date will be set, and sold to highest bidder. 
- **Error Pages** Add custom 404/500 error messages
- **Email of confirmation order** After successfully ordering a product, email confirmation is sent for order to the user's email
- **Blog system** Allow guests to add comments a blog post, and like buttons
- **Delivery Tracking** -  Product Delivery tracking system, basically a small system that has some statuses like IN_TRANSIT, DELIVERED, RETURNED etc for the status of the delivery.


## Technologies
 - GitHub Wiki TOC generator - *Generates a MarkDown TOC online*
 - HTML - *To create the basics*
 - CSS - *To improve placements and design*
 - JavaScript - *The engine to create user interaction*
 - Python - *Programming language*
 - Postgresql - *Opensource database to save the transactions, profile, and orders*
 - Django - *Web framework in python*
 - Bootstrap - *To make the design responsive*
 - Font Awesome - *Easy icon access for the icons*

### Python & Django Libraries
 - pillow - *Python Imaging Library*
 - Stripe - *Credit card payments and transaction security*
 - boto3 - *To connect to AWS*
 - django-allauth - *Authentication, registration & account management*
 - django-countries - *Provides country choices for use with forms*
 - django-phonenumber-field - *A Django library which interfaces with python-phonenumbers to validate*
 - django-crispy-forms - *Controls the rendering behaviour of Django forms*
 - django-filter - *Easy searching and filtering query sets*
 - oauthlib - *Allow OAuth with social accounts*

### JavaScript Libraries
 - Stripe - *For credit card transactions*
 - jQuery - *To improve input field feedback*


### Deployed

* [Heroku](https://www.heroku.com/)

***

## Testing

#### Code Validation

#### Devices used to Test

The myGreenfriends website was tested with the following devices:

MacBook Pro Laptop
HP Pavilion Laptop
Samsung Galaxy S9 Mobile
Lenovo Thinkpad, Chromium
iPhone XS Max

Google Chrome
Microsoft Edge
Mozilla Firefox

Experience for mobile devices could not view the bottom of carts due to overlapping footer.(FIXED)

#### Manual Testing 

Please visit the manual testing file [here](TEST.md).

* Feedback from Users;
  - The add log form seemed to have been allowing creation of log with empty fields. (FIXED)
  - [More feedback](https://github.com/Honey20103/mygreenfriends/blob/master/wireframes/Mygreenfriends%20user%20feedback.pdf)

#### [Web Accessibility](https://www.webaccessibility.com/)

<img src="https://github.com/Honey20103/mygreenfriends/blob/master/static/img/accessibility.png" style="margin: 0;" >

Avoid use of placeholder values to label or explain input
Severity: 8
A placeholder attribute should not be used as a label. The placeholder is a short hint intended to aid the user with data entry. The placeholder may not be available to assistive technology and thus may not be relied upon to convey an accessible name or description -- it acts similar to fallback content.


#### Chrome Developer Tools and Gitpod vscode
Constantly used to ensure the app is mobile-first, and works well with all kinds of devices and provide real-time ability to identify errors in my HTML code, and helped me troubleshoot my HTML/CSS.

Gitpod terminal providing lint issues and problems when it comes to the different scripts/languages.

Further more for css testing I used this [site](http://csslint.net/) reported 1 errors. (fixed)

Used the DOM to detect how to properly fix issue with Fade in Overlay CSS hover effect not functioning well for mobile devices, and inserted necesarry media queries in CSS to fix the issue, the text now no longer overlaps the image background when size decreases.

[W3C CSS Validator](https://jigsaw.w3.org/) reported 6 errors and several warnings.

HTML valid according to [site](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-green-friends.herokuapp.com%2F)

#### Random User Testing
Sent to friends, family and collegues fro the manual testing.

#### Python Testing
I used [PEP8online](http://pep8online.com/) together with gitpod Problem tab to observe errors and warnings. At the moment errors have been fixed, only warnings exist naming the warning "line too long"

#### Other testings
The following tests have been used to ensure proper site functionality:

- [GTmetrix](https://gtmetrix.com/): To test on website loading times.
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB): Inspecting on overflow errors.
- [JSHint](https://jshint.com/): A static code analysis tool for JavaScript.
- [Gitpod](https://gitpod.io/): Using the built-in tools to test on proper code, like flake8 linter.
- [Travis](https://travis-ci.org/): from the start of the project to ensure commits where good.


#### SQLite Testing
Two ways to test that when a user signed up they were stored in the database or it worked;
  - Used a sqlite database viewer to look at the row that was added to the table


#### Known Bugs
- Stopped code refactoring due to many errors and bugs it was causing with webhooks etc.

#### Expected Behavior
* Email confirmation not being received by end users.(FIXED)

* webhook specific payment_success_intent failing after code refactoring


***

## Deployment 

This project was developed using the GitPod (https://gitpod.io/).
In GitHub the repository is (https://github.com/Honey20103/mygreenfriends). 

Below is the way to deploy the files to Github:
1. Log into GitHub. 
2. From the list of repositories on the screen, select ‘Honey20103/mygreenfriends’
3. From the menu items near the top of the page, select ‘Settings’.
4. Scroll down to the ‘GitHub Pages’ section.
5. Under ‘Source’ click the drop-down menu labelled ‘None’ and select ‘Master Branch’


Below is the way to deploy the files to Heroku:
1. From by GitPod terminal log into my Heroku account by typing in 'heroku login' and press return .
2. I then press any key on the keyboard to continue and it will log me into my heroku account.
3. In GitPod terminal I push the files to Heroku by typing in 'git push heroku master'.
4. From heroku I click on my project which is 'poster-king'.
5. I then click on Deploy which is a tab along the top.
6. From this page I scroll down to the bottom and click on 'Deploy Branch' and make sure 'master' is selected.
7. After this is then lets me know it is seccessfully deployed and can be found at (https://my-green-friends.herokuapp.com/).


### Heroku up Heroku
To deploy the project to Heroku, follow the steps above in "Local Deployment", then complere the following steps:

1. Register/sign in for Heroku.[Heroku](https://www.heroku.com/) 
2. Once signed in, click the "new" button on the dashboard to create a new application.
3. Name the App and choose the region you are currently in. to set up an app 'myGreenfriends'
4. To use the Postgres database for deployment, select 'Heroku Postgres' as a free add-on.
5. After the app is created, go to the 'Settings' tab and click on the 'Reveal Config Variables' button. Input the following values:

| Key               | Value                                   |
|-------------------|-----------------------------------------|
| DATABASE_URL      | Heroku Postgres database url            |
| SECRET_KEY        | secret key used for your Django project |
| STRIPE_PUBLIC_KEY | obtained through your Stripe account    |
| STRIPE_SECRET_KEY | obtained through your Stripe account    |
| STRIPE_WH_SECRET  | obtained through your Stripe account    |
| ADMINS_EMAIL      | email admin for the emails feature      |

6. Create a requirements.txt file in your gitpod terminal/
        
        pip3 freeze --local > requirements.txt

7. Create a Procfile with the following content
        
        echo web: gunicorn mug_shots.wsgi:application > Procfile

8. Set up the database with Postgres.
        
        python3 manage.py makemigrations
        python3 manage.py migrate
        python3 manage.py loaddata products
        python3 manage.py loaddata categories

9. Create a Superuser for your project to work as an admin. Add the following command to the terminal, then create username and password for the superuser.
        
        python3 manage.py createsuperuser
        python3 manage.py loaddata blog

10. You can now run the cloned application to test it using the following command:
        
        python3 manage.py runserver

11. Commit these changes to your repository:
  
        git add .
        git commit -m "<your commit message here>"

12. With these changes made and commited in gitpod, log into heroku and enter your login credentials.
        
        heroku login -i

13. Once you have successfully logged into Heroku from the terminal, link your Heroku app to your remote repository
        
        heroku git:remote -a <your app name here>

14. Finally, push the project to Heroku

        git push heroku master

##### Hosting media files with AWS
The static files and media files for this project are currently hosted in an AWS S3 Bucket. To host them, you need to create an AWS account and create your S3 bucket, making sure to allow public access.
After creating an account and uploading the files, the following environment variables should be added via the settings or .env file.
        
        USE_AWS (set to True)
        AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY

##### Sending Emails with Gmail
In order to send real emails from the website, you must connect it to a Gmail account. 
Either use an existing Gmail account or create a new one, then sign in and navigate to the Google Account Security page. From here, create two-step authentication by creating an App password for a Django app. 
Add the following environment variables to your settings or .env file.
       
        EMAIL_HOST_USER
        EMAIL_HOST_PASS

Finally add Google API key in django admin under Social Applications for the Google login to function


### App Link
When your build is successful your app would be deployed at similar [link:https://your-app-name.herokuapp.com/](https://brewmaster-app.herokuapp.com/) to this one.


***

## Credits

### Content
All text content for this system were written by me and product pictures of my home plants.

### Media
Background overlays images from: https://www.pexels.com/

### Acknowledgements
- Multiple images on products [link](https://bookmarkinglists.com/how-to-upload-multiple-images-in-django/unsplashed)
- Admin nested inline help [link](https://stackoverflow.com/questions/14308050/django-admin-nested-inline)
- W3schools.com [link](https://www.w3schools.com/)
- Django 3.0 documentation [link](https://docs.djangoproject.com/en/3.0/)
- How to handles names for blogs [link](https://stackoverflow.com/questions/12340789/split-first-name-and-last-name-using-javascript)
- control date templates [link](https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-the-view-and-template-in-django)
- How to Authenitcate using Google [link](https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-https://www.youtube.com/watch?v=NG48CLLsb1A)


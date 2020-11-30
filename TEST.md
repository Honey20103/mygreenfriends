
# Manual Testing Checks

## Test Navbar :white_check_mark:

### General Functionalities :white_check_mark:

1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com)
3. Click every nav item

### Logged in and non-logged in users see different options :white_check_mark:

1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Check if navbar contains  
   Different Categories 
   Blog   
   Userplaccount-icon  
   Cart-icon  
   Search-icon  
4. Click Userprofile-icon and login with 
5. Check that navbar icons changed and the follow are present  
   Useraccount-icon  
   Cart-icon  
   Search-icon  

### Searchbar opens below nav when search icon is clicked :white_check_mark:

1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click Search-icon
5. Searchbar should open below nav

##  Footer :white_check_mark:

1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Scroll to bottom



##  Shop 

### Shop Categories :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Check that products are displayed and the page title shows the Category


### Sort Products  :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOw
4. Click Desert or Rainforest or Low Maintenance Categories
5. Toggle the Sort switch through all options and check that sorting works accordingly  
    ...Featured Products :white_check_mark:  
    ...Price :white_check_mark:
    ...Size :white_check_mark:  
    ...Name :white_check_mark:  

    
### Check Product extra images :white_check_mark:
1. Open Browser
2. Navigate to [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOw
4. Click on any plant
5. Click on 'Original pic' ensure viewing or carousel

### Non-logged-in user: Get Product Details :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click on LOW MAINTENANCE
5. Choose any product by clicking the image
6. New page should open
7. Page should contain  
   Product image  
   Descripton  
   Size info
   Add to Cart Button  
   Care information  
   Delivery Information

### Logged-in-user: Get Stored user info & past orders Details :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Login with your account
4. Click on SHOP
5. Under my profile
5. View order history and saved delivery settings


##  Cart :white_check_mark:

### Check empty Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on Cart-Icon
4. Placeholder "Your Cart is empty" should be displayed

### Add item to Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Chosen Product should be inside the cart view

### Open Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP
4. Click any category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open

### Add more than 1 item to Cart and check Position :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Continue shopping by clicking on the grey overlay or on to the Close button in the top right
9. Cart should Close
10. Choose another product
11. Add Item to Cart
12. Side Drawer Cart should and last added item should be on top

### Checkout from Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press Checkout Button
9. Checkout Page should open

### Checkout from Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open
10. Press Checkout Button
11. Checkout Page should open

### Increase Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "+" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be increased by 1

### Decrease Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "-" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be decreased by 1

### Remove Item(s) in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "Remove" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Product should be removed from Cart

### Increase Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "+" Button
11. Page should be reloaded and quantity increased by one

### Decrease Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP NOW
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "-" Button
11. Page should be reloaded and quantity decreased by one

### Remove Item(s) in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "x" Button
11. Page should be reloaded and item should be removed from cart
12. And view page should show "Your cart is empty" Continue shopping.

## Checkout :white_check_mark:

### Checkout AnonymousUser :white_check_mark:\:beetle:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click on SHOP
4. Click any Category
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click Checkout-Button
9. Should be redirected to checkout page
10. Form for address details & Order Summary should be displayed
11. Fill in form & use test credit card (4242 4242 4242 4242)
12. Submit orderv
13. Loading animation should be displayed
14. Checkout success page should be shown

### Checkout registered user (3 :white_check_mark: / 1 :beetle:)

1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click Userprofile-icon and login with puffin1@byom.de pw: testuser1
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
6. Choose any product by clicking the image
7. Add Item to Cart
8. Side Drawer Cart should open
9. Click Checkout-Button
10. Should be redirected to checkout page
10. Form for address details should be prefilled & Order Summary should be displayed
11. add test credit card (4242 4242 4242 4242)
12. Submit order
13. Loading animation should be displayed (BUGGY)
14. Checkout success page should be shown

##  Sign Up :white_check_mark:

### Sign Up :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Click MyPlaccount Icon
4. Choose Sign Ups
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 11. Registered Users: Useraccount :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click MyPlaccount Icon and login with 
4. Click on MyPlaccount Icon
5. Should see Form 
6. Should see Order History

### View Blog :white_check_mark:
1. Open Browser
2. Open [myGreenfriends](https://my-green-friends.herokuapp.com/)
3. Login with 
4. Click on SHOP
5. Click on BLOG icon
5. View listed blog posts
6. Click any blog
7. Return to main blog page






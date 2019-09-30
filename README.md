# A Bad Cookbook

This is a project to made using django to allow comics to be viewed and bought and commitiond to be requested.
This is an update of anouther poject also made by me that can be seen [here](http://akiroteacomics.com/)

## UX I used a basic mockup to guide how i built this project.

mockup of homepage 

![mockup of homepage ](https://imgur.com/ZMJppAu)

The homepage staded mostly the same as the mockup. The hire link in the header was made bold and underlined for an obvious call to action for anyone who wants a commition.
There are large links to all the ongoing work by the artist on the homepage as well as links to social media in the navbar and footer allowing easy access to any content by the artist. 

mockup of about page

![mockup of about ](https://imgur.com/q2LbbPq)

The about page is just a simple page to provide adional information about the artist.

mockup of hire page

![mockup of hire ](https://imgur.com/kHwu3kX)

The hire page was changed significantly from the original design. it was changed to a form that can be filled
in. this then give the user feedback about how much this work will cost as well as sending an email with all the details 
to the artist. This makes sure the artist gets all the information they need and make the prosess easier and
simpler for the user.

The shop page

the shop was originaly handled by gumroad but is now handled on the website. 

## Features

### existing features

commition form - by having users fill out a form users can commiton art to easily send a message to the artist and get an estimate of the cost. sends an email to the artist with all the relevent details

shop - users can push a button to add item to cart

cart - users can push adjust cart button to edit the items they are buying or by pushing the checkout button they can go to the checkout

checkout - a form allows users to to imput details and purchace products.




## Technologies Used

JQuery - The project uses JQuery to simplify DOM manipulation.

Bootstrap - To easily get the foundations of the design in place.

django - To handle routing on the site and backend.

Stripe - to easily manage card payments


## Testing

All links on the page have been tested and work.

All forms have been tested. shop form is currenly giving error 

stripe is currenly giving error {
"error": {
"message": "You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/.",
"type": "invalid_request_error"
}
when working with enviroment variable but works correctly when not
more work needed to fix this bug, contacted tutor support and got no response

register forms has been tested and is working correctly/

login form currntly not working and can currently only log in through https://comic-project-django.herokuapp.com/admin

loginrequired has been commented out on checkout views for testing
and login/register links have been commented out as are not adding anything to this project at this time

a css validator was used and found no errors (https://validator.w3.org/)

Some automated testing a has been done on views and models. 

Commition form is working correctly


## Deployment

Website is deployed through Heroku pages https://comic-project-django.herokuapp.com/

## how to deploy locally

the following must be installed

pip python 3 Git

Save the project locally or use the git clone command to clone this project. install all the reqirements using "pip -r requirements.txt"

update all envirn variable to your details

install gunicorn though heroku and get enviroment variable

get api keys from stripe and update enviroment variable. 

update email and password enviroment variable and 

## Credits

checkout, cart, shop and login app are edited vertions of ecomers app by code institute.
 
all images belong to akirotea 
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

All forms hove been tested to add recipies. all forms work and are easy to follow. When a name that is already being used is entered the correct error is displayed. when nothing is entered the correct error is also displayed.

All forms have been tested to edit the recipie and all work correctly.

a css validator was used and found no errors (https://validator.w3.org/)

a bug was found in the routing for edit methourd. the routing was updated.

a bug was found in the javascript for the search bars on the homepage, show and hide were the wrong way round.

A bug was found when editing the recipie name, when the name was updated it removed the rest of the recipie. this was fixed by using $set so it only updated that part of the recipie.

## Deployment

Website is deployed through Heroku pages https://recipes-data-project.herokuapp.com/

## how to deploy locally

the following must be installed

pip python 3 Git

Save the project locally or use the git clone command to clone this project. install all the reqirements using "pip -r requirements.txt"

set up a mongoDB account and a databace named recipes (if you do not want the databace named recipies you will need to update line 16 in recipies.py "recipes = mongo.db.recipes")

update line 11 of recipes.py "app.config["MONGO_URI"] = 'your mongodb Connection String goes here'" or you can update the enviroment variables in your IDE.

Credits
 
all images belong to akirotea 
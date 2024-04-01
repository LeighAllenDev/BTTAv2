# Back To The Arcade Again!

### Code Institute Portfolio Project 04

## Site Overview

![Am I Responsive](/static/images/readme/AmIResponsive.png)

This is a revised version of my first project with added features to utilise the skills I have developed since partaking in that project.

While the original **[Back To The Arcade]** site primarily used the **Front-end** and was built solely with **HTML** and **CSS**, this version utilises the **Full-Stack** using the following **languages and frameworks:
* **HTML5**
* **CSS**
* **JavaScript**
* **Python3**
* **Django**
* **Bootstrap**

The bulk of the project is built with Django which is a Python Framework.

The project focuses on a fictional retro arcade based in Brighton that offers customers a nostalgic experience with classic and modern arcade games as well as a selection of modern consoles, it also has an in house food hall. The aim of the site is to give users an overview of all the available services, users are also able to login to their accounts, and register new accounts, to book their visits in advance. 

## Table of Contents
1. [Site Overview](#site-overview)
2. [Planning Phase](#planning-phase)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
    * [Site Aims](#site-aims)
    * [Design](#design)
3. [Features](#features)
    * [Common Features](#features-common-across-all-sites)
    * [Front End](#front-end-for-the-user)
    * [Back End](#back-end-for-the-site-admin)
4. [Future Enhancements](#future-enhancements)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Tech](#tech)



## Planning Phase

### Target Audience
The target audience for this project is anyone interested in Retro games, classic arcade machines and modern gaming, whether you’re into console gaming or tabletop gaming. 

This arcade offers a friendly welcoming environment for all the family. We also have a wide range of food and customisable bundles available to make the most of your visit.

### User Stories
During the research phase of this project I asked a selection of potential users and site admins what functionality they wanted to get out of this site, my findings were then put in the form of issues on the project to work with. The following are my findings:

#### Account Registration
As a **Site User** I can **register an account** so that I can **book multiple visits**
1. *The customer can provide an email address to register an account*
2. *The user is able to log in to there account*
3. *When they are logged in they can book as many visits as they like.*

#### Bundle Selection
As a **Site User** I can **pick my own bundle** so that I can **plan my visit**
1. *Once logged in the customer can choose a bundle*
2. *They can choose their own options for food drinks and times*
3. *They can tailor the experience to their needs*

#### Edit/Delete a Bundle
As a **Site User** I can **edit my bundle** so that I can **change it if my plans change**
1. *I can view my bundle in my account*
2. *I can edit my bundle by changing my selections*
3. *I can cancel my bundle if required*

#### Approve Bookings
As a **Site Admin** I can **approve bookings** so that I can **control the footfall of the arcade**
1. *I can approve or decline bookings if its too busy on the chosen day*
2. *I can alert users if their bookings need to be amended*

#### Site Navigation
As a **Site User** I can **easily navigate the site** so that I can **make the most of its features and functionality**
1. *I can use the navigation menu to find my way around the site*
2. *I can make the most of the site so that I know what I’m booking*

#### Login Status
As a **Site User / Admin** I can **see my login status** so that I **know whether I’ve logged in or not**
1. *A logged in user will see their name on the navigation bar*
2. *If not logged in, there will be “login” and “register” buttons*

### Site Aims
The site aims to give users all the required information about the arcade in a professional and stylish way, allowing users to easily navigate between the pages to view even more content.

The improvements of this site over the original project also allow the user to create an account, make bookings for the arcade while also allowing them to view, edit and delete their existing bookings.

The backend for this project also allows site admins to add, edit and remove items from the menu and bundle tables as well as giving the ability to view, approve and delete users bookings. This site implements full C.R.U.D functionality.

### Design
The colour scheme for this project resembles that of my original #**BackToTheArcade** site. This comprises of a black background across all pages, Orange headers and logos, and white text to stand out over the opposing black background. This in-turn helps with accessibility making everything easier to read as well as causing less strain on the eyes while also being more efficient for battery life on mobile devices.

The specific colors used are:

- Black.. insert colour codes here
- Orange..
- White
- Navbar color

For this project I’ve chosen the font (font-name) as it has a retro feel but like the aesthetic of the arcade, It’s the kind of font that gives off nostalgia for the target audience and is eye catching within the project.

## Features

### Features common across all sites

#### Navigation

![Nav bar design](/static/images/readme/nav-log.png)

The site utilizes a fixed universal navigation bar that clearly outlines the sections of the site and is responsive so it transforms into a dropdown list on smaller screens while spanning the top of the page on larger devices. The logo is also across every page so users always know what site they are on. The nav bar indicates which page the user is on every time they click to a new page.

![login status](/static/images/readme/loginstatus.png)

The navbar updates based on a users login status, if the user is not logged in there are two additional links to allow users to either register or login to their account. When a user has logged in, these links will be hidden as their is no need for them to be displayed. The Navbar will also display a message to the user when they are logged in. (insert image here). 


![login or register](/static/images/readme/register.png)


**Headers and hero images**

Each page utilizes a similar layout with the main headers for each page over a hero image. I have designed it this way to replicate the original project, give the page a little colour and make everything pop a little more. This makes the site more aesthetically pleasing and draws the users attention to see exactly what each page is displaying.

**Main Content**

The main content for each page of the site is displayed to be eye-catching and stand out to the user below the hero images. The content is clearly labeled and easy to read.

**Footer**

The **footer element** displays the same content across all pages and it’s designed to be very minimalist as to not take attention away from the main content. Its a basic footer, sharing the same colour as the header, with links to popular social networks. These links open as empty tabs by default.

### Front-End for the User

**Registration and login**

The site gives a user the ability to register for an account which then gives them the ability to make bookings. Once they have an account they are able to log in with the same account and (hopefully) view and manage bookings within their account page.

The login, signup and logout templates are all taken from all-auth which is a Django/Python framework, they have then been customized to match the overall layout of the site. They are laid out to be easy to read and make the sign in process simple for all users.

**Menu and Bundles**

The menu and bundles pages are displayed to the user as a series of tables split into categories, these categories are also used in the booking form. The tables are laid out so they are easy to read and their colours also match the style of the site. This page only has the hero image and the tables so users don’t get distracted by too much going on when its really only to outline the menu options.

**Booking Form**

If a user is not logged into an account, the booking form page will simply advise them that they need to either login or register in order to book a visit. It provides links to take the user to the existing login or registration pages. Once the user has successfully created an account or logged in they are greeted with the booking form.

The booking form allows users to pick a bundle and and choose a date of time for their visit. It has functions in place to make sure the user cannot book for the same day, and only during the opening times of 9:00 and 22:00.

### Back-End for the Site Admin

The admin page that is built into **Django** gives site admin users more features than those of which seen by users on the front-end. Admins have the ability to edit items across site in the following ways:

**Menu Items** - Admins are able to add and remove menu items as well size options, they can also increase or decrease the price and change which category they belong to and these changes will be updated in real time on the website. This would be useful if a particular item was out of stock in the restaurant. 

**Categories** - Admins are Add and remove categories, as well as change the token costs for each category, these would also be linked in real time to the bundles and booking system.

**Bundles** - Admins are able to manage what items and categories are included in bundles as well as viewing and deleting the bundles.

**Users** - Admins are able to view all users and previous bookings, while maintaining the security of the user and not revealing any passwords. 

**Bookings** - Admins are able to view (and approve) users bookings ahead of the booking date, as well as notifying users of cancellations and verified bookings.

## Future Enhancements

This project is an improved version of my first project with *Code Institute*, Having said that there are still some future enhancements I would like to add.

The booking form is a very basic version of what I intended to do. The plan with this form was to allow the user to choose their menu items as part of the booking process, but this involved a dynamic JAvaScript form to calculate the tokens available - the token cost of each item, and tldr, I couldn't get that working as intended so it is being put on the backburner for now.

Another enhancement would be for the user to get an email or notification once their booking slot had been approved or rejected by the Arcade. This wouldn't be too hard to implement as admins already have the ability to approve bookings.

## Bugs
There are as few known bugs/issues with my project, these are mostly things that I'm sure I could fix with more time or research, and a the majority of them are just asthetics.

**The Footer** - The footer element doesn't show as intended, all the styling is there but the icons show as blue rather than white and they are positioned incorrectly. This is not a major problem as all the icons function correctly and link to the proper sites, opening blnak tabs as they should.

**Signup/Login Pages** - these pages dont follow the styling of the rest of the site, and I can't, for the life of me work out why my css for them won't style the properties correctly, this is resulting in the main headers being partially hidden by the nav bar. Again this is mostly a design issue and the page forms work exactly as intended. 

**Booking form** - The booking form is meant to let the customer choose a bundle, display the total amount of food/drink tokens available within the bundle and dynamically update to display more food options based on the remaining tokens. There seems to be an issue with my JS code so the form doesn't count down the tokens or give extra fields for food items. So as a fix, I have simplified the booking form to only need the bundle name, time and date.

## Testing

During this project I have done extensive manual testing, and relied heavily chrome developer tools and the built-in Django debugging mode. Stack-overflow has also been invaluable to this project. 

Responsiveness for the templates has been tested extensively with Chrome Developer tools, allowing me to see how the project would look on a selection of screen sizes. This also helped me with trying to style the majority of the project.

Testing the database was mainly achieved in the django admin panel as this will show when I've created models. It took 2 databases to make this project as the first one stopped updating when migrating changes. It was also essential that I remembered to make migrations when I made changes to the database.

Updates to the database happen when adding items to the menu or the bundles, a user registering on the site, or a booking form being completed. To test all of these features, I made a number of test users, added a lot of items to the menus and bundles tables, checking the live site after each addition to make sure it updated. 

I tested the booking form extensively to make sure it would update on the database correctly. This involved filling in the form, submitting it, seeing the error message display, resolving the error message, filling in the form, submitting the form, then checking the admin panel. To start with the food items werent displaying in the admin, and the tokens werent counting, so after removing the food choice options and reconfiguring the models, eventually the bundles were showing up as they should.

The Django built in debug mode shows an error message when something doesn't line up in the code, it also provides the line and area that is throwing an error, then it's just a case of trying to fix the code until the site loads. 

The majority of my testing was to repeat the same processes several times until they worked as expected.

## Deployment

As this project is built primarily with Django, a Python Framework, it is deployed to a hosting platform that is capable of displaying such projects. For the deployment I used Heroku.com. To deploy the project onto Heroku I used the following process:

1. Log in to **Heroku**
2. On the top of the **Dashboard** page, click the **New** button
3. Select the **Create New App** option in the dropdown menu
4. Choose a unique name for the project, I went with **BTTAv2** to match my GitHub repository
5. Next, select a Region for the app then click the **Create App** button
6. From the **Deploy** page, and click on **Settings**
7. After scrolling down the page a bit, click on **Convig Vars** and select *Reveal Convig Vars.*
8. In the *Convig Vars* set the **Database url** and the **secret key** for the project, this is crucial for the *running of the database* within the **Heroku** platform
9. Head back over to the **Deploy** tab and select **GitHub** as the deployment method
10. Search for the correct repository and click the **Deploy** button at the bottom of the page.

## Tech

This project is built with a vast array of tech, different software, languages, frameworks all contribute to the outcome of this project. A detailed list of these can be found below:

### Languages

- **HTML** - Hypertext Markup Language, used for the base code for each of the website pages.
- **CSS** - Cascading Style Sheets, used to customize aspects of the website
- **JavaScript** - This language was used for the dynamically updating form
- **jQuer**y - Used in conjunction with JavaScript
- **Python3** - The base of the project
- **SQL** - Used for managing the database

### Frameworks

- **Django** - A Python Framework that is used for the entire project
- **Bootstrap 5** - This is a CSS based framework, used for styling and customizing the web pages.
- **AllAuth** - A Python framework used to enable secure logins to the sites.

### Software

During the development of this project I’ve used a variety software to make this project a reality. Some examples are as follows:

- **GitHub**
- **Heroku**
- **GitPod IDE**
- **Cloud Anywhere IDE**
- **VS Code IDE**
- **Chrome Developer Tools**

### Extras

During the development and testing of this site I was able to use a number of devices to test the responsiveness of the site, these include:

- Macbook Air 13”
- Mac Mini connected to a 23” monitor
- iPhone 14 Pro
- iPad Air 4th Gen
- Moto G62

## Credits
I would like to give an honorable mention to my mentor, Richard Wells, as hes been a great help to me during this and every project I've done with Code Institute so far.

### Text Content
The majority of the text content for this site was taken directly from my orginal BackToTheArcade project as this is just a more refined version with additional features.

The font is Exo 2, taken from Google Fonts.

### Media
Every picture in this project, other than the logo designed by myself, was hosted on Pexels.com, a stock image hosting site. 

The artists are Cottonbro studio, Francesco Ungaro and Mikhail Nilov.



## Login
As an unauthorized user, I want to be able to login to the website via a form, so that I can access my private information.

### Questions
* Will the user enter a username or an email address to login?
    * User will login via email and password
* What routes should we use for login?
    * User will login via "/" homepage or through the login modal via a profile button
* Where should the user be redirected after login?
    * User will be redirected to the ‘/’ homepage
* What happens if the user enters the wrong password?
    * Display the message Invalid Login.
* Should logging in use session-based or use token-based authentication?
    * We will use session based authentication for now

### ### Acceptance Criteria
* When I try to fill out the form with an invalid email or password combination and press Enter or press the "Login" button
    * Then at the bottom of the form, the user will be prompted a message explaining the error
* When I try to fill out the form with a valid email and password and press Enter or press the "Login" button
    * Then I will be directed to my home page

## Logout
As an authorized user, I want to be able to log out of the website by clicking a button in order to end my current session.

### Questions
* Where will the user who logs out be redirected?
    * A logged out user will be redirected to "/" homepage.
* When will the user be able to access website features?
    * As soon as the user either logs in or registers.
* How will the user know they are logged out after clicking the logout button?
    * The homepage will display a login button and contribution features will be disabled.

### Acceptance Criteria
* Given that I'm a logged-out user and
    * When I'm on the / route
    * Then there will be a login and signup button that will redirect to the respective form

## Signup
As an unauthorized user, I want to be able to sign up for the website via a signup form, so that I can access the website.

### Questions
* What features are accessible to a user who is not logged in?
    * The user will have access to view the site but will be blocked from creating a sip, writing/editing/deleting a comment, and rating coffees
* Will the user enter a username and an email address to signup?
    * Yes, the user will enter both.
* Will we confirm their password during sign up?
    * Yes, their passwords will need to match
* What routes should we use for signup?
    * The sign up form will appear in a modal
* Where should the user be redirected after signup?
    * The user will be redirected to / the homepage
* What happens if the user with the username or email already exists?
    * The user will be given a message explaining the username or email is already in use
* What happens if the user enters the wrong password confirmation?
    * The user will be prompted a message explaining the passwords do not match

### Acceptance Criteria
* Given that I'm a user who has not yet signed up and
    * When I'm on the / route
    * Then there will be a signup button that open a modal with a form with an email, username, and password field and a "Sign Up" button to submit the form.
* When I try to fill out the form with an email or username that already exists with a valid password and press Enter or press the "Sign Up" button
    * Then at the bottom of the form, I will see a message “User with that email or username already exists”.
* When I try to fill out the form with a valid email, username, and password and press Enter or press the "Sign Up" button
    * Then I will be redirected to the homepage at the / route.
* Given that I am a user that just signed up
    * When I refresh the homepage at the / route
    * Then I will still be logged in

## Demo User
As a first-time user who just wants to demo Brewd, I want to be able to try out the site with a demo user login via a single button click on the login form, so that I can access the site without having to go through the trouble of creating a new account.

### Questions
* What features will the demo-user be able to access?
    * The demo-user will have access to everything. Their inputs will be posted as demo-user.

### Acceptance Criteria
* When the Demo user tries to "sip" a coffee
    * Then a sip, comment, rating, and location are entered into the database

## The Coffee House Feed
As an authorized user, I want to be able to see sips with reviews from all users, in order to find coffees that I am interested in trying.

### Questions
* When the user logs in or signs up, will the user land on the "The Coffee House" feed?
    * No, users will land on their personal feed but will have access to the The Coffee House feed.
* Will users be able to comment and/or like sips activity in the coffee house feed?
    * Yes, commenting or liking is enabled for all authorized users regardless of which feed they are in.

### Acceptance Criteria
* When I comment on a user's sip
    * Then I will see my comment pop up at the top of the comment list
* When I like a user's sip
    * Then the user's sip's like section will increase by one

## Top Rated Feed
As an any user, I want to be able to see top rated coffees, in order to find coffees that I might want to sip on.

### Questions
* When a user goes to the Top Rated feed, will they be able to click on a coffee to see details and add to their sips?
    * Yes, users will be able to click on a coffee, view coffee details, add it to their sips, and view other user's sips activity

### Acceptance Criteria:
* When I navigate to the Top Rated feed as any user (authorized or not)
    * Then I will see all of the top rated coffees and some details

## Profile Page
As an authorized user, I want to be able to see all of my recent "sips" activity, so I can see all of the coffees I have recently sipped and my reviews for them

### Questions
* What information will be displayed on my user profile page?
    * Users will be able to see their short personal bio, user details, and feed of coffee sipped
* Will users be able to edit their sips?
    * Yes, they can edit/update or delete their sips
* Will users be able to undo a deleted sip?
    * No, but they will get an alert asking them to confirm they want to delete the sip

### Acceptance Criteria
* When I login, my profile page's sips activity will be sorted by date & time posted
    * Then I can scroll through and choose sips to edit and/or delete
* When I click on one of my coffees' names in my activity feed
    * Then I will be taken to the coffee's detail page

## Coffee Sips
As an authorized user, I want to be able to add a coffee to my "sips" list, so that I can add a comment, rating, and/or location for that coffee

### Questions
* Are there any restrictions on which coffees users can sip on?
    * No, all authorized users can sip any coffee
* Are all sips visible?
    * Yes, sips will be listed in order of creation, newer sips activity shown first
* How many sips are allowed per user?
    * For now, unlimited sips per user
* How do I sip a coffee?
    * From wherever a coffee shows, a user can click on the name and be directed to that coffee's detail page
    * Then a user can click on the "sip coffee" button
* How do I edit/delete one of my sips?
    * Wherever a user sees their "sip" (The Coffee House, Top Rated, My Profile, Coffee Detail Page), edit and delete buttons will be visible for them to click

### Acceptance Criteria:
* When I sip a coffee
    * Then I will be able to write a comment, rate, and/or add a location for that coffee
    * And be able to see my sip appear at the top of The Coffee House feed
* When I edit/delete one of my sips
    * Then it will update accordingly across the site and in the database

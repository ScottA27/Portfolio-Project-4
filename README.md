# KickBack Blog

## About

The KickcBack Blog is a football blog developed using Python, Django, HTML and CSS.

The blog allows football fans around the world to talk everything football. The main page has all the most recent posts and there is
a plethora of categories for fans to delve into and share their opinion.

Registered users can create, edit and delete posts. They can also like posts and create categories. Anyone who comes to the blog can comment on posts without
creating an account.

<a href="https://github.com/ScottA27/Portfolio-Project-4">Repo Link</a>

![Techsini Multi Mockup](/docs/readme/techsini-pp4-multi.png)

- - -

## Contents


- - -

## User Experience

I used a simple design in regards to layout and tried to add more flair with the colours and background image. There is a base green colour
throughout and a simple background image of a football pitch to compliment with a different shade of green.

### Wireframes

I used the recommended [Balsamiq](https://balsamiq.com/wireframes/) to sketch a basic desgin of my project.

#### Home Page Wireframe

<details>
<summary>Click to View Home Page wireframe</summary>

![blog page](/docs/readme/pp4-home-page.png)
</details>

#### Categories Page Wireframe

<details>
<summary>Click to View Categories Page wireframe</summary>

![blog page](/docs/readme/pp4-categories-page.png)
</details>

#### Category Posts Page Wireframe

<details>
<summary>Click to View Category Posts Page wireframe</summary>

![blog page](/docs/readme/pp4-category-post-list.png)
</details>

#### Add Post Page Wireframe

<details>
<summary>Click to View Add Post Page wireframe</summary>

![blog page](/docs/readme/pp4-add-post.png)
</details>

#### Post Details Page Wireframe

<details>
<summary>Click to View Post Details Page wireframe</summary>

![blog page](/docs/readme/pp4-post-details.png)
</details>

#### Login Page Wireframe

<details>
<summary>Click to View Login Page wireframe</summary>

![blog page](/docs/readme/pp4-login.png)
</details>

- - -

## Agile

### The Ideal User

- The site is for anyone with an interest in football.

- Anyone who wants to voice their opinion on football or a situation going on in the footballing world.

- Someone who has a question or query on anything football related can ask on this site.

### User Goals

- As a Site User I can view a list of posts so that I can select one to read
- As a Site User I can click on a post so that I can read the full text
- As a Site User I can view the number of likes on each post so that I can see which is the most popular
- As a Site User I can view comments on an individual post so that I can read the conversation
- As a Site User I can register an account so that I can make posts, like posts and create categories
- As a Site User I can leave comments on a post so that I can be involved in the conversation
- As a Site User I can like or unlike a post so that I can interact with the post

### Developer Goals

- As a Site Admin I can create draft posts so that I can finish writing the content later
- As a Site Admin I can create, read, update and delete posts so that I can manage the blog content
- As a Site Admin I can search through the posts and categories so that I can find what I'm looking for easily

- - -

## Logic and Features

### Logic

#### Data Model

- Allauth User Model

  - The User model was built using Django's Allauth library. When a user is created, they're automatically
  assigned a profile through the Profile model.

Table: **Post**

| id | Type | Notes |
| --- | --- | --- |
| title | CharField | max_length=200 |
| slug | AutoSlugField | populate_from='title', null=False, unique=True, default=None |
| author | ForeignKey | User, on_delete=models.CASCADE, related_name="blog_posts" |
| content | TextField | |
| featured_image | CloudinaryField | 'image', default='placeholder' |
| created_on | DateTimeField | auto_now_add=True |
| likes | ManyToManyField | User, related_name='blogpost_like', blank=True |
| category | ForeignKey | Category, max_length=60, on_delete=models.CASCADE |

***

Table: **Comment**

| id | Type | Notes |
| --- | --- | --- |
| post | ForeignKey | Post, on_delete=models.CASCADE, related_name="comments" |
| name | CharField | max_length=100 |
| body | TextField |  |
| created_on | DateTimeField | auto_now_add=True |

***

Table: **Category**

| id | Type | Notes |
| --- | --- | --- |
| name | CharField | max_length=200 |

- - -

### Features

- #### **Home Page**
  - This is the home page, all users logged in or not see this page and get to scroll through recent posts.

<details>
    <summary>Click to View Home Page</summary>

  ![Blog Page](/docs/readme/kickback-home.png)
</details>

***

- #### **Categories Page**
  - This is the page with all the different topics to talk about.

<details>
    <summary>Click to View Categories Page</summary>

  ![Blog Page](/docs/readme/kickback-categories.png)
</details>

***

- #### **Category Posts Page**
  - This is the page with all the posts from that specific category.

<details>
    <summary>Click to View Category Posts Page</summary>

  ![Blog Page](/docs/readme/kickback-category-posts.png)
</details>

***

- #### **Add Category Page**
  - This is where users can add a new category.

<details>
    <summary>Click to View Add Category Page</summary>

  ![Blog Page](/docs/readme/kickback-add-category.png)
</details>

***

- #### **Post Details Page**
  - This is the page with all of the content of the post.

<details>
    <summary>Click to View Post Details Page</summary>

  ![Blog Page](/docs/readme/kickback-post-details.png)
</details>

***

- #### **Add Post Page**
  - This is the page which users can use to add posts.

<details>
    <summary>Click to View Add Post Page</summary>

  ![Blog Page](/docs/readme/kickback-add-post.png)
</details>

***

- #### **Edit Page**
  - This is the page users can use to edit their posts.

<details>
    <summary>Click to View Edit Post Page</summary>

  ![Blog Page](/docs/readme/kickback-edit-post.png)
</details>

***

- #### **Delete Post Page**
  - This is the where users can choose if they want to delete the specified post.

<details>
    <summary>Click to View Delete Post Page</summary>

  ![Blog Page](/docs/readme/kickback-delete-post.png)
</details>

***

- #### **Register Page**
  - This is the page which new users can use to register an account.

<details>
    <summary>Click to View Register Page</summary>

  ![Blog Page](/docs/readme/kickback-register.png)
</details>

***

- #### **Login Page**
  - This is the page where users already registered can login to their account.

<details>
    <summary>Click to View Login Page</summary>

  ![Blog Page](/docs/readme/kickback-login.png)
</details>

***

- #### **Logout Page**
  - This is the page where logged in users can logout.
<details>
    <summary>Click to View Logout Page</summary>

  ![Blog Page](/docs/readme/kickback-logout.png)
</details>

***

- #### **Navbar When Signed In**
  - This is the navbar shown when users are logged into an account.

<details>
    <summary>Click to View Navbar When Signed In</summary>

  ![Blog Page](/docs/readme/kickback-nav-logged-in.png)
</details>

***

- #### **Navbar When Signed out**
  - This is the navbar shown when users are not logged into an account.

<details>
    <summary>Click to View Navbar When Signed Out</summary>

  ![Blog Page](/docs/readme/kickback-nav-logged-out.png)
</details>

***

- #### **Footer**
  - This is the footer shown across the entire site.

<details>
    <summary>Click to View Footer</summary>

  ![Blog Page](/docs/readme/kickback-footer.png)
</details>

### Future Features

1. Ability to connect the comments section to authorized users instead of allowing anyone to comment.
2. A profile page with all of the users posts.
3. A dislike button for posts.

- - -

## Technology Used

### Languages Used

HTML, CSS and Python.

### Django

- Gunicorn - as the server for Heroku.
- Cloudinary - to host the static files and media for the site.
- Dj_database_url - to parse the database URL from the environment variables in Heroku.
- Psycopg2 - as an adaptor for Python and PostgreSQL databases.
- Allauth - for authentication, registration, account management.
- Autoslug - improved slug field which can automatically populate itself from another field and preserve uniqueness of the value.

### Frameworks, Libraries & Programs Used
* [Techsini Multi Mockup](https://techsini.com/multi-mockup/) - to show site across a range of devices.
* Git - for version control. 
* GitHub - to save and store the code pushed from Git.
* GitPod - using GitPod terminal to commit to Git and push to GitHub.
* Balsamiq - to create the wireframes when designing the website.
* Dev Tools - for testing and troubleshooting.
* [Font Awesome](https://fontawesome.com/) - to add social media icons and football in the logo.
* [Wave](https://wave.webaim.org/) - to test web accessibility.
* [W3C](https://validator.w3.org/) - HTML validator.
* [Jigsaw](https://jigsaw.w3.org/css-validator/) - CSS validator.
* Bootstrap - a framework for building responsive, mobile-first sites.
* Heroku - used to deploy the live project.
* PostgreSQL - database used through heroku.

- - -

## Testing

### Manual Testing

* All pages have been checked over for bugs and errors, none can be found apart from a timezone issue on posts. All buttons, links and forms
work 100% as intended.

#### Browser and Responsiveness tests:

* Tests were carried out on desktop using Chrome, Firefox and Microsoft Edge.
* Tests were carried out on mobile using Safari and Chrome.

### PEP8

Testing carried out using Code Institutes Python Linter. No errors apart from lines being too long which I have tried to fix.

### Kickback:

* asgi.py

<details>
    <summary>Click to View asgi.py</summary>

  ![Blog Page](/docs/testing/kickback-asgi.py.png)
</details>

***

* settings.py

<details>
    <summary>Click to View settings.py</summary>

  ![Blog Page](/docs/testing/kickback-settings.py.png)
</details>

***

* urls.py

<details>
    <summary>Click to View urls.py</summary>

  ![Blog Page](/docs/testing/kickback-urls.py-2.png)
</details>

***

* wsgi.py

<details>
    <summary>Click to View wsgi.py</summary>

  ![Blog Page](/docs/testing/kickback-wsgi.py.png)
</details>

***

### Blog:

* admin.py

<details>
    <summary>Click to View admin.py</summary>

  ![Blog Page](/docs/testing/kickback-admin.py.png)
</details>

***

* apps.py

<details>
    <summary>Click to View apps.py</summary>

  ![Blog Page](/docs/testing/kickback-apps.py.png)
</details>

***

* forms.py

<details>
    <summary>Click to View forms.py</summary>

  ![Blog Page](/docs/testing/kickback-forms.py.png)
</details>

***

* models.py

<details>
    <summary>Click to View models.py</summary>

  ![Blog Page](/docs/testing/kickback-models.py.png)
</details>

***

* urls.py

<details>
    <summary>Click to View urls.py</summary>

  ![Blog Page](/docs/testing/kickback-urls.py.png)
</details>

***

* views.py

<details>
    <summary>Click to View views.py</summary>

  ![Blog Page](/docs/testing/kickback-views.py.png)
</details>

***

### W3C Validator

Tests carried out using [W3C Validator](https://validator.w3.org/) there were no errors in any of the pages.

* Home

<details>
    <summary>Click to View Home page</summary>

  ![Blog Page](/docs/testing/kickback-home-test.png)
</details>

***

* Categories

<details>
    <summary>Click to View Categories</summary>

  ![Blog Page](/docs/testing/kickback-categories-test.png)
</details>

***

* Category Posts

<details>
    <summary>Click to View Category Posts</summary>

  ![Blog Page](/docs/testing/kickback-category-posts-test.png)
</details>

***

* Add Category

<details>
    <summary>Click to View Add Category</summary>

  ![Blog Page](/docs/testing/kickback-add-category-test.png)
</details>

***

* Post Details

<details>
    <summary>Click to View Post Details</summary>

  ![Blog Page](/docs/testing/kickback-post-details-test.png)
</details>

***

* Add Post

<details>
    <summary>Click to View Add Post</summary>

  ![Blog Page](/docs/testing/kickback-add-post-test.png)
</details>

***

* Edit Post

<details>
    <summary>Click to View Edit Post</summary>

  ![Blog Page](/docs/testing/kickback-edit-post-test.png)
</details>

***

* Delete Post

<details>
    <summary>Click to View Delete Post</summary>

  ![Blog Page](/docs/testing/kickback-delete-post-test.png)
</details>

***

* Register

<details>
    <summary>Click to View Register</summary>

  ![Blog Page](/docs/testing/kickback-register-test.png)
</details>

***

* Login

<details>
    <summary>Click to View Login</summary>

  ![Blog Page](/docs/testing/kickback-login-test.png)
</details>

***

* Logout

<details>
    <summary>Click to View Logout</summary>

  ![Blog Page](/docs/testing/kickback-logout-test.png)
</details>

***

### Lighthouse

Tests were carried out using [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).

* Home

<details>
    <summary>Click to View Home</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-home.png)
</details>

***

* Categories

<details>
    <summary>Click to View Categories</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-categories.png)
</details>

***

* Category Posts

<details>
    <summary>Click to View Category Posts</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-category-posts.png)
</details>

***

* Add Category

<details>
    <summary>Click to View Add Category</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-add-category.png)
</details>

***

* Post Details

<details>
    <summary>Click to View Post Details</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-post-details.png)
</details>

***

* Add Post

<details>
    <summary>Click to View Add Post</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-add-post.png)
</details>

***

* Edit Post

<details>
    <summary>Click to View Edit Post</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-edit-post.png)
</details>

***

* Delete Post

<details>
    <summary>Click to View Delete Post</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-delete-post.png)
</details>

***

* Register

<details>
    <summary>Click to View Register</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-register.png)
</details>

***

* Login

<details>
    <summary>Click to View Login</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-login.png)
</details>

***

* Logout

<details>
    <summary>Click to View Logout</summary>

  ![Blog Page](/docs/testing/lighthouse-kickback-logout.png)
</details>

***

### Accessibility

Tests were carried out using [WAVE](https://wave.webaim.org/). There were subtle errors with contrast because of my use of a background image across the site, the test doesn't pick up on this so it is essentially throwing a false error.

* Home

<details>
    <summary>Click to View Home</summary>

  ![Blog Page](/docs/testing/wave-kickback-home.png)
</details>

***

* Categories

<details>
    <summary>Click to View Categories</summary>

  ![Blog Page](/docs/testing/wave-kickback-categories.png)
</details>

***

* Category Posts

<details>
    <summary>Click to View Category Posts</summary>

  ![Blog Page](/docs/testing/wave-kickback-category-posts.png)
</details>

***

* Add Category

<details>
    <summary>Click to View Add Category</summary>

  ![Blog Page](/docs/testing/wave-kickback-add-category.png)
</details>

***

* Post Details

<details>
    <summary>Click to View Post Details</summary>

  ![Blog Page](/docs/testing/wave-kickback-post-details.png)
</details>

***

* Add Post

<details>
    <summary>Click to View Add Post</summary>

  ![Blog Page](/docs/testing/wave-kickback-add-post.png)
</details>

***

* Edit Post

<details>
    <summary>Click to View Edit Post</summary>

  ![Blog Page](/docs/testing/wave-kickback-edit-post.png)
</details>

***

* Delete Post

<details>
    <summary>Click to View Delete Post</summary>

  ![Blog Page](/docs/testing/wave-kickback-delete-post.png)
</details>

***

* Register

<details>
    <summary>Click to View Register</summary>

  ![Blog Page](/docs/testing/wave-kickback-register.png)
</details>

***

* Login

<details>
    <summary>Click to View Login</summary>

  ![Blog Page](/docs/testing/wave-kickback-login.png)
</details>

***

* Logout

<details>
    <summary>Click to View Logout</summary>

  ![Blog Page](/docs/testing/wave-kickback-logout.png)
</details>

- - -

### Solved Bugs

1. There was a bug with getting slugged title tags for each post being made. I figured it out by using AutoSlugField and populating the title tag from the title.

2. There was an issue with my category title tags as well due to them being generated from Jinja. I spoke with a tutor from Code Institute and we figured out that the field I was calling was incorrect.

3. There was an issue with the comments section of the post pages where I couldn't get the layout how I wanted and the text would show outside of the boxes I wanted them in. I figured this out by using the Bootstrap documentation and some trial and error. I iterated through the comments using a for loop with a div for each one with the styling I desired.

### Unsolved Bugs

1. I have noticed with each post that I make that it is an hour behind, I learned that this is due to the time zone for the database. I tried fixing this so that the site would realise the time zone being used on the device making the posts. However, I couldn't figure it out in the time that I had.

- - -

## Deployment 

The project is deployed using Heroku.

### Create the live database which can be accessed by Heroku:

1. Go to the ElephantSQL dashboard and click the create new instance button on the top right.
2. Name the plan, select the tiny turtle plan and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL.

### Heroku app setup:

1. From the Heroku dashboard, click the new button in the top right corner and select create new app.
2. Give your app a unique name, select the region that is closest to you and then click the create app button bottom left.
3. Open the settings tab and create a new config var of DATABASE_URL and paste the database URL you copied from elephantSQL into the value (remove quotation marks from value).

### Prepare env.py and settings.py files

1. In your GitPod workspace, create an env.py file in the main directory and add the DATABASE_URL value and your chosen SECRET_KEY value to the file.
3. Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
4. Comment out default database configuration then save all files and make migrations.
5. Add the Cloudinary URL to env.py and the Cloudinary libraries to the list of installed apps.
6. Add the STATIC files settings
7. Link the file to the templates directory in Heroku.
8. Change the templates directory to TEMPLATES_DIR
9. Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
1. Create a requirements.txt file
2. Create directories in the main directory
3. Create a "Procfile" in the main directory and add the following: web: gunicorn project_name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
* SECRET_KEY = yoursecretkey
* CLOUDINARY_URL = URL
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1
* DATABASE_URL = URL

### Deploy

1. Make sure that in the settings.py that DEBUG = True if in development and DEBUG = False if not.
2. Remove config vars DISABLE_COLLECTSTATIC = 1 from Heroku settings.
3. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
5. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Please note, manually deployed branches will need re-deploying each time the GitHub repository is updated.
6. Click 'Open App' to view the deployed live site.

The site should now be up and running.

***

## Credits

* Code Institute - Blog Walkthrough Project
* [Codemy Simple Blog with Python and Django](https://www.youtube.com/watch?v=B40bteAMM_M&list=LL&index=1&t=1s&ab_channel=Codemy.com) used the walkthrough as a guide throughout my project for several aspects including the forms, views and templates.
* Bootstrap
* MDBootsrap
* Stack Overflow
* W3Schools
* LearDjango
* Django Docs
* Traversy Media Python Django 7 Hour Course
* CI's Slack Community

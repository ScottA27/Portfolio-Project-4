# KickBack Blog

## About

The KickcBack Blog is a football blog developed using Python, Django, HTML and CSS.

The blog allows football fans around the world to talk everything football. The main page has all the most recent posts and there is
a plethora of categories for fans to delve into and share their opinion.

Registered users can create, edit and delete posts. They can also like posts and create categories. Anyone who comes to the blog can comment on posts without
creating an account.

<a href="https://github.com/ScottA27/Portfolio-Project-4">Repo Link</a>

![Techsini Multi Mockup](/docs/readme/techsini-pp4-multi.png)


## Contents

## User Experience

I used a simple design in regards to layout and tried to add more flair with the colours and background image. There is a base green colour
throughout and a simple background image of a football pitch to compliment the different shade of green.

### Wireframes

I used the recommend [Balsamiq](https://balsamiq.com/wireframes/) to sketch a basic desgin of my project.

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
| category | CharField | max_length=200, default='Uncategorized' |

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

***

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
* [Font Awesome](https://fontawesome.com/) - to add icons.
* [Wave](https://wave.webaim.org/) - to test web accessibility.
* [W3C](https://validator.w3.org/) - HTML validator.
* [Jigsaw](https://jigsaw.w3.org/css-validator/) - CSS validator.
* Bootstrap - a framework for building responsive, mobile-first sites.
* Heroku - used to deploy the live project.
* PostgreSQL - database used through heroku.


## Testing



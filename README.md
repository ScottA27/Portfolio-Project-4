# KickBack Blog

## About

The KickcBack Blog is a football blog developed using Python, Django, HTML and CSS.

The blog allows football fans around the world to talk everything football. The main page has all the most recent posts and there is
a plethora of categories for fans to delve into and share their opinion.

Registered users can create, edit and delete posts. They can also like posts and create categories. Anyone who comes to the blog can comment on posts without
creating an account.

<a href="https://github.com/ScottA27/Portfolio-Project-4">Repo Link</a>


## Contents

# User Experience

I used a simple design in regards to layout and tried to add more flair with the colours and background image. There is a base green colour
throughout and a simple background image of a football pitch to compliment the different shade of green.

## Wireframes

I used the recommend [Balsamiq](https://balsamiq.com/wireframes/) to sketch a basic desgin of my project.

### Home Page Wireframe

<details>
<summary>Click to View Home Page wireframe</summary>

![blog page](/docs/readme/pp4-home-page.png)
</details>

### Categories Page Wireframe

<details>
<summary>Click to View Categories Page wireframe</summary>

![blog page](/docs/readme/pp4-categories-page.png)
</details>

### Category Posts Page Wireframe

<details>
<summary>Click to View Category Posts Page wireframe</summary>

![blog page](/docs/readme/pp4-category-post-list.png)
</details>

### Add Post Page Wireframe

<details>
<summary>Click to View Add Post Page wireframe</summary>

![blog page](/docs/readme/pp4-add-post.png)
</details>

### Post Details Page Wireframe

<details>
<summary>Click to View Post Details Page wireframe</summary>

![blog page](/docs/readme/pp4-post-details.png)
</details>

### Login Page Wireframe

<details>
<summary>Click to View Login Page wireframe</summary>

![blog page](/docs/readme/pp4-login.png)
</details>

# Agile

## The Ideal User

- The site is for anyone with an interest in football.

- Anyone who wants to voice their opinion on football or a situation going on in the footballing world.

- Someone who has a question or query on anything football related can ask on this site.

## User Goals

- As a Site User I can view a list of posts so that I can select one to read
- As a Site User I can click on a post so that I can read the full text
- As a Site User I can view the number of likes on each post so that I can see which is the most popular
- As a Site User I can view comments on an individual post so that I can read the conversation
- As a Site User I can register an account so that I can make posts, like posts and create categories
- As a Site User I can leave comments on a post so that I can be involved in the conversation
- As a Site User I can like or unlike a post so that I can interact with the post

## Developer Goals

- As a Site Admin I can create draft posts so that I can finish writing the content later
- As a Site Admin I can create, read, update and delete posts so that I can manage the blog content
- As a Site Admin I can search through the posts and categories so that I can find what I'm looking for easily


# Logic and Features

## Logic

### Data Model

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


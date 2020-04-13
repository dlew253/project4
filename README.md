# P4: remindMe 


![]

RemindMe is a simple to-do list created with React.js, that allows simple text inputs that can be edited, and deleted as they are completed.

## Tech Stack
**Front end:** React

**Back end:** Python, Flask, SQLAlchemy (PostGreSQL)


## MVP

Create a web application using a React front end and Flask (python) back end that allows users to create task lists. 

## Models

### 1. User
| Column | Type | Other |
|--------|------|-------|
| Id | Integer | PK |
| Firstname | String | Required|
| Lastname | String | Required|
| Email | String | Required, Unique |
| Password | Password | Limit 8-30 char

### 2. Poem (1 user: Many Poems)
| Column | Type | Other |
|--------|------|-------|
| Id | Integer | PK |
| Title | String | Required |
| Date | Integer | Required |
| UserID | Integer | FK


## Routes

![]//add diagrams here//
*User Flow Diagram*

### Back End (Flask)

| Type | Address | Description|
|------|---------|------------|
|GET| /profile | Send user data |
|PUT| /profile | Update user data |
|GET| /posts | Get all list|
|POST| /posts | Post a list |
|GET| /posts/:id | Send list info |
|DELETE | /posts/:id | Delete post |
|POST| /login | Log user in
|POST| /signup | Create new user
| - | /logout | Log user out

### Front End (React Components)
| Address | Description|
|------|---------|
|/ |landing page| 
|/home| Welcome Page |
|/posts | Shows Posts
|/edit| Form to edit profile |
|/New| Renders a new form | 
|/login| Form to login | 
|/signup| Form to sign up | 


## Project Log

### Friday-Monday
* Preplanning phase
* Decide colors, theme, style, fonts

### Monday - Thursday
* Built basic react pages and components
* Started first database
* Built initial list creator
* Try to implement auth.

### Friday
* Mass panic
* Re-work front end components to connect all pages
* Try again to do auth (unsuccessful)

### Saturday
* Struggle with flask/React auth
* Add User/Post CRUD files
* Worked on styling and making pages pretty

### Sunday
* More panicking
* Accept my fate
* Blitz backend to no success
* ReadMe work






## Stretch Goals & Unsolved Problems
* Connect back and front ends
* Being able to save created lists with a title and date


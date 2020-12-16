Url Shortner

Tech Stack - Python, Django


**Steps to set-up**

1. Install requirements.
2. Create postgres database 'movingworlds'
3. run 'python manage.py makemigrations'
4. run 'python manage.py migrate'.
5. run 'python manage.oy runserver'.

**Routes**

1. http://localhost:8000/ - Home
2. http://localhost:8000/login - Login Page
3. http://localhost:8000//register - Sign Up Page
4. http://localhost:8000/dashboard - List of shot_url created by user and **Form** to create new **short_url** 
5. http://localhost:8000/dashboard/< int:pk > - Edit short_url with **id-pk**
6. http://localhost:8000/< str:string >/stats - Stats of **short_url=query**


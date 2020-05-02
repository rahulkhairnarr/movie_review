# Django REST API - Movies & Rating

# Project Description
- The API is read-only for guest users would be able to search for a specific movie by movie name.
- The API for A user should be able to sign up / login
- The API for Logged In users would be able to rate a movie and comment on it.
- There is currently one user authorized to manipulate data on this API. The user name is 'rahul', and the password is '123456'


# Instructions
1. To start the API
  - Open your terminal
  - $ sudo easy_install pip         # installs Pip package manager
  - $ pip install virtualenv				# Virtualenv is a tool to create isolated Python environments.
  - $ git clone https://github.com/rahulkhairnarr/movie_review.git
  - $ source env/bin/activate       # Launch the environment
  - $ cd movie_review                     # Browse into the project directory
  - $ python manage.py runserver    # Start the server
2. To be able to Install all required package through the terminal
  - $ pip install requirements.txt           # installs HTTPie package
3. API for user to Sign up 
  - CLI: curl --location --request POST 'http://localhost:8000/signup/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "username": "username",
            "password": "password",
            "email": "email@eample.com"
            }'
4. API for user to login
  - CLI: curl --location --request POST 'http://localhost:8000/login/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "username": "username",
            "password": "password",
            }'
5. API to search for a movie with name which will provide movie's title, it's average rating, count of people who have rated the returned movie.
  - CLI: curl --location --request GET 'http://localhost:8000/api/movie?search={{movie_name}}'
6. API for movie details consist of movie information, all users comments and ratings.
  - CLI: curl --location --request GET 'http://localhost:8000/api/moviedetails/{{movie_name}}/'
7. API to rate and comment a movie (keep both the fields mandatory, allow only logged in user to rate and comment on movie)
  - CLI: curl --location --request POST 'http://localhost:8000/api/review/create/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "comment":"the universe is in ruins. With the help of remaining allies",
            "rating": 3.6,
            "content_type": 7, # Content ID
            "object_id": 1, #Movie ID
            "user": 1, #User ID
            }'


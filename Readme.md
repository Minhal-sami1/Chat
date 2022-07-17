# Chat with your buddy 
Hi ! I am Minhal Abdul Sami, I made this "Chat with your buddy" Webapp. You might have seen many chatting webapps and apps but there is always a questions about its standard of security and privacy, they give new and free features in trade of your security and privacy. But this webapp is unique on its own. The features will be discussed later. lets move which tech is used to build this.

## Tech stack

* Django
* Vanilla Javascript
* HTML/CSS
* Bootsrap

**Yes its that simple.**

## Getting Started

**Be sure run all these commands in the project folder/directory**

1. First install all the dependencies to run it.
```python
Python install -r requirements.txt
```
2. Make migrations to setup Django Models for your DB
```python
Python manage.py makemigrations
```
3. Apply the migrations to setup your DB
```python
Python manage.py migrate
```
4. Register as a superuser
```python
Python manage.py createsuperuser
```
5. Run your server locally and enjoy
```python
Python manage.py runserver
```

## How its different from others ? || Distinctiveness and Complexity:
* First of all you need your friend's unique ID in order to connect with him, there is no other option. If you don't share your ID with someone unknown, the unknown will not be able to message you
* Second If someone tries to login as you, they will not be able to see your previous chat
* Third If someone tries to read your current open chat then he will not be able to know who is the **Friend** you are talking to.
* All of the messages are encrypted and even the owner of the webapp will not be able to know what is written in the messages

## Why I made this?

I made this because there is a huge lack of trust on messaging and chatting platforms. The users are not sure of their privacy. So I made this to be sure that all my chats are encrypted and secure and no one can access them or sell them in any way.

# Where is it available ?
[Hosted online !](https://chat.minhal.xyz)
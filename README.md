# The Daily Eight
Eight trending stories condensed, packaged, and delivered to your inbox every morning at 8 a.m.

# How it works
The Daily Eight is a set of python scripts that runs on an Amazon AWS EC2 server indefinitely. The script scrapes the front page of Reuters.com every morning at 8 a.m. EST and compiles the eight most trending stories for the day, including titles and images. Then using Natural Language Processing, the body of each article is processed and condensed down. Everything is then neatly sent through a premade HTML/CSS template to a specified list of emails each morning.

# Example of news article
Below is an image of an article that was sent to a participant's email one morning:
![Daily Eight Article](/assets/email page.png)

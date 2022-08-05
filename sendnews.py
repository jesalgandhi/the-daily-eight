from newsfetch import fetchTodayNews
from dotenv import load_dotenv
from datetime import date
import os
import time
import yagmail

ARTICLES_PER_DAY = 8
ALL_RECIPIENTS = [
    'jesalgandhi9988@gmail.com',
    'customdailynews@gmail.com',
    'jgandhi5@stevens.edu'
]

def generate_html(body):
    html = '''
        <html> 
            <body style="color: #00ff00;">
                <h1 style="margin-bottom:20px; font-family: 'Playfair Display', serif; font-weight: 900;font-size: 80px;text-transform: uppercase;display: inline-block;line-height: 20px;">
                    The Daily Eight
                </h1>
                <h2 style="margin-bottom: 25px;">Eight trending stories condensed, packaged, and delivered to your inbox every morning at 8 a.m.</h2>
                {content}
                <h2>Thank you for reading today's issue.</h2>
                <h3><a href="https://jesalgandhi.com/">Contact Me</a></h3>
                <p>Jesal Gandhi © 2022</p>
            </body>
        </html>
    '''

    content = ''
    
    for k, v in body.items():
        # article title
        content += '<h1>' + str(k+1) + ': ' + v[0] + '</h1> \n'
        
        # article photos
        for photo in v[2]:
            if 'resizer' not in photo:
                string = '<img height="300" src="{source}"> '.format(source=photo)
                content += string

        # article text
        content += '<p style="font-size:1.25em;">' + v[1].strip('\n') + '</p>'

    return html.format(content=content).replace("\n", "")

def send_articles():
    load_dotenv()
    yag = yagmail.SMTP(os.getenv('GMAIL_USERNAME'), os.getenv('GMAIL_APP_PASSWORD'))
    body = fetchTodayNews(ARTICLES_PER_DAY)
    today = date.today().strftime("%B %d, %Y")

    html = generate_html(body)


    yag.send(bcc=ALL_RECIPIENTS, subject=today, contents=html)

    print(fetchTodayNews(ARTICLES_PER_DAY))
    print('Emails sent!')

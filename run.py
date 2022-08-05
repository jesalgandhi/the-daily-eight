from sendnews import send_articles
import time
import schedule

print('Server running')
schedule.every().day.at("08:00").do(send_articles)

while True:
    schedule.run_pending()
    time.sleep(1)

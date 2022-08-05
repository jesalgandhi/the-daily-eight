from sendnews import send_articles
import time
import schedule

print('Server running')
# AWS server is UTC time, so 12:00 UTC = 8:00 EST
schedule.every().day.at("12:00").do(send_articles)

while True:
    schedule.run_pending()
    time.sleep(1)

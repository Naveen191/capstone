from api_request import free_news_api_request
import schedule
import time

free_news_api_request()
#schedule.every(10).seconds.do(free_news_api_request)
#while True:
 #   schedule.run_pending()
  #  time.sleep(1)
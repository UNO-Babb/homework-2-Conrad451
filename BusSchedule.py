#BusSchedule.py
#Name: Connor Pell  
#Date: October 21st, 2025
#Assignment: Homework 2

import re
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Converts HH:MM to 24 hour time for easy math.
def convert24Hours(time_str):
  #Split our hours and minutes by the :
  hour, mins = time_str.split(":", 1)
  #Split the AM or PM off the minutes
  minutes = mins[:2]
  ampm = mins[2:]
  #Convert back into int
  hour = int(hour)
  minutes = int(minutes)

  #logic here to split it up.

  #if its the afternoon, add 12 hours to the PM time, unless its already 12 pm.
  if ampm == "PM" and hour != 12:
    hour += 12
  #if its the AM, and it's midnight, set hour to 0
  elif ampm == "AM" and hour == 12:
    hour = 0

  return hour, minutes

def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents


def main():
  test_url = "https://myride.ometro.com/Schedule?stopCode=2269&routeNumber=11&directionName=EAST"
  
  stopCode = "3018"
  routeNumber = "18"
  directionName = "EAST"
  

  base = "https://myride.ometro.com/Schedule"
  url = f"{base}?stopCode={stopCode}&routeNumber={routeNumber}&directionName={directionName.upper()}" 

  #c1 = loadURL(url) #loads the web page
  c1 = loadTestPage() #loads the test page

  #get time for now, delta back to CST since codespaces isn't in CST
  now = datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=5)

  #convert datetime object into a string
  now_string = now.strftime("%I:%M:%p")

  print(f"Current Time {now_string}")
  
  #Extract times from the page with some regexing
  busTimes = re.findall(r"\b((?:0?[1-9]|1[0-2]):[0-5]\d ?(?:AM|PM))\b", c1)
 
 

  #Initialize our vars for keeping track of the busses.
  nextBus = None
  nextDifference = None

  for time in busTimes:
    print(time)
    hours, minutes = convert24Hours(time)
    print(f"{hours}:{minutes}")











main()

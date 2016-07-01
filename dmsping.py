#!/usr/bin/env python

import json
import os
import sys
import requests

def read_config():
  config_location = 'config.json'
  if os.path.isfile(config_location):
    with open(config_location) as config_file:    
      config = json.load(config_file)
    return config
  else:
    print 'config file %s is missing' % config_location
    sys.exit()

def check_host(host,url):
  response = os.system("ping -c 1 " + host)
  if response == 0:
    res = requests.get(url)  
  
def run():
  config = read_config()
  url = config['url']
  host = config['host']
  check_host(host,url)

# Make it so!
run()

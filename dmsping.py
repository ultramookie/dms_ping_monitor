#!/usr/bin/env python

import json
import os
import optparse
import sys
import requests

def read_config(conf_file):
  if os.path.isfile(conf_file):
    with open(conf_file) as config_file:    
      config = json.load(config_file)
    return config
  else:
    print 'config file %s is missing' % config_location
    sys.exit()

def get_conf_file():
  parser = optparse.OptionParser()
  parser.add_option('-i', action="store", help="Where are your input files located?", dest="conf_file", default="./config.json")
  (options, args) = parser.parse_args()
  return options.conf_file

def check_host(host,url):
  response = os.system("ping -c 1 " + host)
  if response == 0:
    res = requests.get(url)  
  
def run():
  conf_file = get_conf_file() 
  config = read_config(conf_file)
  url = config['url']
  host = config['host']
  check_host(host,url)

# Make it so!
run()

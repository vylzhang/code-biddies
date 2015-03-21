# two types of parsers - one for global market, one for our shits

# 2 parameters - command, ticker, data
# parse one line

import clientpy3

def run_securities(): # returns list of lists
  output = clientpy3.run("Better_Biddys","gibsonsux","SECURITIES")
  outputP = output.split(" ");

  i = 1
  lol = []
  while i<len(outputP):
    lol.append(outputP[i:i+4])
    i+=4

  # for o in lol:
  #   print(" ", o ," ")

  return lol

if __name__ == '__main__':
  # service.py executed as script
  # do something
  #service_func()
  out = run_securities()
  print(out)

import socket
import sys
import parse

maxMarketHistorySize = 50
numOfStocks = 10

def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            temp = rline.strip()
            rline = sfile.readline()
            return temp

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\nSUBSCRIBE\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()

## HING
class stock:

    def __init__(self):
        self.ticker = ""
        self.netWorth = -1
        self.bid = -1
        self.ask = -1
        self.currDividendRatio = -1
        self.volitility = -1
        self.marketHistory = list() # market value

    def updateStockInfo(self, ticker, netWorth, dividendRatio, volitility):
        # call this method every iteration to receive all the parsed data
        #   for the stock
        self.ticker = ticker
        self.netWorth = netWorth
        self.prevDividendRatio = self.currDividendRatio
        self.currDividendRatio = dividendRatio
        self.volitility = volitility

    def updateOrderInfo(self):
        #get the bid and ask prices of the tickers
        
        
    def setShareValue(self):
        # this only needs to get calculated once
        # all actions depend on this long-term stock price
        initialDividendPayout = marketHistory(0) * prevDividendRatio
        decreasefactor = currDividendRatio / prevDividendRatio
        self.ShareValue = initialDividendPayout / (1-dividendRatio)

    def getTicker(self):
        return self.ticker
    
    def getBid(self):
        # return the bid
        return self.bid

    def getAsk(self):
        # return the ask
        return self.ask

## LEIGHTON
def run_securities(): # returns list of lists
  output = run("Better_Biddys","gibsonsux","SECURITIES")
  outputP = output.split(" ");

  i = 1
  lol = []
  while i<len(outputP):
    lol.append(outputP[i:i+4])
    i+=4

  # for o in lol:
  #   print(" ", o ," ")

  return lol

def run_orders(tkr): # returns list of market orders
  output = run("Better_Biddys","gibsonsux","ORDERS AAPL")
  print(output)
  outputP = output.split(" ");

  i = 1
  lol = []
  bidAsk = []
  while i<len(outputP):
    lol.append(outputP[i:i+4])
    i+=4
  bidAsk.append(lol[0])
  bidAsk.append(lol[len(lol)-1])
  return bidAsk        

def run_orders(tkr): # returns list of market orders
  output = run("Better_Biddys","gibsonsux","ORDERS AAPL")
  outputP = output.split(" ");

  i = 1
  lol = []
  bidAsk = []
  while i<len(outputP):
    lol.append(outputP[i:i+4])
    i+=4
  bidAsk.append(lol[0])
  bidAsk.append(lol[len(lol)-1])
  return bidAsk 

## VIVIAN
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Enter username, password, command")
    else:
        arg = sys.argv
        run(arg[1],arg[2],arg[3])
    stocks = [] #list of lists that will contain the current market information
    for i in range(0, numOfStocks): #instantiate each stock
        x = stock()
        stocks.append(x)

    #per second loop starts here
    marketInfo = run_securities()
    for i in range(0, len(marketInfo)):
        stocks[i].updateStockInfo(marketInfo[i][0], marketInfo[i][1], marketInfo[2], marketInfo[3]) #ticker, networth, div ratio, volatility
    for each in stocks:
        print(each.ticker)
        

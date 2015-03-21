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
        bidAsk = run_orders(self.ticker)
        self.bid = bidAsk[0][2]
        self.ask = bidAsk[1][2]
        #print("The bid price of " + self.ticker + " is " + self.bid + ". \n The ask price is " + self.ask + ".")
        
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
        return float(self.bid)

    def getAsk(self):
        # return the ask
        return float(self.ask)

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
    output = run("Better_Biddys","gibsonsux","ORDERS " + tkr)
    outputP = output.split(" ")
    
    i = 1
    lol = []
    bidAsk = []
    while i<len(outputP):
        lol.append(outputP[i:i+4])
        i+=4
    bidAsk.append(lol[0])
    bidAsk.append(lol[len(lol)-1])
    return bidAsk

def bid(ticker, price, qty):
    run("Better_Biddys","gibsonsux","BID " + ticker + " " + str(price) + " " + str(qty))

def ask(ticker, price, qty):
    run("Better_Biddys","gibsonsux","ASK " + ticker + " " + str(round(price)) + " " + str(qty))

## VIVIAN
if __name__ == "__main__":
#    if len(sys.argv) != 4:
#        print("Enter username, password, command")
#    else:
#        arg = sys.argv
#        run(arg[1],arg[2],arg[3])
    while True:
        cash_temp = run("Better_Biddys","gibsonsux","MY_CASH")
        cash_temp = cash_temp.split(" ")
        cash = float(cash_temp[1])

        print("Cash: " + str(cash))
        stocks = [] #list of lists that will contain the current market information
        for i in range(0, numOfStocks): #instantiate each stock
            x = stock()
            stocks.append(x)

        #per second loop starts here
        marketInfo = run_securities()
        for i in range(0, len(marketInfo)):
            stocks[i].updateStockInfo(marketInfo[i][0], marketInfo[i][1], marketInfo[2], marketInfo[3]) #ticker, networth, div ratio, volatility

        for each in stocks:
            #print(each.ticker)
            each.updateOrderInfo()
        print(stocks[0].getBid())
        bid("AAPL", stocks[0].getBid(), 5)
        #run("Better_Biddys","gibsonsux","BID AAPL " + str(round(stocks[0].getBid())+0.01) + " 5")
        if cash < 1000:
            ask("AAPL", stocks[0].getAsk(), 5)
            #run("Better_Biddys","gibsonsux","ASK AAPL " + (stocks[0].getAsk()-0.01) + " 5")
        

import socket
import sys
import parse
#from collections import deque


maxMarketHistorySize = 50
numOfStocks = 10
initialCash = 1000
timeToSell = 100

timeCount = 0 
blackList = [0,0,0,0,0,0,0,0,0,0]

HOST, PORT = "codebb.cloudapp.net", 17429
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sfile = sock.makefile()
user = "Better_Biddys"
password = "gibsonsux"
data=user + " " + password + "\n"
sock.sendall(bytes(data, 'UTF-8'))

def run(user, password, *commands):

    data = "\n".join(commands) + "\n"

    sock.sendall(bytes(data, 'UTF-8'))

    rline = sfile.readline()
    return rline.strip()

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\nSUBSCRIBE\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, 'UTF-8'))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()

## HING
class stock:
    def __init__(self):
        self.ticker = ""
        self.prevNetWorth = -1
        self.currNetWorth = -1
        self.bid = -1
        self.ask = -1
        self.currDividendRatio = -1
        self.volitility = -1
        self.marketHistory = list() # market value
        self.trend = []

    def updateStockInfo(self, ticker, netWorth, dividendRatio, volitility):
        # call this method every iteration to receive all the parsed data
        #   for the stock
        self.ticker = ticker
        self.prevNetWorth = float(self.currNetWorth)
        self.currNetWorth = float(netWorth)
        self.prevDividendRatio = self.currDividendRatio
        self.currDividendRatio = dividendRatio
        self.volitility = volitility

    def updateOrderInfo(self):
        #get the bid and ask prices of the tickers
        bidAsk = run_orders(self.ticker)
        #print(bidAsk[0])
        #print(bidAsk[1])
        self.bid = bidAsk[0][2]
        self.ask = bidAsk[1][2]
        #print("The bid price of " + self.ticker + " is " + self.bid + ". \n The ask price is " + self.ask + ".")
        
    def setShareValue(self):
        # this only needs to get calculated once
        # all actions depend on this long-term stock price
        initialDividendPayout = marketHistory(0) * prevDividendRatio
        decreasefactor = currDividendRatio / prevDividendRatio
        self.ShareValue = initialDividendPayout / (1-dividendRatio)

    def isIncreasing(self):
        return self.currNetWorth > self.prevNetWorth

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
    run("Better_Biddys","gibsonsux","ASK " + ticker + " " + str(price) + " " + str(qty))

def numSecurity(ticker):
    temp = run("Better_Biddys","gibsonsux","MY_SECURITIES")
    temp2 = temp.split(" ")
    i = 1
    lol = []
    while i<len(temp2):
        lol.append(temp2[i:i+2])
        #print("dirt!!" + temp2[i] + " " + temp2[i+1])
        i+=3
    for each in lol:
        if each[0] == ticker:
            return each[1]
    return -1

def numOrders(ticker):
    temp = run("Better_Biddys","gibsonsux","MY_ORDERS")
    temp2 = temp.split(" ")
    i = 1
    lol = []
    while i < len(temp2):
        lol.append(temps2[i:i+3])
        i+=3

def setInitialCash(num):
    initialCash = num

## VIVIAN
if __name__ == "__main__":
#    if len(sys.argv) != 4:
#        print("Enter username, password, command")
#    else:
#        arg = sys.argv
#        run(arg[1],arg[2],arg[3])
    cash_temp = run("Better_Biddys","gibsonsux","MY_CASH")
    cash_temp = cash_temp.split(" ")
    cash = float(cash_temp[1])
    setInitialCash(cash)

    stocks = [] #list of lists that will contain the current market information
    for i in range(0, numOfStocks): #instantiate each stock
        x = stock()
        stocks.append(x)
    
    while True:
        cash_temp = run("Better_Biddys","gibsonsux","MY_CASH")
        cash_temp2 = cash_temp.split(" ")
        currCash = float(cash_temp2[1])

        print("Cash: " + str(cash))

        
        #per second loop starts here
        marketInfo = run_securities()
        for i in range(0, len(marketInfo)):
            stocks[i].updateStockInfo(marketInfo[i][0], marketInfo[i][1], marketInfo[i][2], marketInfo[i][3]) #ticker, networth, div ratio, volatility
            
            #for each in stocks:
                #each.updateOrderInfo()
            stocks[i].updateOrderInfo()
            sum = 0

            print("curr" + str(stocks[i].currNetWorth))
            print("prev" + str(stocks[i].prevNetWorth))
            #print(initialCash)
        
            if len(stocks[i].trend) >= 5:
                stocks[i].trend.pop(0)                    
            if stocks[i].currNetWorth > stocks[i].prevNetWorth:
                (stocks[i].trend).append(1)
            elif stocks[i].currNetWorth < stocks[i].prevNetWorth:
                (stocks[i].trend).append(-1)
            else:
                (stocks[i].trend).append(0)

            #print(len(each.trend))
            for j in range(0,len(stocks[i].trend)):
                sum = sum + stocks[i].trend[j]

            print("sum is " + str(sum))
            
            if currCash > (0.25 * initialCash) and sum == 4 and blackList[i] == 0:
                print("WE MADE A BIDDDDDDDD!")
                bid(stocks[i].ticker, stocks[i].getBid()+0.01, 4)
                timeCount = 0
            if currCash < (0.90 * initialCash) and sum <= -3:
                ask(stocks[i].ticker, stocks[i].getAsk()-0.01, numSecurity(stocks[i].ticker))
                timeCount = 0
            else:
                timeCount = timeCount+1
            #if 0.75 * stock[i].ticker * numSecurity(stocks[i].ticker)
            print(currCash)

        if timeCount >= 100:
            for i in range(0, len(marketInfo)):
                if int(numSecurity(stocks[i].ticker)) > 10:
                    ask(stocks[i].ticker, stocks[i].getBid(), numSecurity(stocks[i].ticker))
                    blackList[i] = 1
            timeCount = 0
        print("\n                         " + str(timeCount))
        print(blackList)
        #temp = subscribe("Better_Biddys","gibsonsux")
        #print(temp)

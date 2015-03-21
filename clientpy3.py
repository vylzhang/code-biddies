import socket
import sys

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
            print(temp)
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
            
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Enter username, password, command")
    else:
        arg = sys.argv
        run(arg[1],arg[2],arg[3])
    main()

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
        #self.bid = bid
        #self.ask = ask
        self.prevDividendRatio = currDividendRatio
        self.currDividendRatio = dividendRatio
        self.volitility = volitility
        if len(self.marketHistory) >= 50:
            marketHistory.pop(0)
        marketHistory.append(marketHistory)

    def setShareValue(self):
        # this only needs to get calculated once
        # all actions depend on this long-term stock price
        initialDividendPayout = marketHistory(0) * prevDividendRatio
        decreasefactor = currDividendRatio / prevDividendRatio
        self.ShareValue = initialDividendPayout / (1-dividendRatio)

    def getBid(self):
        # return the bid
        return self.bid

    def getAsk(self):
        # return the ask
        return self.ask

## LEIGHTON
    def main():
        
        stocks = [] #list of lists that will contain the current market information
        for i in range(0, numOfStocks) #instantiate each stock
            x = stocks()
            stocks.append(x)

        #per second loop starts here
        marketInfo = getMarketInfo()
        for stock in stocks
            for stockData in marketInfo:
                stock.updateStockInfo(stockData[0], stockData[1], stockData[2], stockData[3]) #ticker, networth, div ratio, volatilit
        

## VIVIAN

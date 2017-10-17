import CSVFileReader as csvfr
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
#import pandas

"""
Displays a candlestick graph for a given dataset. 

Currently only works with a dictionary, with key 'datetime.date' object
and 'open' 'high' 'low' 'close' data in that order. 

Will eventually:
    be able to take 'open''high''low''close' args in any order
    change name for different data set
    use valid list to produce graph
    use valid SQL database entries to produce graph
    
@param 'dictionary' of valid values. 'bool' to save current graph
"""
class CandlestickGraph():
    def __init__(self):
        self.fileCounter = 0
    
    def produceCandlestickGraph(self, entries, save): 
            
        dates = sorted(entries)
            
        fig, ax1 = plt.subplots()
        
        dateVals = []
        opens = []
        closes = []
        highs = []
        lows = []
        
        for d in dates:
            dateVals.append(mdates.date2num(d))
            opens.append(entries[d][0])
            highs.append(entries[d][1])
            lows.append(entries[d][2])
            closes.append(entries[d][3])
        
        quotes = [tuple([dateVals[i],
                        opens[i], 
                        highs[i], 
                        lows[i], 
                        closes[i]]) for i in range(len(dates))]
            
                            
        candlestick_ohlc(ax1, quotes, width = 0.6, colorup='#53c156', colordown='#ff1717')
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        
        fig.autofmt_xdate()
        fig.tight_layout()
        
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.set_ylim(0,max(max(opens), max(highs), max(closes)))
        ax1.grid(True)
    
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Candlestick Graph')
        plt.legend()
        
        if(save):
            plt.savefig('candlestickgraph_' + str(self.fileCounter)+ '.png')
            self.fileCounter+=1
        #plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
        plt.show()  
 
 
"""
Test main function
"""
if __name__ == "__main__":
    
    csg = CandlestickGraph()
    csg.produceCandlestickGraph(csvfr.getDictionary('Data/bitcoin_price.csv'), False)
from flask import Flask, render_template
from alpha_vantage.timeseries import TimeSeries
from pymongo import MongoClient

app = Flask(__name__)

# Get all symbols (compagnies) that will be shown on the web page
file1 = open("symbolList.txt","r")
symbols=file1.read().splitlines()
file1.close()

# API key and MongoDB connection string
API_KEY = "EBH16WHORBLPBIUA"
MONGO_URI = "mongodb://mongodb:27017/"

# Initialize the Alpha Vantage API client and MongoDB client
ts = TimeSeries(key=API_KEY)
mongo_client = MongoClient(MONGO_URI)

# Get the database and collection objects
db = mongo_client['stock_prices']
collection = db['prices']

# Define a route to fetch and store the latest stock prices
@app.route('/update_prices')
def update_prices():
    
    #delete previous registrations of the stock prices
    collection.delete_many({})

    for symbol in symbols:

    	# Get the latest stock prices
    	data, _ = ts.get_intraday(symbol, interval='1min')

    	# Insert the prices into the MongoDB collection
    	collection.update_one({'_id': symbol}, {'$set': data}, upsert=True)

    return 'prices updated'

# Define a route to display the stock prices on a web page
@app.route('/')
def show_prices():
    # Get the latest prices for all symbols from the MongoDB collection
    latest_prices = collection.find()

    # Extract the price data and convert it to a list of tuples (symbol, price)
    prices = []
    for doc in latest_prices:
        symbol = doc['_id']
        latest_price = float(doc[list(doc.keys())[-1]]['4. close'])
        prices.append((symbol, latest_price))

    # Render the template with the stock prices
    return render_template('prices.html', prices=prices)

if __name__ == '__main__':
    app.run(host="0.0.0.0")

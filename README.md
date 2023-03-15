# financial_App

In order to run this app, you need to enter the directory in a command prompt and run the command __"docker-compose up"__

After the containers have been started, you can go to __localhost:5000__ and should get an empty list if it is the first time you run the app.

To fill the list, you just need to go to __localhost:5000/update_prices__ and let the app get the most recent stock prices available on alpha_vantage 
(the API used for this app)

After it, you can go back to the main page, reload and here are your stock prices for your next investment ;)

If you want to change the symbols (compagnie names on stock market), just edit the symbolList file in the app directory (make sure that the symbol you add are available
on alpha_vantage). Do not put more than 5 compagnies on the list as alpha_vantage free version does offer only 5 calls per minute. 

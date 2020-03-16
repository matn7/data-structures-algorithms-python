from string import ascii_lowercase

message = "The price of the stock is:"
price = "$1100"

print(id(message))

print(message + " " + price)

message = message + " " + price
print(id(message))

greeting = "hello"
user = "majka"
message = "          welcome to the Algorithms course              "

print(len(message))
print(type(message))
print(type(5))
print(id(greeting))

print(greeting.upper(), user.capitalize(), message.strip())
print(message.find('course'))

print(message.split())
message = "welcome-to-the-algorithm"
print(message.split("-"))

my_languages = ['Python', 'Ruby', 'JavaScript']

print("-".join(my_languages))

print(ascii_lowercase)

stock_price = "1100"
print("Today's price for google stock is: {}".format(stock_price))
print(f"Today's price for google stock is: {stock_price}")

today_price = "1100"
yeaterday_price = "1000"

print("Today's price: {}, yesterday's price: {}".format(today_price, yeaterday_price))

print(f"Today's price: {today_price}, yesterday's price: {yeaterday_price}")

# \ - escape character
# \n - new line
# \t - tab

print("My name is jon snow and not only \
know nothing but also \
do nothing")

print(""" 
Know nothing
Do nothing
""")



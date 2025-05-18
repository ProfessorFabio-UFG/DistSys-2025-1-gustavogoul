import zmq, time, random
from constPS import *

quotes = [
    "Keep it simple.",
    "Less is more.",
    "Stay hungry, stay foolish.",
    "The best way out is always through.",
    "Do or do not. There is no try."
]

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://" + HOST + ":" + PORT
s.bind(p)

while True:
    time.sleep(5)

    msg_time = str.encode("TIME " + time.asctime())
    msg_date = str.encode("DATE " + time.strftime("%Y-%m-%d"))
    msg_weather = str.encode("WEATHER " + random.choice(["Sunny", "Rainy", "Cloudy", "Windy"]))
    msg_temp = str.encode("TEMP " + str(random.randint(15, 35)) + "°C")
    msg_quote = str.encode("QUOTE " + random.choice(quotes))

    s.send(msg_time)
    s.send(msg_date)
    s.send(msg_weather)
    s.send(msg_temp)
    s.send(msg_quote)

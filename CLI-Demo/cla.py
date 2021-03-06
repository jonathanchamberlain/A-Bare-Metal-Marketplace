import time
from datetime import datetime
def get_node():
    print("")
    print ("Welcome to the Node Dashboard!")
    print("You can enter the name of any node to receieve more information!")
    print("Here is a list of your nodes:")
    print("Node A, Status: In Use")
    print("Node B, Status: In Use")
    print("Node C, Status: In Use")
    print("Node D, Status: In Use")
    print("Node E, Status: In Use")
    while True:
        statement = input("> ")

        if statement == "A" :
          print("Node: A ")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "B" :
          print("Node: B")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "C" :
          print("Node: C ")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "D" :
          print("Node: D ")
          print("Owner: Harvard ECE")
          print("Status: Rented by You and In Use")
          print("Price: Bought at 11$ / hour")
          print("Time: 2.25 hours remaining")

        elif statement == "E" :
          print("Node: F ")
          print("Owner: MIT ECE")
          print("Status: Rented by You and In Use")
          print("Price: Bought at 10$ / hour")
          print("Time: 5.25 hours remaining")

        elif statement == "quit":
            break


        else :
          print("Please enter a valid node or type 'quit' to exit.")
def add_credits():
  print("Please enter the ID of the Organization you would like to give credits to.")
  print("Here is a list of organizations you can give credits to.")
  print("Harvard ECE")
  print("MIT ECE")
  print("BU ECE")
  print("NEU ECE")
  while True:
    statement = input("> ")

    if statement == "Harvard ECE":
      credit_number = input("How many credits would you like to give to Harvard ECE? ")
      print("Transferred {} credits to Harvard ECE!".format(credit_number))
    elif statement == "MIT ECE":
      credit_number = input("How many credits would you like to give to MIT ECE? ")
      print("Transferred {} credits to MIT ECE!".format(credit_number))
    elif statement == "BU ECE":
      credit_number = input("How many credits would you like to give to BU ECE? ")
      print("Transferred {} credits to BU ECE!".format(credit_number))
    elif statement == "NEU ECE":
      credit_number = input("How many credits would you like to give to NEU ECE? ")
      print("Transferred {} credits to NEU ECE!".format(credit_number))
    elif statement == "quit":
      break
    else:
      print("Please enter a valid Organization ID or type quit to exit.")
def remove_credits():
  print("Please enter the ID of the Organization you would like to remove credits from.")
  print("Here is a list of organizations you can remove credits from.")
  print("Harvard ECE")
  print("MIT ECE")
  print("BU ECE")
  print("NEU ECE")
  while True:
    statement = input("> ")

    if statement == "Harvard ECE":
      credit_number = input("How many credits would you like to give to Harvard ECE? ")
      print("Transferred {} credits to Harvard ECE!".format(credit_number))
    elif statement == "MIT ECE":
      credit_number = input("How many credits would you like to give to MIT ECE? ")
      print("Transferred {} credits to MIT ECE!".format(credit_number))
    elif statement == "BU ECE":
      credit_number = input("How many credits would you like to give to BU ECE? ")
      print("Transferred {} credits to BU ECE!".format(credit_number))
    elif statement == "NEU ECE":
      credit_number = input("How many credits would you like to give to NEU ECE? ")
      print("Transferred {} credits to NEU ECE!".format(credit_number))
    elif statement == "quit":
      break
    else:
      print("Please enter a valid Organization ID or type quit to exit.")
def rent_node():
  print("Welcome to the interactive Bare Metal Renting Service!")
  cpu = input("How many CPUs do you need? ")
  ram = input("How much RAM do you need (in GB) ")
  timing = input("How long do you need access to the node for? ")
  price = input("What is the max price you are willing to rent the node for? ")

  print("You requested {} CPUs, {} GB of RAM, for {} at a {} max price.".format(cpu, ram, timing, price))
  print("Running your specifications through our Auction Engine...")
  time.sleep(5)
  now = datetime. now()
  current_time = now.strftime("%H:%M:%S")
  print("A match has been found. You will be given access to Node A for {} starting at {}".format(timing,current_time))
def sell_node():
  print("Welcome to the interactive Bare Metal Selling Service!")
  cpu = input("How many CPUs does your node have? ")
  ram = input("How much RAM does it have (in GB) ")
  timing = input("How long can you sell access to the node for? ")

  print("You are selling a bare metal node with {} CPUs, {} RAM for {}.".format(cpu, ram, timing))
  print("Running your specifications through our Auction Engine...")
  time.sleep(3)
  print("Mutliple matches have been identified. Our Auction Engine is currently determining the price.")
  time.sleep(3)
  now = datetime. now()
  current_time = now.strftime("%H:%M:%S")
  print("A match has been found! You will be renting your node out for {} starting at {}. The price determined was $400.".format(timing,current_time))
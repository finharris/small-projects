# show how much it costs for how long
# ask how long staying for
# calculate ticket cost

# insert coins
# ensure only correct coins entered
# recieved correct amount for ticket?
# no -> keep inserting
# yes -> make sound to show correct money recieved

# press button to get ticket
# print ticket
# include current date and time and expire date and time
# no change returned


from datetime import timedelta, datetime

def calculateTicketCost(stay_duration, cost_per_hour):
  # 2 standard flat fee
  return (cost_per_hour * stay_duration) + 2

def createTicket(ticket_cost, entered_amount, stay_duration):
  now_date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  expire_date_time = (datetime.now() + timedelta(hours=int(stay_duration))).strftime("%d/%m/%Y %H:%M:%S")

  
  ticket_message = """-----
  Ticket cost: £{:.2f}
  Entered amount: £{:.2f}
  Stay duration: {} hours
  
  Date issued: {}
  Date expired: {}
  -----
  """.format(ticket_cost, entered_amount, stay_duration, now_date_time, expire_date_time)
  return ticket_message


accepted_coins = [2, 1, 0.5, 0.2, 0.1]
cost_per_hour = 1.25

start_message = f"""\n
-----
Cost per hour: {cost_per_hour}
Accepted coins: {', '.join(['£'+'{:.2f}'.format(i) for i in accepted_coins])}

NO CHANGE GIVEN
-----
"""

print(start_message)

while True:
  try:
    stay_duration = float(input('How long are you staying for in hours? '))
    break
  except Exception as e:
    print('Enter a number.')

ticket_cost = calculateTicketCost(stay_duration, cost_per_hour)
print('Cost: £{:.2f}'.format(ticket_cost))

entered_amount = 0
while entered_amount < ticket_cost:
  try:
    coin_entered = float(input('What coin are you entering? '))
    if coin_entered not in accepted_coins:
      raise TypeError
    else:
      entered_amount += coin_entered
      print('Current amount entered: £{:.2f}\n'.format(entered_amount))
  except Exception as e:
    print('Enter a valid coin.')

print('beep boop. Correct amount entered.\nNo change given.')

# press button
input('Press enter to print ticket...')

print(createTicket(ticket_cost, entered_amount, stay_duration))
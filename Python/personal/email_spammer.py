import smtplib, ssl
import random

port = 465  # For SSL
password = "T26bhNJtC6KV" # input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Send email here

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	while True:
		sender_email = "doe34027@gmail.com"
		# receiver_email = str(input("What is the email you want to send to? "))
		receiver_email = "harrf2016@swbgs.com"
		while True:
			try:
				# amt = int(input("How many do you want to send? "))
				amt = 10
				break
			except ValueError:
				print("Not a whole number.")
				continue

		server.login(sender_email, password)

		# TODO: Send email here
		count = 0
		while count < amt:
			msg = str(random.randint(1,100))
			server.sendmail(sender_email, receiver_email, msg)
			count += 1
			print("Sent message number {} to {} from {}.".format(count, receiver_email, sender_email))

		done = str(input("Do you want to do another spam y/n? "))
		if done.lower() == "y":
			continue
		elif done.lower() == "n":
			break
		else:
			print("Not a valid option.")
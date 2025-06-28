emails = []

with open('emails.txt', 'r') as file:
  for email in file:
    print(email)
    emails.append(email.split(' ')[-1][1:-2])
    
with open('final_emails.txt', 'w') as file:
  for email in emails:
    file.write(f'{email}\n')
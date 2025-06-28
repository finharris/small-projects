from bs4 import BeautifulSoup

with open('f.txt', 'r', encoding='utf8') as file:
  soup = BeautifulSoup(file, 'html.parser')
  body = soup.body
  lnLepds = body.findAll('div', class_='LnLepd')
  
  names=[]
  for i, l in enumerate(lnLepds):
    if i == 0:
      continue
    names.append(l.find(text=True))
  
  with open('student_names.txt', 'a') as namesFile:
    for  name in names:
      namesFile.write(f'\n{name}')

from Services.PrintWeb import print_web
from Services.SendEmail import send_email
from datetime import datetime
from Services.SendEmail import send_email2
#Get atual date
date = datetime.today().strftime('%m-%d-%y')    
path = f"C:\\Users\\Acer\\Desktop\\Arquivos\\Py\\Screenshot_Email\\Prints\\Print  {date}.png"

print_web(path)

send_email2()

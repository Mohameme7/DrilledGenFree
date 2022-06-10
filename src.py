import json
import os
from colorama import Fore, init
import httpx
import time
init(convert=True)
session = httpx.Client()





def menu():
    os.system('cls; clear')
    logo = f'''{Fore.LIGHTCYAN_EX}
    ██████╗░██████╗░██╗██╗░░░░░██╗░░░░░███████╗██████╗░  ░██████╗░███████╗███╗░░██╗
    ██╔══██╗██╔══██╗██║██║░░░░░██║░░░░░██╔════╝██╔══██╗  ██╔════╝░██╔════╝████╗░██║
    ██║░░██║██████╔╝██║██║░░░░░██║░░░░░█████╗░░██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
    ██║░░██║██╔══██╗██║██║░░░░░██║░░░░░██╔══╝░░██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
    ██████╔╝██║░░██║██║███████╗███████╗███████╗██████╔╝  ╚██████╔╝███████╗██║░╚███║
    ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
    {Fore.LIGHTRED_EX}
    (1) Generate (2) Set API Key 
    
    {Fore.RESET}
    '''

    for line in logo.split('\n'):
        print(line)
    print(Fore.RESET)
    choiceinput = input("-")
    if choiceinput == "2":
        keyinput = input("Enter your API Key: ")
        with open('key.json', 'w') as file:
            data = {"key" : keyinput}
            json.dump(data, file, indent = 4)
        input(f'\n\n{Fore.LIGHTCYAN_EX}{Fore.RESET}Press enter to go back')
        menu()
    elif choiceinput == "1":

       amountinput = input("Enter amount you wanna generate (Max 50 Daily): ")
       with open('key.json') as f:
           filedata = json.load(f)
           key = filedata[str("key")]
       with open('savedalts.txt', 'a+') as accfile:
        try:
         for amountinput in range(int(amountinput)):
          time.sleep(1)
          generaterequest = session.get("http://drilledalts.xyz/api/gen?key=" + key)

          if generaterequest.status_code == 404:
             print("Error! Your API Key is invalid, Please Change it!")
             input(f'\n\n{Fore.LIGHTCYAN_EX}{Fore.RESET}Press enter to go back')
             menu()
          elif generaterequest.status_code == 200:
            jsonresponse = generaterequest.json()

            email = jsonresponse['email']
            password = jsonresponse['password']
            account = email + ":" + password
            accfile.write(account + '\n')
          elif generaterequest.status_code == 201:
            print("Max Generations Reached Today, come back tomorrow.")
            break
        except:
            print("Error")
       input("press enter to continue")
       menu()
    else:
        input("Error!, Press enter to go back")
        menu()
menu()

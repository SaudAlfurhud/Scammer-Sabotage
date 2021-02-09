import requests
import os
import random
import string


url = 'http://107.161.176.122/~sysupdat/updateyourinfo/index.php'
print("ID, Card Number, Pin, CCV, Account Number, Phone Number, Expire Date")

for i in range(1000):
    ID = '1' + str(random.randint(1,2)) + ''.join(random.choice(string.digits) for i in range(8))
    cardNumber = '45' + ''.join(random.choice(string.digits) for i in range(14))
    Pin = ''.join(random.choice(string.digits) for i in range(4))
    CCV = ''.join(random.choice(string.digits) for i in range(3))
    accountNumber = ''.join(random.choice(string.digits) for i in range(8))
    phoneNumber = '05' + ''.join(random.choice(string.digits) for i in range(8))
    expireDate = str(random.randint(0,12)) + '/' + str(random.randint(21,31))

    requests.post(url, allow_redirects=False, data={
    
        'text': ID,
        'text1': cardNumber,
        'text5': Pin,
        'text2': CCV,
        'text3': accountNumber,
        'text4': phoneNumber,
        'text7': expireDate
        })
    print("Sending...")
    print(ID, cardNumber, Pin, CCV, accountNumber, phoneNumber, expireDate)


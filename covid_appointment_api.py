import requests

pincode=input("Enter the pincode")
date=input("Enter date in dd-mm-yyyy formate")
#pincode='500001'
#date='24-07-2021'

url = '''https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'''.format(pincode, date)
headers = {"accept": "application/json" , "Accept-Language": "en_US"}

r = requests.get(url, headers=headers)


data = r.json()['sessions']

for i in data:
    print("--------------------------------------")
    for j in i:
        
        print('{} : {}'.format(j, i[j]))

print("=======================================================")
print("================================")

for i in data:
    print("----------------------------------------")
    if i['available_capacity']>0:
        for j in i:
            
            print('{} : {}'.format(j, i[j]))
    







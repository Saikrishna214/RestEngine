import requests
import csv

SingleUsr = {
  "method":"Get",
  "input data":"User Name",
  "Status.reason":200,
  "expected data":"Details of User"
  
}

x=SingleUsr.get("Status.reason")

url="https://reqres.in/api/users/2"

response=requests.get(url)

y=response.status_code

if x==y:
    print("pass")
   
with open("Sample tests.csv", 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    for line in csv_dict_reader:
        print(line)

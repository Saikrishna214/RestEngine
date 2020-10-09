import requests
import csv

url="https://reqres.in/api/users/2"

response=requests.get(url)

y=response.status_code

SingleUsr = {
  "method":"Get",
  "input data":"User Name",
  "Status.reason":200,
  "expected data":"Details of User"
  
}

x=SingleUsr.get("Status.reason")

if x==y:
        print('pass')

test_details=[]


with open('Sample tests.csv','r') as csv_file:
    csv_dict_reader=csv.DictReader(csv_file)

    for row in csv_dict_reader:
        Status_Reason=row['Status.Reason']
        Expected_Data=row['Expected Data']
  
        if Status_Reason==200:
            test_details.append({'Test case Title':row['Test case Title'],'Method':row['Method']})  
                      
with open('test_details.csv','w',newline='') as test_details:
    s=['Test case Title','Method']
    
    csv_dict_writer=csv.DictWriter(test_details,fieldnames=s)
    csv_dict_writer.writerheader()
    
    for details in test_details:
        csv_dict_writer.writerow(details)
        
        
        
        
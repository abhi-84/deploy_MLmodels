import requests, json
url = 'http://0.0.0.0:5000/api/'
lst = []

# number of elemetns as input
n = int(input("Enter total number of features, followed by feature values: "))
# iterating till the range
#for i in range(0, n):
ele = float(input("Enter patient 'Age' feature >> "))
lst.append(ele) # adding the element
ele = float(input("Enter patient 'Sex' feature (Female:0; Male:1) >> "))
lst.append(ele) # adding the element
ele = float(input("Enter patient 'BP' feature (High:0; Low:1; Normal:2) >> "))
lst.append(ele) # adding the element
ele = float(input("Enter patient 'Cholestrol' feature (High:0; Low:1; Normal:2) >> "))
lst.append(ele) # adding the element
ele = float(input("Enter patient 'Na_to_K' feature >> "))
lst.append(ele) # adding the element
print("\n")
#print(lst)
data=[lst]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
#print(r,r.text)
print("\npatient is prescibed to take {} medicine based upon patient's given symptoms" .format(r.text[2:9]))

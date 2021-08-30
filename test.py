import requests

BASE = "http://127.0.0.1:5000/"

a = 10

# data = [{"likes" : 10 , "name" : "Ruturaj" , "views" : 100},
#         {"likes" : 100 , "name" : "Tony" , "views" : 1000},
#         {"likes" : 1000 , "name" : "Stark" , "views" : 10000},
#         {"likes" : 10000 , "name" : "Sutar" , "views" : 100000}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(a), data[i])
#     a = a + 1
#     print(response.json())

response1 = requests.get(BASE + "video/10")
print(response1.json())

response = requests.patch(BASE + "video/10", {"name" : "Tony Stark"})
print(response.json())



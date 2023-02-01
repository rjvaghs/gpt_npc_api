import requests

#r = requests.post("http://127.0.0.1:5000/getresponse",data={'Character': input("Who do you want to interview: ")})


for i in range(30):
    r = requests.post("http://127.0.0.1:5000/getresponse", data={'query': input("Question: ")})
    print(r.text, "\n")

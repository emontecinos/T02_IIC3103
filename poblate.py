import json
import requests

#DELETE
def delete_ham(json_obj):  
    i=1
    for j in json_obj:
        url="http://localhost:8000/hamburguesa/{}".format(i)
        # x=requests.post(url,data=j)
        # print(x.text)
        x=requests.delete(url)
        print(x,x.text)
        i+=1
# #POST
def post_ham(json_obj):
    url_i="http://localhost:8000/ingrediente"
    for j in json_obj:
        x=requests.post(url_i,data=j)
        print(x)

#PUT ing in ham
def put_ing_ham(ham_id,ings_id):
    for ing_id in ings_id:
        url="http://localhost:8000/hamburguesa/{}/ingrediente/{}".format(ham_id,ing_id)
        x=requests.put(url)
        print(x)

if __name__ == "__main__":
    json_obj=[]
    with open ('hamburguesas.txt') as json_file:
        for j in json_file:
            hamdict=json.loads(j)
            json_obj.append(hamdict)

    ings=[]
    with open ('ingredientes.txt') as json_file:
        for i in json_file:
            ing=json.loads(i)
            ings.append(ing)
    
    put_ing_ham(8,[1,9])
    put_ing_ham(9,[7])
    put_ing_ham(10,[2,3,6])
    put_ing_ham(11,[1,2,3,4,6,7,8])
    put_ing_ham(12,[1,5])
    put_ing_ham(13,[1,3,5,6,7,8,9])



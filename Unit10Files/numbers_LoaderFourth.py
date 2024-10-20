import json


username =input('enter your name')#prompt通常被用作提示
file_name='username.json'
with open(file_name,'w') as fobj:
    json.dump(username , fobj)
    print('we will rememeber you ')
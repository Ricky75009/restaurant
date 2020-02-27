print('love')
import cgi
import http.server
import socketserver
import os
path="/Users/macbook/Desktop/Roman/Scolaire/CODE/Projects/8- SE_foundation/foundations-restaurant/restaurants.txt"
resto_area=[]
resto_classes=[]
list_of_res=[]
file_data = open(path, 'r')
list_of_res=file_data.readlines()






number_of_res=len(list_of_res)
for i in range(number_of_res):
    resto_area.append(list_of_res[i].split(','))


for i in resto_area:
    i[1]=i[1][:-1]

class Restaurants():
    '''this is about having restaurants'''
    def __init__(self,name,area):
        self.name=name
        self.area=area


for i in range (len(resto_area)):
    temp = Restaurants(resto_area[i][0],resto_area[i][1])
    resto_classes.append(temp)     



    
index_text='''<!DOCTYPE html>
   <html lang="en">
   <head>
    <title>restaurants in town</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
   </head>  
  

   <body style="background-color:pink">'''

for i in range(number_of_res):
       index_text=index_text+f'''
    <h1 style="font-family: arial; font-style: italic">{resto_classes[i].name} is a good restaurant in {resto_classes[i].area}</h1>'''
    
index_text=index_text+''' 
</body>
</html>'''

def create_index(index_text):
    file= open("index.html","w+")
    file.write(index_text)
    file.close()
create_index(index_text)

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running on port", PORT)
    httpd.serve_forever()




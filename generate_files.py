import os

location = os.path.expanduser('~')
location2 = os.path.join(location,"\\Desktop")




string = ""
for i in range(100):
    string = string + "Let us celebrate the life and have a tea\n\n"



   
filecount = 0
for filecount in range(10):
    file = open('texter{}.txt'.format(filecount),'w')
    file.write(string)
   
    file.close()
    filecount =+ 1

for filecount in range(10):
    file = open('texter{}.txt'.format(filecount),'wb')
    ###Enter the amount of file size you wish to create.
    
    file.seek(10745-1)

    file.write(b"\0")
    
   
    file.close()



print(os.walk("."))







#exercise 5
#with try and except
print("Health management system")
client_list={1:"Harry",2:"Rohan",3:"Hamad"}
log_list={1:"Exercise",2:"Diet"}

def getdata():
    import datetime
    return datetime.datetime.now()

try:
    print("select client name")
    for key,value in client_list.items():
        print("press",key,"for",value,"\n",end="")
        client_name=int(input())

        print("selected client:",client_list[client_name],"\n",end="")

        print("press 1 for log")
        print("press 2 for retrieve")
        op=int(input())
        if op==1:
            for key,value in log_list.items():
                print("press",key,"to log",value,"\n",end="")
                log_name=int(input())
                print("selected job:",log_list[log_name])
                f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
                k="y"
                while(k is not n):
                    print("enter",log_list[log_name],"\n",end="")
                    mytext=input()
                    f.write("["+str(getdata())+"]:"+mytext+"\n")
                    k=input("ADD MORE?y/n:")
                    continue
                f.close()
        elif op==2:
                for key, value in log_list.items():
                    print("press", key, "to retrieve", value, "\n", end="")
                    log_name = int(input())
                    print(client_list[client_name],"-",log_list[log_name],"report:","\n",end="")
                    f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt")
                    contents =f.readlines()
                    for line in contents:
                        print(line,end="")
                    f.close()
        else:
            print("invalid input")
except Exception as e:
    print("wrong input")











import time

with open('/var/log/auth.log', 'r') as inf:
    a = ''
    timeattace = ''
    count = 0
    while True: 
        position = inf.tell() #Текущая позиция указателя — это позиция (количество байт), с которой будет осуществляться следующее чтение/запись.
        line = inf.readline()
        if not line:
            time.sleep(1)
            inf.seek(position)
        else:
            a = line.split(' ')
            for i in range (len(a)-2):
                if a[i] == "Failed" and a[i+1] == "password":
                    if count == 0:
                        timeattace = a[3]
                    count += 1
            if count == 8:
                print ("BRUTE FORCE!",timeattace, "SSH")
                count = 0
                timeattace = ''
from datetime import date




## 13.1

now = date.today()

fmt = "It's %A, %B %d, %Y"
print (now.strftime(fmt))

fout = open('today.txt', 'wt')
print(now.strftime(fmt), file=fout)
fout.close()

## 13.2

fin = open('today.txt', 'rt')
today_string = fin.read()
fin.close()

## 13.3

##format = "%d"
##today_string.strptime(today_string, format)

##print(format)

#15.1

import multiprocessing,time,datetime



def loop(name):

    start = time.time()
    process1 = loop.process1()
    process2 = loop.process1()
    process3 = loop.process1()

    print(datetime.datetime.now())
    if __name__=="__main__":
        
        
        
        p1 = multiprocessing.Process(target=process1)
        p2 = multiprocessing.Process(target=process2)
        p3 = multiprocessing.Process(target=process3)

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()

    end = time.time()
        

    print("It takes " +str(end-start)+" seconds")

if __name__=="__main__":
    loop("main") 


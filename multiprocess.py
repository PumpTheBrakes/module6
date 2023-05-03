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
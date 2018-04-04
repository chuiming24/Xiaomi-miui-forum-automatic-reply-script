import post,time

t=0
#post.main()
wait=161
errmax=900
err=0
while(t<900):
    
    try:
        tm=0
        post.main()
        t=t+1
        err=0
    except Exception as e:
        print('ERR!')
        print(e)
        tm=int(wait*9/10)+err
        err=err+1;

    if(err>errmax):
        raise RuntimeError("ERR LIMIT")
    
    while(tm<wait):
        time.sleep(1)
        tm=tm+1
        if(tm%10==0):
            print('tm:%3d' % tm,end=' ')
    
    
    print('t:'+str(t))

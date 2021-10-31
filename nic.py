while True :
    num=input("Input:    ") #input 9 digit NIC number
    d={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    year="19"+num[0:2] #derive year
    x=int(num[2:5])
    if x > 500 :
        x -= 500
        gender = 'F'
    else :
        gender = "M"

    total,month = 0,0

    for i in d.values():
        total = total+i
        month += 1     #month
        if total > x:
            date = x-(total - i )
            break
    if month < 10:
        month="0"+str(month)
    print("Output:   "+year+"-"+str(month)+"-"+str(date)+"\n"+"          "+gender)


   

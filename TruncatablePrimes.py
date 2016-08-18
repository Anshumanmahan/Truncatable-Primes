for i in range(1,10000):
        flag = 0
        temp = 0
        temp1 = 0
        temp2 = 0
        z = 0
        z1 = 0
        x = 0
        y = 0
        sav = i
        count = i
        new = count
        while(new > 0):
                y = new%10
                x = x*10 + y
                new = new/10
          
        x1 = x/10       
        while(i>0):
                i=i/10
                flag = flag + 1
                
        while(sav>0):
                if(sav == 1):
                        break
                for j in range(2,sav-1):
                        if(sav%j == 0):
                                z = z+1  
                if(z >= 1):
                        break 
                else:           
                        sav = sav/10
                        temp = temp + 1       
        
        
        while(x1>0):
                if(x1 == 1):
                        break

                for j in range(2,x1-1):
                        if(x1%j == 0):
                                z1 = z1+1
                                temp2 = temp2 + 1  
                
                if(z1 >= 1):
                        break 
                else:           
                        x1 = x1/10
                        temp1 = temp1 + 1
                                 
           
        if(temp == flag and temp1 == flag-1):
                print count
                
                

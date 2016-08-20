sum = 0
for i in range(10,1000000):
        flag = 0
        temp = 0
        temp1 = 0
        temp2 = 0
        z = 0
        z1 = 0
        x = 0
        y = 0
        y1 = 0
        sav = i
        count = i
        new = count
        
        while(new > 0):
                y = new%10
                x = x*10 + y
                new = new/10
          
        x1 = x/10       
        
        while(i > 0):
                i=i/10
                flag = flag + 1
                
        while(sav > 0):
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
        
        
        while(x1 > 0):
		x2 = x1
		x3 = 0
		while(x2 > 0):
		        y1 = x2 % 10
		        x3 = x3*10 + y1
		        x2 = x2/10
		          
                if(x3 == 1):
                        break

                for j in range(2,x3-1):
                        if(x3%j == 0):
                                z1 = z1+1
                                temp2 = temp2 + 1  
                
                if(z1 >= 1):
                        break 
                else:           
                        x1 = x1/10
                        temp1 = temp1 + 1
                                 
           
        if(temp == flag and temp1 == flag-1):
                print count
                sum = sum + count
        
print sum                
                

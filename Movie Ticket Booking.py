#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


pip install PyAudio


# In[3]:


pip install py-media-player==1.0.1


# In[2]:


pip install ffpyplayer


# In[2]:


import numpy as np
from ffpyplayer.player import MediaPlayer


# In[4]:


class Idoxcinema:
    def __init__(rp):
        from colorama import Fore,Style
        print(Fore.RED,Style.BRIGHT+"\t\t\t\t\t      I-DOX CINEMA",Fore.BLACK,Style.BRIGHT+"\t\t\t\t\t\t   www.idoxcinema.com")
        
        
        print(Fore.BLUE,Style.BRIGHT+"\t\t\t\t\t (A unit of INOX cinema)")
        print("\t\t\t\t\t  A PVR INOX Experience")
        
    def Shershah(rp):

        r=input("\ndo you want to see trailer before booking (yes/no)")
        if r=="yes":
            import cv2 as cv
            capture = cv.VideoCapture("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Shershah.mp4")
            player=MediaPlayer("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Shershah.mp4")
            if(capture.isOpened()==False):
                print("Error opening the trailer")
                
            while(capture.isOpened()):
                ret,frame=capture.read()
                audio_frame,val=player.get_frame()
                if ret==True:
                    cv.imshow('frame',frame)
                    if cv.waitKey(20) & 0xff==ord('q'):
                        break
                else:
                    break
        
            capture.release()
            cv.destroyAllWindows()
            player.close_player()
        else:
            pass
        w=["9:00 AM","12:20 PM","4:00 PM","7;20 PM","10:45 PM"]
        print("\nTime Slot:",w)
        w=input("\nselect the time at which you want to book(Please give space befor writing (AM/PM)):")
        if w=="9:00 AM" or w=="12:20 PM" or w=="4:00 PM" or w=="7;20 PM" or w=="10:45 PM" or w=="9:00 am" or w=="12:20 pm" or w=="4:00 pm" or w=="7;20 pm" or w=="10:45 pm" :
            x=["EXECUTIVE","CLUB","ROYAL","ROYAL RECLINER","ROYAL EXECUTIVE RECLINER"]
            y=[160,190,250,330,460]
            Shershah={"SEAT CLASS":x,"PRICE":y}
            import pandas as pd
            df=pd.DataFrame(Shershah)
            print("\n\n Shershah")
            print(df)
            d=[]
            while x:
             
                b=int(input("enter the seat class no. you want to book:"))
                c=int(input("Enter the no. of seat you want to book"))
                z=Shershah["PRICE"][b]
                y=z*c
                d.append(y)
                break 
            t=sum(d)
            m=(sum(d)*0.18)
            k=t+m
            print("Amount:",t,"Rupees")
            print("Taxes:",m)
            print("Total amount:",k,"Rupees")
            print("Taking you to the payment page.")
            payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
            if payment=="paytm" or payment=="Paytm":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="phonepe" or payment=="Phonepe":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.waitKey()
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey() 
                print("Your Booking Was Confirmed.Thank you!")
            else:
                print(" Wrong payment option choosen")
            import random
            book=random.randint(1001,100000)   
            print("\n\nBOOKING DETAILS:\n")
            print("Booking no.:",book)
            print("Movie Name: Shershah")
            print("Ticket Booked:",c)
            print("Time:",w)
            print("Screen: NA-3")
            print("Payment Type:",payment)  
                
        else:
            print("No Show was availiable at this time")
        
        if w=="9:00 AM" or w=="12:20 PM" or w=="4:00 PM" or w=="7;20 PM" or w=="10:45 PM" or w=="9:00 am" or w=="12:20 pm" or w=="4:00 pm" or w=="7;20 pm" or w=="10:45 pm":
        
            f=input("\n\nDo you want to pre-book your food (yes/no)")
            if f=="yes":
                i=["OTC Pizza","Popcorn","Pepsi","Sprite","Mountain Due","Burger","Cheese Popcorn"]
                p=[345,220,80,80,80,140,320]
                food={"ITEM":i,"Price":p}
                import pandas as pd
                df=pd.DataFrame(food)
                print("\n\n FOOD MENU")
                print(df)
                j=[]
                while i:
                    i=True
                    item=int(input("\nEnter the code of the food you want to order:"))
                    Quan=int(input("How much Quatity you want to order:"))
                    pr=food["Price"][item]
                    Qa=Quan*pr
                    j.append(Qa)
                    x=input("Do you want to order more?(yes/no)")
                    if x=="no":
                        print("please check the amount")
                        break
                
                j1=sum(j)
                j2=(j1*0.05)
                j3=j1+j2
                print("Amount:",j1,"Rupees")
                print("Tax:",j2)
                print("Total Amount:",j3,"Rupees")
                print("Taking you to the payment page.")
                payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
                if payment=="paytm" or payment=="Paytm":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                
                    print("Your Food Order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="phonepe" or payment=="Phonepe":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                    print("Your Food Order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey() 
                    print("Your Food order Was Confirmed for your recent movie booking. Thank you!")
                else:
                    print("Wrong payment option choosen")  
            
            
            
            
    def sam_bahadur(rp):
        r=input("\ndo you want to see trailer before booking (yes/no)")
        if r=="yes":
            import cv2 as cv
            capture = cv.VideoCapture("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Sam bahadur.mp4")
            player=MediaPlayer("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Sam bahadur.mp4")
            if(capture.isOpened()==False):
                print("Error opening the trailer")
                
            while(capture.isOpened()):
                ret,frame=capture.read()
                audio_frame,val=player.get_frame()
                if ret==True:
                    cv.imshow('frame',frame)
                    if cv.waitKey(20) & 0xff==ord('q'):
                        break
                else:
                    break
                    
            capture.release()
            cv.destroyAllWindows()
            player.close_player()
        else:
            pass
        
        w=["7:00 AM","11:00 AM","3:30 PM","5:20 PM","8:45 PM","11:00 PM"]
        print("\nTime Slot:",w)
        w=input("\nselect the time at which you want to book")
        if w=="7:00 AM" or w=="11:00 AM" or w=="3:30 PM" or w=="5;20 PM" or w=="8:45 PM" or w=="11:00 PM" or w=="7:00 am" or w=="11:00 am" or w=="3:30 pm" or w=="5;20 pm" or w=="8:45 pm" or w=="11:00 pm":
            x=["EXECUTIVE","CLUB","ROYAL","ROYAL RECLINER","ROYAL EXECUTIVE RECLINER"]
            y=[160,190,250,330,460]
            sam_bahadur={"SEAT CLASS":x,"PRICE":y}
            import pandas as pd
            df=pd.DataFrame(sam_bahadur)
            print("\n\n Sam Bahadur")
            print(df)
            d=[]
            while x:
                b=int(input("enter the position of the seat class:"))
                c=int(input("Enter the no. of seat you want to book"))
                z=sam_bahadur["PRICE"][b]
                y=z*c
                d.append(y)
                break
        
            t=sum(d)
            m=(sum(d)*0.18)
            k=t+m
            print("Amount:",t,"Rupees")
            print("Taxes:",m)
            print("Total amount:",k,"Rupees") 
            print("Taking you to the payment page.")
            payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
            if payment=="paytm" or payment=="Paytm":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="phonepe" or payment=="Phonepe":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey() 
                print("Your Booking Was Confirmed.Thank you!")
            else:
                print(" Wrong payment option choosen")
            import random
            book=random.randint(1001,100000)    
            print("\n\nBOOKING DETAILS:\n")
            print("Booking NO.:",book)
            print("Movie Name: Sam Bahadur")
            print("Ticket Booked:",c)
            print("Time:",w)
            print("Screen: NA-2")
            print("Payment Type:",payment)    
        else:
            print("No show was availiable at this time!")
        
        if w=="7:00 AM" or w=="11:00 AM" or w=="3:30 PM" or w=="5:20 PM" or w=="8:45 PM" or w=="11:00 PM" or w=="7:00 am" or w=="11:00 am" or w=="3:30 pm" or w=="5;20 pm" or w=="8:45 pm" or w=="11:00 pm":
        
        
        
                f=input("\n\nDo you want to pre-book your food (yes/no)")
                if f=="yes":
                    i=["OTC Pizza","Popcorn","Pepsi","Sprite","Mountain Due","Burger","Cheese Popcorn"]
                    p=[345,220,80,80,80,140,320]
                    food={"ITEM":i,"Price":p}
                    import pandas as pd
                    df=pd.DataFrame(food)
                    print("\n\n FOOD MENU")
                    print(df)
                    j=[]
                    while i:
                        i=True
                        item=int(input("\nEnter the code of the food you want to order:"))
                        Quan=int(input("How much Quatity you want to order:"))
                        pr=food["Price"][item]
                        Qa=Quan*pr
                        j.append(Qa)
                        x=input("Do you want to order more?(yes/no)")
                        if x=="no":
                            print("Taking you to the Payment page,Please wait.\n")
                            break
                    j1=sum(j)
                    j2=(j1*0.05)
                    j3=j1+j2
                    print("Amount:",j1,"Rupees")
                    print("Tax:",j2)
                    print("Total Amount:",j3,"Rupees")
                    print("Taking you to the payment page.")
                    payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
                
                    if payment=="paytm" or payment=="Paytm":
                        import cv2 as cv
                        img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                        cv.imshow("img4",img)
                        cv.waitKey()
                
                        print("Your Food Order Was Confirmed for your recent movie booking.Thank you!")
                    elif payment=="phonepe" or payment=="Phonepe":
                        import cv2 as cv
                        img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                        cv.imshow("img4",img)
                        cv.waitKey()
                        print("Your Food Order Was Confirmed for your recent movie booking.Thank you!")
                    elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                        import cv2 as cv
                        img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                        cv.imshow("img4",img)
                        cv.waitKey() 
                        print("Your Food Order Was Confirmed for your recent movie booking.Thank you!")
                    else:
                        print("Wrong payment option Choosen")
        
        
    def omg(rp):
        r=input("\ndo you want to see trailer before booking (yes/no)")
        if r=="yes":
            import cv2 as cv
            capture = cv.VideoCapture("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\OMG2.mp4")
            player=MediaPlayer("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\OMG2.mp4")
            if(capture.isOpened()==False):
                print("Error opening the trailer")
                
            while(capture.isOpened()):
                ret,frame=capture.read()
                audio_frame,val=player.get_frame()
                if ret==True:
                    cv.imshow('frame',frame)
                    if cv.waitKey(20) & 0xff==ord('q'):
                        break
                else:
                    break

        
            capture.release()
            cv.destroyAllWindows()
            player.close_player()
        else:
            pass
        
        w=["9:30 AM","7;40 PM"]
        print("Time Slot:",w)
        w=input("\nselect the time at which you want to book")
        if w=="9:30 AM" or w=="7:40 PM" or w=="9:30 am" or w=="7:40 pm":
            x=["EXECUTIVE","CLUB","ROYAL","ROYAL RECLINER","ROYAL EXECUTIVE RECLINER"]
            y=[160,190,250,330,460]
            omg_={"SEAT CLASS":x,"PRICE":y}
            import pandas as pd
            df=pd.DataFrame(omg_)
            print("\n\n OMG 2")
            print(df)
            d=[]
            while x:
                b=int(input("enter the position of the seat class:"))
                c=int(input("Enter the no. of seat you want to book"))
                z=omg_["PRICE"][b]
                y=z*c
                d.append(y)
                break
            t=sum(d)
            m=(sum(d)*0.18)
            k=t+m
            print("Amount:",t,"Rupees")
            print("Taxes:",m)
            print("Total amount:",k,"Rupees") 
            print("Taking you to the payment page.")
            payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
            if payment=="paytm" or payment=="Paytm":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="phonepe" or payment=="Phonepe":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey() 
                print("Your Booking Was Confirmed.Thank you!")
            else:
                print(" Wrong payment option choose")
            import random
            book=random.randint(1001,100000)    
            print("\n\nBOOKING DETAILS:\n")
            print("Booking NO.:",book)
            print("Movie Name: OMG 2")
            print("Ticket Booked:",c)
            print("Time:",w)
            print("Screen: NA-1")
            print("Payment Type:",payment)    
        else:
            print("No show was availiable at this time!")
                
        if w=="9:30 AM" or w=="7:40 PM" or w=="9:30 am" or w=="7:40 pm":
        
        
        
            f=input("\n\nDo you want to pre-book your food (yes/no)")
            if f=="yes":
                i=["OTC Pizza","Popcorn","Pepsi","Sprite","Mountain Due","Burger","Cheese Popcorn"]
                p=[345,220,80,80,80,140,320]
                food={"ITEM":i,"Price":p}
                import pandas as pd
                df=pd.DataFrame(food)
                print("\n\n FOOD MENU")
                print(df)
                j=[]
                while i:
                    i=True
                    item=int(input("\nEnter the code of the food you want to order:"))
                    Quan=int(input("How much Quatity you want to order:"))
                    pr=food["Price"][item]
                    Qa=Quan*pr
                    j.append(Qa)
                    x=input("Do you want to order more?(yes/no)")
                    if x=="no":
                        print("please check the amount")
                        break 
                        
                j1=sum(j)
                j2=(j1*0.05)
                j3=j1+j2
                print("Amount:",j1,"Rupees")
                print("Tax:",j2)
                print("Total Amount:",j3,"Rupees")
                print("Taking you to the payment page.")
                payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
                
                if payment=="paytm" or payment=="Paytm":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="phonepe" or payment=="Phonepe":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey() 
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                else:
                    print("Wrong payment option choosen")
            
            
            
    def Attack(rp):
        r=input("do you want to see trailer before booking (yes/no)")
        if r=="yes":
            import cv2 as cv
            capture = cv.VideoCapture("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\AttackOf2611.mp4")
            player=MediaPlayer("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\AttackOf2611.mp4")
            if(capture.isOpened()==False):
                print("Error opening the trailer")
                
            while(capture.isOpened()):
                ret,frame=capture.read()
                audio_frame,val=player.get_frame()
                if ret==True:
                    cv.imshow('frame',frame)
                    if cv.waitKey(20) & 0xff==ord('q'):
                        break
                else:
                    break
        
            capture.release()
            cv.destroyAllWindows()
            player.close_player()
            
        else:
            pass
        
        w=["6:30 AM","4:30 PM"]
        print("Time Slot:",w)
        w=input("\nselect the time at which you want to book")
        if w=="6:30 AM" or w=="4:30 PM" or w=="6:30 am" or w=="4:30 pm":
            x=["EXECUTIVE","CLUB","ROYAL","ROYAL RECLINER","ROYAL EXECUTIVE RECLINER"]
            y=[160,190,250,330,460]
            akeli_={"SEAT CLASS":x,"PRICE":y}
            import pandas as pd
            df=pd.DataFrame(Attack)
            print("\n\n Attack of 26/11")
            print(df)
            d=[]
            while x:
                b=int(input("enter the position of the seat class:"))
                c=int(input("Enter the no. of seat you want to book"))
                z=Attack["PRICE"][b]
                y=z*c
                d.append(y)
                break
            t=sum(d)
            m=(sum(d)*0.18)
            k=t+m
            print("Amount:",t,"Rupees")
            print("Taxes:",m)
            print("Total amount:",k,"Rupees")
            print("Taking you to the payment page.\n\n")
            payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
            if payment=="paytm" or payment=="Paytm":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="phonepe" or payment=="Phonepe":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey() 
                print("Your Booking Was Confirmed.Thank you!")
            else:
                print(" Wrong payment option choosen")
            import random
            book=random.randint(1001,100000)    
            print("\n\nBOOKING DETAILS:\n")
            print("Booking No.:",book)
            print("Movie Name: Attack of 26/11")
            print("Ticket Booked:",c)
            print("Time:",w)
            print("Screen: NA-4")
            print("Payment Type:",payment)    
        else:
            print("No show was availiable at this time!")       
                
        if w=="6:30 AM" or w=="4:30 PM" or w=="6:30 am" or w=="4:30 pm":
        
        
        
            f=input("\n\nDo you want to pre-book your food (yes/no)")
            if f=="yes":
                i=["OTC Pizza","Popcorn","Pepsi","Sprite","Mountain Due","Burger","Cheese Popcorn"]
                p=[345,220,80,80,80,140,320]
                food={"ITEM":i,"Price":p}
                import pandas as pd
                df=pd.DataFrame(food)
                print("\n\n FOOD MENU")
                print(df)
                j=[]
                while i:
                    i=True
                    item=int(input("\nEnter the code of the food you want to order:"))
                    Quan=int(input("How much Quatity you want to order:"))
                    pr=food["Price"][item]
                    Qa=Quan*pr
                    j.append(Qa)
                    x=input("Do you want to order more?(yes/no)")
                    if x=="no":
                        print("please check the amount")
                        break 
                        
                j1=sum(j)
                j2=(j1*0.05)
                j3=j1+j2
                print("Amount:",j1,"Rupees")
                print("Tax:",j2)
                print("Total Amount:",j3,"Rupees")
                print("Taking you to the payment page.")
                payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
                
                if payment=="paytm" or payment=="Paytm":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="phonepe" or payment=="Phonepe":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey() 
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")    
                else:
                    print("Wrong payment option choosen")     
                        
            
    def mission(rp):
        r=input("do you want to see trailer before booking (yes/no)")
        if r=="yes":
            import cv2 as cv
            capture = cv.VideoCapture("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Mission Mangal.mp4")
            player=MediaPlayer("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\Mission Mangal.mp4")
            if(capture.isOpened()==False):
                print("Error opening the trailer")
                
            while(capture.isOpened()):
                ret,frame=capture.read()
                audio_frame,val=player.get_frame()
                if ret==True:
                    cv.imshow('frame',frame)
                    if cv.waitKey(20) & 0xff==ord('q'):
                        break
                else:
                    break

        
            capture.release()
            cv.destroyAllWindows()
            player.close_player()
        else:
            pass
        
        w=["6:00 AM","1:00 PM","4:20 PM","11:00 PM"]
        print("Time Slot:",w)
        w=input("\nselect the time at which you want to book")
        if w=="6:00 AM" or w=="1:00 PM" or w=="4:20 PM" or w=="11:00 PM" or w=="6:00 am" or w=="1:00 pm" or w=="4:20 pm" or w=="11:00 pm":
            x=["EXECUTIVE","CLUB","ROYAL","ROYAL RECLINER","ROYAL EXECUTIVE RECLINER"]
            y=[160,190,250,330,460]
            mission_={"SEAT CLASS":x,"PRICE":y}
            import pandas as pd
            df=pd.DataFrame(mission_)
            print("\n\n MISSION MANGAL")
            print(df)
            d=[]
            while x:
                b=int(input("enter the position of the seat class:"))
                c=int(input("Enter the no. of seat you want to book"))
                z=mission_["PRICE"][b]
                y=z*c
                d.append(y)
                break
            t=sum(d)
            m=(sum(d)*0.18)
            k=t+m
            print("Amount:",t,"Rupees")
            print("Taxes:",m)
            print("Total amount:",k,"Rupees")
            print("Taking you to the payment page.")
            payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
            if payment=="paytm" or payment=="Paytm":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="phonepe" or payment=="Phonepe":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey()
                print("Your Booking Was Confirmed.Thank you!")
            elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                import cv2 as cv
                img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                cv.imshow("img4",img)
                cv.waitKey() 
                print("Your Booking Was Confirmed.Thank you!")
            else:
                print(" Wrong payment option choosen")
            import random
            book=random.randint(1001,100000)    
            print("\n\nBOOKING DETAILS:\n")
            print("Booking No.:",book)
            print("Movie Name: Mission Mangal")
            print("Ticket Booked:",c)
            print("Time:",w)
            print("Screen: NA-1")
            print("Payment Type:",payment)    
                
        else:
            print("No show was availiable at this time!")        
                
        if w=="6:00 AM" or w=="1:00 PM" or w=="4:20 PM" or w=="11:00 PM" or w=="6:00 am" or w=="1:00 am" or w=="4:20 pm" or w=="11:00 pm":
        
        
        
            f=input("\n\nDo you want to pre-book your food (yes/no)")
            if f=="yes":
                i=["OTC Pizza","Popcorn","Pepsi","Sprite","Mountain Due","Burger","Cheese Popcorn"]
                p=[345,220,80,80,80,140,320]
                food={"ITEM":i,"Price":p}
                import pandas as pd
                df=pd.DataFrame(food)
                print("\n\n FOOD MENU")
                print(df)
                j=[]
                while i:
                    i=True
                    item=int(input("\nEnter the code of the food you want to order:"))
                    Quan=int(input("How much Quatity you want to order:"))
                    pr=food["Price"][item]
                    Qa=Quan*pr
                    j.append(Qa)
                    x=input("Do you want to order more?(yes/no)")
                    if x=="no":
                        print("please check the amount")
                        break 
                j1=sum(j)
                j2=(j1*0.05)
                j3=j1+j2
                print("Amount:",j1,"Rupees")
                print("Tax:",j2)
                print("Total Amount:",j3,"Rupees")
                print("Taking you to the payment page.")
                payment=input("enter the name of any one app from these given app to which you want to pay \n1)Paytm \n2)Phonepe \n3)GooglePay \nNOTE-> Please do not close the next window till you completed the payment.\n")
                if payment=="paytm" or payment=="Paytm":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="phonepe" or payment=="Phonepe":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey()
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                elif payment=="GooglePay" or payment=="googlepay" or payment=="Googlepay":
                    import cv2 as cv
                    img=cv.imread("C:\\Users\\Sapna\\OneDrive\\Desktop\\Cinema\\QRcode.png")
                    cv.imshow("img4",img)
                    cv.waitKey() 
                    print("Your food order Was Confirmed for your recent movie booking.Thank you!")
                else:
                    print("Wrong payment option choosen")        


obj=Idoxcinema()
ci=["\n\nCities:: 1) Jaipur 2) Ahemdabad 3) Mumbai 4) Delhi 5) Bengluru 6) Pune 7) Gandhinagr(Gujrat) 8) Kolkata 9) Lucknow 10) Chennai 11) Agra 12) Chandigarh 13) Noida 14) Jodhpur 15) Bikaner 16) Surat"]
for k in ci:
    from colorama import Fore,Style
    print(Fore.MAGENTA,Style.BRIGHT+k,end=" ")
ci=input("\nSelect the city")    
if ci=="Jaipur" or ci=="Ahemdabad" or ci=="Mumbai" or ci=="Delhi" or ci=="Bengluru" or ci=="Pune" or ci=="Gandhinagr(Gujrat)" or ci=="Kolkata" or ci=="Lucknow" or ci=="Chennai" or ci=="Agra" or ci=="Chandigarh" or ci=="Noida" or ci=="Jodhpur" or ci=="Bikaner" or ci=="jaipur" or ci=="ahemdabad" or ci=="mumbai" or ci=="delhi" or ci=="bengluru" or ci=="pune" or ci=="gandhinagr(gujrat)" or ci=="kolkata" or ci=="lucknow" or ci=="chennai" or ci=="agra" or ci=="chandigarh" or ci=="noida" or ci=="jodhpur" or ci=="bikaner":    
    print(Fore.GREEN,Style.BRIGHT+"\n\n \t\t\t\t\t    NOW PLAYING Movie")
    x=["[1] Shershah ","[2] Sam bahadur","[3] OMG 2","[4] Attack of 26/11","[5] MISSION Mangal"]
    for k in x:
        from colorama import Fore,Style
        print(Fore.CYAN,Style.BRIGHT+"\n",k)
if (ci=="Jaipur" or ci=="Ahemdabad" or ci=="Mumbai" or ci=="Delhi" or ci=="Bengluru" or ci=="Pune" or ci=="Gandhinagr(Gujrat)" or ci=="Kolkata" or ci=="Lucknow" or ci=="Chennai" or ci=="Agra" or ci=="Chandigarh" or ci=="Noida" or ci=="Jodhpur" or ci=="Bikaner" or ci=="jaipur" or ci=="ahemdabad" or ci=="mumbai" or ci=="delhi" or ci=="bengluru" or ci=="pune" or ci=="gandhinagr(gujrat)" or ci=="kolkata" or ci=="lucknow" or ci=="chennai" or ci=="agra" or ci=="chandigarh" or ci=="noida" or ci=="jodhpur" or ci=="bikaner"):
    x=input("Enter the movie code you want to proceed with :")
    if x=="1":
        print(obj.Shershah())
    elif x=="2":
        print(obj.sam_bahadur())
    elif x=="3":
        print(obj.omg())
    elif x=="4":
        print(obj.Attack())
    elif x=="5":
        print(obj.mission())  
    else:
        print("Wrong Code Enter. Please try again. Thank you!")
else:
    print("Currently not availiable in your city.We will try our best to availiable soon in your city.Thank you,Have a nice day!")







# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





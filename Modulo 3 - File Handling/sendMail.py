import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
print("==============================================================")
print("**************************************************************")
print("*=*=*=*=*=*=*=*=*=*= BAD RABBIT GMAIL *=*=*=*=*=*=*=*=*=*=*=*=")
print("*=*=*=*=*=*=*=*   By: @DeveloperJoseph    *=*=*=*=*=*=*=*=*=*=")
print("**************************************************************")
print("==============================================================")
sender_email = str(input(">> Enter your gmail: "))  # Enter your address
receiver_email = str(input(">> Enter receiver gmail: "))  # Enter receiver address
password = input(">> Type your password and press enter: ")

context = ssl.create_default_context() #create a context
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:            
        stateConnection = False
        try:
            server.login(sender_email, password)
            stateConnection = True # succesfull connection 
        except:
            print(">> Something went wrong error with you user y/o password..")
            stateConnection = False # wrong connection

        if stateConnection == True:
            #subject and message
            subject = str(input(">> Subject: ")) #subject
            bodyMessage = str(input(">> Message: ")) #body message
            message = """\
            Subject: {}
            '{}'""".format(subject,bodyMessage) #adjunt(Format) subject and body message
            try:
                cant = int(input(">> Cant. emails to send: "))
                for x in range(cant):
                    server.sendmail(sender_email,receiver_email,message) #send message
            except:
                print(">> Wrong the send your message, I'm sorry..") #except
            finally:
                print(">> ",cant," Message sends, congratulations.") #finally
except:
    print("> Something went wrong error connection..") #except
finally:
    print("> Thanks you, come back soon..")#farewell

#MORE INFORMATION: https://realpython.com/python-send-email/
#                   https://yagmail.readthedocs.io/
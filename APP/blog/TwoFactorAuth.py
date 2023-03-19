import pyotp,qrcode
Key="HelloWorld"
totp=pyotp.TOTP(Key).provisioning_uri(name="Auth",issuer_name="FirstAPP")


  

#Function for Time-Based One time password and this will change after certain time mention as 30 sec
# def TwoFactAuthTOTP(key):
#         totp=pyotp.TOTP(key)

#         print(totp.now())

#         time.sleep(0)
#         print(totp.now())


# key="PrabhjotSingh"
#TwoFactAuthTOTP(key)

#Function for HOTP is Has-Based One time password this will expire only after the event is completed
# def TwoFactAuthHOTP(key):
#         counter=0
#         hotp=pyotp.HOTP(key)

#         print(hotp.at(0))
#         for counter in range(3):
#                 print(hotp.verify(input("EnterCode: "),counter))
#                 counter +=1
# TwoFactAuthHOTP(key)        
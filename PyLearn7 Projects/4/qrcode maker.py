import qrcode
name = input("Enter Your Name: ")
phone_number = int(input("Enter Your Phone Number: "))


img = qrcode.make(f"{name} | {phone_number}")

img.save("qr_code.jpg")

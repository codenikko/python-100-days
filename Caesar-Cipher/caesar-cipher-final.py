alp = "abcdefghijklmnopqrstuvwxyz"
lists= list(alp)


def encrypt(text, shift):
    string="" 
    
    for i in text:

        if i in lists:
            new_index=(lists.index(i)+shift)%26
            string += lists[new_index]
            # if new_index not in range(0,26):
            #     new_index = new_index-26
            # else:
            #     new_index = new_index

            # string += lists[new_index]
        
        else:
            string+=i 

    print(f"Your encoded message : {string}")  





def decrypt(text, shift):
    string=""
    
    for i in text:

        if i in lists:
            new_index=(lists.index(i)-shift)%26
            string += lists[new_index]
            # if new_index not in range(0,26):
            #     new_index = new_index+26
            # else:
            #     new_index = new_index

            # string += lists[new_index]
        
        else:
            string+=i

    print(f"Your decoded message : {string}")  

x = True
while x:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode","decode"]:
        print("enter properly")
    else:
        x= False
        
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:print("wrong choice") 

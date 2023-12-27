print("""
______  _____   ______  ___   _____ _____ _____  _____ _   _ 
| ___ \/  ___|  | ___ \/ _ \ /  ___/  ___|  __ \|  ___| \ | |
| |_/ /\ `--.   | |_/ / /_\ \\ `--.\ `--.| |  \/| |__ |  \| |
|    /  `--. \  |  __/|  _  | `--. \`--. \ | __ |  __|| . ` |
| |\ \ /\__/ /  | |   | | | |/\__/ /\__/ / |_\ \| |___| |\  |
\_| \_|\____/   \_|   \_| |_/\____/\____/ \____/\____/\_| \_/
                                                             
                                                             
                                                          
                                                           """)
print("------------------------------------------------------")
print("This python script generates a random strong password")
print("------------------------------------------------------")
passlen=int(input("Enter the length of your required password :"))
import random
password=''
count=0

for i in range(passlen):
    choice=random.randint(0,69)
    char=['a','b','c','d','f','g','h','i','j','1','2','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','!','$','|','-','^','@','#','$','3','4','5','6','7','8','9','0']
    password=password+char[choice]    
print("Here is your password : ",password)

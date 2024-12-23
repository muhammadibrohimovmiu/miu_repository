import random
import datetime
import json

# users = []

with open("bank-users.json" , "r") as file:
    users = json.load(file)

class Bank:
    def __init__(self , fullname , birthday , order , phone , password):

        self.check_fullname(fullname)
        self.fullname = fullname

        self.check_birthday(birthday)
        self.birthday = birthday

        self.age = self.register_age()

        self.create_account_number(order)

        self.check_phone(phone)
        self.phone = phone

        self.balance = 100000

        self.check_password(password)
        self.password = password

        self.time = self.register_time()

        users.append(self.to_dict())

        print("\nTabriklaymiz🎉!!!\nSizning hisobingiz yaratildi!\n")


    def check_fullname(self , fullname : str):

        assert len(fullname.split()) == 4 , "To'liq ismingizni F.I.Sh tarzida kiriting!"
        assert fullname.lower().endswith("o'g'li") or fullname.lower().endswith("qizi"), "To'liq ismning oxiri 'o'gli' yoki 'qizi' tarzida tugashi kerak!"

    def check_birthday(self , birthday : str):

        date = birthday.split(".")
        assert len(date) == 3 ,"Tug'ilgan kun notog'ri kiritlgan!"

        try :
            self.new = datetime.datetime(year = int(date[2]) , month = int(date[1]) , day = int(date[0]))
        
        except Exception as error:
            raise Exception("Tug'ilgan kun notog'ri kiritlgan!")
        
        else :
            self.today = datetime.datetime.now()

            if (self.today - self.new).days < 6580:
                raise Exception("Siz hali 18 yoshga to'lmagansiz!")
            
    def register_age(self):
        return (self.today - self.new).days // 365
    
    def create_account_number(self , order):
        if order == 1 :
            self.account_number = 9860000000000000 + random.randint(100 , 1000000000000)
            for i in users:
                if i["account number"] == self.account_number:
                    self.account_number = 9860000000000000 + random.randint(10 , 1000000000000)
            self.type = "Uzkard"
                
        elif order == 2:
            self.account_number = 8600000000000000 + random.randint(100 , 1000000000000)
            for i in users:
                if i["account number"] == self.account_number:
                    self.account_number = 8600000000000000 + random.randint(10 , 1000000000000)
            self.type = "Humo"   
        else : raise Exception("Noto'gri buyruq kiritldi!")
            

    def check_phone(self , phone):

        assert phone.startswith("+998") , "Telefon raqami '+998' tarzida boshlanishi kerak!"
        assert phone[1:].isdigit() , "Telefon raqami faqatgina raqamlardan iborat bo'lisi kerak!"
        assert len(phone[1:]) == 12 , "Telefon raqami uzunligi kamida 12 ta raqamdan iborat bo'lishi kerak!"

    def check_password(self , password):

        assert len(password) >= 8 , "Yaratgan parolingiz kamida 8 uzunlikka ega bo'lishi kerak!"

        katta = 0
        kichik = 0
        belgi = 0
        raqam = 0

        for i in password:
            if i.isspace():
                raise Exception("Parolda bo'sh joy mavjud bo'lmasligi kerak!")
            
            if i.isupper():
                katta += 1
            
            if i.islower():
                kichik += 1

            if i.isdigit():
                raqam += 1
            
            else : belgi += 1

        assert katta > 0 and kichik > 0 and raqam > 0 and belgi > 0 , "Parol kamida 1 ta Katta harf , 1 ta raqam , 1 ta kichik harf , 1 ta belgidan iborat bo'lishi kerak!"

    def register_time(self):
        return datetime.datetime.now()

    def to_dict(self):
        return {
            "fullname" : self.fullname,
            "birthday" : self.birthday,
            "age" : self.age,
            "account number" : self.account_number,
            "type" : self.type,
            "phone number" : self.phone,
            "password" : self.password,
            "sign up time" : str(self.time),
            "balance" : self.balance
        }
    
    def print_new(self):
        print(f"To'liq ismi : {self.fullname}")
        print(f"Tug'ilgan sanasi va yoshi : {self.birthday} , {self.age}")
        print(f"Hisob raqami : {self.account_number}")
        print(f"Foydalaniladigan plastik karta turi : {self.type}")
        print(f"Telefon raqami : {self.phone}")
        print(f"Ro'yxatdan o'tgan vaqti : {self.time}")
        print(f"Hisob raqami balansi : {self.balance} so'm")
        print("Bizda hisob ochgan mizojga 100000 so'm bonus taqdim etamiz!")

        with open("bank-users.json" , "w") as file:
            json.dump(users , file , indent = 4)

def print_user_data():
    print()
    print("Bizning ilovamizdan ro'yxatdan o'tgan insonlar : ")

    for i in users:

        print("----------------------------------------------------------------")
        print(f"To'liq ismi : {i["fullname"]}")
        print(f"Tug'ilgan sanasi va yoshi : {i["birthday"]} , {i["age"]}")
        print(f"Hisob raqami : {i["account number"]}")
        print(f"Plastik karta turi : {i["type"]}")
        print(f"Telefon raqami : {i["phone number"]}")
        print(f"Ro'yxatdan o'tgan vaqti : {i["sign up time"]}")
        print(f"Hisob raqami balansi : {i["balance"]} so'm")

def check_existing_account(existing_account):
    assert len(existing_account) == 16 , "Hisob raqamining uzunligi 16 ta raqamdan iborat bo'lishi kerak"

    if " " in existing_account: raise Exception("Hisob raqamida bo'sh joy bo'lishi mumkin emas!")

    for i in users:
        if int(existing_account) == i["account number"]:

            remove_balance = float(input("Qancha mablag' yechib olmoqchisiz : "))

            if remove_balance > i["balance"]: 
                raise Exception("Operatsiyani amalga oshirb bo'lmaydi ! Hisob raqamida mablag' yetarlik emas!")
            
            else :
                i["balance"] -= remove_balance

                with open("bank-users.json" , "w") as file:
                    json.dump(users , file , indent = 4)
                
                print("Hisobingizdan mablag' muvaffaqiyatli yechildi!")
                break
                
    else :
        raise Exception("Bunday hisob raqami serverda mavjud emas !")
    
def check_existing_account0(existing_account):
    assert len(existing_account) == 16 , "Hisob raqamining uzunligi 16 ta raqamdan iborat bo'lishi kerak"

    if " " in existing_account: raise Exception("Hisob raqamida bo'sh joy bo'lishi mumkin emas!")

    for i in users:
        if int(existing_account) == i["account number"]:

            remove_balance = float(input("Qancha mablag' hisoningizga qo'shmoqchisiz : "))

            i["balance"] += remove_balance

            with open("bank-users.json" , "w") as file:
                json.dump(users , file , indent = 4)
                
            print("Hisobingizga mablag' muvaffaqiyatli qo'shildi!")
            break
                
    else :
        raise Exception("Bunday hisob raqami serverda mavjud emas !")
    
def check_balance(existing_account):
    assert len(existing_account) == 16 , "Hisob raqamining uzunligi 16 ta raqamdan iborat bo'lishi kerak"

    if " " in existing_account: raise Exception("Hisob raqamida bo'sh joy bo'lishi mumkin emas!")

    for i in users:
        if int(existing_account) == i["account number"]:
            print(f"Balansingiz : {i["balance"]}")
            break
    
    else :
        raise Exception("Bunday hisob raqami serverda mavjud emas !")



print()
print("'MIU.bank services' ga xush kelibsiz!")

while True:
    
    print("\n1.Hisob raqami yaratish")
    print("2.Mavjud hisob raqamida mablag' yechish")
    print("3.Mavjud hisob raqamiga mablag' qo'shish")
    print("4.Mavjud hisob raqamining balansini ko'rish")
    print("5.'MIU.bank services' mijozlari ro'yxatini ko'rish")
    print("6.Dasturni tark etish")

    or1 = int(input("Buyruqni kiritng (1-5): "))

    match or1:

        case 1:
            fullname = input("\nIsmingizni to'qliq kiritng (misol , Ali Aliyev Ali o'g'li) : ")
            birthday = input("Tug'ilgan sanangizni kiritng (misol , 01.01.2001) : ")
            phone = input("Telefon raqamingizni kiritng (misol , +998999999999) : ")
            password = input("Parol yarating (misol , 1234#Ngm.) : ")
            order  = int(input("Qanday turdagi plastik kartasi turidan foydalanmoqchisiz?\n1.Uzkard\n2.Humo kard\nBuyruqni kiritng (1 yoki 2) : "))

            user0 = Bank(fullname , birthday , order , phone , password)
            user0.print_new()

            with open("bank-users.json" , "w") as file:
                json.dump(users , file , indent = 4)
        
        case 2:
            exist_account = input("\nMavjud bo'lgan hisob raqamni kirting : ")
            check_existing_account(exist_account)

        case 3:
            exist_account = input("\nMavjud bo'lgan hisob raqamni kiritng : ")
            check_existing_account0(exist_account)

        case 4:
            exist_account = input("\nMavjud bo'lgan hisob raqamni kiritng : ")
            check_balance(exist_account)

        case 5:
            print_user_data()

        case 6:
            print("\nDastur to'xtatildi !")
            break
        
        case _:
            print("Noto'gri buyruq!")

lst = []
class Book:
    def __init__(self,id,name,author,count,narx):
        self.id = id
        self.name = name
        self.avtor = author
        self.count = count
        self.price = narx
        with open('info.txt') as f:
            idlar = [i.split(',')[0] for i in f.read().split('\n') if len(i) != 0]
        if str(self.id) not in idlar:
            with open('info.txt', 'a') as t:
                t.write(f"{self.id},{self.name},{self.avtor},{self.count},{self.price}\n")

    def chiqarish():
        with open('info.txt') as f:
            for i in f.read().split('\n'):
                if len(i) != 0:
                    i = i.split(',')
                    print(f'''
Id: {i[0]}
Nomi: {i[1]}
Muallifi: {i[2]}
Miqdori: {i[3]}
Narxi: {i[4]} so'm''')

    def count_pasaytirish(id):
        text = ""
        with open('info.txt') as f:
            for i in f.read().split('\n'):
                if len(i) != 0:
                    i = i.split(',')
                    if i[0] == str(id):
                        if int(i[3]) <= 0:
                            print('Shundoq ham bu kitobdan yoq')
                            return 
                        i[3] = str(int(i[3]) - 1)
                    text += f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n"
        
        if len(text) != 0:
            with open('info.txt', 'w') as t:
                t.write(text)
        if id in lst:
            print('Bu id ochirilgan')
        else:
            print('Bunday idli kitob mavjud emas')

    def ochirish(id):
        text = ""
        id_topish = False
        with open('info.txt') as f:
            for i in f.read().split('\n'):
                if len(i) != 0:
                    i = i.split(',')
                    if i[0] != id:
                        text += f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n"
                    else:
                        id_topish = True
                        lst.append(i[0])
        if id_topish:
            with open('info.txt', 'w') as t:
                t.write(text)
        else:
            print("Bunday id mavjud emas")

b1 = Book(1, 'Harry Potter', 'J.K.Rowling', 10, 50000)
b2 = Book(2, 'Otgan kunlar', 'Abdulla Qodiriy', 20, 35000)
b3 = Book(3, 'Stiv Jobs', 'Steve Jobs', 14, 25000)

Book.ochirish(input('Qaysi ID dagi kitobni ochirmoqchisiz , id kiriting: '))
Book.chiqarish()
Book.count_pasaytirish(input('Id kriting kitob miqdorini kamaytirish uchun: '))

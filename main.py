import os
import mysql.connector
import time


class Dictionary:
    def __init__(self):
        # self.read_show_database()
        self.select_option()

    def select_option(self):
        self.show_options()
        input_options = input(" >>> ").strip()

        while input_options not in ['1', '2', '3', '4', '5']:
            self.clear_windov()
            self.show_options()
            print("[1/2/3/4/5]")
            input_options = input(" >>> ").strip()

        if input_options == '1':
            self.add_dict()
        elif input_options == '2':
            self.wiev_dict()
            input_exit = input("\nexit[q] >>> ").strip()
            while input_exit not in ['q']:
                self.clear_windov()
                self.wiev_dict()
                input_exit = input("\nexit[q] >>> ").strip()
            self.clear_windov()
            self.__init__()
        elif input_options == '3':
            self.clear_windov()
            input_search_word = input("\n\n\tQidirilayotgan so'zni kiriting: ").strip().lower()
            while not input_search_word.isalpha():
                self.clear_windov()
                input_search_word = input("\n\n\tQidirilayotgan so'zni kiriting: ").strip().lower()
            print(f" \n\n\n\t{input_search_word}   {self.search(input_search_word)}")
            input_exit = input("\nexit[q] >>> ").strip()
            while input_exit != 'q':
                self.clear_windov()
                self.add_dict()
                input_exit = input("\nexit[q] >>> ").strip()
            self.clear_windov()
            self.__init__()
        else:
            os.system("exit")

    # ___________________________________________ main function __________________________

    def add_dict(self):
        self.clear_windov()
        print("\n\n\n\t\tLug'atga so'z qo'shing !!!")
        new_eng_word = input("\nEnglizcha So'z kiriting: ").strip().lower()
        while not new_eng_word.isalpha():
            self.clear_windov()
            print("\n\n\n\t\tLug'atga so'z qo'shing !!!")
            new_eng_word = input("\nEnglizcha So'z kiriting: ").strip().lower()

        new_uzb_word = input("Uzbekcha tarjimasini kiriting: ").strip().lower()
        while not new_uzb_word.isalpha():
            self.clear_windov()
            print("\n\n\n\t\tLug'atga so'z qo'shing !!!")
            print(f"\nEnglizcha So'z kiriting: {new_eng_word}")
            new_uzb_word = input("Uzbekcha tarjimasini kiriting: ").strip().lower()

        self.add_word_to_db(new_eng_word, new_uzb_word)
        self.clear_windov()
        print("\n\n\n\t\tlug'atga yangi so'z qo'shildi !!!")
        time.sleep(2)
        self.clear_windov()
        self.__init__()

    def wiev_dict(self):
        result = self.read_database()
        print("\tEngilizcha       Uzbekcha\n")
        for i in result:
            print(f"\t{i[0]}\t\t {i[1]}")

    def search(self, word):
        words = self.read_database()
        for i in words:
            if i[0] == word:
                return i[1]
            elif i[1] == word:
                return i[0]
        return "So'zi topilmadi"

    def read_database(self):
        self.clear_windov()
        mydb = mysql.connector.connect(
            host='localhost',
            user='abdulla',
            password='123456789',
            database='users'
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from dict;")
        result = mycursor.fetchall()
        return result


    def add_word_to_db(self, eng, uzb):
        mydb = mysql.connector.connect(
            host='localhost',
            user='abdulla',
            password='123456789',
            database='users'
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into dict(eng_word, uzb_word) values('{eng}', '{uzb}');")
        mydb.commit()

    def show_options(self):
        print("""
    ________________________________________
    ingilizcha - o'zbekcha lug'at
    
                1. Yangi so'z qo'shish.
                2. Lug'at ichidagi so'zlarni ko'rish.
                3. Izlash.
                4. Chiqish
                
        """)

    def clear_windov(self):
        os.system("clear")


lugat = Dictionary()

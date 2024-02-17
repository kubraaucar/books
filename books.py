
import time 
class Library:
    
    def __init__(self):
        self.books_file_create() 
    
    def books_file_create(self): 
        file = open("books.txt","a+",encoding="utf-8")
        file.close()

    def book_add(self): 
        book_name   = input("Enter the book title  : ") 
        book_author = input("Enter the author  : ") 
        book_year   = input("Enter the release year : ")
        book_page   = input("Enter the number of pages : ")

        print(f"""
    Book name  : {book_name}
    Author     : {book_author}
    Book year  : {book_year}
    Book page  : {book_page}""")
        
        while True:
            choice_add = input(f"'{book_name}' save book t/f : ")

            if choice_add == "t":

                file = open("books.txt","a",encoding="utf-8")
                file.write(book_name + "," + book_author + "," + book_year + "," + book_page + "\n")
                file.close

                print(f"\n'{book_name}'  recorded")
                time.sleep(0.5)
                break

            elif choice_add == "f":

                print(f"\n'{book_name}' not recorded ")
                break

            else:
                print("wrong choice")
        
    def books_list_print(self): 
        file = open("books.txt","r",encoding="utf-8") 
        books_list = file.readlines() 
        file.close()

        if len(books_list) == 0:
            print("No Books in the Library.")
            time.sleep(0.5)

        count = 1 
        for i in books_list: 
            book_attribute = i.split(",") 
            time.sleep(0.2)

            
            print(f"""
**************   {count}. book  *********
Book name  : {book_attribute[0]}
Author     : {book_attribute[1]}""")
            
            count += 1 

    def book_delete(self): 

        book_delete = input(" Enter the book title to remove: ")
        file = open("books.txt","r",encoding="utf-8") 
        books_list = file.readlines()
        file.close

        index_no = 0
        for i in books_list: 
            find_book = i.startswith(book_delete) 

            if find_book:
                books_list.pop(index_no)
                break
            index_no += 1 

        file = open("books.txt","w",encoding="utf-8") 
 
        for i in books_list:
            file.write(i)
        file.close
        
       
        print(f"'{book_delete}'book deleted")
        time.sleep(0.2)

class Menu():
        
        def __init__(self):
            self.menu()
        
        def menu(self):
      
            while True:
                print("""
        ****** Menü *****
        1) List Books
        2) Add Book
        3) Remove Book
        q) Quit
        *****************
        """)
                choice = input("Enter your choice (1-2-3-q) : ") 
                if choice == "1":
                    lib.books_list_print() 

                elif choice == "2":
                    lib.book_add() 

                elif choice == "3":
                    lib.book_delete() 

                elif choice == "q":
                    time.sleep(0.3)
                    print(f"Exiting the application") 
                    time.sleep(0.3)
                    break

                else:
                    print("Please enter a valid option")
                    time.sleep(0.5)

if __name__ == '__main__':
    lib = Library()
    menu = Menu()
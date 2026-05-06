class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
        
    def displayBooks(self):
        print('Here are the books we have: ',self.name)
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('Lender book database has been updated. You can take the book now')
        else:
            print("Book is aleady bein used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print('Book has been added to book list')
    
    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    books = Library(['Percy Jackson', 'Python', 'Harry Potter', 'Folk of the air', 'Powerless'], 'Lets Upskill')

    while(True):
        print(f"Welcome to the {books.name} library! Enter your choice to continue")
        print('1. Display Books')
        print('2. Lend a book')
        print('3. Add a book')
        print('4. Return a Book')
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
           print("Please enter a valid option")
           continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of book: ")
            user = input("Enter your name: ")
            books.lendBook(user, book)
        
        elif user_choice == 3:
            book = input("Enter the name of the book: ")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book: ")
            books.returnBook(book)

        else:
            print("Not a valid option")

        print('Press q to quit and c to continue')
        user_choice2 = ""
        while (user_choice2!='c' and user_choice2!='q'):
            user_choice2 = input()
            if user_choice2=='q':
                exit()
            elif user_choice2 == 'c':
                continue

        




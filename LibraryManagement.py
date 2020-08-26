# CREATE A LIBRARY CLASS WITH METHODS OF 
#  1 DISPLAYING ALL THE BOOKS
#  2  LEND BOOKS
#  3 ADD BOOKS
#  4 RETURN A BOOK
class Library:
    def __init__(self,lbooks, libname):
        self.lbooks = list(lbooks)
        self.libname = libname
        self.lend = {} 

    def showBooks(self):
        a = len(self.lbooks)
        print(f"<---{a}--BOOKS--PRESENT--IN--YOUR--LIBRARY--->")
        for items in self.lbooks:   
            print(items)

    def lendBook(self,lendname, bookname, duration):
        if bookname in self.lbooks and duration <= 30 :
            print("The Book Is Available We Will Courier It To Your Home")
            self.lbooks.remove(bookname)
            self.lend[bookname] = lendname
        else:
            print("SORRY WE DON'T HAVE THIS BOOK RIGHT NOW")

    def addBook(self, bookname):
        if bookname not in self.lbooks:
            self.lbooks.append(bookname)
            print("BOOK SUCCESFULLY ADDED ")
        else:
            print("CAN'T ADD DUPLICATE ITEM BOOK ALREADY PRESENT IN THE LIBRARY")

    def returnBook(self, bookname):
        if bookname not in self.lbooks:
            self.lbooks.append(bookname)
            self.lend.pop(bookname)
        else:
            print("<--PLEASE LOOK FOR YOUR INPUT--> YOU ENTRED WRONG BOOK NAME ")





        
books = ["Methodology","Continuous Delivery","Algorithms", "The Self-Taught Programmer", "Rapid Development","Coders at Work", "Domain-Driven Design", "The Art of Computer Programming", "Structure and Interpretation of Computer Programs", "Patterns of Enterprise Application Architecture", "Programming Pearls", "Peopleware", "Introduction to Algorithms" ,"Code", "Don't Make Me Think", "Soft Skills", "Rework", "Crackink The Coding Interview", "Design Patterns", "Working Effectively with Legacy Code", "The Clean Coder", "The Mythical Man-Month", "Head First Design Patterns", "Refactoring", "Code Complete", "Clean Code", "The Progmatic Programmer" ]
MyLib = Library(books, "Vinay-Library")

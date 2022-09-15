class classList:
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
    def info(self):
        print("\t%s is a famous %s written by  %s"%(self.title,self.genre,self.author))
booklist=[]
#print(booklist) empty listwhile True:
while True:
    title=input("\tInput title: ")
    author=input("\tInput author: ")
    genre=input("\tInput genre: ")
    obj1=classList(title,author,genre)
    booklist.append(obj1)
    print("data inserted successfully")
    option=input("Do you want to add more data?= y/n: ")
    if option.lower()=='n':
        break

print("All available data")
for obj in booklist:
    obj.info()

class stack:
    items = []
    def start(self):
        print("Select what you want to chose ! For Push 1,pop 2,quit 3...")

        self.num=int(input('Enter chosen number : '))

    def push(self):

            self.pushitem = int(input("Enter item you want to push : "))
            self.items.append(self.pushitem)
            print(self.items)


    def pop(self):
        if len(self.items)==0:
            print('List is already empty..')
        else:
            self.items.pop()
            print(self.items)


    def check(self):
        while True:
            self.start()
            if self.num == 1:
                self.push()
            elif self.num == 2:
                self.pop()
            elif self.num==3:
                break
            else:
                print('chose valid number......')

obj=stack()
obj.check()











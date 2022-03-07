class queue:
    items=[]

    def enqueue(self):
        num=int(input('Enter Number : '))
        self.items.append(num)
        print(self.items)

    def dequeue(self):

        self.items.pop(0)
        print(self.items)

    def start(self):
        print('Select what you want to do ? 1.add 2.remove 3.quit....')
        self.chose =int(input('Enter number..'))

    def process(self):
        while True:
            self.start()
            if self.chose==1:
                self.enqueue()
            elif self.chose==2:
                self.dequeue()

            else:
                break


obj=queue()
obj.process()




import collections


class queue_deque:
    que = collections.deque()

    def start(self):
        print('Select what you want? 1.add 2.remove from deque!!')
        self.select=int(input('chose your number..'))

    def add(self):
        num=int(input('enter number : '))

        self.que.appendleft(num)
        print(self.que)

    def rem(self):
        self.que.pop()
        print(self.que)

    def process(self):
        while True:
            self.start()
            if self.select==1:
                self.add()
            elif self.select==2:
                self.rem()
            else:
                break
if __name__=='__main__':
    obj = queue_deque()
    obj.process()





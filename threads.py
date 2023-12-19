import threading

sum = 0
threadlock = threading.Lock()

class adding_up(threading.Thread):
    def __init__(self, ni, nf):
        self.ni = ni
        self.nf = nf
        self.s = 0

    def run(self):
        for i in range(self.ni, self.nf+1):
            self.s += i

        threadlock.acquire()
        print("in lock")
        threadlock.release()

if __name__ == "__main__":
    thread1 = adding_up(1, 50)
    thread2 = adding_up(51, 100)

    thread1.run()
    thread2.run()

    thread1.join()
    thread2.join()

    print(sum)





import WaterrowerBle
import WaterrowerInterface
import threading
from queue import Queue
from collections import deque

def main():

    def BleService(out_q,ble_in_q):
        print("THREAD - Start BLE Advertise and BLE GATT Server")
        bleService = WaterrowerBle.main(out_q,ble_in_q)
        bleService()


    def Waterrower(in_q,ble_out_q):
        print("THREAD - Start BLE GATT Server")
        Waterrowerserial = WaterrowerInterface.main(in_q,ble_out_q)
        Waterrowerserial()

    # def task3():
    #     print("THREAD - Start RS232 Interface")
    #     interface = rs232.main()
    #     interface()
    #TODO: Switch from queue to deque
    q = Queue()
    ble_q = deque(maxlen=1)
    t1 = threading.Thread(target=BleService,args =(q,ble_q ))
    t2 = threading.Thread(target=Waterrower,args =(q,ble_q ))
    # t3 = threading.Thread(target=task3) # will be for ant+
    # t4 = threading.Thread(target=task4)

    t1.start()
    t2.start()
    #t3.start() Would be for Ant+
    # t4.start()

    # t1.join()
    # t2.join()
    # t3.join()


if __name__ == '__main__':
    main()
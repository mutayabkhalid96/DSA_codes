import threading
import time
from queue import queue

order_queue = queue()

def place_orders(order_list):
  for order in order_list:
    time.sleep(0.5)
    order_queue.enqueue(order)
    print("Order placed for you. You have ordered {}".format(order))
    print("Please wait while your order is being prepared. :)")

def serve_orders(order_list):
  for order in order_list:
    time.sleep(0.55)
    order_queue.dequeue()
    print("Enjoy your meal. You have ordered {}".format(order))

order_list = ['pizza','samosa','pasta','biryani','burger']

t = time.time()
multi_thread = True

if (multi_thread):
  t1 = threading.Thread(target=place_orders, args=(order_list, ))
  t2 = threading.Thread(target= serve_orders, args=(order_list, ))

  t1.start()
  t2.start()

  t1.join()
  t2.join()
else:
  place_orders(order_list)
  serve_orders(order_list)

print ("Time taken: {}".format(time.time()-t))

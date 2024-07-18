# Primero se realiza importaciones
 import asyncio
 import peer-to-peer
 
# Se define la class Message
class Message:
  def __init__(red, num_nodes, num_rooms):
        red.nodes = [Process(i, []) for i in range(num_nodes)]
        red.initiador=[send_message(processes)]
        red.mutexes = [RicartAgrawalaMutex(i, num_nodes) for i in range(num_nodes)]
     
        red.rooms = [False] * num_rooms  # El falso significa disponible
        red.collector = CheneyCollector(100)  # El tamaño de arbitrario es 100 
    
   def synchronize_clocks(red):
        return berkeley_sync(red.nodes)


# Se realiza la importaciones
import time
import threading
import asyncio
from concurrent.futures.ThreadPoolExecutor
# Se define esta función de ayuda para imprimir en formato de columna
def print_cpu(cpu, str):
    print((' ' * cpu * 35) + str)
    return

def total_working_set(recur):
        cache_sum = 0
        for j_name in recur.cache_contents:
            cache_sum += recur.jobs[j_name].working_set_size
        return cache_sum

def adjust_size(recur):
working_set_total = recur.total_working_set()
        while working_set_total > recur.cache_size:
            last_entry = len(recur.cache_contents) - 1
            job_gone = recur.cache_contents[last_entry]
           
            del recur.cache_contents[last_entry]
            recur.cache_warming.append(job_gone)
            recur.cache_warming_counter[job_gone] = recur.cache_warmup_time
            working_set_total -= recur.jobs[job_gone].working_set_size
        return

    def get_cache_state(recur, j_name):
        if j_name in recur.cache_contents:
            return 'w'
        else:def get_precise_time(recur):
        times = [(node.time, 1) for node in recur.nodes]  # 1 es una incertidumbre arbitraria
            return ' '
        
    def get_rate(recur, j_name):
        if j_name in recur.cache_contents:
            return recur.cache_rate_warm
        else:
            return recur.cache_rate_cold

    def update_warming(recur, j_name):
        if j_name in recur.cache_warming:
            recur.cache_warming_counter[j_name] -= 1
            if recur.cache_warming_counter[j_name] <= 0:
                recur.cache_warming.remove(j_name)
                recur.cache_contents.insert(0, j_name)
                

                
        return
  
num_cpus = int(options.num_cpus)
time_slice = int(options.time_slice)

# Se realiza la definicion  de get_precise_time
def get_precise_time(recur):
        times = [(node.time, 1) for node in recur.nodes]  # La incertidumbre arbitraria es el 1
        

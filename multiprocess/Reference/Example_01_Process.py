import multiprocessing, time, signal

p = multiprocessing.Process(target=time.sleep, args=(1000,))
print(p, "is_alive() = %s"%p.is_alive())
p.start()
print(p, "is_alive() = %s"%p.is_alive())
p.terminate()
time.sleep(0.1)
print(p, "is_alive() = %s"%p.is_alive())
print("(exitcode == -signal.SIGTERM) = %s"%(p.exitcode == -signal.SIGTERM))

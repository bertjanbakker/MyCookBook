import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mt-example")
# logger.setLevel(logging.DEBUG)


# Function executed by each thread
def query_database(event, result_list):
    # Perform database query
    # ...
    begin = time.time()
    sleeptime = random.uniform(1.0, 3.0)
    time.sleep(sleeptime)
    # Once query is done, store result in result_list
    duration = time.time() - begin
    logger.debug("result")
    result = f"Result from database in ${duration}"
    result_list.append(result)

    # Signal that query is complete
    event.set()


# Function executed by the coordinator thread
def coordinator_thread(events, result_lists):
    begin = time.time()
    # Wait for all events to be set
    for event in events:
        event.wait()

    # Collect results from all threads
    all_results = []
    for result_list in result_lists:
        all_results.extend(result_list)

    duration = time.time() - begin

    # Perform further processing with all_results
    print(f"All results collected in ${duration}:", "\n".join(all_results))
    # Further processing logic here...


# Number of databases
num_databases = 3

# Create events and result lists for each database
events = [threading.Event() for _ in range(num_databases)]
result_lists = [[] for _ in range(num_databases)]

# Create and start threads for each database
threads = []
for i in range(num_databases):
    t = threading.Thread(target=query_database, args=(events[i], result_lists[i]))
    threads.append(t)
    t.start()

# Start the coordinator thread
coordinator = threading.Thread(target=coordinator_thread, args=(events, result_lists))
coordinator.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Wait for the coordinator thread to complete
coordinator.join()

import threading
import time
from runner import Runner
from hand import ResultType

start_time = time.time()

print_output = False
size = 10000
runners = []
for i in range(size):
    runners.append(Runner())

for i in range(len(runners)):
    runners[i].run_hand(print_output)

win_count = 0
blackjacks = 0
push_count = 0
bust_count = 0

for i in range(len(runners)):
    if runners[i].hand.result_type == ResultType.Win:
        win_count += 1
    if runners[i].hand.result_type == ResultType.Blackjack:
        win_count += 1
        blackjacks += 1
    if runners[i].hand.result_type == ResultType.Push:
        push_count += 1
    if runners[i].hand.result_type == ResultType.Bust:
        bust_count += 1

end_time = time.time()
print("Time elapsed: " + str(end_time - start_time))

print("Win rate: " + str(win_count / len(runners)))
print("Blackjack rate: " + str(blackjacks / len(runners)))
print("Push rate: " + str(push_count / len(runners)))
print("Bust rate: " + str(bust_count / len(runners)))
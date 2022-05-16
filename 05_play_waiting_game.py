import time
from string import digits


def waiting_game():
  print("That is a little waiting game")
  print("You're should input number and I'm starting a timer")
  print("You're should to stop timer afret inputed amount of Seconds")

  tmp_delay = input("Please input amount of time\n")
  while not tmp_delay in digits:
      tmp_delay = input("Please input amount of time\n")

  delay = int(tmp_delay)

  input("Press Enter for start timer....")
  start = round(time.perf_counter(),4)

  input(f"Wait for {delay} seconds and press Enter.....")
  stop = round(time.perf_counter(),4)

  target = start+delay
  diff = round(stop - (start+delay),4)
  elapsed = round(stop-start,4)
  zero = 0.01

  if (diff>zero):
      result = f"for {abs(diff)} seconds too slow"

  if (diff<-zero):
    result = f"for {abs(diff)} seconds too fast"

  if (diff> -zero) and (diff<zero):
      result = f"you're great, difference only {abs(diff)} seconds."

  print (f"Elapsed time: {elapsed} seconds ({result})")


if __name__ == "__main__":
    waiting_game()
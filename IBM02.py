def sentTimes(numberOfPorts, transmissionTime, packet_id):

  ans, t = [], 1
  avail = [0] * numberOfPorts
  #to use deque
  from collections import deque
  queue = deque()
  for pid in packet_id:
      # pop from queue if the port is available
      while queue and avail[queue[0]] <= t:
          queue.popleft()
      # if no ports available, wait until there is one available
      if len(queue) == numberOfPorts:
          t = avail[queue.popleft()]
      # try port until find one available
      port = pid % numberOfPorts
      while avail[port] > t:
          port = (port + 1) % numberOfPorts
      # send packet, update available time for the port
      avail[port] = t + transmissionTime
      queue.append(port)
      ans.append(port)
      t += 1
  return ans
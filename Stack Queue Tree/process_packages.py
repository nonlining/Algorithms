# python2

from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def full(self):
        if len(self.finish_time) == self.size:
            return True
        return False

    def empty(self):
        if len(self.finish_time) == 0:
            return True
        return False

    def Process(self, request):

        while len(self.finish_time) > 0:
            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.popleft()
            else:
                break

        if self.full():
            return Response(True, -1)

        if self.empty():
            self.finish_time.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)

        response = Response(False, self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request.process_time)

        return response

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, raw_input().strip().split(' '))
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, raw_input().strip().split(' '))
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)

# In this challenge, the task is to debug the existing code to successfully execute all provided test files.


def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())


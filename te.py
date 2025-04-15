import sys

def mocked_tracer(frame, event, arg=None):
    print(frame)
    print(event)
    print(arg)
    return mocked_tracer

# print(sys.gettrace())

sys.settrace(mocked_tracer)


print("Hello World")

def ss(user):
    print(user)


def QQ(q):
    # print(q)
    pass


QQ('QQ')

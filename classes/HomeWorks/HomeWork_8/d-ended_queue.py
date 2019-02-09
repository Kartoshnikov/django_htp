from collections import deque
def clear(x):
    stack.clear()
    print('OK')

def usage_print(x):
    print('Usage:\n', *('{}) {}'.format(str(i+1), key) for i, key in enumerate(usage.keys())), sep='\n')

stack = []
usage = {
    'push': lambda x: stack.append(x),
    'pop': lambda x: print(stack.pop()),
    'back': lambda x: print(stack[-1]) if stack else print('Stack is empty'),
    'size': lambda x: print(len(stack)),
    'clear': clear,
    'usage': usage_print,
    'show': lambda x: print(stack),
    'exit': None
}

print('Enter "usage" to show help')
while True:
    command = input('root@lockalhost# ').split()
    if not command or command[0] == 'exit': break
    usage[command[0]](None if len(command) < 2 else command[1])
print(stack)

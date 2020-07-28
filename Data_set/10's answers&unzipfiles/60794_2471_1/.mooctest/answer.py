
class stack:
    def __init__(self, value=None):
        if value is None:
            self.value = None
        self.value = [value]
    
    def push(self, value):
        if self.value is None:
            self.value = [value]
        else:
            self.value.insert(0, value)
    
    def pop(self):
        if self.value == None:
            return None
        tmp = self.value[0]
        del self.value[0]
        return tmp

    def read_top(self):
        #self.print()
        if self.value is None or not self.value:
            return None
        return self.value[0]
        
    def print(self):
        print(self.value)

def get_reverse(input):
    if input == '[':
        return ']'
    elif input == '{':
        return '}'
    elif input == '(':
        return ')'
    else:
        return None
        

input_count = int(input())
for i in range(input_count):
    input_str = input()
    stk = stack(input_str[0]) 
    not_balances=False
    for ii in input_str[1:]:
        if ii in [']', ')', '}'] and ii == get_reverse(stk.read_top()):
            stk.pop()
        elif ii in [']', ')', '}']:
            not_balances = True
            break
        else:
            stk.push(ii)
        #stk.print()    
    if stk.read_top() == None and not not_balances:
        print("balanced")
    else:
        print("not balanced")

        
    
        
        
    
    
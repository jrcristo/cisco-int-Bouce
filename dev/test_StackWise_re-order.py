from netmiko import ConnectHandler
import funtions_jose
import re

print('==> testing StackWise re-order <==')

if __name__ == '__main__':

    # connecting the device
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting the stackWise results
    output = net_connect.send_command('show sw')
    # print(output)

    # filtering the output
    stack = re.findall(r'.*\bActive\b.*|.*\bMember\b.*|.*\bStandby\b.*', output)

    # new list
    new_stack = []

    # removing leading spaced and *
    for i in stack:
        j = re.sub(r'..', '', i, count = 1)
        # getting the StackWise id (only)
        k = re.search(r'^\d', j)
        '''
        if k.group() == stack.index(i)+1:
            print('=> No need for changes on the stack')
        else:
            pass
        '''

        # getting the position on the list
        # print(stack.index(i))
        print('The list position is ', stack.index(i)+1, 'the value of the fist member is', k.group())

    print('The stack has', len(stack), 'member(s)')



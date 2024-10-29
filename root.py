from app import process_command

def call():
    while True:
        command=input('t-cli:>')
        if command == 'exit':
            print('Bye')
            break
        process_command(command)

if __name__=="__main__":
    call()
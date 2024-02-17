import socket


def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #otwarcie gniazda
    except:
        print('Socket error')
        return 1
    try:
        client_socket.connect(('2001:6d8:10:8210::24b', 14))
    except:
        print('Connection error')
        return 1
    print('Connected to server')
    try:
        nickname = input("Enter your nickname: ")
    except:
        print('Input error')
        return 1
    try:
        client_socket.sendall(nickname.encode('utf-8'))
    except:
        print('Write error')
        return 1
    while True:
        while True:
            try:
                choice = input('Enter your choice (rock/paper/scissors): ')
            except:
                print('Input error')
                return 1
            if choice.lower() == "rock" or choice == "paper" or choice == "scissors":
                try:
                    client_socket.sendall(choice.encode('utf-8'))
                except:
                    print('Write error')
                    return 1
                try:
                    data = client_socket.recv(1024)
                except:
                    print('Read error')
                    return 1
                result = data.decode('utf-8')
                print(result)
                if result:
                    while True:
                        try:
                            choice = input('Do you want to continue playing? (y/n): ')
                        except:
                            print("Input error")
                            return 1
                        if choice.lower() == 'y':
                            break
                        elif choice.lower() == 'n':
                            client_socket.close()
                            return
                        else:
                            print("Type correct letter")
                    break
            else:
                print("Type correct symbol")
                continue


if __name__ == '__main__':
    print('Starting server...')
    start_client()

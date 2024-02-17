import random
import socket
import threading


def add_result(nickname, win_streak):
    with open('wyniki.txt', 'a') as f:
        f.write(f'{nickname},{win_streak}\n')


def get_top_results():
    with open('wyniki.txt', 'r') as f:
        results = [line.strip().split(',') for line in f.readlines()]
    results.sort(key=lambda x: int(x[1]), reverse=True)
    top_results = '\n'.join([f'{row[0]}, {row[1]}' for row in results[:3]])
    return top_results


def play_game(client_choice, win_streak, nickname):
    server_choice = random.choice(['rock', 'paper', 'scissors'])
    result = ""

    if client_choice == server_choice:
        result = f"It's a tie! Server choice: {server_choice} \nWin streak: {win_streak}"
    elif (client_choice == 'rock' and server_choice == 'scissors') or \
            (client_choice == 'paper' and server_choice == 'rock') or \
            (client_choice == 'scissors' and server_choice == 'paper'):
        win_streak += 1
        result = f"You win! Server choice: {server_choice} \nWin streak: {win_streak}"
    elif (server_choice == 'rock' and client_choice == 'scissors') or \
            (server_choice == 'paper' and client_choice == 'rock') or \
            (server_choice == 'scissors' and client_choice == 'paper'):

        add_result(nickname, win_streak)
        top_results = get_top_results()
        print(f"Nickname, Highest Score\n{top_results}")
        result = f"You lose! Server choice: {server_choice} \nYour final score: {win_streak}"
        win_strike = 0
    return result, win_streak, nickname


def handle_client(conn, addr):
    print(f'Connected by {addr}')
    nickname = conn.recv(1024).decode('utf-8')

    win_streak = 0
    while True:
        data = conn.recv(1024)
        if not data:
            break
        client_choice = data.decode('utf-8')
        result, win_streak, nickname = play_game(client_choice, win_streak, nickname)
        conn.sendall(result.encode('utf-8'))
    conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 14))
    server_socket.listen(5)
    print('Server is listening on port 14')

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == '__main__':
    print('Starting server...')
    start_server()
# 🪨📄✂️ Paper Rock Scissors – Server-Based Game

A simple **Paper Rock Scissors** game project with server support. Multiple players can connect to the server and play independently against it. The server keeps track of scores and displays a scoreboard with the top 3 highest scores.

🎓 This project was created as part of a university course and works **only with IPv6**.


## 🔧 Requirements

- Python 3.x
- Standard Python libraries:
  - `socket`
  - `threading`

## 🗂️ Project Files

.  
├── server.py # Starts the game server  
└── client.py # Connects a player to the server


## ▶️ How to Run

1. **Start the Server**

   On the host machine, run:

   ```bash
   python server.py

2. **Start a Client**

   On the same or a different machine (in the same network), run:

   ```bash
   python client.py <server_ipv6_address>
   ```

   Replace <server_ipv6_address> with the actual IPv6 address of the server.  
   Example:

   ```bash
   python client.py [::1]

3. **Play the Game**

   Each client plays independently against the server. The server handles multiple players simultaneously using threads.

## 🧠 How It Works

- The server listens for incoming IPv6 connections and starts a new thread for each player.
- The player chooses a move: paper, rock, or scissors.
- The server responds with its own move and determines the result.
- After each round, the server updates and displays the top 3 scores.

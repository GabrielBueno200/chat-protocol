## 💻 The Project

In this project, we've implemented a chat application protocol in python.

Our application runs on the terminal using *telnet* client.


<!-- HOW TO RUN -->
## 🚀 How To Run

### Server
```bash

# Cloning repository
$ git clone https://github.com/GabrielBueno200/chat-protocol.git

# Accessing project folder
$ cd chat-protocol

# Download dependencies
$ pip install peewee

# Running application
$ python3 __main__.py

# The application will run at port 8000

```
### Client
```bash

# Use telnet client to connect to the server
$ telnet 127.0.0.1 8000

```

## </> Commands

### 🆕 Create

#### 1 - Creating users:
Type `create <username> <pass>` to register in the server

#### 2 - Creating rooms
Type `create -r <room name>` to create a room. 
Requires: authentication

### 🔒 Login
Type `login <username> <pass>` to login in the server

### ⬇️ Logout
Type `logout` to logout the server
Requires: authentication

### 📜 List

#### 1 - Users

##### 1.1 - Users at room
Type `list users` to see users joined at room
Requires: authentication; stay in some room and be its admin 

##### 1.2 - Pending users at room
Type `list -r` to see pending users at room
Requires: authentication; stay in some room and be its admin 

#### 2 - Rooms

##### 2.1 - User rooms
Type `list rooms` to see rooms that the logged user is member
Requires: authentication; joined in some room

##### 2.2 - All rooms
Type `list -a` to see all the rooms registered in the server
Requires: authentication

### 🚪 Mv (Move)
Type `mv “<room name>"` to enter in a room
Requires: authentication and an available room

### 🚪 Left
Type `left -r"` to leave a room
Requires: authentication and stay in some room

### 💬 Send (Message)
Type `send –m “<message text>"` to send a message in a room
Requires: authentication and stay in some room

### 🔼 Request
Type `request <room name>` to request join in the room
Requires: authentication and stay in some room

### ✔️ Accept
Type `accept <username>` to accept some pending user in your room
Requires: authentication; stay in some room and be its admin 

### ❌ Decline
Type `decline <username>` to reject some pending user in your room
Requires: authentication; stay in some room and be its admin 

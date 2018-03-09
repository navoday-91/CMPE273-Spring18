Prerequisites:

1. pip install urwid
2. pip install zmq

Instructions:

1. Start the forwarder device by executing - python3 Forwarder.py
2. Launch client application with registration name as arg - python3 chat_window.py <name>
3. Multiple clients can be launched and they will participate in a group chat.

Technology stack:

1. ZMQ for messaging and forwarder device to broadcast.
2. urwid for UI of chat window on client side.
3. Python3

Output:

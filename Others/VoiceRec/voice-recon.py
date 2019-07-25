
# -*- coding: utf-8 -*-

import socket
import sys
import select
import os
import subprocess
import time

host = "127.0.0.1"
port = 10500
bufsize = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
	inputready, outputready, exceptrdy = select.select([client_socket], [],[])
	for s in inputready:
		if s == client_socket:
			message = client_socket.recv(bufsize)
#			print "受信したメッセージ : " + message
			if message == "":
				print 'クライアントの実行を停止します'
				flag = False
				break
			else:
				if "WORD=\"こんにちは\"" in message:
					print "Hello"
				if "WORD=\"おはよう\"" in message:
					print "Good morning"

client_socket.close()

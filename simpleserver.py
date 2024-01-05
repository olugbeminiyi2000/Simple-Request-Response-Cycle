#!/usr/bin/python3

if __name__ == "__main__":
	import platform
	from socket import *
	import sys
	def doOthers(root_path, location):
		if location == "django/" or location == "django":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/django.txt"
				print(location)
			else:
				location = f"{location}/django.txt"
				print(location)
			data = getOthersDocument(root_path, location)
		elif location == "web/" or location == "web":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/web.txt"
			else:
				location = f"{location}/web.txt"
			data = getOthersDocument(root_path, location)
		elif location == "postgres/" or location == "postgres":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/postgres.txt"
			else:
				location = f"{location}/postgres.txt"
			data = getOthersDocument(root_path, location)
		else:
			if location == "":
				data = getOthersDocument(root_path, location)
			else:
				location_split = location.split("/")
				new_location = ""
				for i in range(len(location_split)):
					if i == len(location_split) - 1:
						new_location += f"{location_split[i]}"
						continue
					new_location += f"{location_split[i]}/"
				location = new_location
				data = getOthersDocument(root_path, location)
		return data
	
	def getOthersDocument(root_path, location="", error=0):
		search_file = f"{root_path}/{location}"
		if error == 1:
			with open(search_file, mode="r", encoding="utf-8") as efp:
				error_data = ""
				for line in efp:
					line += "\r\n"
					error_data += line
				return error_data
		try:
			with open(search_file, mode="r", encoding="utf-8") as fp:
				data = ""
				for line in fp:
					line += "\r\n"
					data += line
				return data
		except FileNotFoundError:
			default_file = "/python.txt"
			default_data = getOthersDocument(root_path, location=default_file, error=1)
			return default_data
		
	def doWindows(root_path, location):
		if location == "django/" or location == "django":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\django.txt"
				print(location)
			else:
				location = f"{location}\\django.txt"
				print(location)
			data = getWindowsDocument(root_path, location)
		elif location == "web/" or location == "web":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\web.txt"
			else:
				location = f"{location}\\web.txt"
			data = getWindowsDocument(root_path, location)
		elif location == "postgres/" or location == "postgres":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\postgres.txt"
			else:
				location = f"{location}\\postgres.txt"
			data = getWindowsDocument(root_path, location)
		else:
			if location == "":
				data = getWindowsDocument(root_path, location)
			else:
				location_split = location.split("/")
				new_location = ""
				for i in range(len(location_split)):
					if i == len(location_split) - 1:
						new_location += f"{location_split[i]}"
						continue
					new_location += f"{location_split[i]}\\"
				location = new_location
				data = getWindowsDocument(root_path, location)
		return data
	
	def getWindowsDocument(root_path, location="", error=0):
		search_file = f"{root_path}\\{location}"
		if error == 1:
			with open(search_file, mode="r", encoding="utf-8") as efp:
				error_data = ""
				for line in efp:
					line += "\r\n"
					error_data += line
				return error_data
		try:
			with open(search_file, mode="r", encoding="utf-8") as fp:
				data = ""
				for line in fp:
					line += "\r\n"
					data += line
				return data
		except FileNotFoundError:
			default_file = "\\python.txt"
			default_data = getWindowsDocument(root_path, location=default_file, error=1)
			return default_data



	def RapidLiteHTTPServer():
		# create a phone
		serversocket = socket(AF_INET, SOCK_STREAM)
		print(sys.argv)
		root_path = sys.argv[1]
		# set the ipadresses and port number my server would listen to
		try:
			# here we would use 127.0.0.1 or localhost string
			# here since it is not an ideal webserver we would use port 9000
			serversocket.bind(("localhost", 9000))

			# make the server have the capacity to queue other request by setting
			# the maximum amount of request it can accept
			serversocket.listen(5)

			# create a while loop that keeps on inorder to listen to request
			while (1):
				# now make the server socket to accept the incoming request
				# if they actually match the server settings configuration
				# then extract the client socket i.e details and address
				(clientsocket, address) = serversocket.accept()

				# the http request which is receive would be decoded from utf-8
				# to unicode in python and set the total number of characters
				# to receive from the request
				rd = clientsocket.recv(5000).decode()
				pieces = rd.split("\n")
				if len(pieces) > 0:
					print(pieces[0])

				# get the get request part of the http request header
				rq = pieces[0].split()
				
				# get uniform resource locator (url)
				url = rq[1]

				# get location 
				location = url.split("//", maxsplit=1)[1]
				location = location.split("/", maxsplit=1)[1]
				print(location)
				if platform.system() == "Windows":
					data = doWindows(root_path, location)
				else:
					data = doOthers(root_path, location)
				clientsocket.sendall(data.encode())
				
				# this helps us close the connection to the client we recieved 
				clientsocket.shutdown(SHUT_WR)

		except KeyboardInterrupt:
			print("\nShutting down...\n")
		except Exception as exc:
			print("Error:\n")
			print(exc)

		# if any of the exception occurs the sever stops
		serversocket.close()
	RapidLiteHTTPServer()

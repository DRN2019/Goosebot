import pickle

serverID = []
serverToggle = []

with open('servers.data', 'wb') as filehandle:
	pickle.dump(serverID, filehandle)
with open('toggle.data', 'wb') as filehandle:
	pickle.dump(serverToggle, filehandle)
import threading
def say(e):
	print 'say!',e


t = threading.Timer(2.0, say, ('nihao',))
t.start()
print '9999!'
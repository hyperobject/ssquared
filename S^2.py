#Snap! extension base by Technoboy10
import SimpleHTTPServer
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
	print path
	ospath = os.path.abspath('')
	if 'stop' in path:
		bot.stop()
	elif 'motorinf' in path:
		regex = re.compile("\/motor([0-9+])-([0-9]+)")
		m = regex.match(path)
		l = int(m.group(1)) / 100
		r = int(m.group(2)) / 100
		bot.motors(l, r)
	elif 'motortime' in path:
		regex = re.compile("\/motortime([0-9+])-([0-9]+)-([0-9]+)")
		m = regex.match(path)
		l = int(m.group(1)) / 100
		r = int(m.group(2)) / 100
		time = int(m.group(3))
		bot.motors(l, r)	
		time.sleep(time)
		bot.stop()	
	elif 'movetime' in path:
		regex = re.compile("\/movetime([0-9]+)-([0-9]+)")
		m = regex.match(path)
		power = int(m.group(1)) / 100
		time = int(m.group(2))
		bot.translate(power)
		time.sleep(time)
		bot.stop()
	elif 'moveinf' in path:
		regex = re.compile("\/moveinf([0-9]+)")
		m = regex.match(path)
		power = m.group(1) / 100
		bot.translate(power)
	elif 'led' in path:
		regex = re.compile("\/led([left|right])([0-9]+)")
		m = regex.match(path)
		led = m.group(1)
		power = int(m.group(2))
		bot.setLED(led, power)
	elif 'tone' in path:
		regex = re.compile("\/tone([0-9]+)-([0-9]+)")
		m = regex.match(path)
		time = int(m.group(1))
		freq = int(m.group(2))
		bot.beep(time, freq)
	elif path == '/stall': #return data
		f = open(ospath + '/return', 'w+')
		f.write(bot.getStall())
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == '/stall': #return data
		f = open(ospath + '/return', 'w+')
		f.write(bot.getStall())
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == '/name': #return data
		f = open(ospath + '/return', 'w+')
		f.write(bot.getName())
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == '/getpos': 
		regex = re.compile("\/getpos([ir|line|light])-([0-9]+)")
		m = regex.match(path)
		sensor = m.group(1)
		pos = int(m.group(2)) - 1
		f = open(ospath + '/return', 'w+')
		f.write(bot.get(sensor, pos))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
if __name__ == "__main__":
    import os
    import re
    import SocketServer
    from myro import *
    PORT = 3610 #S^2 with a 0
    bot = Scribbler(str(raw_input('What port is your robot at?')))
    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()


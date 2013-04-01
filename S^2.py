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
		regex = re.compile('\/motorinf([0-9]+)-([0-9]+)([+|-])([+|-])')
		m = regex.match(path)
		if m.group(3) == '-':
			l = int(m.group(1)) * -0.01
		else:
			l = int(m.group(1)) * 0.01
		if m.group(4) == '-':
			r = int(m.group(2)) * -0.01
		else:
			r = int(m.group(2)) * 0.01
		bot.motors(l, r)
	elif 'moveinf' in path:
		regex = re.compile("\/moveinf([0-9]+)([+|-])")
		m = regex.match(path)
		if m.group(2) == '-':
			power = int(m.group(1)) * -0.01
		else:
			power = int(m.group(1)) * 0.01
		print int(m.group(1))
		print power
		bot.translate(power)
	elif 'led' in path:
		regex = re.compile("\/led([left|center|right])([on|off])")
		m = regex.match(path)
		led = m.group(1)
		power = int(m.group(2))
		bot.setLED(led, power)
	elif 'tone' in path:
		regex = re.compile("\/tone([0-9]+)-([0-9]+)")
		m = regex.match(path)
		time = int(m.group(1)) * 0.01
		freq = int(m.group(2))
		bot.beep(time, freq)
	elif path == '/stall': #return data
		f = open(ospath + '/return', 'w+')
		f.write(str(bot.getStall()))
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
	elif 'setn' in path:
		regex = re.compile('\/setn([a-zA-z0-9]+)')
		m = regex.match(path)
		bot.setName(m.group(1))
	elif 'light' in path:
		regex = re.compile("\/light([0-9]+)")
		m = regex.match(path)
		pos = int(m.group(1)) - 1
		f = open(ospath + '/return', 'w+')
		f.write(str(bot.getLight(pos)))
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
	elif 'IR' in path:
		regex = re.compile("\/IR([0-9]+)")
		m = regex.match(path)
		pos = int(m.group(1)) - 1
		f = open(ospath + '/return', 'w+')
		f.write(str(bot.getIR(pos)))
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
	elif 'line' in path:
		regex = re.compile("\/line([0-9]+)")
		m = regex.match(path)
		pos = int(m.group(1)) - 1
		f = open(ospath + '/return', 'w+')
		f.write(str(bot.getLine(pos)))
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
    botport = raw_input('What port is your robot at? ')
    bot = Scribbler(botport)
    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()


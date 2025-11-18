hey this is how to install 2 pwas

so we forst need to genrrate the key and cert pair using thr command below


link to solution: https://stackoverflow.com/questions/77510803/how-to-make-a-simple-https-server-in-python-3x

command to generate key and cert
(for common name srrver name you must hse 127.0.0.1)

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem



python code to start server after key and cert created 

Note: Don't forget to set Common Name (e.g. server FQDN or YOUR name) [] to 127.0.0.1 !








import http.server
import ssl


def get_ssl_context(certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile, keyfile)
    context.set_ciphers("@SECLEVEL=1:ALL")
    return context


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data.decode("utf-8"))


server_address = ("127.0.0.1", 5000)
httpd = http.server.HTTPServer(server_address, MyHandler)

context = get_ssl_context("cert.pem", "key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()


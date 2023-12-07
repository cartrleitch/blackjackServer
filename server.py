from http.server import SimpleHTTPRequestHandler, HTTPServer

# thank you chatGPT
class FileDownloadServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/download':
            # Specify the file to be downloaded
            file_path = './blackjack.exe'
            
            # Open the file in binary mode
            with open(file_path, 'rb') as file:
                # Set response headers
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=blckjck.exe')
                self.end_headers()
                
                # Send the file content
                self.wfile.write(file.read())
                print("Downloaded blackjack! Type blackjack.exe to run!")
        else:
            # Serve files as usual
            super().do_GET()

def run_server():
    server_address = ('', 8000)  # You can change the port number if needed
    httpd = HTTPServer(server_address, FileDownloadServer)
    print('File download server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

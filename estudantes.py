import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000
HERE = Path(__file__).resolve().parent

class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()


def main():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        print('Iniciando servidor local para o quiz...')
        webbrowser.open(f'http://localhost:{PORT}/quiz.html')
        with socketserver.TCPServer(('', PORT), QuietHTTPRequestHandler) as httpd:
            print(f'Abra o navegador se ele não abrir automaticamente: http://localhost:{PORT}/quiz.html')
            print('Pressione Ctrl+C para encerrar o servidor.')
            httpd.serve_forever()
    except OSError as error:
        print('Não foi possível iniciar o servidor: ', error)
    except KeyboardInterrupt:
        print('\nServidor encerrado pelo usuário.')


if __name__ == '__main__':
    import os
    os.chdir(HERE)
    main()

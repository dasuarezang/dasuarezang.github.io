"""Servidor local de la web para los scripts: sirve el repositorio tanto en / como en /cv/ (como GitHub Pages)."""
import functools
import http.server
import pathlib
import socketserver
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent


class _Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path == '/cv' or path.startswith('/cv/'):
            path = path[3:] or '/'
        return super().translate_path(path)

    def log_message(self, *args):
        pass


def serve():
    srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(_Handler, directory=str(ROOT)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, 'http://127.0.0.1:%d' % srv.server_address[1]

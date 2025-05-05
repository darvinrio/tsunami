# server.py
from connecpy import context
from connecpy.asgi import ConnecpyASGIApp

from proto.aloha_connecpy import AlohaEthereumServiceServer
from service import AlohaEthereumService

service = AlohaEthereumServiceServer(
    service=AlohaEthereumService()
)
app = ConnecpyASGIApp()
app.add_service(service)
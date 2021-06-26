from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import urls


application = ProtocolTypeRouter({
 'websocket': AuthMiddlewareStack(
  URLRouter(
   urls.urlpatterns
  )
 ),
})
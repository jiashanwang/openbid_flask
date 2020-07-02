# encoding= utf-8
from application import app

from web.controllers.index import index_page
from web.controllers.bidopen import bid_page

app.register_blueprint(index_page, url_prefix="/index")
app.register_blueprint(bid_page, url_prefix="/bidOpen")

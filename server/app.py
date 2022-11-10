import socketio

sio  = socketio.Server()

app = socketio.WSGIApp(sio, static_files= {
    '/': '../web/'
})

@sio.event
def connect(sid, environ):
    print('connected', sid)

@sio.event
def disconnect(sid):
    pass

@sio.event(namespace='association_rules')
def params(sid, data):
    print(data)


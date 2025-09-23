def application(evarion,start_response):
    body = b"<h1>Hello World!</h1><button>Click</button>"
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    start_response = (status,headers)
    return [body]

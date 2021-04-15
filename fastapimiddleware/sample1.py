#HTTPSRedirectMiddleware¶
#Enforces that all incoming requests must either be https or wss.

#Any incoming requests to http or ws will be redirected to the secure scheme instead.

from fastapi import FastAPI

from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()


app.add_middleware(HTTPSRedirectMiddleware)



@app.get("/")
async def main():
    return {"message": "Hello World"}

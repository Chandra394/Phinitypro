#TrustedHostMiddleware¶
#Enforces that all incoming requests have a correctly set Host header, 
# in order to guard against HTTP Host Header attacks.

from fastapi import FastAPI

from fastapi.middleware.trustedhost import TrustedHostMiddleware


app = FastAPI()


app.add_middleware(

    #TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
TrustedHostMiddleware, allowed_hosts=["*"] # it will allow all the host

)



@app.get("/")
async def main():
    return {"message": "Hello World"}

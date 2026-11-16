from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_request1(request: Request, call_next):
    print("中间件1：请求进入", request.url.path)
    response = await call_next(request)
    print("中间件1：响应返回", response.status_code)
    return response


# 后注册的中间件在更外层，请求发起后，会先经过中间件2，再经过中间件1
@app.middleware("http")
async def log_request2(request: Request, call_next):
    # 后注册的中间件位于外层：请求时先执行，响应时后执行。
    print("中间件2：请求进入", request.url.path)
    response = await call_next(request)
    print("中间件2：响应返回", response.status_code)
    return response


@app.get("/")
def home():
    print("接口函数：处理请求")
    return {"message": "Hello"}

from fastapi import Depends, FastAPI

app = FastAPI()


# 创建依赖项
# 依赖函数：集中处理多个接口可能共用的分页参数
def get_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/items")
def list_items(
# 使用依赖项
# 请求过来时，会从请求参数中读取skip,limit，然后调用get_pagination，将函数返回值赋予给pagination
    pagination: dict=Depends(get_pagination)
):
    items = ["苹果", "香蕉", "橙子"]

    # pagination 是 get_pagination() 的返回值，
    # 由 FastAPI 自动传入，这里不用手动调用。
    start = pagination["skip"]
    end = start + pagination["limit"]
    return {"items": items[start:end]}
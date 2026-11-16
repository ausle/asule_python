
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette.responses import HTMLResponse, FileResponse

# 创建一个fastapi实例
app = FastAPI()

# fastapi实例get请求方法，后面接着请求路径
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# 1、路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": f'这是第{item_id}个item'}

# 使用Path函数来限定"路径参数"
# 必填、0~100之间
@app.get("/items/path/{item_id}")
def read_path_item(item_id: int=Path(...,gt=0,lt=100,description='条目ID')):
    return {"item_id": f'这是第{item_id}个item'}

# 路径参数的最小长度和最大长度
@app.get("/books/path/{book_name}")
def get_book_name(book_name: str=Path(...,min_length=2,max_length=4,description='书本名')):
    return {"item_id": f'书籍的名字叫{book_name}'}


# 2、查询参数
# skip：不传时默认为0；lt=100表示必须小于 100，所以 99 可以，100 不可以。
# limit：返回多少条记录，默认 10 条
@app.get("/news/news_list")
async def get_news_list(
    skip: int = Query(0, description="跳过的记录数", lt=100),
    limit: int = Query(10, description="返回的记录数"),
):
    return {"skip": skip, "limit": limit}


# 3、请求体参数
# 根据需求定义类型，使用Field来限定参数的长短，是否必输，默认值、描述等。
class User(BaseModel):
    username: str=Field(default='小明',min_length=2,max_length=5,description='用户名')
    password: str=Field(...,min_length=6,max_length=10,description='密码')

# 4、响应类型
# 默认JSON格式
@app.post("/user")
async def create_user(user: User):
# 默认情况下，FastAPI会自动将Python对象（），经由jsonable_encoder转换为JSON格式。并包装为JSONResponse返回。这样省去了手动序列化的步骤。
    return user

# 响应HTML格式
# 直接输出HTML页面。
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>Hello World</h1>"

# 响应文件内容
@app.get("/get_file")
async def get_file():
    file_path = "./files/img1.png"
    return FileResponse(file_path)

# 自定义响应数据
class News(BaseModel):
    id: int
    title: str
    content: str

# 只能返回News类型，少字段会报错。多字段，多余字段不予显示。
@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    # 异常情况处理
    if id not in id_list:
        raise HTTPException(status_code=404, detail="当前id不存在")
    return {
        "id": id,
        "title": f"这是第{id}本书",
        "content": "这是一本好书",
        "test_field":'测试字段'
    }


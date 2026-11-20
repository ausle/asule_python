from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from sqlalchemy import CHAR, Index, String, text
from sqlalchemy.dialects.mysql import DATETIME, ENUM, LONGTEXT
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 1. 创建异步引擎
# URL 中的 mysql 是数据库类型，aiomysql 是异步 MySQL 驱动。
# 引擎负责管理数据库连接；后续可以通过 AsyncSession 执行 ORM 查询。
ASYNC_DATABASE_URL = "mysql+aiomysql://root:Jszc%402026@192.168.18.200:3306/chance_video_data?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,  # 开发时打印 SQL，便于观察 ORM 实际执行的语句。
    pool_size=10,  # 连接池中最多保留 10 个常规连接。
    max_overflow=20,  # 常规连接用完后，最多再临时创建 20 个连接。
)

# 2. 定义模型类：基类 + 表对应的模型类。
class Base(DeclarativeBase):
    """ORM 模型的公共基类；子类定义的表会记录在 Base.metadata 中。"""

    # 把多个表可能共用的创建时间放在基类中，子类会各自继承一列。
    # 当前 project 表的这一列是 datetime(3)，即时间精确到毫秒。
    # server_default 是数据库端默认值：插入时不传，MySQL 会填当前时间。
    creation_time: Mapped[datetime] = mapped_column(
        DATETIME(fsp=3),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP(3)"),
    )


class Project(Base):
    """把 Python 的 Project 对象映射到 project_1 表。"""

    # 你当前使用 project_1 作为表名；定义模型本身不会读写数据库。
    __tablename__ = "project_1"

    # Mapped[str] 表示在 Python 中按字符串使用；mapped_column 描述数据库列。
    # uuid 是 char(36) 主键。表中没有默认值，新增项目时需要提供 UUID。
    uuid: Mapped[str] = mapped_column(CHAR(36), primary_key=True)

    # 标题对应 varchar(255)；nullable=False 对应数据库的 NOT NULL。
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    # MySQL ENUM 限定了数据库允许保存的两个项目类型。
    type: Mapped[str] = mapped_column(ENUM("图片轮播", "HTML动画"), nullable=False)

    # 两列在数据库中都是 longtext，适合保存较长的文本内容。
    storyboard_outline: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    video_source: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

    # 为创建时间建立索引，便于按时间查询或排序。
    __table_args__ = (Index("idx_project_creation_time", "creation_time"),)


# 3. 单独封装建表操作，应用启动时调用，也方便以后手动复用。
async def create_tables() -> None:
    # begin() 从异步引擎取得连接，并在代码块结束时提交或回滚事务。
    async with async_engine.begin() as connection:
        # create_all() 是同步接口，需要通过 run_sync() 在异步连接上执行。
        # tables 只选择 Project 对应的 project_1 表；存在时默认跳过。
        # 它不会更新已有表的字段；修改表结构需要另行做数据库迁移。
        await connection.run_sync(
            Base.metadata.create_all,
            tables=[Project.__table__],
        )


# 4. 应用生命周期：yield 之前是启动阶段，yield 之后是关闭阶段。
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # FastAPI 启动时调用建表函数；成功后才进入请求处理阶段。
        await create_tables()

        # yield 将控制权交给 FastAPI，应用在此期间处理请求。
        yield
    finally:
        # 应用关闭时释放连接池；即使启动阶段出错，也会执行清理。
        await async_engine.dispose()


# 把 lifespan 交给 FastAPI，启动应用时会自动执行上面的建表检查。
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}

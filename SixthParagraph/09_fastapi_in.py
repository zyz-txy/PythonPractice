from fastapi import FastAPI

#创建FastAPI实例
app = FastAPI()

#定义API接口 ---> 该函数的返回值表示 API接口 返回的数据，接口访路径为 / ，请求方式为 GET
@app.get("/")
def root():
    return {"message": "Hello World"}

#定义API接口
@app.get("/users")
def get_users():
    return [
        {"id": 1,"name": "张三"},
        {"id": 2,"name": "李四"},
        {"id": 3,"name": "王五"}
    ]

#程序运行入口 启动服务----> uvicorn: Python中的轻量级Web服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000) #仅本机
    #host = '0.0.0.0',port = 8000 全域
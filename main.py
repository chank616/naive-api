from fastapi import FastAPI, File
import ddddocr

app = FastAPI()
# 初始化ddddocr对象
ocr = ddddocr.DdddOcr(show_ad=False, beta=True)

# 图片识别接口
@app.post("/image_recognition")
async def image_recognition(file: bytes = File(...)):
    # 处理图片识别逻辑
    result = ocr.classification(file)
    return {"result": result}

@app.get("/")
async def root():
    return {"message": "Hello World"}
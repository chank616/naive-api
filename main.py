from fastapi import FastAPI, File, Request
from fastapi.templating import Jinja2Templates
import ddddocr

app = FastAPI(docs_url=None, redoc_url=None)
# 设置Jinja2模板目录
templates = Jinja2Templates(directory="template")
# 初始化ddddocr对象
ocr = ddddocr.DdddOcr(show_ad=False, beta=True)

# 图片识别接口
@app.post("/image_recognition")
async def image_recognition(file: bytes = File(...)):
    # 处理图片识别逻辑
    result = ocr.classification(file)
    return {"result": result}

@app.get("/", response_class=templates.TemplateResponse)
async def image_recognition_html(request: Request):
    # 处理图片识别html页面
    return templates.TemplateResponse("captcha.html", {"request": request})

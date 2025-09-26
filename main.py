from fastapi import FastAPI, Request  # FastAPI 앱을 만들기 위해 FastAPI 클래스와, 요청 객체를 처리할 때 사용할 Request를 임포트
from fastapi.responses import HTMLResponse  # 클라이언트에게 HTML 형식의 응답을 반환하기 위해
from fastapi.staticfiles import StaticFiles  # CSS, JS, 이미지 등 정적 파일을 제공
from fastapi.templating import Jinja2Templates   # HTML 파일에 데이터를 삽입

app = FastAPI()

# 정적 파일 제공
# 접근 예) http://localhost:8080/static 즉, /static 경로로 들어오는 요청을 static/ 폴더의 파일에서 처리하도록 설정
app.mount("/static", StaticFiles(directory='static'), name='static')
# name="static"; 코드에서 접근할 때

#  html템플릿 제공
templates = Jinja2Templates(directory='templates') # 템플릿 파일이 들어 있는 디렉토리 경로를 지정

@app.get('/', response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})
# request: Request: FastAPI의 요청 객체를 받아옵니다. 템플릿에서 사용하기 위해 반드시 넘겨줘야 합니다.
# {'request': request}: Jinja2 템플릿에서 request 객체를 사용할 수 있게 넘겨줍니다. 이는 FastAPI에서 필수입니다.



@app.get('/api/data')
async def get_data():
    return {'message':'FastAPI에서 보내는 데이터입니다'}
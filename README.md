# FastAPI Project 

이 저장소는 **FastAPI 기반 웹 애플리케이션** 프로젝트입니다.
서버 구동, 클라이언트 연동, 머신러닝 분류기(Shape Classifier) 기능을 포함하고 있습니다.


## 프로젝트 구조


.
├── crawling/               # 크롤링 관련 모듈
├── santa/                  # Santa 관련 기능 모듈
├── static/                 # 정적 파일 (CSS, JS, 이미지 등)
├── templates/              # HTML 템플릿 (Jinja2)
├── .gitignore              # Git 무시 규칙
├── README.md               # 프로젝트 설명 문서
├── ad_client.py            # 광고 클라이언트 모듈
├── ad_server.py            # 광고 서버 모듈
├── main.py                 # FastAPI 메인 실행 파일
├── server.py               # 서버 실행 관련 모듈
├── shape_classifier.py     # 도형 분류기 (머신러닝/딥러닝 모델)
├── shape_client.py         # 도형 분류 클라이언트
└── shape_server.py         # 도형 분류 서버





## 🔑 주요 기능

* **FastAPI 웹 서버**: REST API 및 웹 서비스 제공
* **Shape Classifier**: 이미지 기반 도형 분류기
* **크롤링 모듈**: 데이터 수집 기능
* **광고 모듈**: 클라이언트/서버 구조로 동작하는 광고 처리 기능
* **템플릿 렌더링**: Jinja2 기반 HTML 페이지 지원




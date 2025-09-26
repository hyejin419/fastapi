import gradio as gr
import requests  # FastAPI 서버에 POST 요청을 보내기 위한 HTTP 클라이언트

url = "http://127.0.0.1:8000/create_ad"
def generate_ad(product_name, details, tone_and_manner):
    try:
        response = requests.post(url, json={
            "product_name": product_name,
            "details": details,
            "tone_and_manner": ", ".join(tone_and_manner)
        })  # FastAPI 서버에 JSON 데이터를 POST로 전송. (tone_and_manner는 리스트 형태이므로 문자열로 병합해서 보냄)
        ad = response.json()['ad']
        datas = response.json()["datas"]
        processed_datas = [[d['product_name'], d['details'], d['tone_and_manner'], d['ad']] for d in datas]
        return ad, processed_datas
    except:
        return "서버 연결 실패!", None
    
    # Gradio UI 구성
with gr.Blocks(title="광고 문구 생성기") as demo:
    gr.Markdown("광고 문구를 생성해주는 AI 서비스앱")
    with gr.Row():
        product_input = gr.Textbox(label="제품 이름", placeholder="예: 천연 치약")
        details_input = gr.Textbox(label="주요 내용", placeholder="자극 없는 천연 원료 치약")

    # 체크박스 그룹
    tone_options = gr.CheckboxGroup(
        label="광고 문구의 느낌",
        choices=["기본", "재밌게", "과장스럽게", "참신하게", "고급스럽게", "센스있게", "신선하게", "친근하게", "전문성있게"],
        value=["기본"]
    )

    # 버튼과 출력 구성
    generate_btn = gr.Button("광고 문구 생성하기")
    output_ad = gr.Textbox(label="생성된 광고 문구", lines=3)
    output_table = gr.DataFrame(label="세부 데이터", headers=["key", "value"], wrap=True)
    # 버튼 클릭 이벤트 연결 
    generate_btn.click(fn=generate_ad, inputs=[product_input, details_input, tone_options], outputs=[output_ad, output_table])

    demo.launch()
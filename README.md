# 📧 Phi-2 기반 메일 제목 분류기

**메일 제목을 입력하면, LLM이 자동으로 메일 유형을 분류해주는 데모입니다.**  
Microsoft의 소형 LLM인 [`Phi-2`](https://huggingface.co/microsoft/phi-2)를 기반으로, 로컬에서도 실행 가능한 경량 데모를 구현했습니다.

> ✨ 분류 예시: 광고 / 업무 / 개인 / 스팸 / 뉴스레터

---

## 🚀 데모 미리보기

![demo-screenshot](demo.gif)

---

## 🧠 사용 기술

- **LLM**: [microsoft/phi-2](https://huggingface.co/microsoft/phi-2)
- **Inference**: Hugging Face Transformers
- **UI**: Streamlit
- **로컬 실행**: Docker

---

## 📦 로컬 실행 방법

### 1. 도커 빌드 & 실행
```bash
git clone https://github.com/yourusername/phi2-mail-classifier.git
cd phi2-mail-classifier

# 빌드
docker build -t phi2-mail-classifier .

# 실행 (GPU 있는 경우)
docker run -p 8501:8501 --gpus all phi2-mail-classifier

# 실행 (GPU 없는 경우)
docker run -p 8501:8501 phi2-mail-classifier
```

접속: [http://localhost:8501](http://localhost:8501)

---

## 🧪 분류 방식

프롬프트 기반 분류:

```
Classify the email subject into a category (work, personal, spam, ad, newsletter).
Email subject: '50% off only today!'
Category:
```

Phi-2 모델이 텍스트 생성을 통해 적절한 카테고리를 생성합니다.

---

## 📁 파일 설명

| 파일명 | 설명 |
|--------|------|
| `app.py` | Streamlit 데모 앱 |
| `classify.py` | Phi-2 로딩 및 inference 코드 |
| `Dockerfile` | 도커 환경 정의 |
| `requirements.txt` | 종속 라이브러리 목록 |

---

## 📝 참고

- 모델 출처: [microsoft/phi-2 on Hugging Face](https://huggingface.co/microsoft/phi-2)
- 개발 환경: Python 3.10, CUDA 지원 GPU (선택)
- 라이선스: MIT

---

## 🙋‍♀️ 만든 이유

LLM을 활용한 분류 문제 접근 방식을 학습하고, 실전 프로젝트 포트폴리오에 포함하기 위해 제작했습니다.  
추후 Fine-tuning / QLoRA 적용도 고려하고 있습니다.

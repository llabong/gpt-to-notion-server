# GPT to Notion Server

GPT 기반 주식 추천 데이터를 Notion DB에 자동으로 연동하는 FastAPI 백엔드 서버입니다.

---

## 🧠 Project Purpose (프로젝트 목적)

GPT 또는 사용자가 분석한 종목 추천 정보를 수기로 Notion에 정리하던 기존 방식에서 벗어나,
**구조화된 API + 자동화 로직**을 통해 일관된 기록과 빠른 투자 판단을 가능하게 합니다.

---

## 📦 Features (주요 기능)

* 🚀 **FastAPI 기반 API 서버**
* 📌 **Pydantic 유효성 검증 + 확률 필드 검사**
* 🔗 **Notion DB 연동 자동화**
* 🧠 **유니크 키 기반 중복 삽입 방지**
* ⚙️ `.env` 설정을 통한 민감 정보 분리

---

## 📁 Project Structure (예정)

```
gpt-to-notion-server/
├── main.py
├── models/
│   └── stock.py
├── routers/
│   └── recommendation.py
├── services/
│   └── notion_uploader.py
├── clients/
│   └── notion.py
├── utils/
│   └── response.py
├── .env
└── requirements.txt
```

---

## ⚙️ Tech Stack

* FastAPI + Uvicorn
* Pydantic
* Notion API (`notion-client`)
* Python 3.10+

---

## 🚀 Getting Started (시작하기)

```bash
# 레포 클론
git clone https://github.com/llabong/gpt-to-notion-server.git
cd gpt-to-notion-server

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn main:app --reload
```

---

## 🔐 Environment Variables (.env 예시)

```env
NOTION_API_KEY=your-secret-key
NOTION_DB_ID=your-database-id
```

---

## 👤 Roles (역할 분담)

| 역할                      | 닉네임                  | GitHub                                        |
| ----------------------- | -------------------- | --------------------------------------------- |
| 👨‍💻 Backend Developer | dev-lb (llabong)     | [llabong](https://github.com/llabong)         |
| 👨‍💼 Planner / PM      | pm-gmR (ugamezeRepo) | [ugamezeRepo](https://github.com/ugamezeRepo) |

---

## 📄 License

This project is licensed under the MIT License.

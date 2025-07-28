import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="AI 이미지 퀴즈", layout="centered")

# 스타일 커스터마이징
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .question-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 250px;
        }
        .stButton>button {
            background-color: #0BAB8B;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #099e7e;
        }
        .correct {
            background-color: #d1fadf;
            padding: 10px;
            border-radius: 8px;
        }
        .wrong {
            background-color: #fde2e1;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# 퀴즈 데이터 (이미지 링크는 임시)
quiz_data = [
    {
        "question": "이 캐릭터의 이름은 무엇인가요?",
        "image_path": "1. quiz.png",
        "answer_image": "1. answer.png",
        "options": ["포코타", "코코", "오비스", "펭"],
        "answer": "포코타"
    },
    {
        "question": "이 캐릭터의 이름은 무엇인가요?",
        "image_path": "2. quiz.png",
        "answer_image": "2. answer.png",
        "options": ["포코타", "코코", "오비스", "펭"],
        "answer": "포코타"
    },
    # 최대 10개까지 추가 가능
]

# 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.questions = random.sample(quiz_data, len(quiz_data))
    st.session_state.answered = False
    st.session_state.selected = ""

# 진행도
st.title("🧠 포코 캐릭터 퀴즈")
st.progress((st.session_state.step) / len(st.session_state.questions))

# 현재 문제
current = st.session_state.questions[st.session_state.step]
st.subheader(f"Q{st.session_state.step + 1}. {current['question']}")
st.image(current["image_path"], use_container_width=True)

# 정답 제출
if not st.session_state.answered:
    choice = st.radio("보기 중 정답을 골라주세요.", current["options"], index=None)
    if st.button("제출하기", key="submit") and choice:
        st.session_state.answered = True
        st.session_state.selected = choice
        if choice == current["answer"]:
            st.session_state.score += 1
else:
    # 정답 결과 화면
    st.image(current["answer_image"], caption="정답 이미지", use_container_width=True)
    if st.session_state.selected == current["answer"]:
        st.markdown("<div class='correct'>✅ 정답입니다!</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='wrong'>❌ 오답입니다. 정답은 <b>{current['answer']}</b>입니다.</div>", unsafe_allow_html=True)

    if st.button("다음 문제로", key="next"):
        st.session_state.step += 1
        st.session_state.answered = False
        st.session_state.selected = ""

# 결과 요약
if st.session_state.step >= len(st.session_state.questions):
    st.balloons()
    st.subheader("🎉 퀴즈 완료!")
    st.success(f"총 {len(st.session_state.questions)}문제 중 {st.session_state.score}문제를 맞췄습니다.")
    if st.button("퀴즈 다시 풀기"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.questions = random.sample(quiz_data, len(quiz_data))
        st.session_state.answered = False
        st.session_state.selected = ""

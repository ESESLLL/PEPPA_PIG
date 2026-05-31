import streamlit as st
import random

# ===== 頁面設定 =====
st.set_page_config(page_title="小豬數學樂園 🐷", page_icon="🐷", layout="centered")

# ===== 全域 CSS 美化 =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FFE5F1 0%, #E5F1FF 50%, #FFF5E5 100%);
}
div.stButton > button {
    font-size: 42px !important;
    font-weight: bold !important;
    height: 90px !important;
    border-radius: 25px !important;
    border: 4px solid #FF9ECD !important;
    background: linear-gradient(145deg, #FFF0F7, #FFE0EF) !important;
    color: #FF4F9A !important;
    box-shadow: 0 6px 0 #FFB6D9 !important;
    transition: all 0.1s !important;
}
div.stButton > button:hover {
    transform: translateY(2px) !important;
    box-shadow: 0 4px 0 #FFB6D9 !important;
    background: linear-gradient(145deg, #FFE0EF, #FFD0E7) !important;
}
div.stButton > button:active {
    transform: translateY(6px) !important;
    box-shadow: 0 0px 0 #FFB6D9 !important;
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.bounce { display:inline-block; animation: bounce 1s infinite; }
</style>
""", unsafe_allow_html=True)

# ===== 自製超可愛角色 (SVG 單行版，免版權) =====
def pig_svg(color="#FFB6C1"):
    return f'<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><ellipse cx="50" cy="55" rx="38" ry="32" fill="{color}"/><ellipse cx="28" cy="32" rx="9" ry="12" fill="{color}"/><ellipse cx="72" cy="32" rx="9" ry="12" fill="{color}"/><ellipse cx="50" cy="68" rx="15" ry="12" fill="#FF8DAA"/><ellipse cx="44" cy="68" rx="3" ry="4" fill="#C25C7C"/><ellipse cx="56" cy="68" rx="3" ry="4" fill="#C25C7C"/><circle cx="38" cy="45" r="7" fill="#fff"/><circle cx="62" cy="45" r="7" fill="#fff"/><circle cx="39" cy="46" r="3.5" fill="#000"/><circle cx="61" cy="46" r="3.5" fill="#000"/><circle cx="40.5" cy="44.5" r="1.5" fill="#fff"/><circle cx="62.5" cy="44.5" r="1.5" fill="#fff"/><ellipse cx="32" cy="58" rx="6" ry="4" fill="#FFA0C0" opacity="0.6"/><ellipse cx="68" cy="58" rx="6" ry="4" fill="#FFA0C0" opacity="0.6"/><path d="M42 80 Q50 86 58 80" stroke="#C25C7C" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>'

def cat_svg():
    return '<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><polygon points="25,28 38,52 14,50" fill="#FFA64D"/><polygon points="75,28 62,52 86,50" fill="#FFA64D"/><polygon points="25,32 35,48 19,47" fill="#FFD1A0"/><polygon points="75,32 65,48 81,47" fill="#FFD1A0"/><circle cx="50" cy="58" r="33" fill="#FFB870"/><circle cx="40" cy="52" r="7" fill="#fff"/><circle cx="60" cy="52" r="7" fill="#fff"/><circle cx="40" cy="53" r="3.5" fill="#000"/><circle cx="60" cy="53" r="3.5" fill="#000"/><circle cx="41.5" cy="51.5" r="1.5" fill="#fff"/><circle cx="61.5" cy="51.5" r="1.5" fill="#fff"/><polygon points="50,60 45,65 55,65" fill="#FF6B6B"/><path d="M50 65 Q50 70 45 70 M50 65 Q50 70 55 70" stroke="#000" stroke-width="1.5" fill="none"/><ellipse cx="32" cy="62" rx="5" ry="3" fill="#FFCBA0"/><ellipse cx="68" cy="62" rx="5" ry="3" fill="#FFCBA0"/><line x1="18" y1="58" x2="36" y2="60" stroke="#888" stroke-width="1.5"/><line x1="18" y1="64" x2="36" y2="64" stroke="#888" stroke-width="1.5"/><line x1="64" y1="60" x2="82" y2="58" stroke="#888" stroke-width="1.5"/><line x1="64" y1="64" x2="82" y2="64" stroke="#888" stroke-width="1.5"/></svg>'

def rabbit_svg():
    return '<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><ellipse cx="40" cy="22" rx="8" ry="20" fill="#fff" stroke="#EEE" stroke-width="1.5"/><ellipse cx="60" cy="22" rx="8" ry="20" fill="#fff" stroke="#EEE" stroke-width="1.5"/><ellipse cx="40" cy="24" rx="4" ry="14" fill="#FFD1DC"/><ellipse cx="60" cy="24" rx="4" ry="14" fill="#FFD1DC"/><circle cx="50" cy="60" r="31" fill="#fff" stroke="#EEE" stroke-width="1.5"/><circle cx="40" cy="55" r="6" fill="#000"/><circle cx="60" cy="55" r="6" fill="#000"/><circle cx="42" cy="53" r="2" fill="#fff"/><circle cx="62" cy="53" r="2" fill="#fff"/><ellipse cx="50" cy="64" rx="4" ry="3" fill="#FF8DAA"/><path d="M50 67 Q45 71 42 69 M50 67 Q55 71 58 69" stroke="#000" stroke-width="1.5" fill="none"/><ellipse cx="33" cy="63" rx="5" ry="4" fill="#FFD1DC" opacity="0.7"/><ellipse cx="67" cy="63" rx="5" ry="4" fill="#FFD1DC" opacity="0.7"/></svg>'

def dog_svg():
    return '<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><ellipse cx="24" cy="42" rx="11" ry="22" fill="#B5835A"/><ellipse cx="76" cy="42" rx="11" ry="22" fill="#B5835A"/><circle cx="50" cy="58" r="33" fill="#E0C097"/><circle cx="40" cy="52" r="7" fill="#fff"/><circle cx="60" cy="52" r="7" fill="#fff"/><circle cx="40" cy="53" r="3.5" fill="#000"/><circle cx="60" cy="53" r="3.5" fill="#000"/><circle cx="41.5" cy="51.5" r="1.5" fill="#fff"/><circle cx="61.5" cy="51.5" r="1.5" fill="#fff"/><ellipse cx="50" cy="64" rx="6" ry="5" fill="#000"/><path d="M50 69 Q50 75 44 74 M50 69 Q50 75 56 74" stroke="#000" stroke-width="2" fill="none"/><ellipse cx="50" cy="76" rx="5" ry="3" fill="#FF8DAA"/></svg>'

def bear_svg():
    return '<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><circle cx="28" cy="30" r="13" fill="#C89B6E"/><circle cx="72" cy="30" r="13" fill="#C89B6E"/><circle cx="28" cy="30" r="7" fill="#E5C9A5"/><circle cx="72" cy="30" r="7" fill="#E5C9A5"/><circle cx="50" cy="58" r="33" fill="#C89B6E"/><circle cx="40" cy="52" r="6" fill="#000"/><circle cx="60" cy="52" r="6" fill="#000"/><circle cx="42" cy="50" r="2" fill="#fff"/><circle cx="62" cy="50" r="2" fill="#fff"/><circle cx="50" cy="64" r="9" fill="#E5C9A5"/><ellipse cx="50" cy="61" rx="5" ry="4" fill="#000"/><path d="M50 65 L50 70 M50 70 Q46 72 44 70 M50 70 Q54 72 56 70" stroke="#000" stroke-width="2" fill="none"/></svg>'

def frog_svg():
    return '<svg width="58" height="58" viewBox="0 0 100 100" style="display:inline-block;margin:3px"><ellipse cx="50" cy="62" rx="36" ry="30" fill="#7AC74F"/><circle cx="32" cy="32" r="15" fill="#7AC74F"/><circle cx="68" cy="32" r="15" fill="#7AC74F"/><circle cx="32" cy="30" r="9" fill="#fff"/><circle cx="68" cy="30" r="9" fill="#fff"/><circle cx="32" cy="31" r="4.5" fill="#000"/><circle cx="68" cy="31" r="4.5" fill="#000"/><circle cx="33.5" cy="29.5" r="1.5" fill="#fff"/><circle cx="69.5" cy="29.5" r="1.5" fill="#fff"/><path d="M35 65 Q50 78 65 65" stroke="#3D8B27" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="35" cy="60" rx="5" ry="3" fill="#FF8DAA" opacity="0.6"/><ellipse cx="65" cy="60" rx="5" ry="3" fill="#FF8DAA" opacity="0.6"/></svg>'

CHARACTERS = {
    "🐷 粉紅豬": pig_svg("#FFB6C1"),
    "🐷 紫色豬": pig_svg("#D8B5E8"),
    "🐷 黃色豬": pig_svg("#FFE5A0"),
    "🐱 小貓咪": cat_svg(),
    "🐰 小白兔": rabbit_svg(),
    "🐶 小狗狗": dog_svg(),
    "🐻 小熊熊": bear_svg(),
    "🐸 小青蛙": frog_svg(),
}

# ===== 音效 (Web Audio API，免外部檔案) =====
def play_sound(kind):
    if kind == "correct":
        js = """
        <script>
        var ctx = new (window.AudioContext || window.webkitAudioContext)();
        var notes = [523, 659, 784, 1047];
        notes.forEach((f, i) => {
            var o = ctx.createOscillator();
            var g = ctx.createGain();
            o.connect(g); g.connect(ctx.destination);
            o.frequency.value = f; o.type = 'triangle';
            g.gain.setValueAtTime(0.2, ctx.currentTime + i*0.12);
            g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + i*0.12 + 0.15);
            o.start(ctx.currentTime + i*0.12);
            o.stop(ctx.currentTime + i*0.12 + 0.15);
        });
        </script>
        """
    else:
        js = """
        <script>
        var ctx = new (window.AudioContext || window.webkitAudioContext)();
        var o = ctx.createOscillator();
        var g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.frequency.setValueAtTime(300, ctx.currentTime);
        o.frequency.linearRampToValueAtTime(150, ctx.currentTime + 0.3);
        o.type = 'sawtooth';
        g.gain.setValueAtTime(0.15, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3);
        o.start(); o.stop(ctx.currentTime + 0.3);
        </script>
        """
    st.components.v1.html(js, height=0)

# ===== 🔐 登入系統 (密碼 = ally) =====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center'>🐷 小豬數學樂園 🌈</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FF69B4'>🔒 請先登入才能開始玩喔！</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-size:60px'>🐷🐱🐰🐶🐻🐸</div>", unsafe_allow_html=True)

    pwd = st.text_input("🔑 請輸入密碼：", type="password")
    if st.button("🚪 登入", use_container_width=True):
        if pwd == "ally":
            st.session_state.logged_in = True
            st.balloons()
            st.rerun()
        else:
            st.error("😅 密碼錯誤，再試試看！")
    st.stop()  # 沒登入就停在這裡

# ===== 初始化狀態 =====
for key, val in [("score", 0), ("stars", 0), ("question", None),
                 ("answered", False), ("result", None)]:
    if key not in st.session_state:
        st.session_state[key] = val

# ===== 出題函數 =====
def new_question(level):
    char_name = random.choice(list(CHARACTERS.keys()))
    max_num = {"簡單 (1-5)": 5, "中等 (1-10)": 10, "困難 (1-20)": 20}[level]

    op = random.choice(["+", "-"])
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)

    if op == "-":
        a, b = max(a, b), min(a, b)
        answer = a - b
    else:
        while a + b > max_num:
            a = random.randint(1, max_num)
            b = random.randint(1, max_num)
        answer = a + b

    options = {answer}
    while len(options) < 3:
        wrong = answer + random.randint(-3, 3)
        if wrong >= 0:
            options.add(wrong)
    options = list(options)
    random.shuffle(options)

    st.session_state.question = {
        "char_name": char_name, "a": a, "b": b,
        "op": op, "answer": answer, "options": options
    }
    st.session_state.answered = False
    st.session_state.result = None

# ===== 標題 =====
st.markdown("<h1 style='text-align:center'>🐷 小豬數學樂園 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#FF69B4'>一起來玩加減數學遊戲吧！</h3>", unsafe_allow_html=True)

# ===== 側邊欄 =====
with st.sidebar:
    st.header("⚙️ 遊戲設定")
    level = st.selectbox("選擇難度", ["簡單 (1-5)", "中等 (1-10)", "困難 (1-20)"])
    st.markdown("---")
    st.metric("⭐ 得到星星", st.session_state.stars)
    st.metric("🏆 答對題數", st.session_state.score)
    if st.button("🔄 重新開始"):
        st.session_state.score = 0
        st.session_state.stars = 0
        st.session_state.question = None
        st.rerun()
    if st.button("🚪 登出"):
        st.session_state.logged_in = False
        st.rerun()

# ===== 第一題 =====
if st.session_state.question is None:
    new_question(level)

q = st.session_state.question
svg = CHARACTERS[q["char_name"]]

# ===== 視覺化題目 =====
st.markdown("---")

def show_chars(n):
    return f"<div style='text-align:center; line-height:1.4'>{svg * n}</div>"

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.markdown(show_chars(q["a"]), unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#FF6B9D'>{q['a']}</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h1 style='text-align:center; margin-top:40px; color:#FF6B9D'>{q['op']}</h1>", unsafe_allow_html=True)
with col3:
    st.markdown(show_chars(q["b"]), unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#FF6B9D'>{q['b']}</h2>", unsafe_allow_html=True)

st.markdown(
    f"<h1 style='text-align:center; color:#FF4F9A'><span class='bounce'>{q['a']} {q['op']} {q['b']} = ❓</span></h1>",
    unsafe_allow_html=True
)

# ===== 答案按鈕 (用 CSS 美化，不用 ##) =====
st.markdown("<h3 style='text-align:center'>👇 點選正確答案 👇</h3>", unsafe_allow_html=True)
cols = st.columns(3)
for i, opt in enumerate(q["options"]):
    with cols[i]:
        if st.button(f"{opt}", key=f"opt_{i}", use_container_width=True):
            if not st.session_state.answered:
                st.session_state.answered = True
                if opt == q["answer"]:
                    st.session_state.score += 1
                    st.session_state.stars += 1
                    st.session_state.result = "correct"
                else:
                    st.session_state.result = "wrong"
                st.rerun()

# ===== 顯示結果 + 音效 =====
if st.session_state.answered:
    if st.session_state.result == "correct":
        st.markdown("<h2 style='text-align:center; color:#4CAF50'>🎉 答對了！太棒了！🌟</h2>", unsafe_allow_html=True)
        st.markdown("<div style='text-align:center; font-size:50px'>🐷🎊🥳🎊🐷</div>", unsafe_allow_html=True)
        play_sound("correct")
        st.balloons()
    else:
        st.markdown(f"<h2 style='text-align:center; color:#FF6B6B'>😅 再試試看！答案是 {q['answer']} 喔！</h2>", unsafe_allow_html=True)
        play_sound("wrong")

    if st.button("➡️ 下一題", use_container_width=True):
        new_question(level)
        st.rerun()

# ===== 鼓勵訊息 =====
st.markdown("---")
if st.session_state.stars >= 10:
    st.markdown("<h2 style='text-align:center'>🏆 哇！你是數學小天才！🐷👑</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-size:50px'>🌈🎉🏆🎉🌈</div>", unsafe_allow_html=True)
elif st.session_state.stars >= 5:
    st.markdown("<h2 style='text-align:center'>🌟 做得很好！繼續加油！</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align:center; color:#888'>加油！答對 5 題就有驚喜喔！🎈</h3>", unsafe_allow_html=True)

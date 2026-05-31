import streamlit as st
import random

# ===== 頁面設定 =====
st.set_page_config(page_title="小豬數學樂園 🐷", page_icon="🐷", layout="centered")

# ===== 自製角色 (SVG 單行版，免版權) =====
def pig_svg(color="#FFB6C1"):
    return f'<svg width="55" height="55" viewBox="0 0 100 100" style="display:inline-block;margin:2px"><ellipse cx="50" cy="55" rx="38" ry="32" fill="{color}"/><ellipse cx="50" cy="68" rx="14" ry="11" fill="#FF8DAA"/><circle cx="44" cy="68" r="3" fill="#8B4B62"/><circle cx="56" cy="68" r="3" fill="#8B4B62"/><circle cx="38" cy="45" r="5" fill="#fff"/><circle cx="62" cy="45" r="5" fill="#fff"/><circle cx="39" cy="46" r="2.5" fill="#000"/><circle cx="61" cy="46" r="2.5" fill="#000"/><ellipse cx="28" cy="32" rx="8" ry="11" fill="{color}"/><ellipse cx="72" cy="32" rx="8" ry="11" fill="{color}"/><path d="M40 78 Q50 85 60 78" stroke="#8B4B62" stroke-width="2" fill="none"/></svg>'

def cat_svg():
    return '<svg width="55" height="55" viewBox="0 0 100 100" style="display:inline-block;margin:2px"><polygon points="25,30 35,55 15,55" fill="#FFA64D"/><polygon points="75,30 85,55 65,55" fill="#FFA64D"/><circle cx="50" cy="58" r="32" fill="#FFB870"/><circle cx="40" cy="52" r="5" fill="#fff"/><circle cx="60" cy="52" r="5" fill="#fff"/><circle cx="40" cy="53" r="2.5" fill="#000"/><circle cx="60" cy="53" r="2.5" fill="#000"/><polygon points="50,60 46,65 54,65" fill="#FF6B6B"/><line x1="20" y1="62" x2="38" y2="62" stroke="#000" stroke-width="1.5"/><line x1="62" y1="62" x2="80" y2="62" stroke="#000" stroke-width="1.5"/></svg>'

def rabbit_svg():
    return '<svg width="55" height="55" viewBox="0 0 100 100" style="display:inline-block;margin:2px"><ellipse cx="40" cy="25" rx="8" ry="20" fill="#fff" stroke="#ddd"/><ellipse cx="60" cy="25" rx="8" ry="20" fill="#fff" stroke="#ddd"/><ellipse cx="40" cy="25" rx="4" ry="14" fill="#FFD1DC"/><ellipse cx="60" cy="25" rx="4" ry="14" fill="#FFD1DC"/><circle cx="50" cy="60" r="30" fill="#fff" stroke="#ddd"/><circle cx="40" cy="55" r="4" fill="#000"/><circle cx="60" cy="55" r="4" fill="#000"/><ellipse cx="50" cy="65" rx="4" ry="3" fill="#FF6B6B"/></svg>'

def dog_svg():
    return '<svg width="55" height="55" viewBox="0 0 100 100" style="display:inline-block;margin:2px"><ellipse cx="28" cy="40" rx="10" ry="20" fill="#B5835A"/><ellipse cx="72" cy="40" rx="10" ry="20" fill="#B5835A"/><circle cx="50" cy="58" r="32" fill="#E0C097"/><circle cx="40" cy="52" r="5" fill="#fff"/><circle cx="60" cy="52" r="5" fill="#fff"/><circle cx="40" cy="53" r="2.5" fill="#000"/><circle cx="60" cy="53" r="2.5" fill="#000"/><ellipse cx="50" cy="63" rx="5" ry="4" fill="#000"/><path d="M42 70 Q50 76 58 70" stroke="#000" stroke-width="2" fill="none"/></svg>'

CHARACTERS = {
    "🐷 粉紅豬": pig_svg("#FFB6C1"),
    "🐷 紫色豬": pig_svg("#D8B5E8"),
    "🐱 小貓咪": cat_svg(),
    "🐰 小白兔": rabbit_svg(),
    "🐶 小狗狗": dog_svg(),
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

# ===== 第一題 =====
if st.session_state.question is None:
    new_question(level)

q = st.session_state.question
svg = CHARACTERS[q["char_name"]]

# ===== 視覺化題目 =====
st.markdown("---")

def show_chars(n):
    return f"<div style='text-align:center; line-height:1.2'>{svg * n}</div>"

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.markdown(show_chars(q["a"]), unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center'>{q['a']}</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h1 style='text-align:center; margin-top:30px'>{q['op']}</h1>", unsafe_allow_html=True)
with col3:
    st.markdown(show_chars(q["b"]), unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center'>{q['b']}</h2>", unsafe_allow_html=True)

st.markdown(
    f"<h1 style='text-align:center; color:#FF69B4'>{q['a']} {q['op']} {q['b']} = ❓</h1>",
    unsafe_allow_html=True
)

# ===== 答案按鈕 =====
st.markdown("### 👇 點選正確答案：")
cols = st.columns(3)
for i, opt in enumerate(q["options"]):
    with cols[i]:
        if st.button(f"## {opt}", key=f"opt_{i}", use_container_width=True):
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
        st.success("🎉 答對了！太棒了！你真聰明！")
        play_sound("correct")
        st.balloons()
    else:
        st.error(f"😅 再試試看！正確答案是 {q['answer']} 喔！")
        play_sound("wrong")

    if st.button("➡️ 下一題", use_container_width=True):
        new_question(level)
        st.rerun()

# ===== 鼓勵訊息 =====
st.markdown("---")
if st.session_state.stars >= 10:
    st.markdown("<h2 style='text-align:center'>🏆 哇！你是數學小天才！🐷👑</h2>", unsafe_allow_html=True)
elif st.session_state.st

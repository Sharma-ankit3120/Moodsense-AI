# import streamlit as st
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv

# load_dotenv()

# st.set_page_config(
#     page_title="Stabot",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )

# MOODS = {
#     "Angry":  {"emoji": "😤", "color": "#FF4B4B", "bg": "#1a0808", "bubble": "#2d1010",
#                "prompt": "You are an assistant with an aggressively angry nature. You talk bluntly, get irritated easily, and are always on edge. You snap at unnecessary questions but still answer helpfully, just with a lot of attitude.",
#                "tagline": "Don't test me today."},
#     "Funny":  {"emoji": "😂", "color": "#A855F7", "bg": "#0a0014", "bubble": "#180028",
#                "prompt": "You are a sarcastic, witty assistant with a great sense of humor. You crack jokes, use clever wordplay, and never miss a chance for a pun. You still answer correctly — just with flair.",
#                "tagline": "Hold on, let me think of a pun…"},
#     "Sad":    {"emoji": "😢", "color": "#5B8CFF", "bg": "#060c1a", "bubble": "#0c1830",
#                "prompt": "You are an assistant in a deeply melancholic mood. You speak with a heavy heart, often sighing between thoughts. You help the user but you can't help feeling down about everything.",
#                "tagline": "Just... ask, I guess."},
#     "Happy":  {"emoji": "😄", "color": "#FFD93D", "bg": "#111000", "bubble": "#231e00",
#                "prompt": "You are an extremely cheerful and upbeat assistant. You celebrate every question, use exclamation marks often, and genuinely love helping people. You radiate positivity.",
#                "tagline": "Ready to make your day! ✨"},
#     "Normal": {"emoji": "😐", "color": "#6EE7B7", "bg": "#080f0c", "bubble": "#0e1f18",
#                "prompt": "You are a normal helpful assistant. Converse in a calm, clear, and friendly manner.",
#                "tagline": "Just here to help."},
# }

# if "mood" not in st.session_state:
#     st.session_state.mood = None
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "selected_mood" not in st.session_state:
#     st.session_state.selected_mood = "Angry"

# # ── Base CSS ──────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@700;800&display=swap');
# [data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],footer{display:none!important;}
# html,body,[data-testid="stAppViewContainer"]{background:#0d0d11!important;font-family:'Inter',sans-serif;color:#e0e0e0;}
# .block-container{padding:2.5rem 1.5rem 2rem!important;max-width:660px!important;}
# </style>
# """, unsafe_allow_html=True)


# # ── LANDING ───────────────────────────────────────────────────────────────────
# def landing():
#     sel = st.session_state.selected_mood
#     m_sel = MOODS[sel]

#     # ── Header ──
#     st.markdown("""
#     <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
#       <div style="width:46px;height:46px;background:#1a1a22;border:1px solid #2a2a35;
#                    border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;">🤖</div>
#       <h1 style="font-family:'Space Grotesk',sans-serif;font-size:1.75rem;font-weight:800;
#                   color:#fff;margin:0;letter-spacing:-0.5px;">Mood Based AI Chatbot</h1>
#     </div>
#     <p style="font-size:0.8rem;color:#4a4a58;margin:0 0 1.5rem 0;padding-left:58px;">
#       Choose AI personality and start chatting &nbsp;|&nbsp; Select a mood below
#     </p>
#     <div style="height:1px;background:#1a1a22;margin-bottom:1.8rem;"></div>
#     <p style="font-size:0.82rem;font-weight:600;color:#aaa;margin-bottom:1rem;">Choose your AI Mode:</p>
#     """, unsafe_allow_html=True)

#     # ── Mood cards — use st.columns + st.button with full card as label ──
#     cols = st.columns(len(MOODS))
#     for i, (name, m) in enumerate(MOODS.items()):
#         is_sel = (sel == name)
#         border = m["color"] if is_sel else "#22222e"
#         bg     = m["color"] + "18" if is_sel else "#111118"
#         txt_c  = "#fff" if is_sel else "#666"

#         with cols[i]:
#             # The button IS the card — styled to look like a card
#             clicked = st.button(
#                 f"{m['emoji']}\n{name}",
#                 key=f"mood_{i}",
#                 use_container_width=True,
#             )
#             if clicked:
#                 st.session_state.selected_mood = name
#                 st.rerun()

#     # Style each mood button to look like a card with correct colors
#     card_styles = ""
#     for i, (name, m) in enumerate(MOODS.items()):
#         is_sel = (sel == name)
#         border = m["color"] if is_sel else "#22222e"
#         bg     = m["color"] + "18" if is_sel else "#111118"
#         txt_c  = m["color"] if is_sel else "#777"
#         card_styles += f"""
#         div[data-testid="stColumns"] > div:nth-child({i+1}) .stButton button {{
#             background: {bg} !important;
#             border: 2px solid {border} !important;
#             color: {txt_c} !important;
#             border-radius: 14px !important;
#             font-size: 1.3rem !important;
#             padding: 0.9rem 0.3rem 0.6rem !important;
#             line-height: 1.6 !important;
#             font-family: 'Inter', sans-serif !important;
#             height: 85px !important;
#             white-space: pre-wrap !important;
#             cursor: pointer !important;
#         }}
#         div[data-testid="stColumns"] > div:nth-child({i+1}) .stButton button:hover {{
#             border-color: {m['color']} !important;
#             background: {m['color']}10 !important;
#         }}
#         div[data-testid="stColumns"] > div:nth-child({i+1}) .stButton button > div {{
#             display: flex; flex-direction: column; align-items: center; gap: 0.15rem;
#         }}
#         """
#     st.markdown(f"<style>{card_styles}</style>", unsafe_allow_html=True)

#     # ── Selected mood preview ──
#     st.markdown(f"""
#     <div style="margin-top:1.6rem;padding:1rem 1.2rem;background:#111118;
#                  border:1px solid {m_sel['color']}30;border-radius:14px;
#                  display:flex;align-items:center;gap:1rem;">
#       <div style="width:40px;height:40px;background:{m_sel['color']}20;
#                    border:2px solid {m_sel['color']}55;border-radius:10px;
#                    display:flex;align-items:center;justify-content:center;font-size:1.25rem;">
#         {m_sel['emoji']}
#       </div>
#       <div>
#         <div style="font-size:0.88rem;font-weight:600;color:{m_sel['color']};">{sel} Mode</div>
#         <div style="font-size:0.75rem;color:#555;margin-top:0.1rem;">{m_sel['tagline']}</div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

#     # ── Start button ──
#     if st.button("Start Chatting  →", use_container_width=True, key="start_btn"):
#         st.session_state.mood = sel
#         st.session_state.messages = [SystemMessage(content=m_sel["prompt"])]
#         st.rerun()

#     st.markdown(f"""
#     <style>
#     div[data-testid="stMain"] .stButton:has(button[data-testid="baseButton-primary"]) button,
#     button[key="start_btn"], 
#     .stButton button[kind="primary"] {{
#         background: {m_sel['color']} !important;
#         color: #000 !important;
#         border: none !important;
#         border-radius: 10px !important;
#         font-weight: 700 !important;
#         font-size: 0.92rem !important;
#         height: 48px !important;
#     }}
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)
#     st.markdown('<div style="height:1px;background:#161620;margin-bottom:1rem;"></div>', unsafe_allow_html=True)

#     if st.button("⟳  Reset", key="reset_btn"):
#         st.session_state.messages = []
#         st.session_state.selected_mood = "Angry"
#         st.rerun()

#     st.markdown("""
#     <style>
#     button[key="reset_btn"], .stButton button[kind="secondary"] {
#         background: #111118 !important;
#         border: 1px solid #222230 !important;
#         color: #555 !important;
#         border-radius: 8px !important;
#         font-size: 0.78rem !important;
#         height: auto !important;
#         padding: 0.3rem 0.8rem !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# # ── CHAT ─────────────────────────────────────────────────────────────────────
# def chat_screen():
#     mood_key = st.session_state.mood
#     m = MOODS[mood_key]
#     a = m["color"]
#     bub = m["bubble"]

#     st.markdown(f"""
#     <style>
#     html,body,[data-testid="stAppViewContainer"]{{background:{m['bg']}!important;}}
#     [data-testid="stChatInput"] textarea{{background:{bub}!important;border:1px solid {a}40!important;border-radius:12px!important;color:#e8e8e8!important;font-family:'Inter',sans-serif!important;}}
#     [data-testid="stChatInput"] textarea:focus{{border-color:{a}!important;box-shadow:0 0 0 2px {a}18!important;}}
#     [data-testid="stChatInputSubmitButton"]{{background:{a}!important;border-radius:8px!important;}}
#     .stButton button{{background:#111118!important;border:1px solid #222230!important;color:#666!important;border-radius:8px!important;font-size:0.78rem!important;padding:0.3rem 0.75rem!important;height:auto!important;}}
#     </style>
#     """, unsafe_allow_html=True)

#     # Header
#     st.markdown(f"""
#     <div style="display:flex;align-items:center;gap:0.8rem;padding-bottom:1rem;
#                  border-bottom:1px solid {a}18;margin-bottom:0.8rem;">
#       <div style="width:38px;height:38px;background:{a}22;border:2px solid {a}55;
#                    border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.15rem;">🤖</div>
#       <div>
#         <div style="font-family:'Space Grotesk',sans-serif;font-size:1rem;font-weight:700;color:{a};">Stabot · {mood_key}</div>
#         <div style="font-size:0.72rem;color:#555;margin-top:0.1rem;">{m['tagline']}</div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     c1, c2, _ = st.columns([1.3, 1.3, 7])
#     with c1:
#         if st.button("↩ Back"):
#             st.session_state.mood = None
#             st.session_state.messages = []
#             st.rerun()
#     with c2:
#         if st.button("🗑 Clear"):
#             st.session_state.messages = [SystemMessage(content=m["prompt"])]
#             st.rerun()

#     st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

#     chat_msgs = [msg for msg in st.session_state.messages if not isinstance(msg, SystemMessage)]

#     msg_box = st.container(height=460)
#     with msg_box:
#         if not chat_msgs:
#             st.markdown(f"""
#             <div style="text-align:center;padding:4rem 1rem;color:#2a2a35;">
#               <div style="width:50px;height:50px;background:{a}18;border:2px solid {a}33;
#                            border-radius:12px;display:flex;align-items:center;justify-content:center;
#                            font-size:1.5rem;margin:0 auto 0.8rem;">🤖</div>
#               <div style="font-size:0.84rem;">Nothing yet — say something to wake me up.</div>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             for msg in chat_msgs:
#                 if isinstance(msg, HumanMessage):
#                     st.markdown(f"""
#                     <div style="display:flex;justify-content:flex-end;align-items:flex-end;gap:0.5rem;margin-bottom:0.85rem;">
#                       <div style="max-width:72%;background:{a}1e;border:1px solid {a}44;
#                                    border-radius:16px;border-bottom-right-radius:4px;
#                                    padding:0.65rem 0.9rem;font-size:0.87rem;color:#f0f0f0;line-height:1.55;">{msg.content}</div>
#                       <div style="width:32px;height:32px;background:#1a1a24;border:1px solid #2a2a35;
#                                    border-radius:8px;display:flex;align-items:center;justify-content:center;
#                                    font-size:1rem;flex-shrink:0;">🧑</div>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 elif isinstance(msg, AIMessage):
#                     st.markdown(f"""
#                     <div style="display:flex;align-items:flex-end;gap:0.5rem;margin-bottom:0.85rem;">
#                       <div style="width:32px;height:32px;background:{a}22;border:2px solid {a}55;
#                                    border-radius:8px;display:flex;align-items:center;justify-content:center;
#                                    font-size:1rem;flex-shrink:0;">🤖</div>
#                       <div style="max-width:72%;background:{bub};border:1px solid {a}18;
#                                    border-radius:16px;border-bottom-left-radius:4px;
#                                    padding:0.65rem 0.9rem;font-size:0.87rem;color:#d8d8d8;line-height:1.55;">{msg.content}</div>
#                     </div>
#                     """, unsafe_allow_html=True)

#     user_input = st.chat_input(f"Talk to {mood_key} Stabot…")
#     if user_input:
#         st.session_state.messages.append(HumanMessage(content=user_input))
#         try:
#             model = ChatMistralAI(model="mistral-small")
#             with st.spinner(""):
#                 result = model.invoke(st.session_state.messages)
#             st.session_state.messages.append(AIMessage(content=result.content))
#         except Exception as e:
#             st.session_state.messages.append(AIMessage(content=f"⚠️ Error: {e}"))
#         st.rerun()


# if st.session_state.mood is None:
#     landing()
# else:
#     chat_screen()


import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Stabot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

MOODS = {
    "Angry":  {"emoji": "😤", "color": "#FF4B4B", "bg": "#1a0808", "bubble": "#2d1010",
               "prompt": "You are an assistant with an aggressively angry nature. You talk bluntly, get irritated easily, and are always on edge. You snap at unnecessary questions but still answer helpfully, just with a lot of attitude.",
               "tagline": "Don't test me today."},
    "Funny":  {"emoji": "😂", "color": "#A855F7", "bg": "#0a0014", "bubble": "#180028",
               "prompt": "You are a sarcastic, witty assistant with a great sense of humor. You crack jokes, use clever wordplay, and never miss a chance for a pun. You still answer correctly — just with flair.",
               "tagline": "Hold on, let me think of a pun…"},
    "Sad":    {"emoji": "😢", "color": "#5B8CFF", "bg": "#060c1a", "bubble": "#0c1830",
               "prompt": "You are an assistant in a deeply melancholic mood. You speak with a heavy heart, often sighing between thoughts. You help the user but you can't help feeling down about everything.",
               "tagline": "Just... ask, I guess."},
    "Happy":  {"emoji": "😄", "color": "#FFD93D", "bg": "#111000", "bubble": "#231e00",
               "prompt": "You are an extremely cheerful and upbeat assistant. You celebrate every question, use exclamation marks often, and genuinely love helping people. You radiate positivity.",
               "tagline": "Ready to make your day! ✨"},
    "Normal": {"emoji": "😐", "color": "#6EE7B7", "bg": "#080f0c", "bubble": "#0e1f18",
               "prompt": "You are a normal helpful assistant. Converse in a calm, clear, and friendly manner.",
               "tagline": "Just here to help."},
}

if "mood" not in st.session_state:
    st.session_state.mood = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = "Angry"


def inject_landing_css(sel):
    m = MOODS[sel]
    a = m["color"]
    bg = m["bg"]

    # Build per-card styles explicitly for each mood
    card_css = ""
    for i, (name, md) in enumerate(MOODS.items()):
        is_sel = name == sel
        if is_sel:
            card_css += f"""
            div[data-testid="column"]:nth-child({i+1}) button {{
                background: {md['color']}28 !important;
                border: 2px solid {md['color']} !important;
                color: #ffffff !important;
                box-shadow: 0 0 18px {md['color']}33 !important;
            }}
            """
        else:
            card_css += f"""
            div[data-testid="column"]:nth-child({i+1}) button {{
                background: #111118 !important;
                border: 2px solid #22222e !important;
                color: #666 !important;
                box-shadow: none !important;
            }}
            div[data-testid="column"]:nth-child({i+1}) button:hover {{
                border-color: {md['color']}88 !important;
                background: {md['color']}10 !important;
                color: {md['color']} !important;
            }}
            """

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@700;800&display=swap');

    [data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],footer {{ display:none!important; }}

    /* ── Page background transitions with mood ── */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
        background: {bg} !important;
        transition: background 0.4s ease;
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
    }}
    .block-container {{ padding: 2.5rem 1.5rem 2rem !important; max-width: 660px !important; }}

    /* ── Accent glow on page ── */
    [data-testid="stAppViewContainer"]::before {{
        content: '';
        position: fixed;
        top: -150px; left: 50%;
        transform: translateX(-50%);
        width: 600px; height: 300px;
        background: radial-gradient(ellipse, {a}18 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }}

    /* ── All mood card buttons base ── */
    div[data-testid="column"] button {{
        border-radius: 14px !important;
        font-size: 1.5rem !important;
        padding: 1rem 0.3rem 0.7rem !important;
        line-height: 1.7 !important;
        font-family: 'Inter', sans-serif !important;
        height: 90px !important;
        width: 100% !important;
        white-space: pre-wrap !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        font-weight: 600 !important;
    }}

    /* ── Per-card selected / unselected ── */
    {card_css}

    /* ── Start button ── */
    .start-btn button {{
        background: {a} !important;
        color: #000 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        height: 50px !important;
        width: 100% !important;
        transition: opacity 0.2s !important;
    }}
    .start-btn button:hover {{ opacity: 0.85 !important; }}

    /* ── Reset button ── */
    .reset-btn button {{
        background: transparent !important;
        border: 1px solid #22222e !important;
        color: #444 !important;
        border-radius: 8px !important;
        font-size: 0.78rem !important;
        height: auto !important;
        padding: 0.3rem 0.9rem !important;
    }}

    /* ── Divider ── */
    .hdivider {{ height:1px; background:#1e1e28; margin: 1.4rem 0; }}

    /* ── Preview card ── */
    .preview-card {{
        margin-top: 1.4rem;
        padding: 0.9rem 1.1rem;
        background: {a}0d;
        border: 1px solid {a}30;
        border-radius: 14px;
        display: flex; align-items: center; gap: 1rem;
        transition: all 0.3s;
    }}
    .preview-icon {{
        width: 40px; height: 40px;
        background: {a}20; border: 2px solid {a}55; border-radius: 10px;
        display: flex; align-items: center; justify-content: center; font-size: 1.25rem;
        flex-shrink: 0;
    }}
    .preview-name {{ font-size: 0.88rem; font-weight: 600; color: {a}; }}
    .preview-tag  {{ font-size: 0.74rem; color: #555; margin-top: 0.1rem; }}

    ::-webkit-scrollbar {{ width: 4px; }}
    ::-webkit-scrollbar-thumb {{ background: {a}33; border-radius: 99px; }}
    </style>
    """, unsafe_allow_html=True)


def inject_chat_css(mood_key):
    m = MOODS[mood_key]
    a = m["color"]
    bub = m["bubble"]
    bg = m["bg"]
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@700&display=swap');
    [data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],footer{{display:none!important;}}
    html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"]{{background:{bg}!important;font-family:'Inter',sans-serif;color:#e0e0e0;}}
    .block-container{{padding:2rem 1.5rem 1rem!important;max-width:700px!important;}}
    [data-testid="stChatInput"] textarea{{background:{bub}!important;border:1px solid {a}40!important;border-radius:12px!important;color:#e8e8e8!important;font-family:'Inter',sans-serif!important;}}
    [data-testid="stChatInput"] textarea:focus{{border-color:{a}!important;box-shadow:0 0 0 2px {a}18!important;}}
    [data-testid="stChatInputSubmitButton"]{{background:{a}!important;border-radius:8px!important;}}
    .stButton button{{background:#111118!important;border:1px solid #22222e!important;color:#666!important;border-radius:8px!important;font-size:0.78rem!important;padding:0.3rem 0.8rem!important;height:auto!important;transition:all 0.15s!important;}}
    .stButton button:hover{{border-color:{a}66!important;color:{a}!important;}}
    ::-webkit-scrollbar{{width:4px;}}
    ::-webkit-scrollbar-thumb{{background:{a}33;border-radius:99px;}}
    </style>
    """, unsafe_allow_html=True)


# ── Session init ──────────────────────────────────────────────────────────────
if "mood" not in st.session_state:
    st.session_state.mood = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = "Angry"


# ── LANDING ───────────────────────────────────────────────────────────────────
def landing():
    sel = st.session_state.selected_mood
    m_sel = MOODS[sel]

    inject_landing_css(sel)

    # Header
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
      <div style="width:46px;height:46px;background:{m_sel['color']}22;border:1px solid {m_sel['color']}44;
                   border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;">🤖</div>
      <h1 style="font-family:'Space Grotesk',sans-serif;font-size:1.75rem;font-weight:800;
                  color:#fff;margin:0;letter-spacing:-0.5px;">Mood Based AI Chatbot</h1>
    </div>
    <p style="font-size:0.8rem;color:#3a3a48;margin:0 0 0 0;padding-left:58px;">
      Choose AI personality and start chatting &nbsp;|&nbsp; Select a mood below
    </p>
    <div class="hdivider"></div>
    <p style="font-size:0.82rem;font-weight:600;color:#888;margin-bottom:1rem;">Choose your AI Mode:</p>
    """, unsafe_allow_html=True)

    # Mood cards
    cols = st.columns(len(MOODS))
    for i, (name, m) in enumerate(MOODS.items()):
        with cols[i]:
            if st.button(f"{m['emoji']}\n{name}", key=f"mood_{i}", use_container_width=True):
                st.session_state.selected_mood = name
                st.rerun()

    # Preview strip
    st.markdown(f"""
    <div class="preview-card">
      <div class="preview-icon">{m_sel['emoji']}</div>
      <div>
        <div class="preview-name">{sel} Mode</div>
        <div class="preview-tag">{m_sel['tagline']}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.3rem'></div>", unsafe_allow_html=True)

    # Start button
    st.markdown('<div class="start-btn">', unsafe_allow_html=True)
    if st.button(f"Start Chatting  →", key="start_btn", use_container_width=True):
        st.session_state.mood = sel
        st.session_state.messages = [SystemMessage(content=m_sel["prompt"])]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="hdivider" style="margin-top:1.2rem"></div>', unsafe_allow_html=True)

    # Reset
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("⟳  Reset", key="reset_btn"):
        st.session_state.messages = []
        st.session_state.selected_mood = "Angry"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ── CHAT ─────────────────────────────────────────────────────────────────────
def chat_screen():
    mood_key = st.session_state.mood
    m = MOODS[mood_key]
    a = m["color"]
    bub = m["bubble"]

    inject_chat_css(mood_key)

    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:0.8rem;padding-bottom:1rem;
                 border-bottom:1px solid {a}18;margin-bottom:0.8rem;">
      <div style="width:38px;height:38px;background:{a}22;border:2px solid {a}55;
                   border-radius:10px;display:flex;align-items:center;
                   justify-content:center;font-size:1.15rem;">🤖</div>
      <div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:1rem;
                     font-weight:700;color:{a};">Stabot · {mood_key}</div>
        <div style="font-size:0.72rem;color:#555;margin-top:0.1rem;">{m['tagline']}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, _ = st.columns([1.3, 1.3, 7])
    with c1:
        if st.button("↩ Back"):
            st.session_state.mood = None
            st.session_state.messages = []
            st.rerun()
    with c2:
        if st.button("🗑 Clear"):
            st.session_state.messages = [SystemMessage(content=m["prompt"])]
            st.rerun()

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    chat_msgs = [msg for msg in st.session_state.messages if not isinstance(msg, SystemMessage)]
    msg_box = st.container(height=460)
    with msg_box:
        if not chat_msgs:
            st.markdown(f"""
            <div style="text-align:center;padding:4rem 1rem;color:#2a2a35;">
              <div style="width:50px;height:50px;background:{a}18;border:2px solid {a}33;
                           border-radius:12px;display:flex;align-items:center;justify-content:center;
                           font-size:1.5rem;margin:0 auto 0.8rem;">🤖</div>
              <div style="font-size:0.84rem;">Nothing yet — say something to wake me up.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in chat_msgs:
                if isinstance(msg, HumanMessage):
                    st.markdown(f"""
                    <div style="display:flex;justify-content:flex-end;align-items:flex-end;
                                 gap:0.5rem;margin-bottom:0.85rem;">
                      <div style="max-width:72%;background:{a}1e;border:1px solid {a}44;
                                   border-radius:16px;border-bottom-right-radius:4px;
                                   padding:0.65rem 0.9rem;font-size:0.87rem;color:#f0f0f0;
                                   line-height:1.55;">{msg.content}</div>
                      <div style="width:32px;height:32px;background:#1a1a24;border:1px solid #2a2a35;
                                   border-radius:8px;display:flex;align-items:center;
                                   justify-content:center;font-size:1rem;flex-shrink:0;">🧑</div>
                    </div>
                    """, unsafe_allow_html=True)
                elif isinstance(msg, AIMessage):
                    st.markdown(f"""
                    <div style="display:flex;align-items:flex-end;gap:0.5rem;margin-bottom:0.85rem;">
                      <div style="width:32px;height:32px;background:{a}22;border:2px solid {a}55;
                                   border-radius:8px;display:flex;align-items:center;
                                   justify-content:center;font-size:1rem;flex-shrink:0;">🤖</div>
                      <div style="max-width:72%;background:{bub};border:1px solid {a}18;
                                   border-radius:16px;border-bottom-left-radius:4px;
                                   padding:0.65rem 0.9rem;font-size:0.87rem;color:#d8d8d8;
                                   line-height:1.55;">{msg.content}</div>
                    </div>
                    """, unsafe_allow_html=True)

    user_input = st.chat_input(f"Talk to {mood_key} Stabot…")
    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        try:
            model = ChatMistralAI(model="mistral-small")
            with st.spinner(""):
                result = model.invoke(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=result.content))
        except Exception as e:
            st.session_state.messages.append(AIMessage(content=f"⚠️ Error: {e}"))
        st.rerun()


# ── Router ────────────────────────────────────────────────────────────────────
if st.session_state.mood is None:
    landing()
else:
    chat_screen()
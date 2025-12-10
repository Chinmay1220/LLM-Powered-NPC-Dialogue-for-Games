import streamlit as st

from backend.models import DialogueTurn, DialogueRequest
from backend.dialogue_engine import generate_npc_reply


st.set_page_config(
    page_title="LLM NPC Dialogue – Mira the Tavern Keeper",
    page_icon="🍺",
    layout="centered",
)

st.title("🍺 Mira – LLM-Powered Tavern Keeper (NPC Demo)")
st.write(
    "Talk to Mira, the tavern keeper of Emberfall. "
    "This demo shows how an LLM can power in-game NPC dialogue "
    "with personality, lore, and short-term memory."
)

# -------- Session State --------
if "history" not in st.session_state:
    st.session_state.history = []  # list of {"speaker": ..., "text": ...}

if "npc_id" not in st.session_state:
    st.session_state.npc_id = "tavern_keeper_01"

if "player_name" not in st.session_state:
    st.session_state.player_name = "Ash"

# -------- Sidebar --------
st.sidebar.header("Settings")

st.sidebar.text_input(
    "Player name",
    value=st.session_state.player_name,
    key="player_name",
)

st.sidebar.markdown("**NPC:** Mira (Tavern Keeper)")
st.sidebar.markdown(f"**NPC ID:** `{st.session_state.npc_id}`")

st.sidebar.subheader("World State")
time_of_day = st.sidebar.selectbox(
    "Time of day",
    options=["morning", "afternoon", "evening", "late night"],
    index=2,
)
quest_status = st.sidebar.selectbox(
    "Quest status",
    options=["not_started", "started", "completed"],
    index=0,
)

# -------- Chat History Display --------
st.markdown("### Dialogue")

for turn in st.session_state.history:
    role = turn["speaker"]
    text = turn["text"]

    if role == "player":
        with st.chat_message("user"):
            st.markdown(text)
    else:
        with st.chat_message("assistant"):
            st.markdown(text)

# -------- Input --------
prompt = st.chat_input("Say something to Mira...")

if prompt:
    # 1) Show player's message
    st.session_state.history.append({"speaker": "player", "text": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2) Build DialogueRequest
    turns = [
        DialogueTurn(speaker=msg["speaker"], text=msg["text"])
        for msg in st.session_state.history
    ]

    req = DialogueRequest(
        player_message=prompt,
        player_name=st.session_state.player_name,
        npc_id=st.session_state.npc_id,
        world_state={
            "time_of_day": time_of_day,
            "quest_status": quest_status,
        },
        recent_history=turns,
    )

    # 3) Call dialogue engine
    with st.chat_message("assistant"):
        with st.spinner("Mira is thinking..."):
            try:
                resp = generate_npc_reply(req)
                npc_text = resp.npc_response
            except Exception as e:
                npc_text = f"Error talking to NPC: {e}"

            st.markdown(npc_text)

    # 4) Save NPC reply in history
    st.session_state.history.append({"speaker": "npc", "text": npc_text})

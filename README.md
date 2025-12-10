# LLM-Powered-NPC-Dialogue-for-Games

# 🧠 LLM-Powered NPC Dialogue System  
### 🎮 Dynamic Conversations with Personality, Lore & Memory

> **A complete educational + implementation project that demonstrates how to build intelligent, in-world NPCs powered by LLMs (GPT) using Python and Streamlit.**  
> Instead of static dialogue trees, students design characters using JSON + Markdown and control GPT using constraints, lore, and memory.

---

## 📌 Project Preview

### 🖼️ *(Insert Image Here: “Crafting Smarter NPCs: The LLM Dialogue Pipeline”)*  

<img width="2752" height="1536" alt="llm bot" src="https://github.com/user-attachments/assets/40c9a175-5fd2-457a-b20c-b0fe460b2b6e" />


---

## 🚀 Quick Start Guide

Follow these steps exactly to run the project:

```
# 1️⃣ Clone or Download the Project
git clone <your-repo-url>
cd llm-npc-dialogue

# 2️⃣ Create and Activate a Virtual Environment
python -m venv .venv

# 👉 Windows
.venv\Scripts\activate

# 👉 Mac / Linux
source .venv/bin/activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Add Your API Key
# Create a file named .env (same folder) and add:
OPENAI_API_KEY=your_real_api_key_here

# 5️⃣ Run The NPC Dialogue App (Streamlit UI)
streamlit run streamlit_app.py
```

🔓 After launch, visit: **http://localhost:8501**  
Type into the chat box and interact with the NPC.

---

## 🗂️ Project Structure

```
llm-npc-dialogue/
├─ backend/
│  ├─ __init__.py
│  ├─ models.py              # Data models for dialogue requests/responses
│  ├─ dialogue_engine.py     # Core LLM prompt-builder + GPT call
├─ content/
│  ├─ npcs/                  # NPC Personality JSON files
│  │  └─ tavern_keeper_01.json
│  └─ world/
│     └─ emberfall_lore.md   # Lore / knowledge the NPC must stay inside
├─ streamlit_app.py          # Front-End UI (no backend server needed)
├─ requirements.txt
├─ .env                      # API Keys (DO NOT COMMIT)
└─ README.md
```

---

# 🎓 Teaching Material: LLM-Powered NPC Dialogue for Games

## 📘 Introduction

This lesson plan teaches students to build **dynamic, personality-driven NPCs** using LLMs. It follows a structured **Explain → Show → Try** approach to build knowledge logically and encourage creative experimentation.

---

## 1️⃣ Lesson Overview

### 👥 Target Audience
Beginner–intermediate devs who know basic Python but **have never controlled an LLM in a game context**.

### 🎯 Learning Goals
Students will be able to:
✔ Explain why LLM NPCs outperform static dialogue  
✔ Describe an LLM dialogue architecture  
✔ Build a constrained dialogue backend  
✔ Modify NPC behavior via JSON + Markdown files

### 🔧 Prerequisites
- Basic Python
- Internet connection + API key
- VS Code recommended

---

## 2️⃣ Segment 1: The Why & How (Explain)

### ❌ The Problem: Static Dialogue Trees

Static branching systems:
- Repeat dialogue after short use
- Require enormous writing effort
- Break immersion
- Scale poorly when adding new NPCs

They make NPCs feel like **vending machines**, not people.

---

### 🤖 The Solution: *Controlled* LLM NPCs

LLMs can generate unlimited dialogue, but **must be constrained**:

Without rules, they:
❌ mention being an AI  
❌ talk about the real world  
❌ ignore lore  
❌ behave inconsistently

### 🔐 Key Idea: The NPC Prompt = Script + Rules

| 🚫 Uncontrolled LLM | 🎭 Controlled In-World NPC |
|--------------------|---------------------------|
| “As an AI model…” | “What’s an A-eye? Sounds like a cursed artifact!” |
| “France has a strong economy…” | “France? Never heard of it. Is it east of Emberfall?” |

The goal is not just “chatting.”  
The goal is **role-play + immersion**.

---

### 🔁 Architecture of the Dialogue System

1. 🎮 Player Types a Message
2. 🧠 Backend Builds a Prompt:
   - Personality (JSON)
   - Lore (Markdown)
   - Rules (hard constraints)
   - Conversation Memory (last 6 messages)
3. 🔮 GPT Generates an In-Character Reply
4. 💬 UI Displays Response

---

## 3️⃣ Segment 2: Guided Walkthrough (Show)

### 🧠 Components of the NPC’s Brain

| Component | File Type | Purpose |
|-----------|-----------|---------|
| Personality | `.json` | Defines traits, speech style, job, flaws |
| Lore | `.md` | Knowledge boundaries, history, factions, rumors |
| Rules | Code | Prevent AI breaks, force immersion |
| Memory | Session | Remembers last messages |

### 🌐 The Backend Function

`generate_npc_reply()`:
- Loads persona + lore
- Applies rules
- Adds past conversation
- Sends to GPT
- Returns controlled output

---

### 🎥 Live Demo Ideas (Teacher)

🗣 Ask: **“Tell me about Emberfall.”**  
🔍 Show how it pulls info from lore.

❓ Ask: **“Do you have Wi-Fi?”**  
🙅 NPC should reject the question *in character*.

🧠 Ask follow-up: **“What was the blacksmith’s name again?”**  
📝 NPC should *remember* previous context.

---

## 4️⃣ Segment 3: Hands-On Practice (Try)

Here are student exercises:

### 🎭 Challenge 1 — Create a New NPC
Add a `.json` persona for:
- A suspicious mayor  
- A lazy guardsman  
- A drunk bard  
- A lying merchant  

### 📊 Challenge 2 — React to World State
Add `quest_status`:
```
"not_started" → NPC acts neutral  
"in_progress" → NPC hints & helps  
"completed" → NPC praises or fears the player
```

### 🎭 Challenge 3 — Add Emotion Tags `[happy]`, `[sad]`, `[angry]`
Use it for:
- Text color
- Animations
- Voice tone

---

## 5️⃣ Conclusion & Next Steps

### 🗝️ Key Takeaways
- LLM NPCs must be **constrained** to maintain immersion.
- Persona + Lore + Rules + Memory = Believable Character.
- Better constraints → Better storytelling.

### 🌌 Creative Prompt
> **Write an NPC who hides a secret. Reveal it only through the player’s persistence.**

---

## 🎨 Additional Content Placeholders

### 🧠 Mind Map
<img width="6763" height="9737" alt="NotebookLM Mind Map (2)" src="https://github.com/user-attachments/assets/22818d57-773f-4b15-b33f-8e6ae2dfeae0" />


### 📽️ Slides (Coming Soon)
📍 *Link or attach PDF here*

### 🎥 Video Lecture (Coming Soon)
📍 *Link or thumbnail here*

---

✨ **Happy World-Building!**

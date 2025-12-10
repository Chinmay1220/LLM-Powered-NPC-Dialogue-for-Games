import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from .models import DialogueRequest, DialogueResponse

# Load env vars (OPENAI_API_KEY)
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_DIR = Path(__file__).resolve().parent.parent


def load_npc(npc_id: str) -> dict:
    """
    Load NPC data from JSON file.
    """
    npc_file = BASE_DIR / "content" / "npcs" / f"{npc_id}.json"
    if not npc_file.exists():
        raise FileNotFoundError(f"NPC file not found for id={npc_id}")
    with npc_file.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_lore() -> str:
    """
    Load world lore from markdown file.
    """
    lore_file = BASE_DIR / "content" / "world" / "emberfall_lore.md"
    if not lore_file.exists():
        return ""
    return lore_file.read_text(encoding="utf-8")


def build_prompt(req: DialogueRequest) -> str:
    """
    Build a structured prompt combining:
    - NPC persona & backstory
    - World lore
    - Game rules (stay in character, no AI talk)
    - World state
    - Recent conversation
    - Player message
    """
    npc = load_npc(req.npc_id)
    lore = load_lore()

    # Last 6 turns of history
    history_lines = []
    for turn in req.recent_history[-6:]:
        prefix = "PLAYER" if turn.speaker.lower() == "player" else npc["name"].upper()
        history_lines.append(f"{prefix}: {turn.text}")
    history_block = "\n".join(history_lines) if history_lines else "No prior conversation."

    # World state as bullet list
    world_state_lines = [f"- {k}: {v}" for k, v in req.world_state.items()]
    world_state_block = "\n".join(world_state_lines) or "No special world state."

    prompt = f"""
You are {npc['name']}, a {npc['role']} in the fantasy town of Emberfall.

GAME LORE:
{lore}

NPC BACKSTORY:
{npc['backstory']}

PERSONALITY:
{npc['personality']}

SPEECH STYLE:
{npc['speech_style']}

GAME RULES:
- Stay strictly in character as {npc['name']}.
- Never mention being an AI, language model, chatbot, or anything about 'OpenAI' or 'the real world'.
- Only talk about the game world, Emberfall, its people, and in-world events.
- If the player asks about things that clearly do not exist in Emberfall (like phones, the internet, or real-world countries), respond as if you do not know them and gently redirect to in-world topics.
- Keep responses under 3 sentences by default.
- If the player explicitly asks for a detailed explanation, you may use up to 5 sentences.

CURRENT WORLD STATE:
{world_state_block}

RECENT CONVERSATION:
{history_block}

PLAYER NAME: {req.player_name}

Now continue the conversation.

PLAYER: {req.player_message}
{npc['name'].upper()}:
""".strip()

    return prompt


def call_llm(prompt: str) -> str:
    """
    Call the OpenAI Responses API and return plain text.
    """
    completion = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=150,
        temperature=0.7,
    )
    text = completion.output[0].content[0].text
    return text.strip()


def generate_npc_reply(req: DialogueRequest) -> DialogueResponse:
    """
    Orchestrate:
    - Build prompt
    - Call LLM
    - Wrap in DialogueResponse
    """
    prompt = build_prompt(req)
    raw = call_llm(prompt)

    emotion: Optional[str] = None  # could be extended later

    return DialogueResponse(
        npc_response=raw,
        emotion=emotion,
        meta={
            "model": "gpt-4.1-mini",
            "npc_id": req.npc_id,
        },
    )

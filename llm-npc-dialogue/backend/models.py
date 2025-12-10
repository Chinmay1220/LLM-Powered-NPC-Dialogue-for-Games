from typing import List, Dict, Optional
from pydantic import BaseModel


class DialogueTurn(BaseModel):
    """
    One message in the conversation history.
    speaker: 'player' or 'npc'
    text: what was said
    """
    speaker: str
    text: str


class DialogueRequest(BaseModel):
    """
    Input to the dialogue engine.
    """
    player_message: str
    player_name: str
    npc_id: str
    world_state: Dict[str, str] = {}
    recent_history: List[DialogueTurn] = []


class DialogueResponse(BaseModel):
    """
    Output from the dialogue engine.
    """
    npc_response: str
    emotion: Optional[str] = None
    meta: Dict[str, str] = {}

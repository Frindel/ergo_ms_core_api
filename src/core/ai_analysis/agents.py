from .config import OLLAMA_MODEL, IS_DEBUG
from agno.team import Team


def create_members():
    pass


def create_orchestrator():
    members = create_members()
    return Team(
        model=OLLAMA_MODEL,
        members=members,
        description="",
        instructions="",
        show_members_responses=IS_DEBUG,
    )

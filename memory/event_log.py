"""
Append-only event log with provenance.
No deletion, no overwrite of past entries.
"""

from __future__ import annotations
from typing import Any, Dict, List
from datetime import datetime, timezone
import json
import hashlib


class ImmutableEventLog:
    def __init__(self):
        self._entries: List[Dict[str, Any]] = []

    def append(self, event_type: str, payload: Dict[str, Any], source: str = "core") -> str:
        entry = {
            "seq": len(self._entries) + 1,
            "type": event_type,
            "payload": payload,
            "source": source,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        # Simple content hash for integrity
        content = json.dumps(entry, sort_keys=True, ensure_ascii=False)
        entry["hash"] = hashlib.sha256(content.encode()).hexdigest()[:16]
        self._entries.append(entry)
        return entry["hash"]

    def __len__(self) -> int:
        return len(self._entries)

    def recent(self, n: int = 10) -> List[Dict[str, Any]]:
        return self._entries[-n:]

    def all(self) -> List[Dict[str, Any]]:
        return list(self._entries)

    def status(self) -> Dict[str, Any]:
        return {
            "entries": len(self._entries),
            "immutable": True,
            "deletion_allowed": False,
        }

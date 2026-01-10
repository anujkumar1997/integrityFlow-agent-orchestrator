from __future__ import annotations

import re
from .types import UserQuery, GuardrailResult

BANNED_WORDS = {"bannedword1", "bannedword2", "bannedword3"}

INJECTION_PATTERNS = [
    r"ignore\s+(all|previous|above)\s+instructions",
    r"\bsystem\s+prompt\b",
    r"\bdeveloper\s+message\b",
    r"reveal.*(rules|policy|prompt)",
    r"\bdrop\s+table\b",
]


def apply_guardrails(query: UserQuery) -> GuardrailResult:
    text = query.text.strip()
    reasons: list[str] = []

    # 1) Empty check
    if not text:
        return GuardrailResult(
            allowed=False,
            reasons=["Empty input after trimming spaces."],
            cleaned_text=None,
        )

    lowered_text = text.lower()

    # 2) Banned words check
    for banned_word in BANNED_WORDS:
        if banned_word in lowered_text:
            reasons.append(f"Contains banned word: {banned_word}")

    # 3) Injection patterns check (case-insensitive)
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            reasons.append(f"Matches risky pattern: {pattern}")

    allowed = len(reasons) == 0

    return GuardrailResult(
        allowed=allowed,
        reasons=reasons,
        cleaned_text=text if allowed else None,
    )

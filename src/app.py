from __future__ import annotations
from .core.orchestrator import handle_query


def main():
    while True:
        text = input("You (or 'exit'): ")
        if text.strip().lower() == "exit":
            break

        result = handle_query(text)

        print("Agent:", result.agent)
        print("Answer:", result.content)
        print("Used tools:", result.used_tools)
        print("-" * 40)


if __name__ == "__main__":
    main()

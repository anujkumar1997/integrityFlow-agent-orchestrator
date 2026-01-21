from __future__ import annotations

from .core.orchestrator import handle_query
from .core.tracer import Tracer


def main():
    print("IntegrityFlow CLI. Type 'exit' to quit.\n")

    while True:
        text = input("You: ")
        if text.strip().lower() == "exit":
            print("Goodbye!")
            break

        tracer = Tracer()
        result = handle_query(text, tracer=tracer)

        print("Agent:", result.agent)
        print("Answer:", result.content)
        print("Used tools:", result.used_tools)
        print("-" * 40)

        print("Trace:")
        for event in tracer.events:
            print(f"[{event.stage.upper()}] {event.status} - Agent: {event.agent} - Data: {event.data}")
        print("=" * 40)



if __name__ == "__main__":
    main()


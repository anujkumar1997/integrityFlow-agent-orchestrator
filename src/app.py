from .core.llm_client import chat
from .core.guardrails import apply_guardrails
from .core.types import UserQuery



def main():
    while True:
        user_input = input("Enter your query (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        query = UserQuery(text=user_input)
        guardrail_result = apply_guardrails(query)

        print("Allowed:", guardrail_result.allowed)
        print("Cleaned text:", guardrail_result.cleaned_text)


if __name__ == "__main__":
    main()




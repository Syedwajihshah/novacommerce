import argparse

from novacommerce.config import load_settings
from novacommerce.llm import LLMProvider, OpenAIProvider


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ask NovaCommerce using supplied information."
    )
    parser.add_argument(
        "input_text",
        help="The policy, order details, and question."
    )
    args = parser.parse_args()

    settings = load_settings()
    provider: LLMProvider = OpenAIProvider(settings)

    try:
        answer = provider.generate(
            instructions=(
                "Use only the supplied policy and order details. "
                "If necessary information is missing, ask for it "
                "and set needs_more_information to true. "
                "Keep the answer brief."
            ),
            input_text=args.input_text
        )
        print(answer.model_dump_json(indent=2))
    finally:
        provider.close()


if __name__ == "__main__":
    main()
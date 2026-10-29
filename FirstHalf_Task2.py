import tiktoken
import json
encoding = tiktoken.get_encoding("cl100k_base")
encoding2 = tiktoken.get_encoding("o200k_base")
sentence = "Python is easy to learn and useful for AI."

paragraph = """
Python is a popular programming language.
It is used in data science, automation, and artificial intelligence.
Beginners can use Python to build chatbots and process text.
"""
page = """
Artificial intelligence is changing many industries.
Language models can understand and generate human-like text.
They are used for customer support, document summarization,
translation, coding assistance, and question answering.
Tokenization converts text into smaller units called tokens.
The number of tokens depends on the tokenizer and the text.
Language models can also process structured data and code.
Python makes it easier to build applications using AI models.
"""
json_text = json.dumps({
    "name": "Ravi",
    "course": "LLM Fundamentals",
    "completed": True,
    "skills": ["Python", "AI", "NLP"]
})

tamil_text = "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
texts = {
    "Sentence": sentence,
    "Paragraph": paragraph,
    "Page": page,
    "JSON": json_text,
    "Tamil": tamil_text
}
print("\nTOKEN COUNT REPORT")
token_counts = {}

for name, text in texts.items():
    tokens = encoding.encode(text)
    token_count = len(tokens)
    word_count = len(text.split())
    if token_count > 0:
        words_per_token = word_count / token_count
    else:
        words_per_token = 0
    token_counts[name] = token_count
    print("\nText:", name)
    print("Words:", word_count)
    print("Tokens:", token_count)
    print("Words per token:", round(words_per_token, 2))
    if words_per_token < 0.75:
        print("Comparison: Below 0.75 words per token")
    else:
        print("Comparison: At or above 0.75 words per token")

print("\nCONTEXT WINDOW CHECK")
for name, count in token_counts.items():
    print("\nText:", name)
    print("Token count:", count)
    print("Fits in 8k window:", count <= 8000)
    print("Fits in 128k window:", count <= 128000)

def estimate_cost(input_tokens, output_tokens, price_in, price_out):
    input_cost = (input_tokens / 1_000_000) * price_in
    output_cost = (output_tokens / 1_000_000) * price_out
    total_cost = input_cost + output_cost
    return total_cost

price_in = 0.10
price_out = 0.50
input_tokens_per_chat = 1500
output_tokens_per_chat = 400
one_chat_cost = estimate_cost(
    input_tokens_per_chat,
    output_tokens_per_chat,
    price_in,
    price_out
)
print("\nCOST OF ONE CHAT")
print("Input tokens:", input_tokens_per_chat)
print("Output tokens:", output_tokens_per_chat)
print("Cost of one chat: $", round(one_chat_cost, 6))
chats_per_day = 1000
days_per_month = 30
monthly_input_tokens = (
    chats_per_day * days_per_month * input_tokens_per_chat
)
monthly_output_tokens = (
    chats_per_day * days_per_month * output_tokens_per_chat
)
monthly_cost = estimate_cost(
    monthly_input_tokens,
    monthly_output_tokens,
    price_in,
    price_out
)
print("\nMONTHLY CHATBOT COST")
print("Chats per day:", chats_per_day)
print("Days per month:", days_per_month)
print("Monthly input tokens:", monthly_input_tokens)
print("Monthly output tokens:", monthly_output_tokens)
print("Monthly cost: $", round(monthly_cost, 2))
print("\nBONUS: TOKENIZER COMPARISON")
bonus_sentence = "Artificial intelligence is useful for everyone."
tokens_1 = encoding.encode(bonus_sentence)
tokens_2 = encoding2.encode(bonus_sentence)
print("Sentence:", bonus_sentence)
print("\nTokenizer 1: cl100k_base")
print("Token count:", len(tokens_1))
print("Token IDs:", tokens_1)
print("\nTokenizer 2: o200k_base")
print("Token count:", len(tokens_2))
print("Token IDs:", tokens_2)
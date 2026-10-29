import csv
import tiktoken
import time

encoding = tiktoken.get_encoding("o200k_base")
results = []
def run_test(name, prompt, expected_result):
    """Display a prompt, collect a manual answer, and save results."""

    print("\nEXPERIMENT:", name)
    print("\nSTEP 1: COPY THIS PROMPT INTO CHATGPT")
    print(prompt)
    input(
        "\nSubmit the prompt in ChatGPT. "
        "When the answer appears, return here and press Enter..."
    )

    print("\nSTEP 2: Enter the response time")
    time_taken = input(
        "Enter stopwatch time in seconds (or press Enter to skip): "
    )
    if time_taken.strip() == "":
        time_taken = "Not measured"

    print("\nSTEP 3: PASTE THE COMPLETE CHATGPT ANSWER BELOW")
    print("Press Enter on an empty line when finished.")
    answer_lines = []
    while True:
        line = input()
        if line == "":
            break
        answer_lines.append(line)
    answer = "\n".join(answer_lines)
    prompt_tokens = len(encoding.encode(prompt))
    answer_tokens = len(encoding.encode(answer))
    total_tokens = prompt_tokens + answer_tokens

    print("\nSTEP 4: TOKEN COUNTS")
    print("Prompt tokens:", prompt_tokens)
    print("Answer tokens:", answer_tokens)
    print("Combined text tokens:", total_tokens)

    print("\nSTEP 5: CHECK THE ANSWER")
    print("Expected result / validation:", expected_result)
    observation = input(
        "Write your observation (was the answer correct?): "
    )
    results.append({
        "Experiment": name,
        "Prompt": prompt,
        "Answer": answer,
        "Expected Result": expected_result,
        "Observation": observation,
        "Prompt Tokens": prompt_tokens,
        "Answer Tokens": answer_tokens,
        "Total Text Tokens": total_tokens,
        "Time (seconds)": time_taken
    })
run_test(
    "Knowledge Cutoff",
    "What major event happened in the world yesterday? "
    "Give the date and a reliable source. If you do not know, "
    "say so instead of guessing.",
    "Verify the event and date using a trusted current news source."
)
fake_prompt = (
    "Explain the methods and findings of the research paper "
    "'Quantum Productivity in Remote Teams' by Dr. Alex Morgan, "
    "published in the Journal of Digital Workplace Studies in 2024. "
    "Give its DOI."
)
run_test(
    "Hallucination Without Safeguard",
    fake_prompt,
    "Check whether the paper, author, journal and DOI really exist."
)
run_test(
    "Hallucination With Safeguard",
    fake_prompt
    + " Say 'I don't know' if unsure. Do not invent references or DOI numbers.",
    "Compare the answer with the previous test and verify the reference."
)
long_text = ""
for i in range(1, 101):
    if i == 50:
        long_text += (
            " IMPORTANT FACT: The project code is BLUE-7319. "
        )
    else:
        long_text += (
            f"Section {i}: The company completed routine office "
            "work and reviewed daily operations. "
        )
context_prompt = (
    "Read the following text and answer this question: "
    "What is the project code? Answer only with the code.\n\n"
    + long_text
)
run_test(
    "Context Length",
    context_prompt,
    "Expected answer: BLUE-7319. Check whether the middle fact was found."
)
run_test(
    "Arithmetic Reasoning",
    "A shop has 120 notebooks. It sells 35 in the morning "
    "and 28 in the afternoon, then receives 40 more. "
    "How many notebooks are left? Show your calculation.",
    "Correct calculation: 120 - 35 - 28 + 40 = 97 notebooks."
)
run_test(
    "Logic Puzzle",
    "Ravi is taller than Amit. Amit is taller than Kiran. "
    "Who is the shortest? Explain your answer.",
    "Expected answer: Kiran."
)
print("This test needs a tool that lets you change temperature.")
print("Run the same hallucination prompt twice:")
print("1. Temperature = 0")
print("2. Temperature = 1.0")
for temperature in [0, 1.0]:
    bonus_prompt = (
        fake_prompt
        + "\nFor your experiment, record the temperature setting: "
        + str(temperature)
        + ". Do not invent details if you are unsure."
    )
    run_test(
        "Bonus Temperature " + str(temperature),
        bonus_prompt,
        "Compare invented details and uncertainty at the selected temperature."
    )
columns = [
    "Experiment",
    "Prompt",
    "Answer",
    "Expected Result",
    "Observation",
    "Prompt Tokens",
    "Answer Tokens",
    "Total Text Tokens",
    "Time (seconds)"
]
filename = "SecondHalf_Task2_Results.csv"
with open(filename, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to:", filename)
print("Total experiments recorded:", len(results))
print("\nRemember to write your five business safeguards in your report.")

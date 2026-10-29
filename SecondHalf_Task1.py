
import csv
import time
import tiktoken

# Token counter
encoding = tiktoken.get_encoding("o200k_base")



# Sample text
sample_text = """
ABC Company started a work-from-home policy in January.
Employees can work remotely three days a week.
The policy aims to improve work-life balance and reduce travel costs.
Managers review employee performance every month.
"""

# Five capability tasks
tasks = [
    {
        "task": "Summarisation",
        "prompt": "Summarise this text in two sentences:\n" + sample_text,
        "improvement": "Include all important points in fewer words."
    },
    {
        "task": "Classification",
        "prompt": (
            "Classify this feedback as Positive, Negative, or Neutral "
            "and give one reason: The new policy saves travel time, "
            "but internet problems reduce productivity."
        ),
        "improvement": "Check whether the classification matches the feedback."
    },
    {
        "task": "Extraction",
        "prompt": (
            "Extract the company name, start month, remote work days "
            "per week, and review frequency from this text:\n"
            + sample_text
        ),
        "improvement": "Verify the extracted details against the original text."
    },
    {
        "task": "Translation",
        "prompt": (
            "Translate this sentence into Tamil: "
            "Employees can work remotely three days a week."
        ),
        "improvement": "Check the translation's grammar and meaning."
    },
    {
        "task": "Code Generation",
        "prompt": (
            "Write a Python function called calculate_total that "
            "accepts a list of prices and returns their sum. "
            "Include a simple example."
        ),
        "improvement": "Run the code and test different price lists."
    }
]

results = []
for item in tasks:
    print("\nTASK:", item["task"])
    prompt = item["prompt"]
    print("\nSTEP 1: COPY THIS PROMPT INTO CHATGPT")
    print(prompt)
    input(
        "\nSubmit the prompt in ChatGPT. "
        "When the answer appears, return here and press Enter..."
    )
    print("\nSTEP 2: COPY THE COMPLETE CHATGPT ANSWER")
    print(
        "Start a stopwatch when you submit the prompt "
        "and stop it when the answer appears."
    )
    print("\nSTEP 3: PASTE THE ANSWER BELOW")
    print("Paste the complete answer.")
    print("When finished, press Enter on an empty line.")
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

    print("\nSTEP 4: TOKEN COUNT AND RESPONSE TIME")
    print("Estimated prompt tokens:", prompt_tokens)
    print("Estimated answer tokens:", answer_tokens)
    print("Estimated total text tokens:", total_tokens)
    print(
        "\nThese are local estimates for the prompt and answer text, "
        "not official ChatGPT usage totals."
    )
    time_taken = input(
        "Enter stopwatch time in seconds (or press Enter to skip): "
    )
    if time_taken.strip() == "":
        time_taken = "Not measured"
    print("\nSTEP 5: RATE THE ANSWER")
    print("1 = Very poor, 2 = Poor, 3 = Average,")
    print("4 = Good, 5 = Excellent")
    while True:
        try:
            rating = int(input("Enter correctness rating (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    results.append({
        "Task": item["task"],
        "Prompt": prompt,
        "Answer": answer,
        "Rating": rating,
        "Prompt Tokens": prompt_tokens,
        "Answer Tokens": answer_tokens,
        "Total Text Tokens": total_tokens,
        "Time (seconds)": time_taken,
        "Improvement": item["improvement"]
    })
columns = [
    "Task",
    "Prompt",
    "Answer",
    "Rating",
    "Prompt Tokens",
    "Answer Tokens",
    "Total Text Tokens",
    "Time (seconds)",
    "Improvement"
]

filename = "SecondHalf_Task1_Results.csv"
with open(filename, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)

print("\nCAPABILITIES LAB COMPLETED!")

best = max(results, key=lambda x: x["Rating"])
worst = min(results, key=lambda x: x["Rating"])

print("\nBEST TASK:", best["Task"], "-", best["Rating"], "/ 5")
print("WORST TASK:", worst["Task"], "-", worst["Rating"], "/ 5")

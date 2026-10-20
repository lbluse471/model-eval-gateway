 """Minimal benchmark harness: latency and token accounting for any OpenAI-compatible endpoint."""
     import argparse
     import csv
     import os
     import time

     from openai import OpenAI

     PROMPTS = [
         "Explain GPU memory bandwidth in three sentences.",
         "Write a Python function that reverses a singly linked list.",
         "Summarize the difference between latency and throughput in one paragraph.",
         "List three failure modes of tool calling in LLM agents.",
     ]

     FIELDS = ["prompt", "latency_s", "prompt_tokens", "completion_tokens"]


     def main() -> None:
         parser = argparse.ArgumentParser()
         parser.add_argument("--base-url", required=True)
         parser.add_argument("--model", required=True)
         parser.add_argument("--out", default="results.csv")
         args = parser.parse_args()

         client = OpenAI(base_url=args.base_url, api_key=os.environ["API_KEY"])

         rows = []
         for prompt in PROMPTS:
             started = time.time()
             response = client.chat.completions.create(
                 model=args.model,
                 messages=[{"role": "user", "content": prompt}],
                 stream=False,
             )
             rows.append(
                 {
                     "prompt": prompt[:40],
                     "latency_s": round(time.time() - started, 3),
                     "prompt_tokens": response.usage.prompt_tokens,
                     "completion_tokens": response.usage.completion_tokens,
                 }
             )

         with open(args.out, "w", newline="", encoding="utf-8") as handle:
             writer = csv.DictWriter(handle, fieldnames=FIELDS)
             writer.writeheader()
             writer.writerows(rows)

         print(f"{len(rows)} requests written to {args.out}")


     if __name__ == "__main__":
         main()

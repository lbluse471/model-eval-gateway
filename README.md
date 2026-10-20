  # model-eval-gateway

  An OpenAI-compatible evaluation gateway that sends identical prompts to multiple
  open-weight models and compares them on latency, cost, and tool-calling accuracy.

  ## What it does

  - Sends the same prompt set to several providers through a single OpenAI-compatible endpoint
  - Records time-to-first-token, total latency, token usage and cost per request
  - Scores tool-calling success against an expected call schema
  - Exports results as CSV and renders a comparison table

  ## Status

  Early development. The benchmark harness runs locally against hosted inference endpoints
  (Fireworks AI serverless, OpenAI-compatible base URL).

  Benchmark set in progress: 200 English instructions across three model families.

  ## Planned

  - [x] Unified chat-completions client with streaming
  - [x] Per-request latency and cost accounting
  - [ ] Tool-calling accuracy suite
  - [ ] Public benchmark report

  ## Usage

  Install dependencies and run a benchmark against any OpenAI-compatible endpoint:

  ```bash
  pip install openai
  export API_KEY=your-api-key
  python run_eval.py \
    --base-url https://api.fireworks.ai/inference/v1 \
    --model accounts/fireworks/models/your-model-name
```

Results are written to results.csv with one row per request: prompt excerpt, latency in
seconds, prompt tokens and completion tokens.

Repository layout

```
  run_eval.py    # minimal harness: sends prompts, records latency and token usage
  results.csv    # generated output (not committed)
```

Motivation

Hosted inference providers differ in ways that benchmarks rarely capture: time-to-first-token
under load, cost per completed task, and how reliably a model emits well-formed tool calls.
This project measures those three things on the same prompt set so that model choice can be
made on evidence rather than vibes.

License

MIT

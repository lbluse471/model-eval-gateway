     # model-eval-gateway

     An OpenAI-compatible evaluation gateway that sends identical prompts to multiple
     open-weight models and compares them on latency, cost, and tool-calling accuracy.

     ## What it does

     - Sends the same prompt set to several providers through a single OpenAI-compatible endpoint
     - Records time-to-first-token, total latency, token usage and cost per request
     - Scores tool-calling success against an expected-call schema
     - Exports results as CSV and renders a comparison table

     ## Status

     Early development. Benchmark harness runs locally against hosted inference endpoints
     (Fireworks AI serverless, OpenAI-compatible base URL). 200-message Chinese instruction set
     in progress.

     ## Planned

     - [x] Unified chat-completions client with streaming
     - [x] Per-request latency and cost accounting
     - [ ] Tool-calling accuracy suite
     - [ ] Public benchmark report

     ## Usage

     ```bash
     pip install openai pandas
     export API_KEY=...            # any OpenAI-compatible provider
     python run_eval.py --base-url https://api.fireworks.ai/inference/v1 --model accounts/fireworks/models/...

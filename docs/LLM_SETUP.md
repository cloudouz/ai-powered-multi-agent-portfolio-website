# LLM Configuration (Gemini primary + OpenAI fallback)

## Install deps
```bash
pip install langchain-core langchain-community langchain-openai langchain-google-genai google-generativeai tavily-python
```

## Environment variables
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_KEY
OPENAI_API_KEY=YOUR_OPENAI_KEY   # optional fallback
TAVILY_API_KEY=YOUR_TAVILY_KEY
```

## Switch providers
```env
LLM_PROVIDER=openai
```

## Streaming
`/api/stream` uses the model streaming API.

## Tool calling
ResearchAgent binds the TavilySearchResults tool and executes tool calls before producing a final cited answer.

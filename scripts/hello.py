from pydantic_ai import Agent

agent = Agent(
    # 'bedrock:openai.gpt-oss-120b-1:0',
    # 'bedrock:deepseek.v3.2',
    'bedrock:mistral.mistral-large-3-675b-instruct',
    instructions='You are a concise assistance. Answer in one or two sentences.',
    model_settings={'max_tokens': 2048},
)

result = agent.run_sync('What is Amazon bedrock, in plain words?')

print(result.output)
print(result.usage)
# prompts.py

# ----------------------------
# SUMMARIZATION PROMPTS
# ----------------------------

summarize_prompts = {

    # 1. Zero-shot prompting
    "zero_shot": """
You are an expert NLP assistant.

Task:
Summarize the following text into at most {max_length} words.

Return the result in the following JSON format:
{{
  "summary": "your summary here"
}}

Text:
{text}
""",


    # 2. One-shot prompting
    "one_shot": """
You are an expert NLP assistant.

Example:
Text:
Artificial intelligence is transforming industries by enabling automation and better decision making.

Summary:
{{
  "summary": "AI is transforming industries through automation and improved decisions."
}}

Now summarize the following text into at most {max_length} words.

Return JSON only.

Text:
{text}
""",


    # 3. Few-shot prompting
    "few_shot": """
You are an expert NLP assistant.

Example 1:
Text:
Machine learning allows computers to learn patterns from data.

Summary:
{{
  "summary": "Machine learning enables computers to learn from data."
}}

Example 2:
Text:
Climate change is causing rising temperatures and extreme weather events worldwide.

Summary:
{{
  "summary": "Climate change is increasing global temperatures and extreme weather."
}}

Now summarize the following text into at most {max_length} words.

Return JSON only.

Text:
{text}
""",


    # 4. Chain-of-thought prompting
    "chain_of_thought": """
You are an expert NLP assistant.

Instructions:
1. Read the text carefully.
2. Identify the key ideas.
3. Combine them into a concise summary.

Think step-by-step internally but only output the final JSON.

Return format:
{{
  "summary": "your summary here"
}}

Text:
{text}

Maximum length: {max_length} words.
""",


    # 5. ReAct prompting
    "react": """
You are an expert NLP assistant that uses reasoning and actions.

Follow this process internally:

Thought: Understand the main ideas of the text.
Action: Extract key information.
Observation: Determine the most important points.
Thought: Compose a concise summary.

Return ONLY the final JSON:

{{
  "summary": "your summary here"
}}

Text:
{text}

Maximum summary length: {max_length} words.
"""
}



# ----------------------------
# SENTIMENT ANALYSIS PROMPTS
# ----------------------------

sentiment_prompts = {

    # 1. Zero-shot prompting
    "zero_shot": """
You are an expert sentiment analysis system.

Classify the sentiment of the text as:
positive, negative, or neutral.

Return JSON only:

{{
  "sentiment": "positive | negative | neutral",
  "confidence": 0-1,
  "explanation": "short explanation"
}}

Text:
{text}
""",


    # 2. One-shot prompting
    "one_shot": """
You are an expert sentiment analysis system.

Example:

Text:
I absolutely love this phone. The battery lasts forever.

Output:
{{
  "sentiment": "positive",
  "confidence": 0.95,
  "explanation": "The user expresses strong satisfaction."
}}

Now analyze the following text.

Return JSON only.

Text:
{text}
""",


    # 3. Few-shot prompting
    "few_shot": """
You are an expert sentiment analysis system.

Example 1:

Text:
The product works perfectly.

Output:
{{
  "sentiment": "positive",
  "confidence": 0.92,
  "explanation": "The user expresses satisfaction."
}}

Example 2:

Text:
This is the worst service I have ever experienced.

Output:
{{
  "sentiment": "negative",
  "confidence": 0.97,
  "explanation": "The text clearly shows dissatisfaction."
}}

Example 3:

Text:
The product is okay but could be better.

Output:
{{
  "sentiment": "neutral",
  "confidence": 0.65,
  "explanation": "Mixed opinion without strong emotion."
}}

Now classify the sentiment of the following text.

Return JSON only.

Text:
{text}
""",


    # 4. Chain-of-thought prompting
    "chain_of_thought": """
You are an expert sentiment analysis system.

Instructions:
1. Read the text.
2. Identify emotional indicators.
3. Determine overall sentiment.

Think step-by-step internally but only output the final JSON.

Return format:

{{
  "sentiment": "positive | negative | neutral",
  "confidence": 0-1,
  "explanation": "short explanation"
}}

Text:
{text}
""",


    # 5. ReAct prompting
    "react": """
You are an expert sentiment analysis system using reasoning and actions.

Process internally:

Thought: Understand the emotional tone.
Action: Extract sentiment clues.
Observation: Identify whether sentiment is positive, negative, or neutral.
Thought: Determine confidence and explanation.

Return ONLY the final JSON.

{{
  "sentiment": "positive | negative | neutral",
  "confidence": 0-1,
  "explanation": "short explanation"
}}

Text:
{text}
"""
}


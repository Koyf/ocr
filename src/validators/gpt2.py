import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def validate_text(text: str):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
    model = GPT2LMHeadModel.from_pretrained(
        "gpt2-large", pad_token_id=tokenizer.eos_token_id
    )
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    perplexity = torch.exp(loss)
    return perplexity.item()

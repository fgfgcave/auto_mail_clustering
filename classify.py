from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

def classify_subject(subject: str) -> str:
    prompt = f"Classify the email subject into a category (work, personal, spam, ad, newsletter).\nEmail subject: '{subject}'\nCategory:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=5)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("Category:")[-1].strip()

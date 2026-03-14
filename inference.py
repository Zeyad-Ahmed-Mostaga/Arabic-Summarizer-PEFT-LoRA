import torch
from transformers import AutoProcessor, AutoModelForSeq2SeqLM, GenerationConfig
from peft import PeftModel
https://github.com/Zeyad-Ahmed-Mostaga/Arabic-Summarizer-PEFT-LoRA/tree/main
# Load Processor and Base Model
MODEL_ID = "google/t5gemma-2-270m-270m"
PEFT_MODEL_ID = "ZeyadAhmedMostafa/t5gemma-arabic-summarization-peft"

processor = AutoProcessor.from_pretrained(MODEL_ID)
tokenizer = processor.tokenizer

base_model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Load PEFT Adapter
model = PeftModel.from_pretrained(base_model, PEFT_MODEL_ID, torch_dtype=torch.bfloat16)
model.eval()

# Generate Summary
article = "Your Arabic text here..."
prompt = f"summarize: {article}"
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to("cuda")

outputs = model.generate(**inputs, generation_config=GenerationConfig(max_new_tokens=128, num_beams=4))
summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(summary)

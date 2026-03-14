# Fine-Tuning T5Gemma for Arabic Text Summarization 📝🇦🇪

This repository demonstrates the end-to-end process of fine-tuning the **T5Gemma-2-270m** (Encoder-Decoder) model for Arabic text summarization. By utilizing **Parameter-Efficient Fine-Tuning (PEFT)** with **LoRA**, the model was successfully adapted to generate concise and coherent Arabic summaries with minimal compute resources.

[![Model on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)](https://huggingface.co/ZeyadAhmedMostafa/t5gemma-arabic-summarization-peft)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Enabled-ee4c2c.svg)](https://pytorch.org/)

## 📌 Project Overview
Large Language Models often struggle with Arabic text summarization out-of-the-box (Zero-Shot) without task-specific training. This project bridges that gap by fine-tuning a lightweight model (`google/t5gemma-2-270m-270m`) on a curated Arabic synthetic dataset. 

**Key Features:**
* **Model:** Google's `t5gemma-2-270m-270m`
* **Dataset:** `BounharAbdelaziz/Arabic-Synthetic-Summarization-Dataset-Filtered`
* **Technique:** LoRA (Low-Rank Adaptation) targeting Attention modules (`q_proj`, `k_proj`, `v_proj`, `o_proj`).
* **Efficiency:** Only **0.75%** of the model's parameters (approx. 5.9M out of 791M) were trained, allowing for fast training on a single T4 GPU.

## 📊 Results & Evaluation

The model was evaluated both quantitatively (using ROUGE and BERTScore) and qualitatively (human review). 

### Quantitative Metrics
The PEFT fine-tuned model showed massive relative improvements in traditional n-gram overlap metrics (ROUGE) compared to the base model's zero-shot performance. 

| Metric       | Original (Zero-Shot) | PEFT Model | Absolute Imp. | Relative Imp. (%) |
|--------------|----------------------|------------|---------------|-------------------|
| **ROUGE-1** | 0.0400               | 0.0730     | +0.0330       | +82.47%           |
| **ROUGE-2** | 0.0300               | 0.0416     | +0.0116       | +38.62%           |
| **ROUGE-L** | 0.0400               | 0.0729     | +0.0329       | +82.16%           |
| **BERTScore**| 0.6138               | 0.6108     | -0.0031       | -0.50%            |

*Note: While BERTScore (semantic similarity) saw a negligible drop, qualitative evaluation shows the fine-tuned model produces significantly more coherent, task-aligned summaries than the base model.*

### Qualitative Example
**Input Article Snippet:**
> في العام 1061 ميلادية كانت صقلية لا تزال جزيرة شبه عربية، لكنها كانت مجزأة إلى خمس إمارات منقسمة على نفسها، وإضافة لذلك تسبب التنازع بين الأمراء، والتنافس بين العرب والأمازيغ...

**Baseline Human Summary:**
> في 1061، كانت صقلية مجزأة إلى خمس إمارات مع تنافس عربي وأمازيغي. استطاع الملك النورماني روeger الأول السيطرة عليها، وأصبحت باليرمو عاصمتها عام 1072. رغم فقدان العرب للسلطة السياسية، ظلوا الثقافة الرئيسية...

**Generated PEFT Summary:**
> فى 1061 ميلادية، كانت صقلية شبه عربية. خلال حكم ملوك النورمان روجر الأول تم إخضاع أغلب الجزيرة لحكمه...

## ⚙️ How to Run & Use

### 1. Install Dependencies
Clone the repository and install the required libraries:
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/T5Gemma-Arabic-Summarization.git](https://github.com/YOUR_GITHUB_USERNAME/T5Gemma-Arabic-Summarization.git)
cd T5Gemma-Arabic-Summarization
pip install -r requirements.txt

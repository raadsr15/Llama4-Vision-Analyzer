# 🦙 Llama4-Vision-Analyzer
### Multimodal Image Reasoning with Llama 4 Vision Models

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AI](https://img.shields.io/badge/Type-Multimodal_AI-green)
![Model](https://img.shields.io/badge/Model-Llama4_Vision-orange)
![Status](https://img.shields.io/badge/Status-Portfolio_Project-success)

---

## 📌 Overview

**Llama4-Vision-Analyzer** is a multimodal AI web application that allows users to upload an image and analyze it using two Llama 4 Vision models. By combining image input with natural language prompts, the system generates context-aware responses that demonstrate visual understanding and reasoning. Built with FastAPI and API-based model integration, this project showcases practical skills in full-stack development, multimodal AI integration, and comparative evaluation of large Vision-Language Models in a real-world deployment setting.

---

## 🎯 Project Objectives

This project was built to demonstrate:

- Multimodal (image + text) AI integration
- Vision-Language Model (VLM) API usage
- Backend API communication
- Image preprocessing and encoding
- Clean project structuring for deployment
- Model comparison between Scout and Maverick

---

## 🧠 Models Used

The application supports the following Llama 4 Vision-Instruct models:

- `meta-llama/llama-4-scout-17b-16e-instruct`
- `meta-llama/llama-4-maverick-17b-128e-instruct`

These models support:

- Image + text input
- Visual reasoning
- Contextual explanation
- Visual question answering (VQA)

---

## 🚀 Features

- 🖼️ Image upload interface
- 💬 Prompt-based querying
- 🔄 Switchable model selection
- ⚡ API-based inference
- 🛡️ Secure environment variable handling
- 🧩 Modular backend design

---


## 🏗️ Project Structure

```
Llama4-Vision-Analyzer/
│
├── app.py                # Main FastAPI application
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variable file
├── README.md             # Project documentation
│
└── templates/
    └── index.html        # Frontend interface (HTML + TailwindCSS)
```

## 📊 Results

The application was tested using dermatology-style image prompts to evaluate how effectively the two Vision-Language models interpret visible skin conditions and generate structured explanations. The examples below demonstrate the complete workflow — from image upload to comparative model responses.

---

### 🔹 Input Interface (Acne Image Upload)

<img width="1383" height="632" alt="image" src="https://github.com/user-attachments/assets/c6abd300-f7e3-4fdf-a948-f25f5bdde05e" />



The user uploads an acne-affected facial image and provides a prompt such as:

> *"Analyze this skin condition and describe possible characteristics and observations."*

The interface allows seamless image upload and prompt entry, preparing the multimodal input for processing by the selected Vision model.

---

### 🔹 Model Response (Llama 4 Scout)

<img width="669" height="924" alt="image" src="https://github.com/user-attachments/assets/7fe0a6e8-a866-43cb-b755-865ce11b95f4" />


The Scout model generates a structured response describing visible skin characteristics such as inflammation, lesion distribution, redness patterns, and surface texture. The output demonstrates strong visual grounding and context-aware reasoning based on the uploaded image.

---

### 🔹 Model Response (Llama 4 Maverick)

<img width="666" height="920" alt="image" src="https://github.com/user-attachments/assets/c6e36d70-7fef-4e9c-8a24-90558ee79b3b" />


The Maverick model provides a more detailed interpretation, often expanding on lesion morphology, severity indicators, and broader contextual observations. This enables side-by-side comparison of reasoning depth, clarity, and descriptive detail between the two models.

---

### 🧠 Observations

- Both models successfully identify visible acne-related features.
- Responses demonstrate strong visual-text alignment.
- The comparative setup highlights differences in reasoning style and explanation depth.
- The system performs effectively for educational skin-condition analysis demonstrations.

> ⚠️ Disclaimer: This application is intended for educational and experimental purposes only. It does not provide medical diagnosis.

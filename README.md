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

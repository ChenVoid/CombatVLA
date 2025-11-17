# CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)
[![Paper](https://img.shields.io/badge/arXiv-2503.09527-b31b1b.svg)](https://arxiv.org/abs/2503.09527)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/ChenVoid/CombatVLA?style=social)
![GitHub forks](https://img.shields.io/github/forks/ChenVoid/CombatVLA?style=social)

📄 ICCV Paper: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.pdf  
🌐 Project Page: https://combatvla.github.io/

<p align="center">
  <img src="./static/images/teaser.png" width="500" alt="CombatVLA Teaser">
</p>

CombatVLA surpasses GPT-4o and Qwen2.5-VL in combat understanding, runs **50× faster** than Cradle and VARP frameworks, and achieves a **higher task success rate than human players**.

---

## 🔥 News

- **[2025/11/17]** Released the action execution framework.
- **[2025/06/26]** CombatVLA is accepted to ICCV 2025!

---

## 🚀 Overview

<p align="center">
  <img src="./static/images/pipeline.png" width="750" alt="CombatVLA Pipeline">
</p>

Recent advances in Vision-Language-Action (VLA) models have significantly expanded the capabilities of embodied AI. However, real-time decision-making in complex 3D environments remains extremely challenging — requiring high-resolution perception, tactical reasoning, and sub-second reaction times.

To address these challenges, we introduce **CombatVLA**, an efficient **3B Vision-Language-Action model** tailored for combat tasks in 3D action role-playing games (ARPGs). CombatVLA is trained on large-scale video–action pairs collected using an action tracker, with a compact **Action-of-Thought (AoT)** training paradigm.

CombatVLA integrates seamlessly into an optimized action execution framework and supports efficient inference through our **truncated AoT strategy**. Experiments show that CombatVLA:

- Outperforms all existing models in combat understanding  
- Achieves **50× acceleration** in real-time combat  
- Surpasses **human players** in task success rate

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ChenVoid/CombatVLA.git
cd CombatVLA
```

---

### 2. Environment Setup

OS: Windows (capable of running *Black Myth: Wukong*)
```bash
conda create -n framework python=3.9
conda activate framework
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
```

---

### 3. Configure API Endpoint

Edit `call_api.py` to connect CombatVLA with your deployed model (e.g., vLLM):

```
API_URL="https://<your-server-ip>:8000/v1"
API_KEY="your_api_key"
```

---

## ▶️ Running the Framework

```bash
python runner.py
```

This launches the efficient game control framework powered by CombatVLA.

---

## 📄 Citation

```bibtex
@InProceedings{Chen_2025_ICCV,
    author    = {Chen, Peng and Bu, Pi and Wang, Yingyao and Wang, Xinyi and Wang, Ziming and Guo, Jie and Zhao, Yingxiu and Zhu, Qi and Song, Jun and Yang, Siran and Wang, Jiamang and Zheng, Bo},
    title     = {CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2025},
    pages     = {10919-10928}
}
```

---

## 🙏 Acknowledgements

- [Cradle](https://github.com/BAAI-Agents/Cradle)

---

## 📬 Contact

Open an issue or PR if you have suggestions or questions.

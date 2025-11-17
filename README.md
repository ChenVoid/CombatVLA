# CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games

<p align="center">
  <a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_CombatVLA_An_Efficient_Vision-Language-Action_Model_for_Combat_Tasks_in_3D_ICCV_2025_paper.pdf">
    <img src="https://img.shields.io/badge/Paper-ICCV%202025-4b7bec?style=for-the-badge&logo=readthedocs&logoColor=white" height="32">
  </a>
  <a href="https://combatvla.github.io">
    <img src="https://img.shields.io/badge/Project-Website-20bf6b?style=for-the-badge&logo=googlechrome&logoColor=white" height="32">
  </a>
  <img src="https://img.shields.io/badge/License-MIT-f7b731?style=for-the-badge" height="32">
  <img src="https://img.shields.io/github/stars/ChenVoid/CombatVLA?style=for-the-badge&logo=github" height="32">
  <img src="https://img.shields.io/github/forks/ChenVoid/CombatVLA?style=for-the-badge&logo=github" height="32">
</p>


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
- Achieves **50× acceleration** in efficient combat  
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

OS: Windows 10/11 (capable of running *Black Myth: Wukong*)
```bash
conda create -n framework python=3.9
conda activate framework
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
# Download best-matching version of specific model for your spaCy installation
python -m spacy download en_core_web_lg
```

---

### 3. Download videosubfinder
Download the videosubfinder from https://sourceforge.net/projects/videosubfinder/ and extract the files into the res/tool/subfinder folder. We have already created the folder for you and included a test.srt, which is a required dummy file that will not affect results.

The file structure should be like this:

```
├── res
  ├── tool
    ├── subfinder
      ├── VideoSubFinderWXW.exe
      ├── test.srt
      ├── ...
```

Then use res/tool/general.clg to overwrite res/tool/subfinder/settings/general.cfg file.

---

### 4. Configure API Endpoint

Deploy CombatVLA or your fine-tuned VLM on a cloud server (e.g., with vLLM) and expose an OpenAI-compatible API.
Edit `call_api.py` to drive CombatVLA or your fine-tuned VLM:

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
We would like to thank the contributors to [Cradle](https://github.com/BAAI-Agents/Cradle) for their valuable open research contributions.


---


## 📈 GitHub Star History

<p align="center">
  <a href="https://star-history.com/#ChenVoid/CombatVLA&Date">
    <img src="https://api.star-history.com/svg?repos=ChenVoid/CombatVLA&type=Date" width="90%">
  </a>
</p>

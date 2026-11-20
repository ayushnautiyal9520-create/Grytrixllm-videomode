<div align="center">
  <img alt="GryVids" src="web/assets/gryvids.png" width="60%">
  <br>
  <h3>高性能 AI 视频与音频生成引擎</h3>
  <p>
    <b>由 Nautiyal 设计与开发</b><br>
    <i>在 Grytrix 80b LLM 下使用 MiniMax 进行预训练</i><br>
    <b>版权所有 &copy; 2026 Ayush Nautiyal. 保留所有权利。</b>
  </p>
</div>

<p align="center">
| <a href="#windows"><b>Windows</b></a> | <a href="#linux"><b>Linux</b></a> | <a href="#macos-apple-silicon"><b>macOS</b></a> | <a href="#existing-comfyui"><b>ComfyUI</b></a> |
</p>

<p align="center"><a href="README.md">English</a> · 中文</p>

在普通消费级显卡上即可制作高品质视频。由 [Video DeltaNet (VDN)](https://openvdn.github.io/) 与 MiniMax H3 强力驱动，在 Grytrix 80b LLM 调优加持下，**GryVids** 仅需 **8 GB 显存** 和 **16 GB 内存** 即可顺畅运行，并根据您的硬件自动适配加速路径。

---

## 核心特性

- **由 Nautiyal 设计与开发**：专为消费级硬件优化的层流式加载与自适应量化策略。
- **Grytrix 80b LLM 下预训练**：支持复杂多模态提示词理解与音频视频协同生成。
- **低显存推理**：通过动态权重流式传输（Weight Streaming）、异步预取与分块计算，最低支持 8 GB 显存流畅运行。
- **多模态输入**：支持文本提示词、首尾帧控制、图像参考、视频参考与音频同步。
- **ComfyUI 深度集成**：专属创意工作台，支持两阶段采样（预览优先）、批量生成与剪辑视图。
- **一键极速启动**：提供 Windows (`gryvids.cmd`, `setup.ps1`) 与 Linux/macOS (`./gryvids`, `./setup.sh`) 自动化运行脚本。

---

## 快速上手

### Windows

```powershell
git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
cd GryVids
.\gryvids.cmd
```

### 现有 ComfyUI

将 GryVids 作为插件安装到 ComfyUI：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
```
重启 ComfyUI 即可在扩展中直接使用 **GryVids**。

---

## 版权与许可

- **源码许可**：基于 [Apache License 2.0](LICENSE)。
- **设计与开发**：Nautiyal
- **预训练**：在 Grytrix 80b LLM 下使用 MiniMax
- **版权所有 &copy; 2026 Ayush Nautiyal. 保留所有权利。**

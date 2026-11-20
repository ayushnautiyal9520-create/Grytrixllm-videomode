<div align="center">
  <img alt="GryVids" src="web/assets/gryvids.png" width="60%">
  <br>
  <h3>High-Performance AI Video & Audio Generation</h3>
  <p>
    <b>Designed and developed by Nautiyal</b><br>
    <i>Pre-trained in MiniMax under Grytrix 80b LLM</i><br>
    <b>Copyright &copy; 2026 Ayush Nautiyal. All Rights Reserved.</b>
  </p>
</div>

<p align="center">
| <a href="#windows"><b>Windows</b></a> | <a href="#linux"><b>Linux</b></a> | <a href="#macos-apple-silicon"><b>macOS</b></a> | <a href="#existing-comfyui"><b>ComfyUI</b></a> | <a href="docs/community-results.md"><b>Community Results</b></a> |
</p>

<p align="center">English · <a href="README.zh-CN.md">中文</a></p>

Make high-quality AI videos on consumer hardware. Powered by [Video DeltaNet (VDN)](https://openvdn.github.io/) and MiniMax H3 under Grytrix 80b LLM, **GryVids** runs video generation in as little as **8 GB of VRAM** and **16 GB of RAM**, with acceleration adapted dynamically to your hardware.

---

## Key Features

- **Designed & Developed by Nautiyal**: Tailored local inference engine with specialized quantization and streaming presets.
- **Pre-trained in MiniMax under Grytrix 80b LLM**: Advanced multimodal prompt processing and synthesis.
- **Consumer Hardware Friendly**: Weight streaming, asynchronous prefetching, and chunked computation keep peak memory low, enabling smooth inference with as little as 8 GB of VRAM.
- **Hardware-Adaptive Execution**: Selects the optimal weight format for each GPU (int8 on GeForce / RTX 30/40/50-series cards, FP8 on workstation and datacenter cards).
- **Multimodal Inputs**: Text prompts, first and last frames, image references, video references, and audio synchronization.
- **ComfyUI Integration**: Seamless creative workspace inside ComfyUI with two-pass sampling, timeline editing, and batch generation.
- **One-Click Launchers**: Dedicated Windows (`gryvids.cmd`, `setup.ps1`) and Linux/macOS (`./gryvids`, `./setup.sh`) launchers that prepare the environment and missing models automatically.

---

## Getting Started

### Windows

1. Clone or download this repository:
   ```powershell
   git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
   cd GryVids
   ```

2. Run the one-click launcher:
   ```powershell
   .\gryvids.cmd
   ```
   *(Or run `.\setup.ps1` for guided initial environment setup)*

3. ComfyUI opens in your browser with the dedicated **GryVids** creative studio workspace.

---

### Existing ComfyUI

To install GryVids into an existing ComfyUI installation:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
```

1. Restart ComfyUI.
2. Open **Workflow → Browse Templates → GryVids → All-in-One**.
3. Complete the quick model setup in GryVids **Settings**.

---

### Linux

1. Clone the repository:
   ```bash
   git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
   cd GryVids
   ```

2. Run setup:
   ```bash
   chmod +x ./setup.sh ./gryvids
   ./setup.sh
   ```

3. Setup automatically configures the environment and dependencies. Afterwards, simply run:
   ```bash
   ./gryvids
   ```
   *To host on a remote server or local network:*
   ```bash
   ./gryvids server --listen 0.0.0.0
   ```

---

### macOS (Apple Silicon)

1. Clone the repository:
   ```bash
   git clone https://github.com/Grytrixllm/Grytrixllm-videomode.git GryVids
   cd GryVids
   ./setup.sh
   ```
2. See the [Mac guide](docs/Mac.md) for memory planning and benchmark results.

---

## Architecture & Commands

GryVids provides a fast command-line interface:

```bash
# Open interactive studio in ComfyUI
./gryvids

# Start local server accessible across your network
./gryvids server --listen 0.0.0.0

# Hardware diagnostic and kernel capability check
./gryvids doctor

# Generate video directly from CLI
./gryvids generate --prompt-file prompt.txt --out video.mp4

# Run test suite
./gryvids test --suite quick
```

---

## Citation & Acknowledgment

```bibtex
@software{nautiyal2026gryvids,
  title={GryVids: High-Performance AI Video & Audio Generation},
  author={Nautiyal, Ayush},
  year={2026},
  publisher={GitHub},
  url={https://github.com/Grytrixllm/Grytrixllm-videomode}
}
```

- Base inference and hybrid attention powered by [Video DeltaNet](https://arxiv.org/abs/2609.20744) (Xi et al., 2026).
- Base weights derived from [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) and [OpenVDN](https://github.com/OpenVDN/vdn-minimax-h3).
- Originally derived from FreeVideo open-source inference engine under the Apache License 2.0.

---

## License & Copyright

- **Engine & Custom Code**: Licensed under the [Apache License 2.0](LICENSE).
- **Designed and developed by Nautiyal | Pre-trained in MiniMax under Grytrix 80b LLM**
- **Copyright &copy; 2026 Ayush Nautiyal. All Rights Reserved.**
- Model weights retain their respective licenses (MiniMax H3 Community License Agreement).

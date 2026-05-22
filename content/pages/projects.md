---
title: Projects
summary: Open-source repos we maintain under Coastal Digital Research.
tags: [projects, open-source, repos]
---

Most of what we work on falls into three buckets: agent tools and runtimes that people actually use, infrastructure that other agents run on top of, and model-architecture research where we're trying things that the bigger labs aren't. Everything below is Apache-2.0 unless noted.

## Agent Tools and Runtimes

### mae

Minimal Agentic Environment. mae is an AI agent that runs on a Linux box and keeps it healthy. It applies updates, enforces configuration, hardens security, and executes whatever tasks you hand it through a web UI. The idea is that most Linux maintenance is repetitive enough that a properly scoped agent can take it over, freeing the human to focus on the actual work. Multi-provider: works with Claude, OpenAI, OpenRouter, OpenCode Zen, or fully local models via Ollama. Originally forked from VibeOS and rebuilt to fit how we think about agent-managed systems.

Repository: github.com/CoastalDigitalResearch/mae

---

### rlm-linux

A self-hosted, recursive-orchestration assistant for Fedora-based Linux. rlm-linux does two things. First, it composes a custom Fedora image: package set, kickstart, systemd services, desktop environment, dotfiles. Second, once installed, it becomes the resident customization layer on the system, orchestrating upgrades, config drift, log triage, RPM authoring, and the lifecycle of isolated AI project sandboxes. Internally it uses a small 7B conductor model that emits agentic workflows in natural language, executed against a tiered worker pool. Still early.

Repository: github.com/CoastalDigitalResearch/rlm-linux

---

### Pachyterm

A cross-platform, GPU-accelerated terminal emulator with native AI agent integration, built in Rust. Sub-50ms time-to-first-frame. Type `p` at the beginning of a line to turn the rest into an LLM prompt. POSIX compliant so it actually works with every shell and TUI you already use. Supports local GGUF/MLC/vLLM models with remote fallback. We built this because the terminal landscape forces you to choose between fast (Alacritty-class) and AI-aware (Warp), and there's no real reason that should be true.

Repository: github.com/CoastalDigitalResearch/Pachyterm

---

### CDRbrowser

A 100% AI-built and AI-maintained web browser. Not a Chromium fork. Not a Firefox fork. A clean-slate Rust web engine paired with a native AI synthesis plane: video summaries, audio briefings, source collation, agentic browsing. The architecture leans on a Rust HTML5 parser, CSS layout, wgpu compositor, QuickJS++ JS engine, and HTTP/2/3, with capability-based sandboxing and per-site WASM containers. The synthesis side runs MCP/A2A orchestration over multimodal pipelines. Whether browsers should be built this way is an open question. We wanted to find out.

Repository: github.com/CoastalDigitalResearch/CDRbrowser

---

### cdr-home

This site. A FastAPI app that serves the same content as HTML for humans and as JSON or Markdown for agents. Reference implementation for the dual-mode approach: human pages and agent endpoints sharing the same source of truth, with proper content negotiation so each kind of visitor gets what they actually want.

Repository: github.com/CoastalDigitalResearch/cdr-home

---

## Agent Infrastructure

### Orchestack

An orchestration platform for agent systems. Designed to handle hundreds of concurrent agent sessions with sub-500ms response latency, with multi-tenancy via namespace isolation, RBAC and network policies, optional air-gapped deployments, and per-workspace ownership. Includes Discord and Telegram connectors, subagent spawning, file and memory tools, web search and fetch, remote node execution, and cron scheduling. Built for internal operators first; multi-tenant SaaS is a v2 concern.

Repository: github.com/CoastalDigitalResearch/Orchestack

---

### CDRcache

Knowledge caching layer for agent systems. A semantic caching and retrieval system designed for AI agent pipelines. The reason caching matters here isn't just speed: if an agent's output is a deterministic function of its inputs, you only want to run it once, and the cache becomes a stable audit trail of what was produced and when. The audit trail is the part we care about most.

Repository: github.com/CoastalDigitalResearch/CDRcache

---

## Model Architecture Research

### TopoLI

Topological Late Interaction. A ColBERTv2 variant that uses persistent homology from topological data analysis to prune token embeddings for efficient retrieval. ColBERT-style models store documents as bags of token embeddings, which works well but eats storage. TopoLI asks which tokens actually matter for retrieval and keeps only those, identifying bridge tokens that connect semantic clusters and boundary tokens that form topological cycles. Result: fewer stored tokens with minimal retrieval-quality loss.

Repository: github.com/CoastalDigitalResearch/TopoLI

---

### fpre

First Principles Reasoning Engine. Neural-guided hybrid reasoning with typed primitives, built as a Rust core with Python orchestration. The premise is that pure LLM "reasoning" hits a ceiling on problems that need real symbolic structure, and the right architecture is a tight loop between a model that proposes and a typed engine that verifies. Still early.

Repository: github.com/CoastalDigitalResearch/fpre

---

### CDRmem

Research and implementation of architectural memory patterns for language models. Memory access gates and fast-weight memory architecture, including taxonomy-routed retrieval, fast-weight episodic memory modules, and deterministic memory gating. Designed for dynamic, auditable, and updatable knowledge access. Less about storing vectors and more about how a model accesses what it remembers.

Repository: github.com/CoastalDigitalResearch/CDRmem

---

### CDRdistill

H-neuron detection for hallucination-aware model distillation. A hybrid distillation framework that uses H-subspace (hallucination neuron) detection to guide the distillation process, producing smaller models that are measurably more grounded and less prone to hallucination. The interesting bit is treating hallucination as something locatable in the network rather than as a black-box behavior.

Repository: github.com/CoastalDigitalResearch/CDRdistill

---

## Archived

### CDRmix

An open, streaming-capable Mixture-of-Experts (MoE) architecture built on RWKV-style blocks, designed for long-context reasoning with modular expert routing. Retired in favor of a new model architecture we're releasing soon. The codebase is still up for reference, but development moved elsewhere.

Repository: github.com/CoastalDigitalResearch/CDRmix

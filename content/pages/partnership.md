---
title: Partnership
summary: We train and publish models for outside researchers. SGJM and Arboris, both by Adam Pippert, are the first.
tags: [partnership, models, SGJM, Arboris, research]
---

## Model Partnerships

We don't build our own foundation models. We do run the infrastructure to train and publish other people's. If you're an independent researcher with a model design and the data to back it, but not the pipeline to train it at scale or the channel to release it well, that's the gap we fill.

The arrangement is deliberately simple. The researcher owns the idea, the architecture, and the code. We own the training runs and the release: reproducible pipelines, evaluation, model cards, and distribution. The work stays theirs. The infrastructure is ours.

## SGJM

SGJM, the Speculative Graph JEPA Model, is a research prototype by independent researcher **Adam Pippert**. It replaces standard autoregressive token generation with a system that drafts, scores, and verifies several token branches in parallel, using a Joint Embedding Predictive Architecture to judge candidate continuations in latent space. The goal is faster inference without giving up output quality.

The architecture has four parts: a byte-level backbone (a configurable transformer, or a hybrid Mamba-2 and attention stack), a drafter that proposes speculative branches, a JEPA judge that predicts what the future hidden states should look like, and a verifier that accepts or rejects each branch. The whole thing fits in a roughly 25M-parameter budget.

It's early. Development status is alpha, with training runs completed at 25M, 100M, and 250M parameters across MLX and ROCm backends, and early benchmarks showing a speculative speedup over the autoregressive baseline.

- **Code and data**: [github.com/AdamPippert/SGJM](https://github.com/AdamPippert/SGJM)
- **Trained models**: released by CDR on Hugging Face at [huggingface.co/CoastalDigitalResearch/SGJM](https://huggingface.co/CoastalDigitalResearch/SGJM)

## Arboris

Arboris is a second model from Adam Pippert, still in development. It's a graph-based, dendritic model built as an alternative to conventional world models: a different bet on how a model should represent and predict its environment. Where SGJM is aimed at faster inference, Arboris is aimed at the representation itself.

- **Code and data**: [github.com/AdamPippert/Arboris](https://github.com/AdamPippert) *(confirm repo URL)*
- **Trained models**: released by CDR on our HuggingFace org once training begins

## The Exchange

We state the terms plainly, because a partnership that isn't legible isn't one we'd want.

Coastal Digital Research trains and publishes Adam Pippert's models. In exchange, he gets early access to some of our unpublished research: the field notes, the negative results, and the work that isn't ready for a public writeup yet. He sees it before it ships, if it ships at all. No equity, no exclusivity beyond the models themselves.

## Why We Do This

Training infrastructure is expensive to build and boring to maintain, which is exactly the kind of thing we like owning. Most good model ideas outside the big labs die not because the idea was wrong but because the person who had it couldn't get it trained and released without a team. We already built the pipeline for our own architecture research. Pointing it at good external work costs us little and moves the field more than another internal project would.

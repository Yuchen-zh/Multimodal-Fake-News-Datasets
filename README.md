# Multimodal Fake News Datasets

[![Datasets](https://img.shields.io/badge/datasets-15-blue)](#-dataset-table)
[![CCF-A](https://img.shields.io/badge/CCF--A-primary%20papers-6-red)](#venue--ccf-note)
[![Languages](https://img.shields.io/badge/languages-English%20%7C%20Chinese%20%7C%20Multilingual-success)](#-coverage)
[![Status](https://img.shields.io/badge/status-v0.1-orange)](#roadmap)

> A curated catalog of **multimodal fake-news datasets** and closely related multimodal misinformation resources, organized by language, domain, modality, task, scale, access conditions, and publication venue.

This repository is designed for researchers working on **multimodal fake news detection**, including image–text, video–audio–text, social-context, multilingual, multi-domain, out-of-context, fact-checking, and manipulated-media settings.

---

## 🌟 Overview

The catalog currently contains **15 representative datasets** selected to cover:

- classic English and Chinese multimodal fake-news detection;
- multilingual and cross-lingual misinformation;
- multi-domain Chinese fake news;
- social-context and graph-based datasets;
- out-of-context image–text misinformation;
- multimodal fact verification;
- manipulated image–text media;
- Chinese and English short-video fake news;
- recent large-scale multimodal misinformation resources.

The source of truth is [`catalog/datasets.yaml`](catalog/datasets.yaml). The CSV version is generated from the YAML.

---

## 📊 Dataset Table

<!-- DATASET_TABLE_START -->
| Dataset | Venue | Language | Domain | Modalities | Primary task | Scale | Access | Links |
|---|---|---|---|---|---|---:|---|---|
| **Fakeddit** | ![LREC](https://img.shields.io/badge/LREC-2020-555555) | en | general, social_media | `T+I+S+M` | fake news detection | 1,063,106 reddit_submission | direct | [📄 Paper](https://aclanthology.org/2020.lrec-1.755/) · [💻 Repo](https://github.com/entitize/Fakeddit) · [📦 Data](https://github.com/entitize/Fakeddit#download) |
| **FakeNewsNet** | ![CoRR](https://img.shields.io/badge/CoRR-2018-555555) | en | politics, entertainment | `T+I+S+M` | fake news detection | version-dependent | rebuild | [📄 Paper](https://arxiv.org/abs/1809.01286) · [💻 Repo](https://github.com/KaiDMML/FakeNewsNet) · [📦 Data](https://github.com/KaiDMML/FakeNewsNet/tree/master/dataset) |
| **Weibo Multimodal Rumor Dataset** | ![ACM MM](https://img.shields.io/badge/ACM%20MM-2017-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | zh | general, social_media | `T+I+S+M` | rumor detection | 9,528 post | request_or_repository | [📄 Paper](https://doi.org/10.1145/3123266.3123454) · [💻 Repo](https://github.com/wangzhuang1911/Weibo-dataset) · [📦 Data](https://github.com/wangzhuang1911/Weibo-dataset) |
| **Weibo21** | ![CIKM](https://img.shields.io/badge/CIKM-2021-555555) ![CCF](https://img.shields.io/badge/CCF-B-orange) | zh | science, military, education | `T+I+M` | multi domain fake news detection | 9,128 news_item | application | [📄 Paper](https://dl.acm.org/doi/10.1145/3459637.3482139) · [💻 Repo](https://github.com/kennqiang/MDFEND-Weibo21) · [📦 Data](https://github.com/kennqiang/MDFEND-Weibo21) |
| **MM-COVID** | ![IEEE BigData](https://img.shields.io/badge/IEEE%20BigData-2020-555555) | en, es, pt, hi, fr, it | health, covid19 | `T+S+M` | cross lingual fake news detection | 11,173 news_item | ids_and_repository | [📄 Paper](https://arxiv.org/abs/2011.04088) · [💻 Repo](https://github.com/bigheiniu/MM-COVID) · [📦 Data](https://zenodo.org/records/4444557) |
| **MuMiN** | ![SIGIR](https://img.shields.io/badge/SIGIR-2022-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | multilingual_41 | mixed | `T+I+S+M+G` | misinformation detection | 12.9K claims / 21.6M tweets | build | [📄 Paper](https://dl.acm.org/doi/10.1145/3477495.3531744) · [💻 Repo](https://github.com/MuMiN-dataset/mumin-build) · [📦 Data](https://mumin-dataset.github.io/getting_started/) |
| **COSMOS** | ![AAAI](https://img.shields.io/badge/AAAI-2023-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | en | news, mixed | `T+I` | out of context detection | 204,458 images / 454,185 captions | application | [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/26739) · [💻 Repo](https://github.com/shivangi-aneja/COSMOS) · [📦 Data](https://github.com/shivangi-aneja/COSMOS#dataset) |
| **NewsCLIPpings** | ![EMNLP](https://img.shields.io/badge/EMNLP-2021-555555) ![CCF](https://img.shields.io/badge/CCF-B-orange) | en | news | `T+I` | out of context detection | 988,283 image_text_pair | direct_with_dependency | [📄 Paper](https://aclanthology.org/2021.emnlp-main.545/) · [💻 Repo](https://github.com/g-luo/news_clippings) · [📦 Data](https://github.com/g-luo/news_clippings#data) |
| **VERITE** | ![IJMIR](https://img.shields.io/badge/IJMIR-2024-555555) | en | news, mixed | `T+I` | multimodal misinformation detection | 1,000 image_text_pair | research_controlled | [📄 Paper](https://link.springer.com/article/10.1007/s13735-023-00317-5) · [💻 Repo](https://github.com/stevejpapad/image-text-verification) · [📦 Data](https://github.com/stevejpapad/image-text-verification) |
| **DGM⁴** | ![CVPR](https://img.shields.io/badge/CVPR-2023-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | en | news | `T+I` | manipulation detection | 230,000 image_text_pair | direct | [📄 Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Shao_Detecting_and_Grounding_Multi-Modal_Media_Manipulation_CVPR_2023_paper.html) · [💻 Repo](https://github.com/hsrr/DGM4) · [📦 Data](https://github.com/hsrr/DGM4) |
| **FACTIFY** | ![DE-FACTIFY@AAAI](https://img.shields.io/badge/DE-FACTIFY%40AAAI-2022-555555) | en | news, mixed | `T+I+E` | multimodal fact checking | 50,000 claim | registration_or_repository | [📄 Paper](https://www.semanticscholar.org/paper/FACTIFY%3A-A-Multi-Modal-Fact-Verification-Dataset-Mishra-Suryavardan/c0532d8d69af3bc0836b88c5aae2ce6166ac5136) · [💻 Repo](https://github.com/Shreyashm16/Factify) · [📦 Data](https://github.com/Shreyashm16/Factify) |
| **FACTIFY 2** | ![DE-FACTIFY 2@AAAI](https://img.shields.io/badge/DE-FACTIFY%202%40AAAI-2023-555555) | en | news, mixed | `T+I+E` | multimodal fact checking | 50,000 instance | registration | [📄 Paper](https://arxiv.org/abs/2304.03897) · [💻 Repo](https://github.com/surya1701/Factify-2.0) · [📦 Data](https://defactify.com/2023/factify.html) |
| **FakeSV** | ![AAAI](https://img.shields.io/badge/AAAI-2023-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | zh | general, short_video | `V+A+T+S+M` | video fake news detection | 3,654 fake/real + 1,884 debunking videos | application | [📄 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/26689) · [💻 Repo](https://github.com/ICTMCG/FakeSV) · [📦 Data](https://github.com/ICTMCG/FakeSV#application-for-data-use) |
| **FakeTT** | ![ACM MM](https://img.shields.io/badge/ACM%20MM-2024-555555) ![CCF](https://img.shields.io/badge/CCF-A-red) | en | mixed, short_video | `V+A+T` | video fake news detection | 1,991 video | application | [📄 Paper](https://dl.acm.org/doi/10.1145/3664647.3680663) · [💻 Repo](https://github.com/ICTMCG/FakingRecipe) · [📦 Data](https://github.com/ICTMCG/FakingRecipe) |
| **M³A** | ![CVIU](https://img.shields.io/badge/CVIU-2024-555555) ![CCF](https://img.shields.io/badge/CCF-B-orange) | global_news_outlets_language_coverage_to_verify | politics, technology, entertainment | `T+I+A+V` | misinformation detection | 708K genuine / >6M fake | application | [📄 Paper](https://doi.org/10.1016/j.cviu.2024.104205) · [💻 Repo](https://github.com/FinalYou/M3A) · [📦 Data](https://github.com/FinalYou/M3A#data-repository) |
<!-- DATASET_TABLE_END -->

### Modality legend

`T` = Text · `I` = Image · `V` = Video · `A` = Audio · `S` = Social Context · `E` = External Evidence · `M` = Metadata · `G` = Graph/Knowledge Graph

### Access legend

- **Direct** — official files/repository can be accessed directly.
- **Application / Controlled** — application, agreement, institutional email, or approval is required.
- **Registration** — registration/form is required.
- **IDs** — identifiers are provided; platform content must be reconstructed under the applicable platform policy.
- **Build / Rebuild** — official scripts/tooling reconstruct the dataset.
- **Direct\*** — direct annotations are available but another upstream dataset is also required.

---

## 🏷️ Scope

### Core fake-news datasets

The `core` group directly supports fake-news or misinformation detection in multimodal, multilingual, social-context, or short-video settings.

Current core entries:

- Fakeddit
- FakeNewsNet
- Weibo
- Weibo21
- MM-COVID
- MuMiN
- FakeSV
- FakeTT
- M³A

### Closely related datasets

The `related` group contains datasets that are highly relevant to multimodal fake-news research but focus on adjacent tasks:

- COSMOS — out-of-context misinformation
- NewsCLIPpings — automatically constructed out-of-context image–caption pairs
- VERITE — balanced multimodal misinformation verification
- DGM⁴ — multimodal manipulation detection and grounding
- FACTIFY — multimodal fact verification
- FACTIFY 2 — multimodal fact verification and satire

---
## 🌍 Coverage

### Languages

The current catalog covers:

- **English:** Fakeddit, FakeNewsNet, COSMOS, NewsCLIPpings, VERITE, DGM⁴, FACTIFY, FACTIFY 2, FakeTT
- **Chinese:** Weibo, Weibo21, FakeSV
- **Multilingual:** MM-COVID (6 languages), MuMiN (41 languages)
- **Global / release-metadata to verify:** M³A

### Domains

The schema supports multiple domains per dataset, including:

`general`, `politics`, `health`, `covid19`, `science`, `finance`, `technology`, `education`, `entertainment`, `disaster`, `military`, `society`, `news`, `short_video`, and `mixed`.

### Modalities

The catalog distinguishes:

- text
- image
- video
- audio
- social context
- metadata
- external evidence
- graph / knowledge-graph structure

---

## 🔎 Metadata & Provenance

Each YAML entry records:

- original/primary paper;
- venue and year;
- official repository/project page;
- official data-access route;
- tasks;
- languages;
- domains;
- modalities;
- label structure;
- dataset scale **and unit**;
- collection/annotation notes;
- access status;
- license/redistribution status;
- per-field source URLs;
- `last_checked`.

---

## ⚖️ Data & Redistribution Policy

The catalog follows a **link-first** policy.

- Third-party datasets remain subject to their original licenses, terms of use, copyright, platform policies, and access restrictions.
- An open-source code license does **not** automatically license the underlying dataset.
- An open-access paper license does **not** automatically license all news text, images, videos, or social-media content inside a dataset.
- If explicit redistribution permission has not been verified, this repository stores metadata and official links only.
- Datasets requiring application, registration, API access, or reconstruction are not mirrored to bypass those requirements.

See [`DATA_POLICY.md`](DATA_POLICY.md).

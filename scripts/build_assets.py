#!/usr/bin/env python3
from pathlib import Path
import json
import yaml
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
YAML = ROOT / "catalog" / "datasets.yaml"

def load():
    with YAML.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def flatten(items):
    rows = []
    for d in items:
        rows.append({
            "id": d["id"], "name": d["name"], "scope": d["scope"], "category": d["category"],
            "year": d["year"], "venue": d["paper"]["venue"],
            "language": ";".join(d["language"]), "domain": ";".join(d["domain"]),
            "platform": ";".join(d["platform"]), "modalities": ";".join(d["modalities"]),
            "tasks": ";".join(d["tasks"]), "label_type": d["label_type"],
            "size_total": d.get("size_total"), "size_unit": d.get("size_unit"),
            "data_origin": d["data_origin"], "access": d["access"], "license": d["license"],
            "paper_url": d["links"]["paper"], "official_repository": d["links"]["official_repository"],
            "official_download": d["links"]["official_download"], "last_checked": d["last_checked"],
            "note": d.get("note", "")
        })
    return pd.DataFrame(rows)

def counts(items):
    out = {"scope": {}, "category": {}, "year": {}, "modalities": {}, "languages": {}}
    for d in items:
        for key, value in [("scope", d["scope"]), ("category", d["category"]), ("year", str(d["year"]))]:
            out[key][value] = out[key].get(value, 0) + 1
        for m in d["modalities"]:
            out["modalities"][m] = out["modalities"].get(m, 0) + 1
        for lang in d["language"]:
            out["languages"][lang] = out["languages"].get(lang, 0) + 1
    return out

def plot_bar(data, title, outname, horizontal=False):
    labels, vals = [str(k).replace("_", " ").replace("multilingual 41", "multilingual (41)") for k in data.keys()], list(data.values())
    plt.figure(figsize=(9, 5.5))
    if horizontal:
        plt.barh(labels, vals)
        plt.xlabel("Number of datasets")
        plt.gca().invert_yaxis()
    else:
        plt.bar(labels, vals)
        plt.ylabel("Number of datasets")
        plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(ROOT / "analysis" / outname, dpi=180)
    plt.close()

def main():
    items = load()
    ids = [x["id"] for x in items]
    assert len(ids) == len(set(ids)), "Duplicate dataset id found"
    required = {"id","name","scope","category","year","paper","links","language","domain","platform","modalities","tasks","access","last_checked"}
    for d in items:
        missing = sorted(required - set(d))
        assert not missing, f"{d.get('id','<unknown>')} missing fields: {missing}"

    df = flatten(items).sort_values(["year","name"], ascending=[False, True])
    (ROOT / "datasets").mkdir(exist_ok=True)
    (ROOT / "analysis").mkdir(exist_ok=True)
    df.to_csv(ROOT / "datasets" / "datasets.csv", index=False)

    c = counts(items)
    summary = {
        "dataset_count": len(items),
        "core_count": c["scope"].get("core", 0),
        "related_count": c["scope"].get("related", 0),
        "years": dict(sorted(c["year"].items())),
        "modalities": dict(sorted(c["modalities"].items(), key=lambda x: (-x[1], x[0]))),
        "languages": dict(sorted(c["languages"].items(), key=lambda x: (-x[1], x[0]))),
        "categories": dict(sorted(c["category"].items(), key=lambda x: (-x[1], x[0]))),
    }
    (ROOT / "analysis" / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    plot_bar(dict(sorted(c["year"].items())), "Datasets by publication year", "datasets_by_year.png")
    plot_bar(dict(sorted(c["modalities"].items(), key=lambda x: (-x[1], x[0]))), "Coverage by modality", "modalities.png", True)
    plot_bar(dict(sorted(c["scope"].items(), key=lambda x: (-x[1], x[0]))), "Catalog scope", "scope.png")
    plot_bar(dict(sorted(c["category"].items(), key=lambda x: (-x[1], x[0]))), "Dataset research categories", "categories.png", True)

if __name__ == "__main__":
    main()

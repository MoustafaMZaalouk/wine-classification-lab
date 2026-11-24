# Wine Classification Lab

[![CI](https://github.com/MoustafaMZaalouk/wine-classification-lab/workflows/Reproducible%20project%20checks/badge.svg)](https://github.com/MoustafaMZaalouk/wine-classification-lab/blob/main/.github/workflows/test.yml)

*Live workflow status, not a production-readiness or model-quality rating.*

Compare a majority baseline, scaled logistic regression and a random forest on a fixed stratified holdout.

A small educational project prepared with AI assistance for Moustafa Zaalouk's portfolio. This is new demonstration code, not a claim about past employment, research, clients or production deployment. It does not reuse another person's project under a different name.

## Run it

Use Python 3.10 or newer. The recorded local run used Python 3.10.12. A virtual environment is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python demo.py
python -m unittest -v
```

On Windows use `.venv\Scripts\activate` instead. The first command runs the full experiment and writes `results.json`. The second runs four checks. No API keys, paid services or internet data downloads are needed after dependency installation.

## Recorded results

These are small educational benchmarks, not evidence of real-world generalization. Perfect scores on this small evaluation are not a production accuracy claim.

![Recorded local result](results.png)

These values are generated from `results.json`, not estimated or copied. Rerun the code to check them. Minor numerical differences may occur across platforms. Full per-example or per-fold details, where applicable, are in the JSON file.

| Measure | Local result |
| --- | ---: |
| Forest: accuracy | 1.000000 |
| Forest: macro F1 | 1.000000 |
| Forest: train CV macro F1 | 0.985380 |
| Logistic: accuracy | 1.000000 |
| Logistic: macro F1 | 1.000000 |
| Logistic: train CV macro F1 | 0.977744 |
| Majority: accuracy | 0.400000 |
| Majority: macro F1 | 0.190476 |
| Majority: train CV macro F1 | 0.189906 |
| Seed | 42 |
| Test rows | 45 |
| Train rows | 133 |

`verification.txt` records the local test run. The included GitHub Actions workflow is a reproducible check, not a claim that remote CI has already passed.

## How to read the code

1. `demo.py`: data construction/loading, split, model, evaluation and output.
2. `test_demo.py`: output consistency and three experiment-specific checks.
3. `results.json`: the actual captured local results.
4. `requirements.txt`: exact versions used locally.

## Publishing and CI

The initial source is stored as a checksummed ZIP inside the workflow so GitHub can restore exact filenames and the chart without a manual multi-file upload. On its first run it unpacks this original AI-assisted source, tests it, runs the experiment and commits the initialized files as `github-actions[bot]`. Later runs test the actual checked-out source; they do not overwrite it from the bundle. This automation history is not a claim of manual authorship or review.

## Data and attribution

scikit-learn built-in Wine dataset, loaded through sklearn.datasets.load_wine. Dataset provenance and its upstream terms are documented by scikit-learn: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html. Dataset bytes are not redistributed in this repository.

The experiment uses NumPy, SciPy and scikit-learn rather than claiming to implement their estimators from scratch. Their licenses and dataset terms remain separate from this repository's MIT license. No upstream code, author name or license was removed.

## What this does not prove

A small, clean benchmark, not a wine production system. The single holdout is high-variance. Cross-validation uses training rows only; preprocessing is inside the pipeline. No hyperparameter search or deployment is claimed.

## شرح بالمصري

الفكرة: نقارن موديل بسيط بموديلين على بيانات أنواع النبيذ. التقسيم ثابت، والتوحيد بيتعلم من التدريب بس. افتح demo.py وشوف الفرق بين نتيجة التدريب المتقاطع ونتيجة الاختبار.

لما تشرح المشروع: قول مصدر الداتا، اتقسمت إزاي، إيه الـbaseline، بنقيس بإيه، وإيه حدود النتيجة. ما تقولش إنه شغال في production أو نتيجة على داتا حقيقية لو التجربة صناعية.

## Next experiment

Replace the demonstration data with an appropriately licensed dataset, define an independent evaluation protocol before tuning, and report failures as well as successes. Keep private data and credentials out of commits.

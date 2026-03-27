# K-Means Slider Visualizer

[Live Demo](https://tanveerkaur29-k-means-slider.hf.space/) (Hugging Face)


An interactive Gradio app to explore how K-Means clustering behaves as you change the number of clusters $K$.

The app generates a synthetic 2D dataset using `make_blobs`, fits a `KMeans` model, and updates a scatter plot in real time.

## Features

- Interactive slider to set cluster count from `1` to `10`
- Live clustering with `scikit-learn` K-Means
- Cluster centers highlighted as red `X` markers
- Simple UI powered by Gradio

## Requirements

- Python 3.9+
- Packages listed in `requirements.txt`:
	- `gradio`
	- `scikit-learn`
	- `matplotlib`
	- `numpy`

## How It Works

1. A fixed synthetic dataset is created with:

```python
X, _ = make_blobs(n_samples=200, centers=4, random_state=42)
```

2. When you move the slider, the app:
	 - trains `KMeans(n_clusters=K)` on `X`
	 - predicts cluster labels
	 - plots points colored by cluster
	 - overlays centroids in red

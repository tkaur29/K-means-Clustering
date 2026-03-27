import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=200, centers=4, random_state=42)

def cluster_data(k):
    kmeans = KMeans(n_clusters=int(k))
    kmeans.fit(X)

    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(centers[:, 0], centers[:, 1], color='red', marker='X', s=200)

    return plt

gr.Interface(
    fn=cluster_data,
    inputs=gr.Slider(1, 10, step=1, label="Number of Clusters (K)"),
    outputs="plot",
    title="K-Means Visualizer",
    description="Adjust K to see how clustering changes"
).launch()
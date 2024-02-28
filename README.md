# Covid-19 Detection using Deep Learning

## About
A Django based Web Application to detect the presence of [COVID-19](https://en.wikipedia.org/wiki/COVID-19) in Chest X-Ray Images. The Deep Learning models are trained on a publicly available dataset of ~21000 Chest X-Ray Images labelled as COVID-19 or Non-COVID or Normal. The models were trained separately on the dataset and the weightfiles were later loaded onto the Webapp to detect the presence of COVID-19

## Demo 
<p align="center">
  <img src="demo/First.png" alt="animated" />
</p>

<p align="center">
  <img src="demo/Last.png" alt="animated" />
</p>

## Model Performance

### CNN Architecture

- **Model Architecture**
<br>
<p align="center">
<img src ="https://user-images.githubusercontent.com/53687927/118810680-c8b25600-b8c9-11eb-9d98-35baa3f3f42e.png"></p>


### Dataset
- Dataset Link - [SARS-COV2-Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset)
  ```
  Soares, Eduardo, Angelov, Plamen, Biaso, Sarah, Higa Froes, Michele, and Kanda Abe, Daniel. "SARS-CoV-2 CT-scan dataset: A large dataset of real patients CT scans for SARS-     CoV-2 identification." medRxiv (2020). doi: https://doi.org/10.1101/2020.04.24.20078584.
  Angelov, P., & Soares, E. (2020). Towards explainable deep neural networks (xDNN). Neural Networks, 130, 185-194.
  ```
- Google Drive Folder : [Dataset] (https://drive.google.com/file/d/1K4xOdV6HHfmJvEfhSlgqqUfsILT9I701/view?usp=drive_link)
 

# Analysis of Climate Data and DNA Sequences with Hidden Markov Models HMM

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Ingridvasc/Portifolio/blob/main/LICENSE) 

# About the Project 👇🏼

The study of climate data is an essential tool for understanding the impacts of environmental change and predicting future patterns. Based on data provided by APAC (Pernambuco Water and Climate Agency), an analysis was carried out that combines real data from monitoring posts with a genetic simulation approach. This approach aims to better understand the relationships between different posts and identify hidden patterns that arise due to climate change. The main focus of this analysis is to demonstrate how weather events directly influence the relationships between the data of the stations, highlighting that every time a significant climate change occurred in the region, the resulting transition matrix was different from the behavior observed in the candlestick chart. This reinforces that external changes directly impact the dynamic relationships between the stations.

# 📋 Prerequisites

- [x] pip install numpy pandas matplotlib plotly hmmlearn requests 

# 🔧 Installation

Clone the repository:
- [x] git clone https://github.com/Ingridvasc/Analysis-of-Climate-Data-and-DNA-Sequences-with-Hidden-Markov-Models-HMM.git

Navigate to the project directory:
- [x] cd Analysis-of-Climate-Data-and-DNA-Sequences-with-Hidden-Markov-Models-HMM

Run the Python script:
- [x] python Analysis of Climate Data and DNA Sequences with Hidden Markov Models HMM.py


# 📦 Implementation


> Simulation of Genetic Sequences:
Genetic sequence simulation was used as an analogy to explore how external changes can impact underlying patterns in a system. Two phases of sequences were generated;

> Before climate change: Balanced genetic frequencies between nucleotides (A, C, G, T); 

> After climate change: Frequencies altered to favor specific mutations (A and C), simulating the impact of external events.
This approach demonstrated how a change in the environment can modify the observed frequencies and generate distinct transitions in the underlying patterns.

> 2023 Climate Data
Actual data provided by APAC regarding the Toritama station during the year 2023 were used:

> Monitored posts: Toritama, Agreste Pernambucano, Pernambuco, Brazil.

> Values for the months of 2023: Represent climatic variables, such as accumulated precipitation, measured for the station.
These values were enriched with additional data (open, high, low, and daily close) to build candlestick charts and study daily variations.

>	Transition Matrix Calculation
The transition matrix was calculated from the November values, with the objective of capturing the dynamic relationships between the stations:

>	Each element of the matrix represents the change between the values of two consecutive stations.

>	This matrix reflects probabilistic transitions and is sensitive to climate change.

>	Hidden Markov Model (HMM)
Based on the transition matrix and the observed data, the Hidden Markov Model was applied  to identify underlying states that are not directly observable in the data. Using the Viterbi algorithm, it was possible to:

>	Predict the most likely hidden states represented by the monitored posts.

>	Analyze how changes in states reflect climate change.

>	Candlestick Chart: Shows variations in the November values of each station, highlighting daily fluctuations.

> Transition Matrix: Presented as a heat map, it visually identifies how stations interact in terms of dynamic transitions.

# ⚙️ Running the Project
![image](https://github.com/user-attachments/assets/5cf01e06-ac3b-4cf8-8d80-dfe5733fbbf0)

![image](https://github.com/user-attachments/assets/16924ad9-24c4-466b-a12f-7d3e4a4853c6)

![image](https://github.com/user-attachments/assets/95a3e2ef-f73b-4109-a57e-ba29a0e8cfed)

![image](https://github.com/user-attachments/assets/a4d56445-3806-4ae2-82c8-92d4297549eb)

# 📌 Version 
2.0 


## Technologies used 🌐

⇨ Python
  
# Autor ✏️

Ingrid Vasconcelos

import pandas as pd 
import numpy as np 
import streamlit as st 

df = pd.read_csv("Goals_Predictor(Sheet1).csv")
data = df[["Season", "DateTime", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]]

st.write("Welcome to the EPL Goal Predictor")


st.write(data)
# Recall: Key feature of a poisson distribution: Mean ~ Variance
# Recall: Key feature of Negative Binomial Distribution: Variance > Mean 

team = st.text_input("Enter an EPL team's name:")


home_goals = df[df["HomeTeam"] == team]["FTHG"]
away_goals = df[df["AwayTeam"] == team]["FTAG"]

goals = pd.concat([home_goals, away_goals])

print(goals)

mean_goals = goals.mean()
variance_goals = goals.var()

print("Mean:", mean_goals)
print("Variance:", variance_goals)

from scipy.stats import poisson
from scipy.stats import nbinom

# Use Poisson Distribution if Mean ~ Variance

probabilities = []

if 0.9 <= variance_goals / mean_goals <= 1.1:

    st.write("Best fit: Poisson Distribution")

    for i in range(6):
        prob = 100 * poisson.pmf(i, mean_goals)

        probabilities.append(prob)

        st.write(f"P(X={i}) = {100 * poisson.pmf(i, mean_goals)}%")

elif variance_goals / mean_goals > 1.1:

    st.write("Best fit: Negative Binomial Distribution")

    r = mean_goals**2 / (variance_goals - mean_goals)
    p = mean_goals / variance_goals

    for i in range(6):
        prob = 100 * nbinom.pmf(i, r, p)

        probabilities.append(prob)

        st.write(f"P(X={i}) = {100 * poisson.pmf(i, mean_goals)}%")

else:

    st.write("Neither Poisson nor Negative Binomial are a good fit")

if len(probabilities) > 0:

    chart = pd.DataFrame({
        "Goals": [0, 1, 2, 3, 4, 5],
        "Probability": probabilities
    })

    st.bar_chart(chart.set_index("Goals"))
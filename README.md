Takes match data from EPL games and predicts probability of a team scoring a number of goals (0 to 5) using either Negative Binomial or Poisson Distribution 

Distribution Selection Logic: 
Uses Poisson Distribution when Mean ~ Variance 
Uses Negative Binomial Distribution when Variance > Mean 

Streamlit for UI, visualizes results through interactive dashboard 


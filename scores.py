import pandas as pd
data = pd.DataFrame({
    "Hours":[1,2,3,4,5,6],
    "Scores":[52,57,65,70,75,80]
})
data.to_csv("Scores.csv")
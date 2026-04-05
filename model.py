import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample training data: hours -> pass (1) or fail (0)
X = np.array([[2], [3], [5], [8]])
y = np.array([0, 0, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved!")

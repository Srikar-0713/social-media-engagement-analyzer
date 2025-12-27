import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("social_media_data.csv")

print("Social Media Engagement Data:")
print(data)

plt.figure()
plt.bar(data["Post"], data["Likes"])
plt.xlabel("Post")
plt.ylabel("Likes")
plt.title("Likes per Post")
plt.show()

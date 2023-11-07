import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter: ")
df = pd.read_csv(file)

delays = df["Delayed"].tolist()
cancs = df["Cancelled"].tolist()

def Average(lst):
    return sum(lst) / len(lst)

avg_delays = Average(delays)
avg_cancs = Average(cancs)

# TODO: Print the average of flight delays and flight cancellations
print("Average delays: ", end="")
print(f"{avg_delays:.2f}")
print("Average cancellations: ", end="")
print(f"{avg_cancs:.2f}")

plt.plot(df["Month"], df["Delayed"], label="Delays")
plt.plot(df["Month"], df["Cancelled"], label="Cancellations")
plt.title("Flight Status at LAX")
plt.xlabel("Months")
plt.ylabel("Number of Flights")
plt.legend(loc="upper right")
plt.savefig('output_fig.png')

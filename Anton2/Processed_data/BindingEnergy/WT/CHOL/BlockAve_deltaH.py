import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.linewidth']=1.5
plt.rcParams['lines.linewidth']=1.5


filename = "CBE1720/IE_NORMAL_PB_Delta_TOTAL.csv"
nblocks = 6

# Read data
df = pd.read_csv(filename)

frames = df["Frames"].to_numpy()
deltaH = df["TOTAL"].to_numpy()

# Split indices into approximately equal blocks
blocks = np.array_split(np.arange(len(deltaH)), nblocks)

results = []

for i, idx in enumerate(blocks):

    values = deltaH[idx]

    mean = np.mean(values)
    std = np.std(values, ddof=1)
    sem = std / np.sqrt(len(values))

    start_frame = frames[idx[0]]
    end_frame = frames[idx[-1]]

    results.append([
        i + 1,
        start_frame,
        end_frame,
        len(values),
        mean,
        std,
        sem
    ])

# Convert to dataframe
results = pd.DataFrame(
    results,
    columns=[
        "Block",
        "Start_frame",
        "End_frame",
        "N",
        "Mean_deltaH",
        "STD",
        "SEM"
    ]
)
results['Time']=1700+results['Block']*50-25
print(results)

# Save results
results.to_csv("DeltaH_block_average.csv", index=False)

# Plot block averages
plt.errorbar(
    results["Time"],
    results["Mean_deltaH"],
    yerr=results["STD"],
    fmt="o",
    capsize=5
)
# raw data 
start_time=1700
end_time=2000

time=np.linspace(start_time, end_time, len(deltaH))


plt.plot(time,deltaH, color='green', alpha=0.5,label=r"$\Delta H$")
plt.plot(results["Time"],results["Mean_deltaH"], color='black', label='Block Average')
plt.xlabel("Time",fontsize=15)
plt.ylabel(r"$\Delta H$ (kcal/mol)", fontsize=15)
plt.xticks(results["Time"])

plt.xlim(1700,2000)
plt.ylim(0,-250)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig("DeltaH_block_average.png", dpi=300)

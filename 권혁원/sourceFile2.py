import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

df = pd.read_csv('thesis_link.csv')
# print(len(df['논문제목'].unique()))
# print(len(df['링크'].unique()))

years = df['연도'].unique()
# print(sorted(years))

num_of_thesis = {}
for year in sorted(years):
    yearDF = df[df['연도'] == year]
    num_of_thesis[year] = yearDF.shape[0]

# colorList = ['mediumslateblue', 'mediumpurple', 'rebeccapurple', 'blueviolet',
#              'indigo', 'darkorchid', 'darkviolet', 'mediumorchid',
#              'thistle', 'plum', 'violet', 'purple',
#              'darkmagenta', 'm', 'magenta', 'fuchsia', 'orchid',
#              'mediumvioletred', 'deeppink', 'hotpink',
#              'palevioletred', 'crimson', 'pink', 'lightpink']

plt.figure(figsize=(12,6))
plt.bar(num_of_thesis.keys(), num_of_thesis.values(), color='darkcyan', width=0.75)
plt.title('연도별 논문 출판량', fontsize=18)
plt.xticks(list(num_of_thesis.keys()), rotation=45)
plt.xlabel('연도', fontsize=12)
plt.ylabel('출판량', fontsize=12)
plt.grid(axis='y', alpha=0.35)
plt.tight_layout()
plt.show()

# colorIDX = 0
# plt.figure(figsize=(12,4))
# for k, v in num_of_thesis.items():
#     if k % 2:
#         color_='darkviolet'
#     else:
#         color_='violet'
#     plt.bar(k, v, color=color_)
#     colorIDX += 1
# plt.title('연도별 논문 출판량')
# plt.xticks(list(num_of_thesis.keys()), rotation=45)
# plt.xlabel('연도', fontsize=12)
# plt.ylabel('출판량', fontsize=12)
# plt.grid(alpha=0.35)
# plt.tight_layout()
# plt.show()
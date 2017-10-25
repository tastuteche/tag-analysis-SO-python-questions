import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

b_dir = '../pythonquestions/'
questions_df = pd.read_csv(b_dir + "Questions.csv", encoding='latin1')
tags_df = pd.read_csv(b_dir + "Tags.csv", encoding='latin1')

# 2008-08-02T15:11:16Z
questions_df['Date'] = pd.to_datetime(
    questions_df['CreationDate'], format='%Y-%m-%dT%H:%M:%SZ')
questions_df['year'] = questions_df['Date'].dt.year
questions_df['year'] = questions_df['year'].astype('int')

questions_id_date = questions_df[['Id', 'year', 'Score']]

questions_date_tag = pd.merge(questions_id_date, tags_df, how='inner', on='Id')

pop_tags = pd.DataFrame(questions_date_tag['Tag'].value_counts()).reset_index()
pop_tags.columns = ['Tag', 'questions']
top_num = 20
pop_tags.head(top_num)

plt.figure(figsize=(15, 5))
sns.barplot(x='Tag', y='questions', data=pop_tags.head(top_num))
# plt.show()
plt.savefig('pop_tags.png', dpi=200)
plt.clf()
plt.cla()
plt.close()

pop_tag_questions = questions_date_tag[(questions_date_tag['Tag'].isin(
    pop_tags.head(top_num)['Tag'])) & (questions_date_tag['Tag'] != 'python')]


tags = list(pop_tags.head(top_num)['Tag'])
tags.remove('python')
ctab = pd.crosstab([pop_tag_questions['year']], pop_tag_questions['Tag']).apply(
    lambda x: x / x.sum(), axis=1)
ctab[tags].plot(kind='bar', stacked=True, colormap='rainbow', figsize=(
    12, 8)).legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.show()
plt.savefig('pop_tag_questions_bar.png', dpi=200)
plt.clf()
plt.cla()
plt.close()


ctab[tags].plot(kind='line', stacked=False, colormap='rainbow', figsize=(
    12, 8)).legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.show()
plt.savefig('pop_tag_questions_line.png', dpi=200)
plt.clf()
plt.cla()
plt.close()


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 8))
sns.boxplot(x='Tag', y='Score', data=pop_tag_questions, palette="muted", ax=ax)
ax.set_ylim([0, 10])
# plt.show()
plt.savefig('pop_tag_questions_box.png', dpi=200)
plt.clf()
plt.cla()
plt.close()

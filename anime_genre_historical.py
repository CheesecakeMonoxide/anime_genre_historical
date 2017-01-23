import pandas as pd
import matplotlib.pyplot as plt 

def per_season_chart(df):
    y = 0
    genre_list = []
    while y < 5:
        for x in range(len(df.loc[0])):
            if df[x][y] != None:
                for item in df[x][y]['anime']['genres']:
                    genre_list.append(item)
        y += 1


    action = 0
    adventure = 0
    ecchi = 0
    romance = 0
    supernatural = 0
    mecha = 0
    sci_fi = 0
    comedy = 0
    slice_of_life = 0
    drama = 0
    mystery = 0
    psychological = 0
    fantasy = 0
    sports= 0
    mahou_shoujo = 0
    music = 0
    horror = 0
    thriller = 0

    for genre in genre_list:
        if genre == 'Action':
            action += 1
        if genre == 'Ecchi':
            ecchi += 1
        if genre == 'Romance':
            romance += 1
        if genre == 'Supernatural':
            supernatural += 1
        if genre == 'Mecha':
            mecha += 1
        if genre == 'Sci-Fi':
            sci_fi += 1
        if genre == 'Comedy':
            comedy += 1
        if genre == 'Slice of Life':
            slice_of_life += 1
        if genre == 'Drama':
            drama += 1
        if genre == 'Mystery':
            mystery += 1
        if genre == 'Psychological':
            psychological += 1
        if genre == 'Adventure':
            adventure += 1
        if genre == 'Fantasy':
            fantasy += 1
        if genre == 'Sports':
            sports += 1
        if genre == 'Mahou Shoujo':
            mahou_shoujo += 1
        if genre == 'Music':
            music += 1
        if genre == 'Horror':
            horror += 1
        if genre == 'Thriller':
            thriller += 1

    genre_df = pd.DataFrame({'Genre': ['Action','Ecchi','Romance','Supernatural','Mecha',
                                       'Sci-Fi','Comedy','Slice of Life','Drama','Mystery',
                                       'Psychological','Adventure','Fantasy', 'Sports',
                                       'Mahou Shoujo','Music','Horror','Thriller'],
                             'Count': [action, ecchi, romance, supernatural, mecha, sci_fi,
                                       comedy, slice_of_life, drama, mystery, psychological,
                                       adventure, fantasy, sports, mahou_shoujo, music,
                                       horror,thriller]})

    return genre_df
    ##print(genre_df.set_index('Genre'))

def y_gen(lst, genre_name, df_name):
    emp = []
    for season in lst:
        emp.append(df_name[season][genre_name])
    return emp


def final_df_per_season(year):
    ##while True:
    ##    if year.isdecimal() and int(year) >= 1995 and int(year) <= 2016:
    link_1 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "1"
    link_2 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "2"
    link_3 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "3"
    link_4 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "4"
    ##        break
    ##    else:
    ##        print('Please type a valid year from 1995 to 2016')
    ##        year = input()


    dframe1 = pd.read_json(link_1)
    df1 = per_season_chart(dframe1)

    dframe2 = pd.read_json(link_2)
    df2 = per_season_chart(dframe2)

    dframe3 = pd.read_json(link_3)
    df3 = per_season_chart(dframe3)

    dframe4 = pd.read_json(link_4)
    df4 = per_season_chart(dframe4)

    merged = df1.merge(df2, on='Genre').merge(df3, on='Genre').merge(df4, on='Genre')

    final_df = merged.set_index('Genre')

    final_df.columns = ['Winter', 'Spring', 'Summer', 'Fall']
    
    ##print(final_df['Winter']['Action'])
    ##print(final_df['Spring']['Action'])
    return final_df


def yearly_df(season_output):
    x_columns = ['Winter', 'Spring', 'Summer', 'Fall']
    rowsum_Action = sum(y_gen(x_columns, 'Action', season_output))
    rowsum_Ecchi = sum(y_gen(x_columns, 'Ecchi', season_output))
    rowsum_Romance = sum(y_gen(x_columns, 'Romance', season_output))
    rowsum_Supernatural = sum(y_gen(x_columns, 'Supernatural', season_output))
    rowsum_Mecha = sum(y_gen(x_columns, 'Mecha', season_output))
    rowsum_Sci_Fi = sum(y_gen(x_columns, 'Sci-Fi', season_output))
    rowsum_Comedy = sum(y_gen(x_columns, 'Comedy', season_output))
    rowsum_Slice_of_Life = sum(y_gen(x_columns, 'Slice of Life', season_output))
    rowsum_Drama = sum(y_gen(x_columns, 'Drama', season_output))
    rowsum_Mystery = sum(y_gen(x_columns, 'Mystery', season_output))
    rowsum_Psychological = sum(y_gen(x_columns, 'Psychological', season_output))
    rowsum_Adventure = sum(y_gen(x_columns, 'Adventure', season_output))
    rowsum_Fantasy = sum(y_gen(x_columns, 'Fantasy', season_output))
    rowsum_Sports = sum(y_gen(x_columns, 'Sports', season_output))
    rowsum_Mahou_Shoujo = sum(y_gen(x_columns, 'Mahou Shoujo', season_output))
    rowsum_Music = sum(y_gen(x_columns, 'Music', season_output))
    rowsum_Horror = sum(y_gen(x_columns, 'Horror', season_output))
    rowsum_Thriller = sum(y_gen(x_columns, 'Thriller', season_output))
    season_output_df = pd.DataFrame({'Genre': ['Action','Ecchi','Romance','Supernatural','Mecha',
                                           'Sci-Fi','Comedy','Slice of Life','Drama','Mystery',
                                           'Psychological','Adventure','Fantasy', 'Sports',
                                           'Mahou Shoujo','Music','Horror','Thriller'],
                               'Count': [rowsum_Action, rowsum_Ecchi, rowsum_Romance,
                                          rowsum_Supernatural, rowsum_Mecha, rowsum_Sci_Fi,
                                          rowsum_Comedy, rowsum_Slice_of_Life, rowsum_Drama,
                                          rowsum_Mystery, rowsum_Psychological, rowsum_Adventure,
                                          rowsum_Fantasy, rowsum_Sports, rowsum_Mahou_Shoujo,
                                          rowsum_Music, rowsum_Horror, rowsum_Thriller]})
    return season_output_df

                                         

print('Hello! I will help you analyze trends in different anime genre in a given year.')
print('Pick a year from 1995 to 2016, type it below and I will show you the graph for it.')

num1 = input()
output1 = pd.DataFrame(final_df_per_season(num1))
yearoutput_df = pd.DataFrame(yearly_df(output1))
print(yearoutput_df)
columns = [num1]
while True:
    print('Type the succeeding year you want to compare this graph to. (You can break this loop without error if you enter nothing in the NEXT iteration.)')
    num2 = input()
    if num2 == '':
        break
    else:        
        output2 = pd.DataFrame(final_df_per_season(num2))
        output2_df = pd.DataFrame(yearly_df(output2))
        print(output2_df)
        yearoutput_df = yearoutput_df.merge(output2_df, on='Genre')
        yearoutput_df = pd.DataFrame(yearoutput_df)
        columns.append(num2)

yearoutput_df.set_index('Genre', inplace=True)
yearoutput_df.columns = columns
print(yearoutput_df)


diff_genres = ['Action','Ecchi','Romance','Supernatural','Mecha',
           'Sci-Fi','Comedy','Slice of Life','Drama','Mystery',
           'Psychological','Adventure','Fantasy', 'Sports',
           'Mahou Shoujo','Music','Horror','Thriller']

#begin constructing chart

x_columns = columns

row_Action = y_gen(x_columns, 'Action', yearoutput_df)
row_Ecchi = y_gen(x_columns, 'Ecchi', yearoutput_df)
row_Romance = y_gen(x_columns, 'Romance', yearoutput_df)
row_Supernatural = y_gen(x_columns, 'Supernatural', yearoutput_df)
row_Mecha = y_gen(x_columns, 'Mecha', yearoutput_df)
row_Sci_Fi = y_gen(x_columns, 'Sci-Fi', yearoutput_df)
row_Comedy = y_gen(x_columns, 'Comedy', yearoutput_df)
row_Slice_of_Life = y_gen(x_columns, 'Slice of Life', yearoutput_df)
row_Drama = y_gen(x_columns, 'Drama', yearoutput_df)
row_Mystery = y_gen(x_columns, 'Mystery', yearoutput_df)
row_Psychological = y_gen(x_columns, 'Psychological', yearoutput_df)
row_Adventure = y_gen(x_columns, 'Adventure', yearoutput_df)
row_Fantasy = y_gen(x_columns, 'Fantasy', yearoutput_df)
row_Sports = y_gen(x_columns, 'Sports', yearoutput_df)
row_Mahou_Shoujo = y_gen(x_columns, 'Mahou Shoujo', yearoutput_df)
row_Music = y_gen(x_columns, 'Music', yearoutput_df)
row_Horror = y_gen(x_columns, 'Horror', yearoutput_df)
row_Thriller = y_gen(x_columns, 'Thriller', yearoutput_df)

plt.plot(x_columns,row_Action,label='Action')
plt.plot(x_columns,row_Ecchi,label='Ecchi')
plt.plot(x_columns,row_Romance,label='Romance')
plt.plot(x_columns,row_Supernatural,label='Supernatural')
plt.plot(x_columns,row_Mecha,label='Mecha')
plt.plot(x_columns,row_Sci_Fi,label='Sci-Fi')
plt.plot(x_columns,row_Comedy,label='Comedy')
plt.plot(x_columns,row_Slice_of_Life,label='Slice of Life')
plt.plot(x_columns,row_Drama,label='Drama')
plt.plot(x_columns,row_Mystery,label='Mystery')
plt.plot(x_columns,row_Psychological,label='Psychological')
plt.plot(x_columns,row_Adventure,label='Adventure')
plt.plot(x_columns,row_Fantasy,label='Fantasy')
plt.plot(x_columns,row_Sports,label='Sports')
plt.plot(x_columns,row_Mahou_Shoujo,label='Mahou Shoujo')
plt.plot(x_columns,row_Music,label='Music')
plt.plot(x_columns,row_Horror,label='Horror')
plt.plot(x_columns,row_Thriller,label='Thriller')

ticks = []
for x in x_columns:
    ticks.append(int(x))
plt.xticks(ticks)
plt.xlabel('Season Released')
plt.ylabel('Number of Anime per Genre')
plt.title('Anime Genre Trend for the year ' + x_columns[0] + ' until ' + x_columns[-1])
plt.legend()
plt.show()



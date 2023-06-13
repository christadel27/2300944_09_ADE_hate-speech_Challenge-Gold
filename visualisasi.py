import pandas as pd
import re
# Membaca file CSV
df = pd.read_csv('csv_data/data_sesuai.csv')

# Menampilkan beberapa baris pertama data
print(df.head())

# Membersihkan data
# Menghapus komentar duplikat
df = df.drop_duplicates(subset='Tweet')

# Membuat kolom baru 'Panjang_Karakter'
df['Panjang_Karakter'] = df['Tweet'].apply(lambda x: len(str(x)))
df['Jumlah_kata'] = df['Tweet'].apply(lambda x: len(x.split(' ')))
df['Jumlah_kata_sensor'] = df['Tweet'].apply(lambda text: len(re.findall("[***]", text)))
df_filtered = df[['Tweet', 'Panjang_Karakter', 'Jumlah_kata','Jumlah_kata_sensor']]

# Menampilkan DataFrame dengan kolom baru
print(df_filtered.head())

# Menghitung mean (rata-rata) panjang karakter
mean_panjang_karakter = df['Tweet'].str.len().mean()
mean_jumlah_kata = df['Tweet'].apply(lambda x: len(str(x).split())).mean()
print("Mean Panjang Karakter:", mean_panjang_karakter)
print("Mean jumlah kata:", mean_jumlah_kata)

# Menghitung modus (nilai yang paling sering muncul) panjang karakter
mode_panjang_karakter = df['Tweet'].str.len().mode().values
mode_jumlah_kata = df['Tweet'].apply(lambda x: len(str(x).split())).mode().values
print("Modus Panjang Karakter:", mode_panjang_karakter)
print("Modus jumlah kata:", mode_jumlah_kata)
# Menghitung median (nilai tengah) panjang karakter
median_panjang_karakter = df['Tweet'].str.len().median()
median_jumlah_kata = df['Tweet'].apply(lambda x: len(str(x).split())).median()
print("Median Panjang Karakter:", median_panjang_karakter)
print("Median Jumlah Kata:", median_jumlah_kata)
# menghitung Range
jumlah_word_max = df['Tweet'].apply(lambda x: len(x.split(' '))).max()
jumlah_word_min = df['Tweet'].apply(lambda x: len(x.split(' '))).min()
jumlah_karakter_max = df['Tweet'].str.len().max()
jumah_karakter_min = df['Tweet'].str.len().min()
range_word = jumlah_word_max - jumlah_word_min
range_karakter = jumlah_karakter_max - jumah_karakter_min
print('Range Word :', range_word)
print('Range Karakter :', range_karakter)
# Quartile
Q1_panjang_karakter = df['Panjang_Karakter'].quantile(0.25)
Q2_panjang_karater = df['Panjang_Karakter'].quantile(0.5)
Q3_panjang_karakter = df['Panjang_Karakter'].quantile(0.75)
Q1_jumlah_kata = df['Jumlah_kata'].quantile(0.25)
Q2_jumlah_kata = df['Jumlah_kata'].quantile(0.5)
Q3_jumlah_kata = df['Jumlah_kata'].quantile(0.75)
IQR_karakter = Q3_panjang_karakter - Q1_panjang_karakter
IQR_kata = Q3_jumlah_kata - Q1_jumlah_kata
print('Q1 :', Q1_panjang_karakter, 'Q2 :', Q2_panjang_karater, 'Q3 :', Q3_panjang_karakter)
print ('Total IQR Karakter:', IQR_karakter)
print ('Total IQR Kata :', IQR_kata)
# variance
variance_karakter = df['Panjang_Karakter'].var()
variance_kata = df['Jumlah_kata'].var()
print("nilai variance karakter :", variance_karakter, "nilai variance kata :", variance_kata)
# Skewness
skewness_karakter = df['Panjang_Karakter'].skew()
skewness_kata = df['Jumlah_kata'].skew()
print("nilai skewness karakter :", skewness_karakter, "dan nilai skewness kata :", skewness_kata)
# Kurtosis
kurtosis_karakter = df['Panjang_Karakter'].kurtosis()
kurtosis_kata = df['Jumlah_kata'].kurtosis()
print("nilai kurtosis karakter :", kurtosis_karakter, "dan nilai kurtosis kata :", kurtosis_kata)


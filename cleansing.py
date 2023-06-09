""" 
Function untuk membersihkan data text
"""
import re
import pandas as pd
from db import get_abusive_data, get_alay_data, create_connection

def text_cleansing(text):
    # Bersihkan tanda baca (selain huruf dan angka)
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # yg lain
    clean_text = clean_text.lower()
    # abusive
    conn = create_connection()
    df_abusive = get_abusive_data(conn)
    abusive_words = df_abusive['word'].tolist()
    for word in abusive_words:
        clean_text = clean_text.replace(word, '***')
    # menggantikan kata sesuai data csv pembeaharuan 1
    conn = create_connection()
    df_alay = get_alay_data(conn)
    replacement_words = dict(zip(df_alay['alay_word'], df_alay['formal_word']))
    for word in replacement_words:
        clean_text = clean_text.replace(word, replacement_words.get(word, word))
    return clean_text

def cleansing_files(file_upload):
    # read csv file upload, jika eror dengan metode biasa
    try:
        df_upload = pd.read_csv(file_upload)
    except:
        df_upload = pd.read_csv(file_upload, encoding="latin-1")
    print("Read dataframe from upload success!")
    # ambil hanya kolom pertama saja
    df_upload = pd.DataFrame(df_upload.iloc[:,[0]])
    # rename kolom menjadi "raw_text"
    df_upload.columns = ["raw_text"]
    # bersihkan teks menggunakan fungsi cleansing
    # simpan di kolom "clean_text"
    df_upload["clean_text"] = df_upload["raw_text"].apply(text_cleansing)
    # mensensor kata abusive sesuai dari data dalam bentuk csv
    
    print("Cleansing text succes!")
    return df_upload
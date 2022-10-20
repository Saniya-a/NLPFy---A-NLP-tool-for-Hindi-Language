# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import nltk
nltk.download('indian')
nltk.download('punkt')

import codecs
from deep_translator import GoogleTranslator

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import tnt
from nltk.corpus import indian 
sw = 'अंदर', 'अत', 'अदि', 'अप', 'अपना', 'अपनि', 'अपनी', 'अपने', 'अभि', 'अभी', 'आदि', 'आप', 'इंहिं', 'इंहें', 'इंहों', 'इतयादि', 'इत्यादि', 'इन', 'इनका', 'इन्हीं', 'इन्हें', 'इन्हों', 'इस', 'इसका', 'इसकि', 'इसकी', 'इसके', 'इसमें', 'इसि', 'इसी', 'इसे', 'उंहिं', 'उंहें', 'उंहों', 'उन', 'उनका', 'उनकि', 'उनकी', 'उनके', 'उनको', 'उन्हीं', 'उन्हें', 'उन्हों', 'उस', 'उसके', 'उसि', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'एसे', 'ऐसे', 'ओर', 'और', 'कइ', 'कई', 'कर', 'करता', 'करते', 'करना', 'करने', 'करें', 'कहते', 'कहा', 'का', 'काफि', 'काफ़ी', 'कि', 'किंहें', 'किंहों', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर', 'किस', 'किसि', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', 'को', 'कोइ', 'कोई', 'कोन', 'कोनसा', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जहां', 'जा', 'जिंहें', 'जिंहों', 'जितना', 'जिधर', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', 'जेसा', 'जेसे', 'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिंहें', 'तिंहों', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थि', 'थी', 'थे', 'दबारा', 'दवारा', 'दिया', 'दुसरा', 'दुसरे', 'दूसरे', 'दो', 'द्वारा', 'न', 'नहिं', 'नहीं', 'ना', 'निचे', 'निहायत', 'नीचे', 'ने', 'पर', 'पहले', 'पुरा', 'पूरा', 'पे', 'फिर', 'बनि', 'बनी', 'बहि', 'बही', 'बहुत', 'बाद', 'बाला', 'बिलकुल', 'भि', 'भितर', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यहां', 'यहि', 'यही', 'या', 'यिह', 'ये', 'रखें', 'रवासा', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वगेरह', 'वरग', 'वर्ग', 'वह', 'वहाँ', 'वहां', 'वहिं', 'वहीं', 'वाले', 'वुह', 'वे', 'वग़ैरह', 'संग', 'सकता', 'सकते', 'सबसे', 'सभि', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'हि', 'ही', 'हुअ', 'हुआ', 'हुइ', 'हुई', 'हुए', 'हे', 'हें', 'है', 'हैं', 'हो', 'होता', 'होति', 'होती', 'होते', 'होना', 'होने'


# NLP Packages
from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_sm')
 
 # Structure and Layout
window = Tk()
window.title("NLPIFy POC")
window.geometry("900x500")
window.config(background='black')

# TAB LAYOUT
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text='NLPFy')
tab_control.add(tab2, text='File Processer')

label1 = Label(tab1, text= 'NLP Made Simple',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
label2.grid(column=0, row=0)


tab_control.pack(expand=1, fill='both')



# Functions FOR NLP  FOR TAB ONE
def get_filtered_text():
	raw_text = str(raw_entry.get())
	new_text = word_tokenize(raw_text)
	final_text = []
	for w in new_text:
		if w not in sw:
			final_text.append(w)
	result = '\nFiltered Text:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

def get_pos_tags():
	raw_text = str(raw_entry.get())
	new_text = hindi_model()
	final_text = (new_text.tag(nltk.word_tokenize(raw_text)))
	result = '\nPOS of Speech : {}'.format(final_text)
	tab1_display.insert(tk.END,result)


def get_sentiment():
	raw_text = str(raw_entry.get())
	text = GoogleTranslator(source='auto', target='en').translate(raw_text)
	new_text = TextBlob(text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab1_display.insert(tk.END,result)

def get_tokens():
	raw_text = str(raw_entry.get())
	final_text = word_tokenize(raw_text)
	result = '\nTokens:{}'.format(final_text)
	tab1_display.insert(tk.END,result)



# Clear entry widget
def clear_entry_text():
	entry1.delete(0,END)

def clear_display_result():
	tab1_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_result():
	tab2_display_text.delete('1.0',END)

# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
	file1 = tk.filedialog.askopenfilename()
	with open(file1,'r',encoding='utf8') as file:
		read_text = file.read()
		file.close()
	displayed_file.insert(tk.END,read_text)


def get_file_tokens():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = word_tokenize(raw_text)
	result = '\nTokens:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_pos_tags():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = hindi_model()
	final_text = (new_text.tag(nltk.word_tokenize(raw_text)))
	result = '\nPOS of Speech : {}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_sentiment():
	raw_text = displayed_file.get('1.0',tk.END)
	text = GoogleTranslator(source='auto', target='en').translate(raw_text)
	new_text = TextBlob(text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab2_display_text.insert(tk.END,result)

def get_file_filter():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = word_tokenize(raw_text)
	final_text = []
	for w in new_text:
		if w not in sw:
			final_text.append(w)
	result = '\nFiltered Text:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)




# MAIN NLP TAB
l1=Label(tab1,text="Enter Text To Analysis")
l1.grid(row=1,column=0)


raw_entry=StringVar()
entry1=Entry(tab1,textvariable=raw_entry,width=110)
entry1.grid(row=1,column=1)

# bUTTONS
button1=Button(tab1,text="Tokenize", width=12,command=get_tokens,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Filter", width=12,command=get_filtered_text,bg='#80d8ff')
button2.grid(row=5,column=0)


button3=Button(tab1,text="POS Tags", width=12,command=get_pos_tags,bg='#BB86FC')
button3.grid(row=4,column=1)


button4=Button(tab1,text="Sentiment", width=12,command=get_sentiment,bg='#f44336',fg='#fff')
button4.grid(row=4,column=2)


button5=Button(tab1,text="Reset", width=12,command=clear_entry_text,bg="#b9f6ca")
button5.grid(row=5,column=1)

button6=Button(tab1,text="Clear Result", width=12,command=clear_display_result)
button6.grid(row=5,column=2)

# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7,column=0, columnspan=5,padx=5,pady=5)

# Allows you to edit
tab1_display.config(state=NORMAL)




# FILE READING  AND PROCESSING TAB
l1=Label(tab2,text="Open File To Process")
l1.grid(row=1,column=1)


displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=4,padx=5,pady=3)


# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#b9f6ca")
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="Tokenize", width=12,command=get_file_tokens,bg='#03A9F4',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)


b3=Button(tab2,text="POS Tags", width=12,command=get_file_pos_tags,bg='#BB86FC')
b3.grid(row=4,column=0,padx=10,pady=10)


b4=Button(tab2,text="Sentiment", width=12,command=get_file_sentiment,bg='#f44336',fg='#fff')
b4.grid(row=4,column=1,padx=10,pady=10)


b5=Button(tab2,text="Filter", width=12,command=get_file_filter,bg='#80d8ff')
b5.grid(row=4,column=2,padx=10,pady=10)


b6=Button(tab2,text="Clear Result", width=12,command=clear_result)
b6.grid(row=5,column=0,padx=10,pady=10)

b7=Button(tab2,text="Close", width=12,command=window.destroy)
b7.grid(row=5,column=1,padx=10,pady=10)

# Display Screen

# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=4,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

window.mainloop()




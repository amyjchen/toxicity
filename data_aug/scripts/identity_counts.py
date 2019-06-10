import csv
import sys
import pandas as pd 

filename = sys.argv[1]

df = pd.read_csv(filename + '.csv')

identity_labels = ['asian', 
    'atheist',  
    'black',  
    'christian', 
    'female', 
    'heterosexual', 
    'homosexual_gay_or_lesbian', 
    'jewish', 
    'latino', 
    'male', 
    'muslim', 
    'psychiatric_or_mental_illness', 
    'transgender', 
    'white']

asian_kws = ['asia', 'chinese', 'china', 'korea', 'japan', 'hmong', 'viet', 'cambod', 'india', 'malay', 'filipin', 'thai', 'singapore', 'chink', 'jap', 'gook', 'of color']
black_kws = ['black', 'africa', 'afro', 'nig', 'zulu', 'kenya', 'cameroon', 'nigeria', 'of color', 'brown', 'n-word', 'n****r', 'negro']
buddhist_kws = ['buddhist', 'monk' , 'zen']
christian_kws = ['christian', 'christ ', 'catholic', 'presbyt', 'church', 'preacher', 'priest']
female_kws = ['woman', 'female', 'femme', 'girl', 'lady', 'women', 'mother', 'wife']
heterosexual_kws = ['straight', 'heterosexual', 'hetero']
homosexual_gay_or_lesbian_kws = ['homo', 'gay', 'lesbian', 'queer', 'lgb', 'fag']
jewish_kws = ['jewish', 'jew']
latino_kws = ['latino', 'hispanic', 'mexican','latin', 'central america', 'chicano', 'of color', 'brown']
male_kws = [' man ', ' male', 'masculine', 'boy', 'gentleman', ' men ', 'father', 'husband']
muslim_kws = ['muslim', 'islam', 'hijab', 'mecca', 'jihad', 'terror']
psychiatric_or_mental_illness_kws = ['depress', 'bipolar', 'narciss', 'anxiet', 'adhd']
transgender_kws = [' trans ', 'transgender', 'ladyboy', 'mtf', 'ftm']
white_kws = ['white', 'cracker']

df['comment_text'] = df['comment_text'].str.lower()
print 'TOTAL', len(df)
print 'asian'
print len(df[df['comment_text'].str.contains('asia|chinese|china|korea|japan|hmong|viet|cambod|india|malay|filipin|thai|singapore|chink|jap|gook')])
print 'atheist'
print len(df[df['comment_text'].str.contains('atheist')])
print 'black'
print len(df[df['comment_text'].str.contains('black|africa|afro|nig|zulu|kenya|cameroon|nigeria|of color|brown|n-word|n\*\*\*\*r|negro')])
print 'christian'
print len(df[df['comment_text'].str.contains('|'.join(christian_kws))])
print 'female'
print len(df[df['comment_text'].str.contains('|'.join(female_kws))])
print 'heterosexual'
print len(df[df['comment_text'].str.contains('|'.join(heterosexual_kws))])
print 'homosexual_gay_or_lesbian'
print len(df[df['comment_text'].str.contains('|'.join(homosexual_gay_or_lesbian_kws))])
print 'jewish'
print len(df[df['comment_text'].str.contains('|'.join(jewish_kws))])
print 'latino'
print len(df[df['comment_text'].str.contains('|'.join(latino_kws))])
print 'male'
print len(df[df['comment_text'].str.contains('|'.join(male_kws))])
print 'muslim'
print len(df[df['comment_text'].str.contains('|'.join(muslim_kws))])
print 'psychiatric_or_mental_illness'
print len(df[df['comment_text'].str.contains('|'.join(psychiatric_or_mental_illness_kws))])
print 'transgender'
print len(df[df['comment_text'].str.contains('|'.join(transgender_kws))])
print 'white'
print len(df[df['comment_text'].str.contains('|'.join(white_kws))])

peak = ['crazy', 'insane', 'silly', 'gay', 'terror']
for each in peak:
    print each
    print len(df[df['comment_text'].str.contains(each)])

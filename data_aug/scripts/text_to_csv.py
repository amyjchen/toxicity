import csv
import sys
import random

identity_labels = ['asian', 
    'atheist', 
    'bisexual', 
    'black', 
    'buddhist', 
    'christian', 
    'female', 
    'heterosexual', 
    'hindu', 
    'homosexual_gay_or_lesbian', 
    'intellectual_or_learning_disability', 
    'jewish', 
    'latino', 
    'male', 
    'muslim', 
    'other_disability', 
    'other_gender', 
    'other_race_or_ethnicity', 
    'other_religion', 
    'other_sexual_orientation', 
    'physical_disability', 
    'psychiatric_or_mental_illness', 
    'transgender', 
    'white']

asian_kws = ['asia', 'chinese', 'china', 'korea', 'japan', 'hmong', 'viet', 'cambod', 'india', 'malay', 'filipin', 'thai', 'singapore', 'chink', 'jap', 'gook', 'of color']
atheist_kws = ['atheist']
bisexual_kws = [' bi ', 'bisexual']
black_kws = ['black', 'africa', 'afro', 'nig', 'zulu', 'kenya', 'cameroon', 'nigeria', 'of color', 'brown', 'n-word', 'n****r', 'negro']
buddhist_kws = ['buddhist', 'monk' , 'zen']
christian_kws = ['christian', 'christ ', 'catholic', 'presbyt', 'church', 'preacher', 'priest']
female_kws = ['woman', 'female', 'femme', 'girl', 'lady', 'women', 'mother', 'wife']
heterosexual_kws = ['straight', 'heterosexual', 'hetero']
hindu_kws = ['hindu']
homosexual_gay_or_lesbian_kws = ['homo', 'gay', 'lesbian', 'queer', 'lgb', 'faggot']
intellectual_or_learning_disability_kws = ['down syndrome', 'dyslexi', 'autis', 'retard']
jewish_kws = ['jewish', 'jew']
latino_kws = ['latino', 'hispanic', 'mexican','latin', 'central america', 'chicano', 'of color', 'brown']
male_kws = [' man ', ' male', 'masculine', 'boy', 'gentleman', ' men ', 'father', 'husband']
muslim_kws = ['muslim', 'islam', 'hijab', 'mecca', 'jihad', 'terror']
physical_disability_kws = ['disabl', 'handicap', 'cripple', 'lame', 'wheelchair']
psychiatric_or_mental_illness_kws = ['depress', 'bipolar', 'crazy', 'insane', 'silly', 'narciss', 'anxiet', 'adhd']
transgender_kws = [' trans ', 'transgender', 'ladyboy', 'mtf', 'ftm']
white_kws = ['white', 'cracker']

def write(x) :
	string = x.decode("ascii", errors="ignore").encode()
	string = string.strip('\" ')
	if len(string) > 8 :
		asian = int(any(x in string.lower() for x in asian_kws))
		atheist = int(any(x in string.lower() for x in atheist_kws))
		bisexual = int(any(x in string.lower() for x in bisexual_kws))
		black = int(any(x in string.lower() for x in black_kws))
		buddhist = int(any(x in string.lower() for x in buddhist_kws))
		christian = int(any(x in string.lower() for x in christian_kws))
		female = int(any(x in string.lower() for x in female_kws))
		heterosexual = int(any(x in string.lower() for x in heterosexual_kws))
		hindu = int(any(x in string.lower() for x in hindu_kws))
		homosexual_gay_or_lesbian = int(any(x in string.lower() for x in homosexual_gay_or_lesbian_kws))
		intellectual_or_learning_disability = int(any(x in string.lower() for x in intellectual_or_learning_disability_kws))
		jewish = int(any(x in string.lower() for x in jewish_kws))
		latino = int(any(x in string.lower() for x in latino_kws))
		male = int(any(x in string.lower() for x in male_kws))
		muslim = int(any(x in string.lower() for x in muslim_kws))
		physical_disability = int(any(x in string.lower() for x in physical_disability_kws))
		psychiatric_or_mental_illness = int(any(x in string.lower() for x in psychiatric_or_mental_illness_kws))
		transgender = int(any(x in string.lower() for x in transgender_kws))
		white = int(any(x in string.lower() for x in white_kws))
		
		wtr.writerow ([string, asian, atheist, bisexual, black, buddhist, christian, female, heterosexual, hindu, homosexual_gay_or_lesbian, intellectual_or_learning_disability, jewish, latino, male, muslim, 0, 0, 0, 0, 0, physical_disability, psychiatric_or_mental_illness, transgender, white])

subgroup = sys.argv[1]

wtr = csv.writer(open (subgroup + '.csv', 'w'))

filename = subgroup + ".txt"
f = open(filename)
contents = f.read()
contents = contents.split('\n')
wtr.writerow(["comment_text"] + identity_labels)
for x in contents : 
	if random.random() <= 0.75:
		if random.random() <= 0.05:
			x = x.replace('.', '\n\n')
			write(x)
		else :
			x = x.split('.')
			for s in x :
				if random.random() <= 0.8:
					s = s + "."
				write(s)

	else :
		write(x)





import csv
import sys 

def list_words(subjectline):
	''' Parsing  each subject line into lower case words and removing words greater than 3 characters'''
	words=[]
	words_tmp = subjectline.lower().split()
	for word in words_tmp:
		if word not in words and len(word) > 2:
			words.append(word)
	
	return words
	
def training(texts):
	
	c_words={}
	c_categories={}
	c_texts=0
	c_tot_words=0
	
	for t in texts:
		
		c_texts += 1
		
		'''Updating c_categories dictionary to capture totals of different categories'''
		if t[1] not in c_categories:
			c_categories[t[1]] = 1
		else:
			c_categories[t[1]] = c_categories[t[1]]+ 1
	
	
	for t in texts:
		words = list_words(t[0])
	
		for p in words:
			if p not in c_words:
				c_tot_words = c_tot_words + 1
				c_words[p]={}
				for c in c_categories:
					c_words[p][c] = 0
			c_words[p][t[1]] = c_words[p][t[1]] + 1
			
	
	return (c_words,c_categories,c_texts,c_tot_words)


def classifier(subject,c_words,c_categories,c_texts,c_tot_words):
		
	category_prob = 0
	
	'''Calculate probability of categories -- prob_cat '''
	for c in c_categories:
		
		
		prob_cat = float(c_categories[c])/float(c_texts)		
		words = list_words(subject)
		prob_total = prob_cat
		
		for word in words:
			
			
			if word in c_words:
				prob_word = float(c_words[word][c])/float(c_tot_words)
				
				'''Calculating P(Cat|Word)'''
				prob_cat_word = prob_word/prob_cat
				
				'''Calculating P(Word|Cat)'''
				prob_word_cat = (prob_cat_word * prob_word)/prob_cat
				
				'''Calculating total probabibily for subject line'''
				prob_total = prob_total * prob_word_cat
			
			''' To extract highest probability among categories'''
			if category_prob < prob_total:
				category = c
				category_prob = prob_total
				
			
	return (category,category_prob)

	
if __name__=="__main__":
	with open('training.csv') as f:
		subjects = dict(csv.reader(f,delimiter=','))
		w,c,t,tp=training(subjects.items())
	
		#Test # 1
		classe = classifier("Plans for new youth units blocked",w,c,t,tp)
		print ("Result: {0} ".format(classe))

		#Test # 2
		with open("test.csv") as f:
			correct = 0
			total = 0
			tests = csv.reader(f)
			for subject in tests:
				total += 1
				classe = classifier(subject[0],w,c,t,tp)
				if classe[0] == subject[1]:
					correct += 1
			perc = (float(correct)/float(total))*100
			print('Efficieny : {0} of {1}. i.e {2}%'.format(correct,total,perc)) 

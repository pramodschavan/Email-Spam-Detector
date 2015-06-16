The 'Spam Tester' project is developed to test email subject lines and predict whether an email is Spam or Not Spam.

Data Source - The Spam dataset was downloaded from https://spamassassin.apache.org/publiccorpus/

EmailCleaning.py - This python module process each file within the folder containing spam/no spam dataset and extract's line starting with 'Subject'. The extracted subject files are labelled as spam and no spam and further stored in separate files dataNoSpam.out and dataSpam.out to form training dataset.

SpamTester.py - The training module process the training dataset to create feature vector required for classification. The category and word dictionary created by training module is further used in classifier function which applies Bayes rule to classify the subject line into one of the two the category, Spam or NoSpam. 

The accuracy of the Spam Tester is further tested using test dataset.
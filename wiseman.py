import os
from operator import itemgetter

# picks a directory r"C:\\Users\\Korisnik\\Desktop\\testovi za prvi zdatak\\public\\set\\7"
os.chdir(input())
cwd = os.getcwd()
ca_list = []
wp_list = []
rootdir = cwd

threshold = 70


class Answer:
    def __init__(self, id, _answer, confidence, prediction, valid):
        super().__init__()
        self.id = id
        self._answer = _answer
        self.confidence = confidence
        if(confidence >= threshold):
            self.prediction = True
        else:
            self.prediction = False
        self.valid = True

    def __str__(self):
        return ''+str(self.id)+'  '+str(self.confidence)+'  '+str(self.prediction) + '  '+str(self.valid)

    def setPrediction(self, threshold1):
        if(self.confidence >= threshold1):
            self.prediction = True
        else:
            self.prediction = False
        self.valid = True


# checks all folders and subfolders
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".txt"):  # checks if file ends with txt
            file_handle = open(filepath, 'r')
            if "ca" in file:
                broj = ''.join(filter(str.isdigit, file))
                string = file_handle.readline()
                if(string == "Yes"):
                    bul = True
                else:
                    bul = False  # casts true and false values
                dodaj = [int(broj), bul]
                ca_list.append(dodaj)
            else:
                broj = ''.join(filter(str.isdigit, file))
                string = ''.join(filter(str.isdigit, file_handle.readline()))
                dodaj = [int(broj), int(string)]  # casts percentages into int
                wp_list.append(dodaj)

# these 4 extract 1st element of list


def Extract1(lst):
    return list(map(itemgetter(0), lst))


def Extract2(lst):
    return list(map(itemgetter(1), lst))


def Extract_first(lst):
    return itemgetter(0)(lst)


def Extract_second(lst):
    return itemgetter(1)(lst)


number_yes = 0
for i in Extract2(ca_list):
    if (i == True):
        number_yes += 1

number_of_no = len(ca_list)-number_yes

ca_modified = []
wa_modified = []
ca_list.sort()
wp_list.sort()

list_intersection1 = [value for value in Extract1(
    ca_list) if value in Extract1(wp_list)]
for item in list_intersection1:  # modifying lists to have the same amount of members and only ones
    if item in Extract1(ca_list):  # that are in both lists
        for i in (ca_list):
            if Extract_first(i) == item:
                ca_modified.append(i)
                break
for item in list_intersection1:
    if item in Extract1(wp_list):
        for i in (wp_list):
            if Extract_first(i) == item:
                wa_modified.append(i)
                break

answers = []  # creating a list of objects, answers
for i in range(len(wa_modified)):
    answers.append(Answer(Extract_first(
        ca_modified[i]), Extract_second(ca_modified[i]), Extract_second(wa_modified[i]), None, None))

true_positives = 0
false_positives = 0
true_negatives = 0
false_negatives = 0
for obj in answers:
    obj.setPrediction(threshold)
    if(obj._answer == True and obj.prediction == True):
        true_positives = true_positives+1
    elif(obj._answer == False and obj.prediction == False):
        true_negatives = true_negatives+1
    elif(obj.prediction == True and obj._answer == False):
        false_positives = false_positives+1
    elif(obj.prediction == False and obj._answer == True):
        false_negatives = false_negatives+1

broj_tacnih = 0
broj_netacnih = 0
for i in answers:
    if(i._answer == True):
        broj_tacnih = broj_tacnih+1
for i in answers:
    if(i._answer == False):
        broj_netacnih = broj_netacnih+1

tpr = true_positives/broj_tacnih
fpr = false_positives/broj_netacnih
tpr1 = tpr
fpr1 = fpr
brulaza = 0
while(abs(tpr+fpr-1) > 0.01):
    brulaza = brulaza+1
    if(brulaza > 39):
        break
    if(fpr > 1-tpr):
        threshold = threshold+1
    else:
        threshold = threshold-1
    true_positives = 0
    false_positives = 0
    for obj in answers:
        obj.setPrediction(threshold)
        if(obj._answer == True and obj.prediction == True):
            true_positives = true_positives+1
        elif(obj.prediction == True and obj._answer == False):
            false_positives = false_positives+1
    tpr = true_positives/broj_tacnih
    fpr = false_positives/broj_netacnih

err = fpr

out = str(number_yes)+','+str(number_of_no)+',' + \
    str(len(answers))+','+str(tpr1)+','+str(fpr1)+','+str(err)

print(out)

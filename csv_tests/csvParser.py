import csv

class HwCsv:
    number = None
    deadline = None
    filesToCopy = None
    filesExist = None
    testFiles = None
    grades = None
    extra = None

# csvFile = open('singleLine.csv', newline='')
# reader = csv.DictReader(csvFile, delimiter=',')
# for row in reader:
#     print('first name: ' + row['first_name'])
#     print('last name: ' + row['last_name'])
#     print('age: ' + row['age'])


# csvFile = open('multiLine.csv', newline='')
# reader = csv.DictReader(csvFile, delimiter=',')
# hw = HwCsv()

# for row in reader:
#     hw4.number = row['hw']
#     hw4.deadline = row['deadline']
#     hw4.filesToCopy.append(row['filesToCopy'])
#     hw4.filesExist.append(row['filesExist'])
#     hw4.testFiles.append(row['testFiles'])
#     hw4.grades.append(row['grades'])
#     hw4.extra.append(row['extra'])


# csvFile = open('multiLine2.csv', newline='')
# reader = csv.DictReader(csvFile, delimiter=',')
# hw = HwCsv()
# for row in reader:
#     hw.number = row['hw']
#     hw.deadline = row['deadline']
#     hw.filesToCopy = row['filesToCopy'].split(' ')
#     hw.filesExist = row['filesExist'].split(' ')
#     hw.testFiles = row['testFiles'].split(' ')
#     hw.grades = row['grades'].split(' ')
#     hw.extra = row['extra'].split(' ')


# print(hw)

class HwConfiguration:
    deadline = None
    files_to_copy = []
    files_should_exist = []
    test_files = []
    grades = []
    is_extra = []

def load_hw_csv_files(hw_number):
    hw_configuration = HwConfiguration()
    hw_csv = open(hw_number + ".csv")
    hw_tests_csv = open(hw_number + "_tests.csv")

    reader = csv.DictReader(hw_csv, delimiter=',')
    for row in reader:
        if(row['deadline'] != ""): hw_configuration.deadline = row['deadline']
        if(row['files_to_copy'] != ""): hw_configuration.files_to_copy.append(row['files_to_copy'])
        if(row['files_should_exist'] != ""): hw_configuration.files_should_exist.append(row['files_should_exist'])
    
    reader = csv.DictReader(hw_tests_csv, delimiter=',')
    for row in reader:
        hw_configuration.test_files.append(row['test_files'])
        hw_configuration.grades.append(row['grades'])
        hw_configuration.is_extra.append(row['is_extra'])

    print(hw_configuration)


load_hw_csv_files("hw4")
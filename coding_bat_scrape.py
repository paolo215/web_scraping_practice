from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import sys
import re
from xlsxwriter import Workbook

# Scrape codingbat Java questions
# Goal: Extract the name of the problem, description, and examples

def scrape():
    # Set up fake user agent
    user_agent = UserAgent()
    headers = {"headers" : user_agent.chrome}


    # Get contents of codingbat.com/java page
    main_url = "http://codingbat.com"
    codingbat_java_contents = requests.get(main_url + "/java", headers=headers).content
    bsoup_codingbat_java = BeautifulSoup(codingbat_java_contents, "lxml")

    # All sections have 'summ' class
    divs_summ = bsoup_codingbat_java.find_all("div", class_="summ")

    challenges = []
    for div in divs_summ:
        section_url = div.a["href"]
        section_name = div.span.string

        # Open section
        codingbat_java_section_contents = requests.get(main_url + section_url, headers=headers).content    

        # Create BeautifulSoup for this section
        bsoup_codingbat_java_section = BeautifulSoup(codingbat_java_section_contents, "lxml")

        # Get all questions. All questions have td tags
        java_questions_div = bsoup_codingbat_java_section.find("div", class_="tabin")
        java_questions_table = java_questions_div.table
        java_questions_entries = java_questions_table.find_all("td")

        # Go over each questions and extract description and examples
        for java_question in java_questions_entries:

            # Get url to the question
            java_url = java_question.a["href"]

            # Get title of this question
            java_question_title = java_question.a.string

            # Get contents of this web page and create BeautifulSoup
            codingbat_java_question = requests.get(main_url + java_url, headers=headers).content
            bsoup_codingbat_java_question = BeautifulSoup(codingbat_java_question, "lxml")

            # Get description and examples
            # Description and examples are in td tags
            java_question_div = bsoup_codingbat_java_question.find("div", class_="tabin")
            java_question_table = java_question_div.table
            java_question_td = java_question_table.find("td")
            java_question_description = java_question_td.div.string


            java_question_children = java_question_td.children
            java_question_examples = []
       
            # Get examples using regex
            regex = re.compile(java_question_title)
            for child in java_question_children:
                if regex.match(child.encode("utf-8")):
                    java_question_examples.append(child)

            data = [java_question_title, java_question_description, java_url] + java_question_examples
            challenges.append(data)

    return challenges


# Put them in worksheet
def write_to_excel(data):
    workbook = Workbook("codingbat_challenges.xlsx")
    worksheet = workbook.add_worksheet()

    # Headers
    worksheet.write(0, 0, "Title")
    worksheet.write(0, 1, "Description")
    worksheet.write(0, 2, "URL")
    worksheet.write(0, 3, "Questions")

    # Data
    for i in range(len(data)):
        challenge = data[i]
        for j in range(len(challenge)):
            worksheet.write(i+1, j, challenge[j])

    workbook.close()

def main():
    challenges = scrape()
    write_to_excel(challenges)



if __name__ == "__main__":
    main()



